from fey import *
from custom_components.dummy_components import *
from fey import Component as Comp


run_context = init(
    FeyConfig(
        original_window_title="Test App",
    )
)


FeyGlobalComponentTable([
    Comp.Empty(name="root0", pos=Point2D(100, 50), dim=FeyGlobalConfig().screen_dims.dim.copy(), comps=[
        Comp.Sprite(pos=Point2D(0, 0), dim=Point2D(40, 40), color=(255, 0, 0), name="sprite1"),
        DummyComponentB(pname="Component B\tDepth: 1", name="root0/b1", pos=Point2D(20, 20), comps=[
            Comp.Sprite(pos=Point2D(0, 0), dim=Point2D(40, 40), color=(0, 255, 0), name="sprite2")
        ]),
        Comp.Render(),
    ])
])

print(FeyGlobalComponentTable().qget("root0").qsearch("sprite2").box.pos)


run(*run_context)
