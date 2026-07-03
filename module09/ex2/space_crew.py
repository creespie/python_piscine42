from pydantic import Field, BaseModel, model_validator, ValidationError
from typing import Annotated
from datetime import datetime
from enum import Enum


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: Annotated[str, Field(min_length=3, max_length=10)]
    name: Annotated[str, Field(min_length=2, max_length=50)]
    rank: Rank
    age: Annotated[int, Field(ge=18, le=80)]
    specialization: Annotated[str, Field(min_length=3, max_length=30)]
    years_experience: Annotated[int, Field(ge=0, le=50)]
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: Annotated[str, Field(min_length=5, max_length=15)]
    mission_name: Annotated[str, Field(min_length=3, max_length=100)]
    destination: Annotated[str, Field(min_length=3, max_length=50)]
    launch_date: datetime
    duration_days: Annotated[int, Field(ge=1, le=3650)]
    crew: Annotated[list[CrewMember], Field(min_length=1, max_length=12)]
    mission_status: str = "planned"
    budget_millions: Annotated[float, Field(ge=1.0, le=10000.0)]

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        if self.mission_id[0] != "M":
            raise ValueError('Mission ID must start with "M"')
        commander = 0
        for member in self.crew:
            if member.rank in [Rank.COMMANDER, Rank.CAPTAIN]:
                commander += 1
        if commander == 0:
            raise ValueError("Must have at least one Commander or Captain")
        elif self.duration_days > 365:
            experienced = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced += 1
            if experienced < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) need "
                    "50% experienced crew (5+ years)"
                )
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.fromisoformat("2026-01-01"),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=40,
                    specialization="Mission Command",
                    years_experience=15,
                    is_active=True,
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=35,
                    specialization="Navigation",
                    years_experience=10,
                    is_active=True,
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=30,
                    specialization="Engineering",
                    years_experience=6,
                    is_active=True,
                ),
            ],
            budget_millions=2500.0,
        )

        print("Valid mission created:")
        print(f"Mission: {valid_mission.mission_name}")
        print(f"ID: {valid_mission.mission_id}")
        print(f"Destination: {valid_mission.destination}")
        print(f"Duration: {valid_mission.duration_days} days")
        print(f"Budget: ${valid_mission.budget_millions}M")
        print(f"Crew size: {len(valid_mission.crew)}")
        print("Crew members:")

        for member in valid_mission.crew:
            print(
                f"- {member.name} ({member.rank.value}) "
                f"- {member.specialization}")

    except ValidationError as e:
        print("Validation error on valid mission (unexpected)")
        for err in e.errors():
            print(f"{err['loc']}: {err['msg']}")

    print("=========================================")
    print("Expected validation error:")
    try:
        invalid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.fromisoformat("2026-01-01"),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=Rank.OFFICER,
                    age=40,
                    specialization="Mission Command",
                    years_experience=15,
                    is_active=True,
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=35,
                    specialization="Navigation",
                    years_experience=10,
                    is_active=True,
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=30,
                    specialization="Engineering",
                    years_experience=6,
                    is_active=False,
                ),
            ],
            budget_millions=2500.0,
        )
        print(invalid_mission)
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
