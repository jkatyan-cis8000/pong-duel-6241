# Runtime Layer

Application lifecycle, orchestration, and wiring.

## Files
- `main.py`: Entry point, main game loop

## Purpose
Starts the application, orchestrates the flow between layers.

## Rules
- May import from: types, config, repo, service, providers, runtime (itself)
- Contains glue code that connects all layers
