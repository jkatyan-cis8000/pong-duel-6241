# Pong config - constants and settings
from src.types.types import Position, Velocity, Paddle, Ball, Score, GameState

# Screen dimensions
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 24

# Paddle dimensions
PADDLE_WIDTH = 2
PADDLE_HEIGHT = 6
PADDLE_OFFSET = 2  # Distance from edge

# Movement speeds
PADDLE_SPEED = 1
BALL_SPEED = 1

# Game settings
WINNING_SCORE = 5

# Initial positions
PADDLE1_X = PADDLE_OFFSET
PADDLE2_X = SCREEN_WIDTH - PADDLE_WIDTH - PADDLE_OFFSET
PADDLE_Y_START = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
BALL_POSITION_START = Position(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
BALL_VELOCITY_START = Velocity(BALL_SPEED, BALL_SPEED)

# Initial game state
INITIAL_PADDLE1 = Paddle(
    x=PADDLE1_X,
    y=PADDLE_Y_START,
    height=PADDLE_HEIGHT,
    width=PADDLE_WIDTH,
    player=1
)

INITIAL_PADDLE2 = Paddle(
    x=PADDLE2_X,
    y=PADDLE_Y_START,
    height=PADDLE_HEIGHT,
    width=PADDLE_WIDTH,
    player=2
)

INITIAL_BALL = Ball(
    position=BALL_POSITION_START,
    velocity=BALL_VELOCITY_START
)

INITIAL_SCORE = Score(player1=0, player2=0)

INITIAL_GAME_STATE = GameState(
    paddle1=INITIAL_PADDLE1,
    paddle2=INITIAL_PADDLE2,
    ball=INITIAL_BALL,
    score=INITIAL_SCORE,
    game_over=False,
    winner=None
)
