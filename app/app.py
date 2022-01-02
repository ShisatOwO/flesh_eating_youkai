from fey import *
from fey.fey_input import *
from fey import Component as Comp

run_context = init(
    FeyConfig(
        original_window_title="Test App",
        target_fps=150,
    )
)


FeyGlobalComponentTable([
    Comp.Empty(name="Scene_01", comps=[
        Comp.Empty(name="ui_cam", comps=[
            Comp.Empty(name="Ruler", comps=[
               Comp.Sprite(color=(0, 255, 0), dim=Point2D(100, 10))
            ]),
            Comp.Render(),
        ]),
        Comp.Empty(name="scene_cam", comps=[
            Comp.Empty(name="Entity", pos=Point2D(0, 15), comps=[
                Comp.Sprite(color=(255, 0, 0), dim=Point2D(50, 50))
            ]),
            Comp.Render(),
        ]),

    ]),
])


run(*run_context)
