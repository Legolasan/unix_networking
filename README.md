# Unix & Networking Learning Platform

An interactive web application for learning Unix command-line and networking concepts through hands-on practice in a safe Docker sandbox environment.

## Features

- **Interactive Terminal Playground** - Execute real commands in a Docker sandbox
- **Structured Learning** - Concepts organized by difficulty (beginner → advanced)
- **Try It Examples** - Pre-configured commands for each concept
- **Safe Environment** - Experiment freely without risk

## Quick Start

### Prerequisites

- Python 3.10+
- Docker (running)

### Setup

1. **Clone and install dependencies:**
   ```bash
   cd linux_networking
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Build the Docker sandbox image:**
   ```bash
   docker build -t linux-sandbox:latest docker/
   ```

3. **Run the application:**
   ```bash
   python run.py
   ```

4. **Open in browser:**
   ```
   http://localhost:5000
   ```

## Project Structure

```
linux_networking/
├── app/
│   ├── __init__.py          # Flask factory
│   ├── concepts/            # Learning concepts (Unix, Networking)
│   ├── routes/              # Route handlers
│   ├── terminal/            # Docker sandbox execution
│   ├── templates/           # Jinja2 templates
│   └── static/              # Static assets
├── docker/
│   └── Dockerfile           # Sandbox image
├── run.py                   # Entry point
└── requirements.txt
```

## Concepts Covered

### Unix (Beginner)
- Unix Basics - Terminal fundamentals, shell concepts
- File System Navigation - ls, cd, pwd, paths
- File Operations - cp, mv, rm, mkdir
- Permissions - chmod, chown, rwx
- Viewing Files - cat, less, head, tail

### Networking (Beginner)
- Networking Fundamentals - OSI model, TCP/IP
- IP Addressing - IPv4, IPv6, CIDR, subnets
- Ports & Protocols - TCP vs UDP, well-known ports
- DNS Explained - Resolution, record types

*More concepts coming soon!*

## Tech Stack

- **Backend:** Flask 3.0+
- **Frontend:** Alpine.js + HTMX + Tailwind CSS
- **Sandbox:** Docker container with Ubuntu 22.04

## Development

```bash
# Run in debug mode (auto-reload)
python run.py

# Build Docker image after changes
docker build -t linux-sandbox:latest docker/
```

## License

MIT
