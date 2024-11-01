# Petri

A hex-based game engine built in Python using an Entity Component System (ECS) architecture.

## Overview

This project implements a game engine that simulates units moving and interacting on a hexagonal grid. The engine uses an Entity Component System (ECS) pattern for flexible and modular game object management.

### Key Features

- Hexagonal grid system with pathfinding
- Entity Component System (ECS) architecture
- Unit movement and combat systems
- Automatic unit spawning system
- Turn-based gameplay

### Core Systems

- **Movement System**: Handles unit movement across the hex grid with pathfinding
- **Combat System**: Manages unit combat and health
- **Spawn System**: Controls the creation of new units
- **Unit System**: Manages unit behavior and interactions

### Technical Architecture

The project is structured around three main concepts:

1. **Entities**: Base game objects that serve as containers for components
2. **Components**: Data containers that define entity properties (Position, Combat, Unit, etc.)
3. **Systems**: Logic processors that operate on entities with specific components