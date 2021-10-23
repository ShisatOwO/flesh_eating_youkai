from fey.fey_types import Singleton
from fey.fey_components.comp_management import FeyComponentManagement
from fey.fey_components.base_component import FeyBaseComponent


class FeyGlobalComponentTable(Singleton, FeyComponentManagement):
    _type = FeyBaseComponent

    def __init__(self, components: [FeyBaseComponent, ]=[]):
        if isinstance(components, list):
            self.add(components)
        else:
            raise ValueError("'fey_components' must be of type list.")
