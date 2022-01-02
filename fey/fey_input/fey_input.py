from dataclasses import dataclass, field
from enum import Enum, auto
from fey.fey_types import FeyDataclass, Point2D, Singleton
from typing import Union


class FeyKeyboardInput(Enum):
    ONE             = auto()
    TWO             = auto()
    THREE           = auto()
    FOUR            = auto()
    FIVE            = auto()
    SIX             = auto()
    SEVEN           = auto()
    EIGHT           = auto()
    NINE            = auto()
    TEN             = auto()
    ZERO            = auto()
    QUESTION_MARK   = auto()
    BACKSPACE       = auto()
    ESCAPE          = auto()
    CONSOLE         = auto()
    TAB             = auto()
    Q               = auto()
    W               = auto()
    E               = auto()
    R               = auto()
    T               = auto()
    Z               = auto()
    U               = auto()
    I               = auto()
    O               = auto()
    P               = auto()
    PLUS            = auto()
    CAPS_LOCK       = auto()
    A               = auto()
    S               = auto()
    D               = auto()
    F               = auto()
    G               = auto()
    H               = auto()
    J               = auto()
    K               = auto()
    L               = auto()
    HASHTAG         = auto()
    SHIFT           = auto()
    Y               = auto()
    X               = auto()
    C               = auto()
    V               = auto()
    B               = auto()
    N               = auto()
    M               = auto()
    COMMA           = auto()
    DOT             = auto()
    DASH            = auto()
    SHIFT_RIGHT     = auto()
    CTRL            = auto()
    ALT             = auto()
    SPACE           = auto()
    ALT_RIGHT       = auto()
    CTRL_RIGHT      = auto()
    DOWN            = auto()
    LEFT            = auto()
    RIGHT           = auto()
    ENTER           = auto()


class FeyGamepadInput(Enum):
    DPAD_UP     = auto()
    DPAD_DOWN   = auto()
    DPAD_LEFT   = auto()
    DPAD_RIGHT  = auto()
    START       = auto()
    BACK        = auto()
    BUTTON_1    = auto()
    BUTTON_2    = auto()
    BUTTON_3    = auto()
    BUTTON_4    = auto()
    RB          = auto()
    RT          = auto()
    LB          = auto()
    LT          = auto()
    STICK_LEFT  = auto()
    STICK_RIGHT = auto()


class FeyMouseInput(Enum):
    #TODO: Implement this
    ...


class FeyInputType(Enum):
    AXIS    = auto()
    BUTTON  = auto()
    TRIGGER = auto()


class FeyInputDevice(Enum):
    GAMEPAD  = auto()
    KEYBOARD = auto()
    MOUSE    = auto()


@dataclass(eq=True, frozen=True)
class FeyInput(FeyDataclass):
    device: FeyInputDevice
    type: FeyInputType
    input: Union[FeyGamepadInput, FeyKeyboardInput]
    timestamp: int
    value: Point2D = field(default=Point2D(0, 0))


