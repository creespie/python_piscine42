from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class Station(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, min_length=0, max_length=200)


def main() -> None:
    station = Station(
        station_id="STN001",
        name="Space Station Alpha",
        crew_size=15,
        power_level=85.5,
        oxygen_level=90.0,
        last_maintenance=datetime.fromisoformat("2026-01-15"),
    )
    print("Space Station Data Validation")
    print("=============================")
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: "
          f"{"Operational" if station.is_operational else "Not Operational"}")
    print("=============================")
    print("Expected validation error:")
    try:
        station_test = Station(
            station_id="hello",
            name="test",
            crew_size=32,
            power_level=145.6,
            oxygen_level=23.6,
            last_maintenance=datetime.fromisoformat("1994-05-12"),
            is_operational=True,
        )
        print(station_test)
    except ValidationError as e:
        for error in e.errors():
            print(f"{error['loc'][0]}: {error['msg']}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
