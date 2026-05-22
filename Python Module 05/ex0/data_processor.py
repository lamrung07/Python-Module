#!/usr/bin/env python3
import typing
import abc

class DataProcessor(abc.ABC):
    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass
    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass
    def output(self) -> typing.Tuple[int, str]:
        pass

class NumericProcessor(DataProcessor):
    def __init__(self, data):
        self.data = data
        self.storage = []
    def validate(self, data: typing.Any) -> bool:
        allowed = {int, float, list[int | float]}
        if type(data) not in allowed:
            return False
        else:
            return True
    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise TypeError (f"Got exception: Improper numeric data")
        if type(data) == list:
            for item in data:
                self.storage.append(str(item))
        else:
            self._storage.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        allowed = {str, list[str]}
        if type(data) not in allowed:
            return False
        else:
            return True
    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if type(data) == list:
            for item in data:
                self.storage.append(str(item))
        else:
            self._storage.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        pass
    def ingest(self, data: typing.Any) -> None:
        pass