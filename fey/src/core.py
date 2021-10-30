import pygame as pg
from fey.config import FeyGlobalConfig, FeyConfig
from fey.fey_components import FeyGlobalComponentTable
from fey.fey_components.components.render import Render


def set_window_title(title: str = "Flesh Eating Youkai"):
    pg.display.set_caption(title)


def init(config: FeyConfig) -> ():
    FeyGlobalConfig().load_config(config)

    pg.init()
    c = FeyGlobalConfig()

    if c.scaling < 1:
        c.scaling = 1

    window = pg.display.set_mode(c.screen_dims.dim.astuple(), pg.GL_DOUBLEBUFFER)
    wbuffer = pg.Surface((int(c.screen_dims.dim.x/c.scaling), int(c.screen_dims.dim.y/c.scaling)))
    clock = pg.time.Clock()
    set_window_title(c.original_window_title)

    return window, wbuffer, clock


def run(window: pg.Surface, wbuffer: pg.Surface, clock: pg.time.Clock) -> int:

    for comp in FeyGlobalComponentTable().get():
        comp.init()

    running = True
    fps = FeyGlobalConfig().target_fps

    while running:
        window.fill((0, 0, 0))
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

        for root in FeyGlobalComponentTable().get():
            if (r := root.get(type=Render)) != [] and r[0].is_active():
                r[0].render(wbuffer)


        #TODO: Keep aspect ration while scaling
        pg.transform.scale(wbuffer, (window.get_width(), window.get_height()), window)

        pg.display.flip()
        clock.tick(fps)
