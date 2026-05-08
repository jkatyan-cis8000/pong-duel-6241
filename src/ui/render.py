# Pong ui - rendering and input handling
import os
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT
from src.types.types import GameState, Paddle

def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')

def render_game(state: GameState) -> str:
    """
    Render game state to a string.
    Returns the complete screen buffer.
    """
    # Create empty screen buffer
    buffer = [[' ' for _ in range(SCREEN_WIDTH)] for _ in range(SCREEN_HEIGHT)]
    
    # Draw paddles
    _draw_paddle(buffer, state.paddle1)
    _draw_paddle(buffer, state.paddle2)
    
    # Draw ball
    ball_x = state.ball.position.x
    ball_y = state.ball.position.y
    if 0 <= ball_x < SCREEN_WIDTH and 0 <= ball_y < SCREEN_HEIGHT:
        buffer[ball_y][ball_x] = 'O'
    
    # Build output string
    lines = []
    
    # Score board
    score_line = f" Player 1: {state.score.player1} | Player 2: {state.score.player2} ".center(SCREEN_WIDTH)
    lines.append(score_line)
    lines.append("-" * SCREEN_WIDTH)
    
    # Game area
    for row in buffer:
        lines.append(''.join(row))
    
    # Game over message
    if state.game_over:
        winner = f"Player {state.winner}" if state.winner else "Draw"
        lines.append("")
        lines.append(f" GAME OVER - {winner} WINS! ".center(SCREEN_WIDTH, '='))
    
    return '\n'.join(lines)

def _draw_paddle(buffer: list[list[str]], paddle: Paddle) -> None:
    """Draw a paddle on the buffer."""
    for y in range(paddle.y, paddle.y + paddle.height):
        if 0 <= y < SCREEN_HEIGHT:
            for x in range(paddle.x, paddle.x + paddle.width):
                if 0 <= x < SCREEN_WIDTH:
                    buffer[y][x] = '#'
