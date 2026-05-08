# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

- src/types/__init__.py: Game type definitions (Position, Velocity, GameState, etc.)
- src/config/__init__.py: Configuration constants (screen size, paddle dimensions, speeds, winning score)
- src/repo/__init__.py: Repository layer - no persistent storage needed for Pong
- src/service/__init__.py: Service layer - game logic (ball movement, paddle movement, collision detection, scoring)
- src/providers/__init__.py: Cross-cutting concerns (input handling abstraction)
- src/utils/__init__.py: Utility functions (collision detection helpers, movement calculations)
- src/runtime/__init__.py: Application lifecycle and event loop
- src/ui/__init__.py: UI layer - terminal rendering and input handling

## Interfaces

### Types (src/types/__init__.py)
- Position(x: int, y: int): Coordinate point
- Velocity(dx: int, dy: int): Direction and speed
- Paddle(x: int, y: int, height: int, width: int, player: int): Paddle state
- Ball(position: Position, velocity: Velocity): Ball state
- Score(player1: int, player2: int): Score tracking
- GameState(paddle1: Paddle, paddle2: Paddle, ball: Ball, score: Score, game_over: bool): Complete game state

### Config (src/config/__init__.py)
- SCREEN_WIDTH: int
- SCREEN_HEIGHT: int
- PADDLE_WIDTH: int
- PADDLE_HEIGHT: int
- PADDLE_SPEED: int
- BALL_SPEED: int
- WINNING_SCORE: int

### Service (src/service/__init__.py)
- update_ball_position(ball: Ball) -> Ball: Move ball based on velocity
- check_wall_collision(ball: Ball) -> Ball: Bounce ball off top/bottom walls
- check_paddle_collision(ball: Ball, paddle: Paddle) -> Ball: Bounce ball off paddle
- update_paddle_position(paddle: Paddle, direction: str, bounds: tuple) -> Paddle: Move paddle up/down
- check_score(ball: Ball, score: Score) -> Score: Check if player scored
- reset_ball() -> Ball: Reset ball to center with random direction
- check_game_over(score: Score) -> bool: Check if anyone won

### UI (src/ui/__init__.py)
- render_game(state: GameState) -> str: Render game state to terminal
- get_input() -> str: Get player input (w/s for player 1, up/down for player 2)
- clear_screen() -> None: Clear terminal screen

### Runtime (src/runtime/__init__.py)
- main(): Entry point, orchestrates game loop

## Shared Data Structures

- All types defined in src/types/__init__.py are the single source of truth
- Game state flows: UI reads GameState, Service computes next state
- Input flows: UI gets input -> Runtime parses to command -> Service updates state

## External Dependencies

- Standard library only (no external dependencies needed for terminal Pong)
