# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

This is a Flask-based interactive learning platform for Unix and networking concepts. Users learn through hands-on practice with a real terminal connected to a Docker sandbox.

## Tech Stack

- **Backend:** Flask 3.0+ with factory pattern
- **Frontend:** Alpine.js + HTMX + Tailwind CSS (loaded via CDN)
- **Sandbox:** Docker container based on Ubuntu 22.04
- **Templating:** Jinja2

## Build & Development Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Build Docker sandbox image
docker build -t linux-sandbox:latest docker/

# Run development server
python run.py

# Run with specific port
flask run --port 5001
```

## Architecture

### Concepts System
- `app/concepts/base.py` - `BaseConcept` dataclass defines structure
- `app/concepts/__init__.py` - Registration system for concepts
- `app/concepts/unix/` - Unix concept modules
- `app/concepts/networking/` - Networking concept modules

Each concept module creates a `BaseConcept` instance and registers it. The registration happens at import time.

### Routes
- `app/routes/main.py` - Home page, navigation
- `app/routes/concepts.py` - Concept listing and detail pages
- `app/routes/playground.py` - Terminal playground with Docker execution

### Terminal Sandbox
- `app/terminal/executor.py` - Execute commands in Docker containers
- `app/terminal/sandbox.py` - Manage persistent sandbox container

Commands run in isolated Docker containers with resource limits (256MB RAM, 50% CPU).

### Templates
- `base.html` - Main layout with Alpine.js, HTMX, Tailwind
- `index.html` - Home page
- `playground.html` - Interactive terminal
- `concepts/detail.html` - Individual concept pages
- `concepts/list.html` - All concepts listing

## Adding New Concepts

1. Create a new file in `app/concepts/unix/` or `app/concepts/networking/`
2. Define a `BaseConcept` with examples:
   ```python
   from app.concepts.base import BaseConcept, TryItExample
   from app.concepts import register_concept

   concept = BaseConcept(
       slug="my-concept",
       title="My Concept",
       category="unix",  # or "networking"
       difficulty="beginner",  # beginner/intermediate/advanced
       order=10,
       short_description="What this covers",
       commands=["cmd1", "cmd2"],
       try_it_examples=[
           TryItExample(
               title="Example Name",
               command="actual command",
               description="What it does"
           ),
       ],
       gotchas=["Common mistake 1"],
       related=["other-concept-slug"],
   )
   register_concept(concept)
   ```
3. Import the module in `app/concepts/__init__.py`

## Code Style

- Python: Standard Flask patterns, type hints where helpful
- Templates: Jinja2 with Tailwind CSS classes
- JavaScript: Alpine.js for interactivity, minimal custom JS

## Testing Locally

1. Ensure Docker is running
2. Build the sandbox image: `docker build -t linux-sandbox:latest docker/`
3. Start the app: `python run.py`
4. Open http://localhost:5000
5. Navigate to Playground and try running commands
