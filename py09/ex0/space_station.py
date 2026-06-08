import json
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def load_json(filename: str) -> list[dict[str, Any]]:
    path = Path(__file__).parent / filename
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: '{filename}' not found")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON in '{filename}' - {e}")
        return []


def main() -> None:
    print("Space Station Data Validation")
    records = load_json("space_stations.json") + load_json(
        "invalid_stations.json"
    )
    for record in records:
        print("=" * 40)
        try:
            station = SpaceStation.model_validate(record)
            print("Valid station created:")
            print(f"ID: {station.station_id}")
            print(f"Name: {station.name}")
            print(f"Crew: {station.crew_size} people")
            print(f"Power: {station.power_level}%")
            print(f"Oxygen: {station.oxygen_level}%")
            status = "Operational" if station.is_operational else "Offline"
            print(f"Status: {status}")
        except ValidationError as e:
            print("Expected validation error:")
            print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
