from __future__ import annotations
from fey.fey_components.comp_management import FeyComponentManagement
from abc import ABC


class FeyBaseComponent(FeyComponentManagement, ABC):
    def __init__(self, comps=[], name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._type = FeyBaseComponent
        self._parent: FeyBaseComponent = None
        self._active: bool = True
        self.comp_id = next(self._id_generator)
        self.name = name
        self._inactive_components = []
        self._inactive_names = {}
        self.add(comps)

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

    def process(self, ctx):
        ...

    def add(self, comps: [FeyBaseComponent, ]=[]):
        for comp in comps:
            assert issubclass(type(comp), FeyBaseComponent)
            comp._parent = self
            if comp._name is not None:
                self._names[comp.name] = comp
            self._components.append(comp)

    def suicide(self) -> bool:
        out = False

        if self._parent is not None:
            out = self._parent.remove(self)
        del self._parent

        return out

    def __search(self, component: FeyBaseComponent, name, type, id) -> [FeyBaseComponent, ]:
        out = []
        out += component.get(name, type, id)

        for comp in component._components:
            out += self.__search(comp, name, type, id)

        return out

    def search(self, name: str = None, type=None ,  id: int = None) -> [FeyBaseComponent, ]:
        if self._parent is not None:
            return self._parent.search(name, type, id)

        return self.__search(self, name, type, id)
