from __future__ import annotations
from fey.fey_components.comp_management import FeyComponentManagement
from fey.fey_config import FeyGlobalConfig
from fey.fey_types import Point2D, Box2D, Interpolation
from fey.fey_game_time import FeyGameTime
from abc import ABC


class FeyBaseComponent(FeyComponentManagement, ABC):
    def __init__(self, comps=[], name=None, pos: Point2D = Point2D(0, 0), dim: Point2D = Point2D(0, 0), *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._inactive_names = {}
        self._inactive_components = []
        self._parent: FeyBaseComponent = None

        self._name = name
        self._active: bool = True
        self._type = FeyBaseComponent
        self.comp_id = next(self._id_generator)

        self.box = Box2D(Point2D(0, 0), dim)

        self._move_interpol: [Interpolation, ] = []

        if isinstance(comps, list):
            self.add(comps)

        self.move(pos)

    def init(self, *args, **kwargs):
        for comp in self._components:
            comp.init(*args, **kwargs)

    def disable(self):
        self._active = False
        self._inactive_names, self._names = self._names, self._inactive_names
        self._inactive_components, self._components = self._components, self._inactive_components

    def enable(self):
        self._active = True
        self._inactive_names, self._names = self._names, self._inactive_names
        self._inactive_components, self._components = self._components, self._inactive_components

    def is_active(self):
        return self._active

    def process(self, ctx=None):
        for comp in self._components:
            comp.process(ctx)

        for i, v in enumerate(self._move_interpol):
            if not (pos := v.interpolate(FeyGameTime().delta * FeyGameTime().time)):
                del self._move_interpol[i]
                break
            self.move(pos)

    def add(self, comps: [FeyBaseComponent, ]=[]):
        for comp in comps:
            assert issubclass(type(comp), FeyBaseComponent)
            comp._parent = self
            if comp._name is not None:
                self._names[comp._name] = comp
            self._components.append(comp)

    def suicide(self) -> bool:
        out = False
        if self._parent is not None:
            out = self._parent.remove(self)

        return out

    def __search(self, component: FeyBaseComponent, name, type, id) -> [FeyBaseComponent, ]:
        out = component.get(name, type, id)
        for comp in component._components:
            out += self.__search(comp, name, type, id)

        return out

    def qsearch(self, name: str = None, id: int = None) -> FeyBaseComponent:
        if len((out := self.search(name, None, id))) == 1:
            return out[0]
        return False

    def global_search(self, name: str = None, type=None ,  id: int = None) -> [FeyBaseComponent, ]:
        if self._parent is not None:
            return self._parent.search(name, type, id)

        return self.__search(self, name, type, id)

    def search(self, name: str = None, type=None ,  id: int = None) -> [FeyBaseComponent, ]:
        return self.__search(self, name, type, id)

    def get_root(self) -> FeyBaseComponent:
        if self._parent is not None:
            return self._parent.get_root()
        return self

    def get_parent_box(self) -> Box2D:
        if self._parent is None:
            return FeyGlobalConfig().screen_dims
        return self._parent.box

    def move(self, pos: Point2D):
        self.box.pos += pos
        for comp in self._components:
            comp.move(pos)

    def move_over_time(self, direction: Point2D, duration: int):
        self._move_interpol.append(Interpolation(direction, duration))

    def scale_over_time(self): ...
    def rotate_over_time(self): ...
    def fade_over_time(self): ...

