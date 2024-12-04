# Usage Guide

## Basic Usage

### Run with default settings
```bash
# Linux/macOS
sudo python -m src

# Windows (run PowerShell/CMD as Administrator)
python -m src
```

> ⚠️ **Note**: Root/Administrator privileges are required for network operations

## 💻 **Usage Examples**

### Basic Monitoring:
```bash
# Linux/macOS
sudo python -m src --target 192.168.1.1

# Windows (run PowerShell/CMD as Administrator)
python -m src --target 192.168.1.1
```

### Pattern Matching:
```bash
# Linux/macOS
sudo python -m src --patterns "HTTP,FTP"

# Windows (run PowerShell/CMD as Administrator)
python -m src --patterns "HTTP,FTP"
```

### Custom Export:
```bash
# Linux/macOS
sudo python -m src --format json

# Windows (run PowerShell/CMD as Administrator)
python -m src --format json
```

### Example:
```bash
# Linux/macOS
sudo python -m src -t 192.168.1.10 -g 192.168.1.1 -p "password" "secret" -f html

# Windows (run PowerShell/CMD as Administrator)
python -m src -t 192.168.1.10 -g 192.168.1.1 -p "password" "secret" -f html
```

## 📋 **Command Options**

| Option       | Description           | Default       |
|--------------|-----------------------|---------------|
| -t, --target | Target IP address     | Auto-detect   |
| -g, --gateway| Gateway IP address    | Auto-detect   |
| -p, --patterns| Search patterns      | None          |
| -f, --format | Export format         | html          |
