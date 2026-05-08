# Pong utils - helper functions
from src.config import SCREEN_HEIGHT, BALL_SPEED
from src.types.types import Ball, Position, Velocity, Paddle
import random

def detect_collision(ball: Ball, paddle: Paddle) -> bool:
    """Check if ball collides with paddle."""
    ball_pos = ball.position
    paddle_top = paddle.y
    paddle_bottom = paddle.y + paddle.height
    paddle_left = paddle.x
    paddle_right = paddle.x + paddle.width
    
    return (
        paddle_left <= ball_pos.x <= paddle_right and
        paddle_top <= ball_pos.y <= paddle_bottom
    )

def reflect_ball(ball: Ball, paddle: Paddle) -> Ball:
    """Reflect ball velocity after collision with paddle."""
    # Reverse horizontal direction and increase speed slightly
    new_dx = -ball.velocity.dx
    new_dy = ball.velocity.dy
    
    # Add some variation based on where ball hit the paddle
    hit_pos = ball.position.y - paddle.y
    normalized_hit = hit_pos / paddle.height - 0.5  # -0.5 to 0.5
    new_dy = int(normalized_hit * 3)  # Add vertical variation
    
    # Ensure minimum vertical speed
    if new_dy == 0:
        new_dy = 1
    
    return Ball(
        position=ball.position,
        velocity=Velocity(dx=new_dx, dy=new_dy)
    )

def is_wall_collision(ball: Ball) -> bool:
    """Check if ball has hit top or bottom wall."""
    return ball.position.y <= 0 or ball.position.y >= SCREEN_HEIGHT - 1

def reset_ball() -> Ball:
    """Reset ball to center with random direction."""
    position = Position(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    # Random upward or downward start
    dy = random.choice([-1, 1]) * BALL_SPEED
    dx = random.choice([-1, 1]) * BALL_SPEED
    return Ball(
        position=position,
        velocity=Velocity(dx=dx, dy=dy)
    )

def update_position(pos: Position, vel: Velocity) -> Position:
    """Update position based on velocity."""
    return Position(x=pos.x + vel.dx, y=pos.y + vel.dy)
