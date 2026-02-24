# Linux Sandbox for Unix & Networking Learning Platform
FROM ubuntu:22.04

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install essential networking and system tools
RUN apt-get update && apt-get install -y \
    # Basic utilities
    bash \
    coreutils \
    findutils \
    grep \
    sed \
    gawk \
    less \
    tree \
    vim-tiny \
    nano \
    # Networking tools
    iputils-ping \
    traceroute \
    mtr-tiny \
    net-tools \
    iproute2 \
    dnsutils \
    curl \
    wget \
    netcat-openbsd \
    tcpdump \
    nmap \
    host \
    # Process management
    procps \
    htop \
    # System utilities
    file \
    man-db \
    # Cleanup
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user for safety
RUN useradd -m -s /bin/bash learner \
    && echo "learner ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Set up sample files and directories for practice
WORKDIR /home/learner

# Create sample directory structure
RUN mkdir -p projects/webapp projects/api documents/notes documents/images downloads \
    && touch projects/webapp/index.html projects/webapp/style.css projects/webapp/app.js \
    && touch projects/api/server.py projects/api/config.json projects/api/README.md \
    && touch documents/notes/todo.txt documents/notes/meeting.md \
    && touch downloads/file1.txt downloads/file2.txt

# Add some content to sample files
RUN echo '<!DOCTYPE html><html><head><title>Sample</title></head><body><h1>Hello World</h1></body></html>' > projects/webapp/index.html \
    && echo 'body { font-family: sans-serif; }' > projects/webapp/style.css \
    && echo 'console.log("Hello from app.js");' > projects/webapp/app.js \
    && echo '#!/usr/bin/env python3\nprint("Hello from server")' > projects/api/server.py \
    && echo '{"port": 8080, "debug": true}' > projects/api/config.json \
    && echo '# API Project\n\nThis is a sample API project.' > projects/api/README.md \
    && echo '- Buy groceries\n- Review PR\n- Update documentation' > documents/notes/todo.txt \
    && echo '# Meeting Notes\n\n## Attendees\n- Alice\n- Bob\n\n## Action Items\n1. Deploy to staging' > documents/notes/meeting.md

# Create a sample log file
RUN echo 'INFO 2024-01-15 10:23:45 Application started\nDEBUG 2024-01-15 10:23:46 Loading configuration\nINFO 2024-01-15 10:23:47 Server listening on port 8080\nWARN 2024-01-15 10:24:01 High memory usage detected\nERROR 2024-01-15 10:24:15 Connection timeout to database\nINFO 2024-01-15 10:24:20 Retry successful' > /var/log/sample-app.log

# Set permissions
RUN chown -R learner:learner /home/learner \
    && chmod -R 755 /home/learner

# Add helpful bashrc
RUN echo '\n# Custom prompt\nPS1="\[\033[01;32m\]learner@sandbox\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ "\n\n# Aliases\nalias ll="ls -la"\nalias la="ls -A"\nalias l="ls -CF"\n' >> /home/learner/.bashrc

# Switch to non-root user
USER learner
WORKDIR /home/learner

# Default command
CMD ["/bin/bash"]
