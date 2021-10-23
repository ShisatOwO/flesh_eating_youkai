from fey import *


class DummyComponentA(FeyBaseComponent):
    def __init__(self, name: str, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)


class DummyComponentB(FeyBaseComponent):
    def __init__(self, name: str, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)


FeyGlobalConfig(
    FeyConfig(
        original_window_title="Test App",
        screen_dims=Box2D(0, 0, 1600, 1200),
        target_fps=60,
    ).custom_config({
        "test_value": 0
    })
)


FeyGlobalComponentTable([DummyComponentA("1")]).name("component_a")
FeyGlobalComponentTable([DummyComponentA("2")])
FeyGlobalComponentTable([DummyComponentA("3")]).name("component_b")

component_b = FeyGlobalComponentTable().get(name="component_b")[0].comp_id
print(f"\n\"component_b\" id: {component_b}")
print(FeyGlobalConfig().get_dict())
