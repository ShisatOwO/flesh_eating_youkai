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

    def __add__(self, other) -> Point2D:
        return Point2D(self.x+other.x, self.y+other.y)

    def __sub__(self, other) -> Point2D:
        return Point2D(self.x-other.x, self.y-other.y)

    def __truediv__(self, other) -> Point2D:
        if not isinstance(other, Point2D):
            return Point2D(self.x / other, self.y / other)

    def __mul__(self, other) -> Point2D:
        if not isinstance(other, Point2D):
            return Point2D(self.x * other, self.y * other)

    def astuple(self):
        return self.x, self.y

    #TODO: add implementations for * and /


@dataclass
class Box2D(FeyDataclass):
    pos: Point2D
    dim: Point2D

    def __add__(self, other) -> Box2D:
        return Box2D(self.pos+other.pos, self.dim+other.dim)

    #TODO: Add implementations for -, * and /


class Interpolation:
    def __init__(self, target: Point2D, duration: float):
        self._duration  = duration
        self._target    = target
        self._velocity  = target / duration
        self._time      = 0
        self._interpolated_by = Point2D(0, 0)

    def interpolate(self, time: float, f=lambda v, t: v):
        if self._time >= self._duration:
            return False

        n = f(self._velocity, self._time)
        self._time += time

        if self._time >= self._duration:
            return self._target - self._interpolated_by

        n = n * time
        self._interpolated_by += n
        return n
