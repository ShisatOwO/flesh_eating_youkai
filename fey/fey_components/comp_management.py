from __future__ import annotations
from fey.src.utility import id_generator
from abc import ABC


class FeyComponentManagement(ABC):

    def __init__(self, *args, **kwargs):
        self._type: type
        self._components = []
        self._id_generator = id_generator
        self._names = {}

    def add(self, comps=[]):
        for comp in comps:
            assert issubclass(type(comp), self._type)
            if comp._name is not None:
                self._names[comp.name] = comp
            self._components.append(comp)

    def remove(self, comp) -> bool:
        try:
            del self._components[(self._components.index(comp))]
            if comp.name in self._names:
                del self._names[comp.name]
            return True

        #TODO: Actually useful exception handling
        except Exception:
            return False

    def get_newest_comp_id(self) -> int:
        if len(self._components) > 0:
            return self._components[-1].comp_id
        else:
            return None

    def get(self, name: str = None, type: type = None, id: int = None) -> []:
        res = []

        if name is not None:
            if name in self._names:
                return[self._components[self._components.index(self._names[name])]]

        elif id is not None:
            for c in self._components:
                if c.comp_id == id:
                    res.append(c)
                    break

        elif type is not None:
            for c in self._components:
                if isinstance(c, type):
                    res.append(c)

        else:
            res = self._components

        return res
