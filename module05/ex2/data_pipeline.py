from abc import ABC, abstractmethod
from typing import Any, Protocol


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [item[1] for item in data]
        csv_str = ",".join(values)
        print("CSV Output:")
        print(csv_str)


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        output: dict[str, str] = {}
        for entry in data:
            output[f"item_{entry[0]}"] = entry[1]
        pairs = [f'"{key}": "{value}"' for key, value in output.items()]
        json_str = "{" + ", ".join(pairs) + "}"
        print("JSON Output:")
        print(json_str)


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
        popped = self._storage.pop(0)
        self._counter += 1
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
                    break
            if not validated:
                print(f"DataStream error - "
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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            popping: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    popping.append(proc.output())
                except IndexError:
                    break
            plugin.process_output(popping)


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
    name = "Text Processor"

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
    print("=== Code Nexus - Data Pipeline ===\n")

    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors")
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(num_proc)
    stream.register_processor(text_proc)
    stream.register_processor(log_proc)

    batch1 = [
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

    print(f"Send first batch of data on stream: {batch1}")
    stream.process_stream(batch1)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    stream.output_pipeline(3, csv_plugin)
    stream.print_processors_stats()

    batch2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {"log_level": "NOTICE",
             "log_message": "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"\nSend another batch of data: {batch2}")
    stream.process_stream(batch2)
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    stream.output_pipeline(5, json_plugin)
    stream.print_processors_stats()
