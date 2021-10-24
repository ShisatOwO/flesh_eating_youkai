from fey import *


run_context = init(
    FeyConfig(
        original_window_title="Test App",
    )
)


run(*run_context)
