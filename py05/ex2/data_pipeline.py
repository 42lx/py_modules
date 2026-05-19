from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):
    name: str = "Data Processor"

    def __init__(self) -> None:
        self._items: list[tuple[int, str]] = []
        self._counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if not self._items:
            raise Exception("No data to output")
        return self._items.pop(0)

    @property
    def total(self) -> int:
        return self._counter

    @property
    def remaining(self) -> int:
        return len(self._items)


def _is_number(x: Any) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


class NumericProcessor(DataProcessor):
    name: str = "Numeric Processor"

    def validate(self, data: Any) -> bool:
        if _is_number(data):
            return True
        if isinstance(data, list) and data:
            return all(_is_number(x) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        items: list[int | float] = data if isinstance(data, list) else [data]
        for x in items:
            self._items.append((self._counter, str(x)))
            self._counter += 1


class TextProcessor(DataProcessor):
    name: str = "Text Processor"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and data:
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")
        items: list[str] = data if isinstance(data, list) else [data]
        for x in items:
            self._items.append((self._counter, x))
            self._counter += 1


def _is_log_dict(d: Any) -> bool:
    return (
        isinstance(d, dict)
        and "log_level" in d
        and "log_message" in d
        and all(
            isinstance(k, str) and isinstance(v, str) for k, v in d.items()
        )
    )


class LogProcessor(DataProcessor):
    name: str = "Log Processor"

    def validate(self, data: Any) -> bool:
        if _is_log_dict(data):
            return True
        if isinstance(data, list) and data:
            return all(_is_log_dict(x) for x in data)
        return False

    def ingest(
        self, data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        items: list[dict[str, str]] = (
            data if isinstance(data, list) else [data]
        )
        for d in items:
            s = f"{d['log_level']}: {d['log_message']}"
            self._items.append((self._counter, s))
            self._counter += 1


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(value for _, value in data))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        parts = [f'"item_{rank}": "{value}"' for rank, value in data]
        print("JSON Output:")
        print("{" + ", ".join(parts) + "}")


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(
                f"{proc.name}: total {proc.total} items processed, "
                f"remaining {proc.remaining} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            data: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc.remaining == 0:
                    break
                data.append(proc.output())
            plugin.process_output(data)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print()
    print("Registering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    batch1: list[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch1}")
    stream.process_stream(batch1)
    stream.print_processors_stats()

    print()
    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    stream.print_processors_stats()

    print()
    batch2: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"Send another batch of data: {batch2}")
    stream.process_stream(batch2)
    stream.print_processors_stats()

    print()
    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
