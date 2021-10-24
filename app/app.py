from fey import *


class DummyComponentA(FeyBaseComponent):
    def __init__(self, pname: str, *args, **kwargs):
        self._name = pname
        super().__init__(*args, **kwargs)


class DummyComponentB(FeyBaseComponent):
    def __init__(self, pname: str, *args, **kwargs):
        self._name = pname
        super().__init__(*args, **kwargs)


class DummyComponentC(FeyBaseComponent):
    def __init__(self, pname: str, *args, **kwargs):
        self._name = pname
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

FeyGlobalComponentTable([
    DummyComponentA(pname="C:A L:0", comps=[
        DummyComponentB(pname="C:B L:1"),
        DummyComponentB(pname="C:C L1"),
    ]),
    DummyComponentA(pname="C:A L:0", name="root1", comps=[
        DummyComponentC(pname="C:C L:1", name="person1", comps=[
            DummyComponentB(pname="C:C L:2", name="person2")
        ]),
    ]),
])

print(FeyGlobalComponentTable().get("root1")[0].search("person2"))
FeyGlobalComponentTable().get("root1")[0].search("person1")[0].disable()
print(FeyGlobalComponentTable().get("root1")[0].search("person2"))
FeyGlobalComponentTable().get("root1")[0].search("person1")[0].enable()

print(FeyGlobalComponentTable().get("root1")[0].search("person2"))
print(FeyGlobalComponentTable().get("root1")[0].search("person1")[0].suicide())
print(FeyGlobalComponentTable().get("root1")[0].search("person2"))
