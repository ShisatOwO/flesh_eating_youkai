from __future__ import annotations
from fey.fey_components.comp_management import FeyComponentManagement
from abc import ABC


class FeyBaseComponent(FeyComponentManagement, ABC):
    def __init__(self, *args, **kwargs):
        self._type = type(self)
        ...
