"""
This module contains all functions in the pyrogue library package. This package
is a wrapper for the `pygame` library which provides a simple function-based API 
for creating roguelike or other ASCII-tile based games.
"""

################################# I M P O R T S ################################

# Standard Library imports:
import random
from typing import IO, List, Tuple, Union

# Third-party imports:
import pygame

######################## C O L O R    C O N S T A N T S ########################

COLOR_BLACK: Tuple[int, int, int] = (0, 0, 0)
COLOR_BLUE: Tuple[int, int, int] = (0, 0, 255)
COLOR_CYAN: Tuple[int, int, int] = (0, 255, 255)
COLOR_FUCHSIA: Tuple[int, int, int] = (255, 0, 255)
COLOR_GRAY: Tuple[int, int, int] = (128, 128, 128)
COLOR_GREEN: Tuple[int, int, int] = (0, 128, 0)
COLOR_LIME: Tuple[int, int, int] = (0, 255, 0)
COLOR_MAROON: Tuple[int, int, int] = (128, 0, 0)
COLOR_NAVY: Tuple[int, int, int] = (0, 0, 128)
COLOR_OLIVE: Tuple[int, int, int] = (128, 128, 0)
COLOR_PURPLE: Tuple[int, int, int] = (128, 0, 128)
COLOR_RED: Tuple[int, int, int] = (255, 0, 0)
COLOR_SILVER: Tuple[int, int, int] = (192, 192, 192)
COLOR_TEAL: Tuple[int, int, int] = (0, 128, 128)
COLOR_YELLOW: Tuple[int, int, int] = (255, 255, 0)
COLOR_WHITE: Tuple[int, int, int] = (255, 255, 255)

######################## E V E N T    C O N S T A N T S ########################

EVENT_ACTIVE_EVENT: int = pygame.ACTIVEEVENT
EVENT_KEYDOWN: int = pygame.KEYDOWN
EVENT_KEYUP: int = pygame.KEYUP
EVENT_MOUSE_BUTTONDOWN: pygame.MOUSEBUTTONDOWN
EVENT_MOUSE_BUTTONUP: pygame.MOUSEBUTTONUP
EVENT_MOUSE_MOTION: int = pygame.MOUSEMOTION
EVENT_QUIT: int = pygame.QUIT
EVENT_VID_EXPOSE: int = pygame.VIDEOEXPOSE
EVENT_VID_RESIZE: int = pygame.VIDEORESIZE

########################## K E Y    C O N S T A N T S ##########################

KEY_0: int = pygame.K_0
KEY_1: int = pygame.K_1
KEY_2: int = pygame.K_2
KEY_3: int = pygame.K_3
KEY_4: int = pygame.K_4
KEY_5: int = pygame.K_5
KEY_6: int = pygame.K_6
KEY_7: int = pygame.K_7
KEY_8: int = pygame.K_8
KEY_9: int = pygame.K_9
KEY_A: int = pygame.K_a
KEY_AMPERSAND: int = pygame.K_AMPERSAND
KEY_ANDROID_BACK: int = pygame.K_AC_BACK
KEY_ASTERISK: int = pygame.K_ASTERISK
KEY_AT: int = pygame.K_AT
KEY_B: int = pygame.K_b
KEY_BACKQUOTE: int = pygame.K_BACKQUOTE
KEY_BACKSLASH: int = pygame.K_BACKSLASH
KEY_BACKSPACE: int = pygame.K_BACKSPACE
KEY_BREAK: int = pygame.K_BREAK
KEY_C: int = pygame.K_c
KEY_CAPSLOCK: int = pygame.K_CAPSLOCK
KEY_CARET: int = pygame.K_CARET
KEY_CLEAR: int = pygame.K_CLEAR
KEY_COLON: int = pygame.K_COLON
KEY_COMMA: int = pygame.K_COMMA
KEY_D: int = pygame.K_d
KEY_DELETE: int = pygame.K_DELETE
KEY_DOLLAR: int = pygame.K_DOLLAR
KEY_DOWN: int = pygame.K_DOWN
KEY_E: int = pygame.K_e
KEY_EQUALS: int = pygame.K_EQUALS
KEY_END: int = pygame.K_END
KEY_ENTER: int = pygame.K_RETURN
KEY_ESCAPE: int = pygame.K_ESCAPE
KEY_EURO: int = pygame.K_EURO
KEY_EXCLAIM: int = pygame.K_EXCLAIM
KEY_F: int = pygame.K_f
KEY_F1: int = pygame.K_F1
KEY_F10: int = pygame.K_F10
KEY_F11: int = pygame.K_F11
KEY_F12: int = pygame.K_F12
KEY_F13: int = pygame.K_F13
KEY_F14: int = pygame.K_F14
KEY_F15: int = pygame.K_F15
KEY_F2: int = pygame.K_F2
KEY_F3: int = pygame.K_F3
KEY_F4: int = pygame.K_F4
KEY_F5: int = pygame.K_F5
KEY_F6: int = pygame.K_F6
KEY_F7: int = pygame.K_F7
KEY_F8: int = pygame.K_F8
KEY_F9: int = pygame.K_F9
KEY_G: int = pygame.K_g
KEY_GREATER: int = pygame.K_GREATER
KEY_H: int = pygame.K_h
KEY_HASH: int = pygame.K_HASH
KEY_HELP: int = pygame.K_HELP
KEY_HOME: int = pygame.K_HOME
KEY_I: int = pygame.K_i
KEY_INSERT: int = pygame.K_INSERT
KEY_J: int = pygame.K_j
KEY_K: int = pygame.K_k
KEY_KP0: int = pygame.K_KP0
KEY_KP1: int = pygame.K_KP1
KEY_KP2: int = pygame.K_KP2
KEY_KP3: int = pygame.K_KP3
KEY_KP4: int = pygame.K_KP4
KEY_KP5: int = pygame.K_KP5
KEY_KP6: int = pygame.K_KP6
KEY_KP7: int = pygame.K_KP7
KEY_KP8: int = pygame.K_KP8
KEY_KP9: int = pygame.K_KP9
KEY_KP_PERIOD: int = pygame.K_KP_PERIOD
KEY_KP_DIVIDE: int = pygame.K_KP_DIVIDE
KEY_KP_MULTIPLY: int = pygame.K_KP_MULTIPLY
KEY_KP_MINUS: int = pygame.K_KP_MINUS
KEY_KP_PLUS: int = pygame.K_KP_PLUS
KEY_KP_ENTER: int = pygame.K_KP_ENTER
KEY_KP_EQUALS: int = pygame.K_KP_EQUALS
KEY_L: int = pygame.K_l
KEY_LEFT: int = pygame.K_LEFT
KEY_LEFTALT: int = pygame.K_LALT
KEY_LEFTBRACKET: int = pygame.K_LEFTBRACKET
KEY_LEFTCTRL: int = pygame.K_LCTRL
KEY_LEFTMETA: int = pygame.K_LMETA
KEY_LEFTPAREN: int = pygame.K_LEFTPAREN
KEY_LEFTSHIFT: int = pygame.K_LSHIFT
KEY_LEFTWIN: int = pygame.K_LSUPER
KEY_LESS: int =  pygame.K_LESS
KEY_M: int = pygame.K_m
KEY_MENU: int = pygame.K_MENU
KEY_MINUS: int = pygame.K_MINUS
KEY_MODE: int = pygame.K_MODE
KEY_N: int = pygame.K_n
KEY_NUMLOCK: int = pygame.K_NUMLOCK
KEY_P: int = pygame.K_p
KEY_PAGEDOWN: int = pygame.K_PAGEUP
KEY_PAGEUP: int = pygame.K_PAGEUP
KEY_PAUSE: int = pygame.K_PAUSE
KEY_PERIOD: int = pygame.K_PERIOD
KEY_POWER: int = pygame.K_POWER
KEY_PLUS: int = pygame.K_PLUS
KEY_PRINTSCREEN: int = pygame.K_PRINT
KEY_Q: int = pygame.K_q
KEY_QUESTION: int = pygame.K_QUESTION
KEY_QUOTE: int = pygame.K_QUOTE
KEY_QUOTEDBL: int = pygame.K_QUOTEDBL
KEY_R: int = pygame.K_r
KEY_RIGHT: int = pygame.K_RIGHT
KEY_RIGHTALT: int = pygame.K_RALT
KEY_RIGHTBRACKET: int = pygame.K_RIGHTBRACKET
KEY_RIGHTCTRL: int = pygame.K_RCTRL
KEY_RIGHTMETA: int = pygame.K_RMETA
KEY_RIGHTPAREN: int = pygame.K_RIGHTPAREN
KEY_RIGHTSHIFT: int = pygame.K_RSHIFT
KEY_RIGHTWIN: int = pygame.K_RSUPER
KEY_S: int = pygame.K_s
KEY_SCROLLOCK: int = pygame.K_SCROLLOCK
KEY_SEMICOLON: int = pygame.K_SEMICOLON
KEY_SLASH: int = pygame.K_SLASH
KEY_SPACE: int = pygame.K_SPACE
KEY_SYSREQ: int = pygame.K_SYSREQ
KEY_T: int = pygame.K_t
KEY_TAB: int = pygame.K_TAB
KEY_U: int = pygame.K_u
KEY_UNDERSCORE: int = pygame.K_UNDERSCORE
KEY_UP: int = pygame.K_UP
KEY_V: int = pygame.K_v
KEY_W: int = pygame.K_w
KEY_X: int = pygame.K_x
KEY_Y: int = pygame.K_y
KEY_Z: int = pygame.K_z

############################ G L O B A L    D A T A ############################

_screen: Union[pygame.Surface, None] = None     # Main display surface
_tsheet: Union[pygame.Surface, None] = None     # Tile sheet surface
_tsz: Union[int, None] = None                   # Tile size (in px.)
_uprects: List[pygame.Rect] = []                # List of rects. to redraw

################################# C L A S S E S ################################

class Tile(pygame.Surface):
    """
    A Tile is a single square ASCII character tile with a given background and
    foreground color.
    """

    def __init__(self, char: str, tsz: int, \
            bg: Tuple[int, int, int] = (0, 0, 0), \
            fg: Tuple[int, int, int] = (255, 255, 255)) -> "Tile":

        self.char: str                      # The character this tile represents
        self.bg: Tuple[int, int, int]       # Foreground color
        self.fg:  Tuple[int, int, int]      # Background color

        super().__init__((tsz, tsz))
        self.char = char
        self.bg = bg
        self.fg = fg
        return

##################### G R A P H I C S    F U N C T I O N S #####################

def draw_tile(tile: Tile, col: int, row: int) -> None:
    """
    Draw a tile to the screen at the given tile-space coordinates.

    ----------------------------------------------------------------------------
    v0.1.0:      Function added (kawright)
    """

    px_x: int               # x-cord. to draw tile (in px. space)
    px_y: int               # y-cord. to draw tile (in px. space)

    # Convert the coordinates to pixel space:
    px_x = col * _tsz
    px_y = row * _tsz

    # Blit the surface and store the resulting rect into _uprects:
    _uprects.append(_screen.blit(tile, (px_x, px_y)))
    return

def draw_tstr(tstr: List[Tile], col: int, row: int) -> None:
    """
    Draw a tile string to the screen at the given tile-space coordinates.

    ----------------------------------------------------------------------------
    v0.1.0:      Function added (kawright)
    """

    for i in range(len(tstr)):
        draw_tile(tstr[i], col+i, row)
    return

def flip() -> None:
    """
    Update the contents of the entire display.

    This is an expensive function, since the entire display is updated. In
    almost all cases, you will want to use `update` instead.
    
    ----------------------------------------------------------------------------
    v0.1.0:      Function added (kawright)
    """

    pygame.display.flip()
    return

def get_tile(code: int, bg: Tuple[int, int, int] = (0, 0, 0), \
        fg: Tuple[int, int, int] = (255, 255, 255)) -> Tile:
    """
    Get a single tile directly from the master tilesheet with the given colors.

    ----------------------------------------------------------------------------
    v0.1.0:      Function added (kawright)
    """

    tile_x: int                     # The x-position of the tile on the sheet
    tile_y: int                     # The y-position of the tile on the sheet
    px_x: int                       # The x-position of the tile in px.
    px_y: int                       # The y-position of the tile in px.
    tile_rect: pygame.Rect          # The rect for the given tile

    # Transform the given ascii code into tile-space coordinates:
    tile_x = code % 16
    tile_y = code // 16

    # Transform the tile-space coordinates into pixel-space coordinates:
    px_x = tile_x * _tsz
    px_y = tile_y * _tsz

    # Create a Rect to store the portion of the master sheet we want to return:
    tile_rect = pygame.Rect(px_x, px_y, _tsz, _tsz)

    # Build the surface to return:
    ret = Tile(chr(code), _tsz, bg, fg)

    ret.blit(_tsheet, (0, 0), tile_rect)

    # Set the colors:
    with pygame.PixelArray(ret) as pxarr:
        pxarr.replace((255, 0, 255), bg)
        pxarr.replace((255, 255, 255), fg)
    return ret

def get_tstr(chars: str, bg: Tuple[int, int, int] = (0, 0, 0), \
        fg: Tuple[int, int, int] = (255, 255, 255)) -> List[Tile]:
    """
    Convert a `str` into a tile string (i.e. a `list` of tiles).

    ----------------------------------------------------------------------------
    v0.1.0:      Function added (kawright)
    """

    ret: List[Tile]                 # Return data

    ret = []
    for char in chars:
        ret.append(get_tile(ord(char), bg, fg))
    return ret

def invert_tile(tile: Tile) -> None:
    """
    Invert the colors of a given `Tile`.

    ----------------------------------------------------------------------------
    v0.1.0:     Function added (kawright)
    """

    temp_color: Tuple[int, int, int]        # Temp color to stage changes
    old_fg: Tuple[int, int, int]            # Old foreground color
    old_bg: Tuple[int, int, int]            # Old background color

    # Find a third temporary color to stage changes so as not to lose data:
    temp_color = rand_color()
    while ((temp_color == tile.fg) or (temp_color == tile.bg)):
        temp_color = rand_color()
    old_fg = tile.fg
    old_bg = tile.bg
    set_tile_fg(tile, temp_color)
    set_tile_bg(tile, old_fg)
    set_tile_fg(tile, old_bg)
    return

def rand_color() -> Tuple[int, int, int]:
    """
    Get a random color.

    ----------------------------------------------------------------------------
    v0.1.0:      Function added (kawright)
    """

    return (random.randint(0, 255), random.randint(0, 255), \
        random.randint(0, 255))

def set_mode(cols: int, rows: int, tsheet: IO, \
        bg: Tuple[int, int, int] = (0, 0, 0), full: bool = False) -> None:
    """
    Set the screen mode.

    `tsheet` is the path to an ASCII tile sheet image.

    ----------------------------------------------------------------------------
    v0.1.0:      Function added (kawright)
    """

    global _screen
    global _tsheet
    global _tsz

    dims: Tuple[int, int]               # Screen dimensions (in px.)
    
    _tsheet = pygame.image.load(tsheet)
    
    # Determine the size of a single tile:
    _tsz = _tsheet.get_size()[0] / 16

    # Calculate the screen dimensions:
    dims = (cols*_tsz, rows*_tsz)

    if full:
        _screen = pygame.display.set_mode(dims, pygame.FULLSCREEN)
    else:
        _screen = pygame.display.set_mode(dims)
    _screen.fill(bg)
    flip()
    return

def set_tile_bg(tile: Tile, color: Tuple[int, int, int]) -> None:
    """
    Set the background color of a given `Tile`.

    ----------------------------------------------------------------------------
    v0.1.0:      Function added (kawright)
    """

    with pygame.PixelArray(tile) as pxarr:
        pxarr.replace(tile.bg, color)
    tile.bg = color
    return

def set_tile_fg(tile: Tile, color: Tuple[int, int, int]) -> None:
    """
    Set the foreground color of a given `Tile`.

    ----------------------------------------------------------------------------
    v0.1.0:      Function added (kawright)
    """

    with pygame.PixelArray(tile) as pxarr:
        pxarr.replace(tile.fg, color)
    tile.fg = color
    return

def update() -> None:
    """
    Updates all tiles that have been drawn to since the last time `update` was
    called.

    ----------------------------------------------------------------------------
    v0.1.0:      Function added (kawright)
    """

    global _uprects

    # Update, then clear _uprects:
    pygame.display.update(_uprects)
    _uprects = []
    return

######################## E V E N T    F U N C T I O N S ########################

def get_events() -> List[pygame.event.Event]:
    """
    Get a list of all events currently in the event queue. All events will be
    removed from the queue before returning.

    ----------------------------------------------------------------------------
    v0.1.0:      Function added (kawright)
    """

    return pygame.event.get()

######################### T I M E    F U N C T I O N S #########################

def get_ticks() -> None:
    """
    Returns the number of milliseconds that have elapsed since `init` was
    called.

    ----------------------------------------------------------------------------
    v0.1.0:      Function added (kawright)
    """

    return pygame.time.get_ticks()

######################## O T H E R    F U N C T I O N S ########################

def init() -> None:
    """
    Initialize pyrogue. 
    
    This function MUST be called at the beginning of your `main` funcion,
    before any other `pyrogue` function is called.

    Calling this function calls pygame.init() in turn.

    ----------------------------------------------------------------------------
    v0.1.0:      Function added (kawright)
    """

    pygame.init()
    return

def quit() -> None:
    """
    Uninitializes pyrogue.

    This function MUST be called at the end of your `main` function.

    Calling this function calls pygame.quit() in turn.
    
    ----------------------------------------------------------------------------
    v0.1.0:      Function added (kawright)
    """

    pygame.quit()
    return
