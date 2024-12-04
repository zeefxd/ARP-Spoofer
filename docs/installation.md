# Installation Guide

## Requirements
- Python 3.8+
- pip package manager

## Setup

1. Clone the repository:
```bash
git clone https://github.com/zeefxd/ARP-Spoofer.git
cd ARP-Spoofer
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
## Development Setup
For development, install additional dependencies:
```bash
pip install -r requirements-dev.txt
```

4. Create `docs/usage.md`:

```markdown
# Usage Guide

## Basic Usage

Run with default settings:
```bash
python -m src.main
```
Command Options
Option	Description	Default
-t, --target	Target IP address	Auto-detect
-g, --gateway	Gateway IP address	Auto-detect
-p, --patterns	Search patterns	None
-f, --format	Export format	html

# Examples
## Basic Monitoring
```bash
python -m src.main --target 192.168.1.1
```
## Pattern Matching
```bash
python -m src.main --target 192.168.1.1
```