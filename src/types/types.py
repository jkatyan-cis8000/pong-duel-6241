# Pong types
from typing import NamedTuple

class Position(NamedTuple):
    x: int
    y: int

class Velocity(NamedTuple):
    dx: int
    dy: int

class Paddle(NamedTuple):
    x: int
    y: int
    height: int
    width: int
    player: int

class Ball(NamedTuple):
    position: Position
    velocity: Velocity

class Score(NamedTuple):
    player1: int
    player2: int

class GameState(NamedTuple):
    paddle1: Paddle
    paddle2: Paddle
    ball: Ball
    score: Score
    game_over: bool
    winner: int | None = None
