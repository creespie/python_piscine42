from pydantic import BaseModel, Field, model_validator, ValidationError
from typing import Annotated
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class Contact(BaseModel):
    contact_id: Annotated[str, Field(min_length=5, max_length=15)]
    timestamp: datetime
    location: Annotated[str, Field(min_length=3, max_length=100)]
    contact_type: ContactType
    signal_strength: Annotated[float, Field(ge=0.0, le=10.0)]
    duration_minutes: Annotated[int, Field(ge=1, le=1440)]
    witness_count: Annotated[int, Field(ge=1, le=100)]
    message_received: Annotated[
        str | None, Field(default=None, max_length=500)]
    is_verified: bool = False

    @model_validator(mode="after")
    def validator(self) -> "Contact":
        if self.contact_id[:2] != "AC":
            raise ValueError(
                'Contact ID must start with "AC" (Alien Contact)')
        elif not self.is_verified and (
                self.contact_type == ContactType.PHYSICAL):
            raise ValueError("Physical contact reports must be verified")
        elif self.witness_count < 3 and (
                self.contact_type == ContactType.TELEPATHIC):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        elif self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")
        return self


def main() -> None:
    test = Contact(
        contact_id="AC_2024_001",
        contact_type=ContactType.RADIO,
        location="Area 51, Nevada",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        timestamp=datetime.fromisoformat("2026-01-15"),
    )
    print("Alien Contact Log Validation")
    print("=============================")
    print("Valid contact report:")
    print(f"ID: {test.contact_id}")
    print(f"Type: {test.contact_type.value}")
    print(f"Location: {test.location}")
    print(f"Signal: {test.signal_strength}/10")
    print(f"Duration: {test.duration_minutes} minutes")
    print(f"Witnesses: {test.witness_count}")
    print(f"Message: {test.message_received}")
    print("=============================")
    print("Expected validation error:")
    try:
        test_test = Contact(
            contact_id="AC_2024_001",
            contact_type=ContactType.TELEPATHIC,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
            timestamp=datetime.fromisoformat("2026-01-15"),
        )
        print(test_test)
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['msg']}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
