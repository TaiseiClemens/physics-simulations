# Physics Simulations

A collection of interactive physics simulations built with Python and Pygame, demonstrating various classical mechanics concepts through real-time visualization.

## Overview

This project contains multiple physics simulation demos that visualize fundamental concepts in classical mechanics. Each simulation uses numerical methods to solve equations of motion and renders the results in real-time using Pygame.

## Features

- **Real-time visualization** of physics phenomena
- **Adjustable time multiplier** for faster/slower simulations
- **Multiple simulation scenarios** covering different physics concepts
- **Accurate physics modeling** using numerical integration

## Simulations

### 1. Single Projectile Motion
**Location:** `demos/single_projectile/`

Simulates projectile motion under constant acceleration (gravity). Demonstrates:
- Kinematic equations of motion
- Parabolic trajectory
- Constant gravitational acceleration

**Run:**
```bash
python demos/single_projectile/main.py
```

### 2. Gravitational Bodies (N-Body Problem)
**Location:** `demos/gravitational_bodies/`

Simulates gravitational interactions between multiple celestial bodies. Demonstrates:
- Newton's law of universal gravitation
- N-body dynamics
- Orbital mechanics

**Run:**
```bash
python demos/gravitational_bodies/main.py
```

### 3. Elastic Collisions
**Location:** `demos/elastic_collisions/`

Simulates elastic collisions between multiple disks with barrier constraints. Demonstrates:
- Conservation of momentum
- Conservation of kinetic energy
- Collision detection and response
- Multi-body collision dynamics

**Run:**
```bash
python demos/elastic_collisions/main.py
```

### 4. Simple Pendulum
**Location:** `demos/simple_pendulum/`

Simulates pendulum motion with both exact and simple harmonic motion (SHM) approximations. Demonstrates:
- Rotational dynamics
- Simple harmonic motion approximation
- Nonlinear vs. linear pendulum equations
- Angular motion

**Run:**
```bash
python demos/simple_pendulum/main.py
```

## Requirements

- Python >= 3.14
- pygame >= 2.6.1
- numpy >= 2.4.0

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd physics-simulations
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies using uv (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install -e .
```

## Usage

Each simulation can be run independently by executing its main.py file:

```bash
python demos/<simulation_name>/main.py
```

### Controls

- **Close window** or **ESC** to exit the simulation
- Time multiplier can be adjusted in each demo's `constants.py` file

## Project Structure

```
physics-simulations/
├── demos/
│   ├── single_projectile/     # Projectile motion simulation
│   │   ├── main.py
│   │   ├── projectile.py
│   │   └── constants.py
│   ├── gravitational_bodies/  # N-body gravitational simulation
│   │   ├── main.py
│   │   ├── planet.py
│   │   ├── physical_object.py
│   │   └── constants.py
│   ├── elastic_collisions/    # Collision dynamics simulation
│   │   ├── main.py
│   │   ├── disk.py
│   │   └── constants.py
│   └── simple_pendulum/       # Pendulum motion simulation
│       ├── main.py
│       ├── pendulum.py
│       ├── SHM_pendulum.py
│       └── constants.py
├── main.py
├── pyproject.toml
└── README.md
```

## Physics Concepts

### Numerical Integration
All simulations use numerical integration methods (typically Euler's method or variants) to solve differential equations of motion in real-time.

### Time Scaling
Each simulation includes a `TIME_MULTIPLIER` constant that allows speeding up or slowing down the simulation while maintaining physics accuracy.

### Coordinate Systems
- Simulations use a physics coordinate system (meters, seconds, kilograms)
- Screen coordinates are converted using `PIXELS_PER_METER` scaling factor
- Origin typically centered on screen for gravitational and collision simulations

## Configuration

Each demo has its own `constants.py` file where you can adjust:
- Screen dimensions (`SCREEN_WIDTH`, `SCREEN_HEIGHT`)
- Physics parameters (masses, initial velocities, etc.)
- Time multiplier for simulation speed
- Scaling factors (`PIXELS_PER_METER`)

## Development

The project uses:
- **uv** for dependency management
- **pygame** for rendering and game loop
- **numpy** for mathematical operations

## License

This is a personal educational project. Feel free to use, modify, and distribute the code as you wish.
