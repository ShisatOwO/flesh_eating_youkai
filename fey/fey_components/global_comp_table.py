from fey.fey_types import Singleton
from fey.fey_components.comp_management import FeyComponentManagement
from fey.fey_components.base_component import FeyBaseComponent
from fey.src.utility import id_generator


class FeyGlobalComponentTable(FeyComponentManagement, Singleton):
    _type: type
    _components = []
    _id_generator = id_generator
    _names = {}

    def __init__(self, components: [FeyBaseComponent, ] = []):
        self._type = FeyBaseComponent

        if isinstance(components, list):
            self.add(components)
        else:
            raise ValueError("'fey_components' must be of type list.")
