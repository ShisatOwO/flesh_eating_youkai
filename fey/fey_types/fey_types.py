from __future__ import annotations

from dataclasses import dataclass, asdict
from abc import ABC
from typing import Any


class FeyDataclass(ABC):
    def __init__(self, *args, **kwargs): ...

    def asdict(self) -> dict:
        return asdict(self)

    def copy(self) -> Any:
        obj = self.__new__(self.__class__)
        obj.__init__(**self.asdict())
        return obj


class Singleton(ABC):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


@dataclass
class Point2D(FeyDataclass):
    x: float
    y: float


@dataclass
class Box2D(FeyDataclass):
    x: float
    y: float
    w: float
    h: float
