try:
    import pygame as pg
except ImportError:
    import sys
    print("Pygame is not installed. Since Fey is built on top of Pygame,\n"
          "Pygame needs to be installed in oder for Fey to work.")
    sys.exit(1)

import fey.config
import fey.fey_components
import fey.fey_types


# Config
class FeyConfig(config.FeyConfig): ...
class FeyGlobalConfig(config.FeyGlobalConfig): ...


# Components
class FeyGlobalComponentTable(fey_components.FeyGlobalComponentTable): ...
class FeyBaseComponent(fey_components.FeyBaseComponent): ...


# Types
class Point2D(fey_types.Point2D): ...
class Box2D(fey_types.Box2D): ...


print("Greetings from the Flesh Eating Youkai...")
