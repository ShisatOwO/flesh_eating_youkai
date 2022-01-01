from fey.fey_components import FeyBaseComponent
from fey.config import FeyConfig


class Empty(FeyBaseComponent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.box.dim = FeyConfig.screen_dims.dim.copy()
