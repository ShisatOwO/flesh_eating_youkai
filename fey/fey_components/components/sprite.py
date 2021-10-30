import pygame as pg
from fey.fey_components import FeyBaseComponent
from fey.fey_types import Box2D


class Sprite(FeyBaseComponent):
    def __init__(self, color=(0, 0, 0), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sprite = None
        self.color = color

    def draw(self, surface: pg.Surface):
        surface.blit(self._sprite, self.box.pos.astuple())

    def init(self, *args, **kwargs):
        super().init(*args, *kwargs)
        self._sprite = pg.Surface(self.box.dim.astuple())
        self._sprite.fill(self.color)

