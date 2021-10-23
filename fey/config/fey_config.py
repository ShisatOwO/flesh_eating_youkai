from __future__ import annotations
from dataclasses import dataclass
from fey.fey_types import Singleton, FeyDataclass, Box2D


"""
Die ganzen Config Sachen sind etwas ungeschickt gelöst...
Es funktioniert aber für jetzt, später werde ich das aber noch überarbeiten.
"""

#TODO: Schauen ob die Implementation hier so Sinnvoll ist.


@dataclass
class FeyConfig(FeyDataclass):
    _custom_config: {} = None

    screen_dims: Box2D = Box2D(0, 0, 800, 600)
    original_window_title: str = "Flesh Eating Youkai"
    target_fps: int = 60

    def custom_config(self, config: {}) -> FeyConfig:
        self._custom_config = config
        for key in config:
            self.__setattr__(key, config[key])
        return self


class FeyGlobalConfig(Singleton):
    _custom_config = None

    screen_dims: Box2D
    original_window_title: str
    target_fps: int

    def __init__(self, conf: FeyConfig = None):
        if isinstance(conf, FeyConfig):
            self.load_config(conf)

    def get_custom_config(self) -> dict:
        return self._custom_config

    def load_config(self, conf: FeyConfig):
        self._custom_config = conf._custom_config
        for key in (config := conf.asdict()):
            self.__setattr__(key, config[key])

    def get_dict(self) -> dict:
        out = {
            "screen_dims": self.screen_dims,
            "original_window_title": self.original_window_title,
            "target_fps": self.target_fps,
        }

        if isinstance(self._custom_config, dict):
            return out | self._custom_config
        return out
