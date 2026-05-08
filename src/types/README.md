# Types Layer

Contains all pure type definitions for the Pong game. No logic here - just data structures.

## Files
- `types.py`: Game types (Position, Velocity, Paddle, Ball, Score, GameState)

## Purpose
Types are the single source of truth for data structures. All other layers depend on these types.

## Rules
- No imports from other layers (only self-imports if needed)
- No business logic
- No side effects
