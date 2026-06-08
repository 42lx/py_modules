import json
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_safety_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        senior_ranks = {Rank.commander, Rank.captain}
        if not any(member.rank in senior_ranks for member in self.crew):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced = sum(
                1 for m in self.crew if m.years_experience >= 5
            )
            if experienced * 2 < len(self.crew):
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced "
                    "crew (5+ years)"
                )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


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


def print_mission(mission: SpaceMission) -> None:
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) "
            f"- {member.specialization}"
        )


def main() -> None:
    print("Space Mission Crew Validation")
    records = load_json("space_missions.json")
    for record in records:
        print("=" * 41)
        try:
            mission = SpaceMission.model_validate(record)
            print_mission(mission)
        except ValidationError as e:
            msg = e.errors()[0]["msg"].removeprefix("Value error, ")
            print("Expected validation error:")
            print(msg)

    print("=" * 41)
    print("Expected validation error:")
    junior_crew = [
        CrewMember(
            member_id="C010",
            name="Bob Junior",
            rank=Rank.cadet,
            age=22,
            specialization="Trainee",
            years_experience=1,
        ),
        CrewMember(
            member_id="C011",
            name="Eve Newby",
            rank=Rank.officer,
            age=27,
            specialization="Comms",
            years_experience=3,
        ),
    ]
    try:
        SpaceMission(
            mission_id="M_SHORT01",
            mission_name="Lunar Survey",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=30,
            crew=junior_crew,
            budget_millions=150.0,
        )
    except ValidationError as e:
        msg = e.errors()[0]["msg"].removeprefix("Value error, ")
        print(msg)


if __name__ == "__main__":
    main()
