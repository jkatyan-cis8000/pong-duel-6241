# Pong service - game logic
from src.config import PADDLE_SPEED, PADDLE_HEIGHT, SCREEN_HEIGHT, SCREEN_WIDTH, BALL_SPEED
from src.types.types import Ball, Paddle, GameState, Score, Velocity
from src.utils import detect_collision, reflect_ball, is_wall_collision, reset_ball, update_position

def update_ball_position(ball: Ball) -> Ball:
    """Move ball based on velocity."""
    new_pos = update_position(ball.position, ball.velocity)
    return Ball(position=new_pos, velocity=ball.velocity)

def check_wall_collision(ball: Ball) -> Ball:
    """Bounce ball off top/bottom walls."""
    if is_wall_collision(ball):
        new_velocity = Velocity(dx=ball.velocity.dx, dy=-ball.velocity.dy)
        return Ball(position=ball.position, velocity=new_velocity)
    return ball

def check_paddle_collision(ball: Ball, paddle: Paddle) -> Ball:
    """Bounce ball off paddle if collision detected."""
    if detect_collision(ball, paddle):
        return reflect_ball(ball, paddle)
    return ball

def update_paddle_position(paddle: Paddle, direction: str) -> Paddle:
    """Move paddle up or down within screen bounds."""
    if direction == 'up':
        new_y = max(0, paddle.y - PADDLE_SPEED)
    elif direction == 'down':
        new_y = min(SCREEN_HEIGHT - PADDLE_HEIGHT, paddle.y + PADDLE_SPEED)
    else:
        new_y = paddle.y
    
    return Paddle(
        x=paddle.x,
        y=new_y,
        height=paddle.height,
        width=paddle.width,
        player=paddle.player
    )

def check_score(ball: Ball, score: Score) -> tuple[Score, bool]:
    """
    Check if ball went past a paddle (scored).
    Returns new score and whether a point was scored.
    """
    scored = False
    new_score = score
    
    if ball.position.x <= 0:
        # Player 2 scored
        new_score = Score(player1=score.player1, player2=score.player2 + 1)
        scored = True
    elif ball.position.x >= SCREEN_WIDTH - 1:
        # Player 1 scored
        new_score = Score(player1=score.player1 + 1, player2=score.player2)
        scored = True
    
    return new_score, scored

def check_game_over(score: Score) -> tuple[bool, int | None]:
    """
    Check if anyone won.
    Returns (game_over, winner) where winner is player number or None.
    """
    if score.player1 >= 5:
        return True, 1
    elif score.player2 >= 5:
        return True, 2
    return False, None

def reset_after_score() -> Ball:
    """Reset ball for new point."""
    return reset_ball()

def update_game_state(
    state: GameState,
    p1_move: str,
    p2_move: str
) -> GameState:
    """
    Update game state for one frame.
    Returns new game state.
    """
    # Update paddle positions
    paddle1 = update_paddle_position(state.paddle1, p1_move)
    paddle2 = update_paddle_position(state.paddle2, p2_move)
    
    # Update ball
    ball = state.ball
    ball = update_ball_position(ball)
    ball = check_wall_collision(ball)
    ball = check_paddle_collision(ball, paddle1)
    ball = check_paddle_collision(ball, paddle2)
    
    # Check for score
    score, point_scored = check_score(ball, state.score)
    
    # Reset ball if point scored
    if point_scored:
        ball = reset_after_score()
    
    # Check for game over
    game_over, winner = check_game_over(score)
    
    return GameState(
        paddle1=paddle1,
        paddle2=paddle2,
        ball=ball,
        score=score,
        game_over=game_over,
        winner=winner
    )
