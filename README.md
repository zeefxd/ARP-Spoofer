# ARP Spoofing Tool 🌐

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-orange.svg)
![Version](https://img.shields.io/badge/version-1.0.0-green.svg)

## 🎯 Overview
Advanced network packet analysis and ARP spoofing tool built with Python. Featuring pattern matching, real-time monitoring, and beautiful reporting interfaces.

## ✨ Key Features

🔍 **Network Analysis**
- Real-time packet capture and filtering
- Pattern-based traffic monitoring
- MAC address resolution
- Hostname detection

🛡️ **ARP Operations**
- Smart gateway detection
- Target device mapping
- Traffic interception
- Custom packet rules

📊 **Reporting & Export**
- Interactive HTML reports
- JSON data export
- CSV compatibility
- Plain text logs

## 🖥️ Screenshots

### ARP Spoofing Tool in Action

![Application Running](https://github.com/user-attachments/assets/338cf463-e9d3-4b49-8980-c1c21bad3036)

*Initializes the tool and displays the status of the ARP spoofing attack.*

### Packet Capture Overview

![Packet Capture](https://github.com/user-attachments/assets/7f34867a-d088-4ce1-9ded-ec7c595651f1)

*Real-time packet capture showing intercepted network packets with source and destination details.*

### Export Format Options

![Export Format Options](https://github.com/user-attachments/assets/dd164e81-62ff-4596-b2ba-196689833d78)

*Options for exporting captured data in various formats such as HTML, JSON, CSV, and plain text.*

### HTML Report

![HTML Report](https://github.com/user-attachments/assets/177ac313-68b5-49df-b5fd-2d993401ef5a)

*Generated HTML report providing a detailed analysis of the captured packets.*


## 🚀 Quick Start

```bash
# Clone repository
https://github.com/zeefxd/ARP-Spoofer.git
cd ARP-Spoofer
```

### Install dependencies
```bash
pip install -r requirements.txt
```

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

## 📁 **Project Structure**
```
src/
├── core/          # Core functionality
├── network/       # Network operations
├── spoofer/       # ARP implementation
├── models/        # Data models
└── utils/         # Helper functions
```

## 📦 **Dependencies**
- scapy - Network packet manipulation
- rich - Terminal UI components
- netifaces - Network interface handling
- jinja2 - Report templating

## 🔧 **Development**
```bash
# Setup development environment
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements-dev.txt
```

## ⚠️ **Security Notice**
Educational Purposes Only: This tool should only be used on networks where you have explicit permission to test.

## 🤝 **Contributing**
1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Submit pull request

## 📜 **License**
MIT License - See LICENSE file

## 👤 **Author**
GitHub: [@zeefxd](https://github.com/zeefxd)

Twitter: [@zeefxd](https://x.com/zeefxd)

💬 **Support**
Report issues on GitHub
