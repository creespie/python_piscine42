from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[Any] = []
        self._counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        self._counter += 1
        popped = self._storage.pop(0)
        return (self._counter - 1, popped)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(instance, (int, float)) for instance in data)
        return False

    def ingest(self, data: list[int | float] | int | float) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        if isinstance(data, list):
            for instance in data:
                self._storage.append(str(instance))
        else:
            self._storage.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(instance, str) for instance in data)
        return False

    def ingest(self, data: list[str] | str) -> None:
        if not self.validate(data):
            raise TypeError("Improper string data")
        if isinstance(data, list):
            for instance in data:
                self._storage.append(instance)
        else:
            self._storage.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(key, str) for key in data.keys()) and all(
                isinstance(value, str) for value in data.values()
            )
        if isinstance(data, list):
            if not data:
                return False
            for entry in data:
                if not isinstance(entry, dict):
                    return False
                if not (
                    all(isinstance(key, str) for key in entry.keys())
                    and all(isinstance(value, str) for value in entry.values())
                ):
                    return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper dict data")
        if isinstance(data, dict):
            for key, value in data.items():
                self._storage.append(": ".join((key, value)))
        else:
            for entry_dict in data:
                for key, value in entry_dict.items():
                    self._storage.append(": ".join((key, value)))


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    num_proc = NumericProcessor()
    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")
    except TypeError as e:
        print(f"Got exception: {e}")

    data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    num_proc.ingest(data)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = num_proc.output()
        print(f"Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    text_proc = TextProcessor()
    print(f"Trying to validate input '42': {text_proc.validate(42)}")

    text_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")
    text_proc.ingest(text_data)
    print("Extracting 1 value...")
    rank, value = text_proc.output()
    print(f"Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")

    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {log_data}")
    log_proc.ingest(log_data)
    print("Extracting 2 values...")
    for _ in range(4):
        rank, value = log_proc.output()
        print(f"Log entry {rank}: {value}")
