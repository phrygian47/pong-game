import pathlib
from re import M
from casting.color import Color
from random import randint

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME

GAME_NAME = "Air Hockey"
FRAME_RATE = 60

# SCREEN  
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "assets/sounds/boing.wav"
SCORE_SOUND = "assets/sounds/point_gain.mp3"
OVER_SOUND = "assets/sounds/win.mp3"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
P1_UP = "w"
P1_DOWN = "s"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"
P2_UP = "up"
P2_DOWN = "down"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_R_GROUP = "r_stats"
STATS_L_GROUP = "l_stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
SCORE_R_GROUP = "score_r"
SCORE_L_GROUP = "score_l"
SCORE_R_FORMAT = "PLAYER 1 SCORE: {}"
SCORE_L_FORMAT = "PLAYER 2 SCORE: {}"
#MIDDLE
MIDDLE_GROUP = 'middle'
MIDDLE_IMAGE = "assets/images/middle_1.png"
MIDDLE_HEIGHT = SCREEN_HEIGHT
# BALL 
BALL_GROUP = "balls"
BALL_IMAGE = "assets/images/ball.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 6

# PADDLES
PADDLE_R_GROUP = "paddles_r"
PADDLE_L_GROUP = "paddles_l"

PADDLE_COLOR_L = ["assets/images/pong_l.png","assets/images/pong_l1.png","assets/images/pong_l2.png", "assets/images/pong_l3.png", "assets/images/pong_l4.png"]

PADDLE_COLOR_R = ["assets/images/pong_r.png","assets/images/pong_r1.png","assets/images/pong_r2.png", "assets/images/pong_r3.png", "assets/images/pong_r4.png"]


PADDLE_IMAGE_L = "assets/images/pong_l.png"
PADDLE_IMAGE_R = "assets/images/pong_r.png"

PADDLE_WIDTH = 28
PADDLE_HEIGHT = 106
PADDLE_RATE = 6
PADDLE_VELOCITY = 7

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START\nDON'T LET THE BALL GET PAST YOUR PADDLE!\nFIRST TO 10 WINS."
PREP_TO_START = "GET READY"
PLAYER_1_WINS = "PLAYER 1 WINS!"
PLAYER_2_WINS = "PLAYER 2 WINS!"