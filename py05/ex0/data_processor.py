from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
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


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("Testing Numeric Processor...")
    np = NumericProcessor()
    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'Hello': {np.validate('Hello')}")
    print(
        "Test invalid ingestion of string 'foo' without prior validation:"
    )
    try:
        np.ingest("foo")  # type: ignore[arg-type]
    except Exception as e:
        print(f"Got exception: {e}")
    batch_n: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {batch_n}")
    np.ingest(batch_n)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = np.output()
        print(f"Numeric value {rank}: {val}")

    print("Testing Text Processor...")
    tp = TextProcessor()
    print(f"Trying to validate input '42': {tp.validate(42)}")
    batch_t = ["Hello", "Nexus", "World"]
    print(f"Processing data: {batch_t}")
    tp.ingest(batch_t)
    print("Extracting 1 value...")
    rank, val = tp.output()
    print(f"Text value {rank}: {val}")

    print("Testing Log Processor...")
    lp = LogProcessor()
    print(f"Trying to validate input 'Hello': {lp.validate('Hello')}")
    batch_l: list[dict[str, str]] = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {batch_l}")
    lp.ingest(batch_l)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = lp.output()
        print(f"Log entry {rank}: {val}")


if __name__ == "__main__":
    main()
