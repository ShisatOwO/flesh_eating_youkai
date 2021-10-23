from __future__ import annotations
from fey.src.utility import generate_id
from abc import ABC


class FeyComponentManagement(ABC):
    _type: type = None
    _components: [_type, ] = []
    _id_generator = generate_id()
    _names = {}

    def add(self, comps: [_type, ]):
        for comp in comps:
            assert issubclass(type(comp), self._type)
            comp.comp_id = next(self._id_generator)
            self._components.append(comp)

    def name(self, name: str, comp_id: int = None):
        if comp_id is None:
            comp_id = self.get_newest_comp_id()

        if comp_id is not None or len(self.get(id=comp_id)) == 1:
            self._names[name] = comp_id
        else:
            raise ValueError("Component Id does not exist")

    def get_newest_comp_id(self) -> int:
        if len(self._components) > 0:
            return self._components[-1].comp_id
        else:
            return None

    def get(self, name: str = None, type: type = None, id: int = None) -> [_type, ]:
        res = []

        if name is not None:
            return[self._components[self._names[name]]]

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
