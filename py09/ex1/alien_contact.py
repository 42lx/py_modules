import json
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Optional

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def check_business_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.physical:
            if not self.is_verified:
                raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.telepathic:
            if self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses"
                )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
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


def main() -> None:
    print("Alien Contact Log Validation")
    records = load_json("alien_contacts.json") + load_json(
        "invalid_contacts.json"
    )
    for record in records:
        print("=" * 38)
        try:
            contact = AlienContact.model_validate(record)
            print("Valid contact report:")
            print(f"ID: {contact.contact_id}")
            print(f"Type: {contact.contact_type.value}")
            print(f"Location: {contact.location}")
            print(f"Signal: {contact.signal_strength}/10")
            print(f"Duration: {contact.duration_minutes} minutes")
            print(f"Witnesses: {contact.witness_count}")
            if contact.message_received:
                print(f"Message: '{contact.message_received}'")
            else:
                print("Message: None")
        except ValidationError as e:
            msg = e.errors()[0]["msg"].removeprefix("Value error, ")
            print("Expected validation error:")
            print(msg)


if __name__ == "__main__":
    main()
