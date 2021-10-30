import pygame as pg
from fey.fey_components import FeyBaseComponent
from fey.fey_components.components.sprite import Sprite


class Render(FeyBaseComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sprites = []
        self.appearance = None

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)

        if len(self.search(type=Render)) > 1:
            raise RuntimeError("A component tree can only have one Render component.")

        self.box = self.get_root().box
        self.sprites = self.get_root().search(type=Sprite)
        self.appearance = pg.Surface(self.box.dim.astuple())

    def render(self, surface: pg.Surface):
        for sprite in self.sprites:
            sprite.draw(self.appearance)
            surface.blit(self.appearance, self.box.pos.astuple())
