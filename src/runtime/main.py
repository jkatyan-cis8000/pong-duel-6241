# Pong runtime - main entry point
import time
import sys
from src.config import INITIAL_GAME_STATE
from src.types import GameState
from src.providers import get_key_timeout, get_player_input
from src.service import update_game_state
from src.ui import clear_screen, render_game

def main() -> None:
    """Main game loop."""
    state = INITIAL_GAME_STATE
    
    print("Welcome to Pong Duel!")
    print("Player 1: W/S keys | Player 2: Up/Down arrows")
    print("First to 5 points wins!")
    print("")
    print("Press any key to start...")
    sys.stdin.read(1)
    
    while not state.game_over:
        # Get input (non-blocking)
        p1_key = get_key_timeout(timeout=0.016)
        p2_key = get_key_timeout(timeout=0.016)
        
        p1_move, p2_move = get_player_input(p1_key, p2_key)
        
        # Update game state
        state = update_game_state(state, p1_move, p2_move)
        
        # Render
        clear_screen()
        screen = render_game(state)
        print(screen, end='\r')
        
        # Small delay to control game speed
        time.sleep(0.016)
    
    # Final render to show game over
    clear_screen()
    print(render_game(state))

if __name__ == '__main__':
    main()
