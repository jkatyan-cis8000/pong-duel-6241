# Pong providers - input handling
import sys
import termios
import tty
import select

def get_key_timeout(timeout: float = 0.016) -> str | None:
    """
    Get a single keypress with timeout (for non-blocking input).
    Returns None if no input within timeout.
    """
    dr, _, _ = select.select([sys.stdin], [], [], timeout)
    if dr:
        # Read raw bytes and decode
        ch = sys.stdin.read(1)
        return ch
    return None

def get_player_input(p1_input: str | None, p2_input: str | None) -> tuple[str, str]:
    """
    Map raw input to paddle directions.
    Player 1: w/s keys
    Player 2: up arrow/down arrow (or i/k as alternatives)
    """
    p1_move = 'none'
    p2_move = 'none'
    
    if p1_input == 'w':
        p1_move = 'up'
    elif p1_input == 's':
        p1_move = 'down'
    
    if p2_input == '\x1b[A':  # Up arrow
        p2_move = 'up'
    elif p2_input == '\x1b[B':  # Down arrow
        p2_move = 'down'
    elif p2_input == 'i':
        p2_move = 'up'
    elif p2_input == 'k':
        p2_move = 'down'
    
    return p1_move, p2_move
