from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    name: str = "Data Processor"

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

    def len(self) -> tuple[int, int]:
        return (len(self._storage), len(self._storage) + self._counter)


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if not isinstance(proc, DataProcessor):
            raise TypeError("Not a data processor")
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for entry in stream:
            validated = False
            for proc in self._processors:
                if proc.validate(entry):
                    proc.ingest(entry)
                    validated = True
                    continue
            if not validated:
                print(
                    f"DataStream error - "
                    f"Can't process element in stream {entry}")

    def print_processors_stats(self) -> None:
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            current_total = proc.len()
            print(
                f"{proc.name}:  total {current_total[1]} items processed, "
                f"remaining {current_total[0]} on processor"
            )


class NumericProcessor(DataProcessor):
    name = "Numeric Processor"

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
    name = "Data Processor"

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
    name = "Log Processor"

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
    print("=== Code Nexus - Data Stream ===\n")

    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    num_proc = NumericProcessor()
    stream.register_processor(num_proc)

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(text_proc)
    stream.register_processor(log_proc)

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()

    stream.print_processors_stats()
