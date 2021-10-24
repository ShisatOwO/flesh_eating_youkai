import pygame as pg
from fey.config import FeyGlobalConfig
from fey.config import FeyConfig


def set_window_title(title: str = "Flesh Eating Youkai"):
    pg.display.set_caption(title)


def init(config: FeyConfig) -> ():
    pg.init()
    FeyGlobalConfig().load_config(config)

    c = FeyGlobalConfig()

    if c.scaling < 1:
        c.scaling = 1

    window = pg.display.set_mode((c.screen_dims.w, c.screen_dims.h), pg.GL_DOUBLEBUFFER)
    wbuffer = pg.Surface((int(c.screen_dims.w/c.scaling), int(c.screen_dims.h/c.scaling)))
    clock = pg.time.Clock()
    set_window_title(c.original_window_title)

    return window, wbuffer, clock


def run(window: pg.Surface, wbuffer: pg.Surface, clock: pg.time.Clock) -> int:
    running = True
    fps = FeyGlobalConfig().target_fps

    while running:
        window.fill((0, 0, 0))
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

        #TODO: Keep aspect ration while scaling
        pg.transform.scale(wbuffer, (window.get_width(), window.get_height()), window)

        pg.display.flip()
        clock.tick(fps)
