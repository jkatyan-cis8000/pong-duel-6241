# Providers Layer

Cross-cutting concerns like auth, telemetry, input, connectors.

## Files
- `input.py`: Non-blocking input handling

## Purpose
Provide reusable functionality that cuts across multiple layers.

## Rules
- May import from: types, config, utils, providers (itself)
- Input handling is separated from UI for testability
