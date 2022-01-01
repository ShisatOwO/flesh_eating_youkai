from __future__ import annotations
from fey.fey_types import Singleton


class FeyGameTime(Singleton):
    time: float = 1
    delta: float = 1

    def set(self, t: float, d: int):
        ...

    def slowmo(self, t: float, d1: float, d2: float):
        ...
