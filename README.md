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
python -m src.main
```

## 💻 **Usage Examples**

### Basic Monitoring:
```bash
python -m src.main --target 192.168.1.1
```

### Pattern Matching:
```bash
python -m src.main --patterns "HTTP,FTP"
```

### Custom Export:
```bash
python -m src.main --format json
```

### Example:
```bash
python -m src.main -t 192.168.1.10 -g 192.168.1.1 -p "password" "secret" -f html
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
├── types/         # Data models
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
