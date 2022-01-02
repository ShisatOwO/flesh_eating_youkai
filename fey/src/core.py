import pygame as pg
from fey.fey_config import FeyGlobalConfig, FeyConfig
from fey.fey_components import FeyGlobalComponentTable
from fey.fey_components.components.render import Render
from fey.fey_game_time import FeyGameTime
from fey.fey_types import Point2D


def set_window_title(title: str = "Flesh Eating Youkai"):
    pg.display.set_caption(title)


def init(config: FeyConfig) -> ():
    FeyGameTime()
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

    delta_a = 0
    delta_b = 0

    while running:
        delta_a = pg.time.get_ticks()
        FeyGameTime.delta = (delta_a - delta_b) / 1000.0
        delta_b = delta_a

        wbuffer.fill((0, 0, 0))

        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

            if e.type == pg.KEYDOWN:


                if e.key == pg.K_m:
                    FeyGlobalComponentTable().qget("Scene_01").qsearch("Entity").move_over_time(Point2D(100, 0), 0.1)

        comps = FeyGlobalComponentTable().get()
        if len(comps) > 0:
            for r in comps[0].global_search(type=Render):
                r.render(wbuffer)

        for comp in FeyGlobalComponentTable().get():
            comp.process()

        #TODO: Keep aspect ration while scaling
        pg.transform.scale(wbuffer, (window.get_width(), window.get_height()), window)

        pg.display.flip()
        clock.tick(60)
