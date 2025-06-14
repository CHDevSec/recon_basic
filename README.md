# 🔎 Recon Total - Automated Network Reconnaissance Tool

> **Powerful network reconnaissance combining Shodan API intelligence with Nmap scanning capabilities**

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Security](https://img.shields.io/badge/security-pentesting-red.svg)](https://github.com/topics/pentesting)

**Network Scanner | IP Intelligence | Security Assessment | Penetration Testing Tool**

---

## 🚀 Features

- **Dual Intelligence**: Combines Shodan API data with local Nmap scanning
- **Automated Reporting**: Generates timestamped reports with complete findings
- **Service Detection**: Identifies open ports, services, and system information
- **Error Handling**: Robust timeout and connection failure management
- **Cross-Platform**: Compatible with Linux, macOS, and Windows

## 📦 Quick Start

### Prerequisites
```bash
# Install dependencies
pip install requests
sudo apt install nmap  # Linux
brew install nmap      # macOS
```

### Installation
```bash
git clone https://github.com/username/recon-total.git
cd recon-total
chmod +x recon_total.py

# Configure Shodan API key
sed -i 's/SEU_TOKEN_API/your_actual_api_key/' recon_total.py
```

### Usage
```bash
python3 recon_total.py <TARGET_IP>

# Example
python3 recon_total.py 8.8.8.8
```

## 🔍 What It Does

1. **Shodan Intelligence**: Queries Shodan database for:
   - Organization and geolocation data
   - Publicly exposed services
   - Historical port information
   - Operating system details

2. **Nmap Scanning**: Performs local network scan for:
   - Active port discovery
   - Service version detection
   - Real-time connectivity status

3. **Report Generation**: Creates comprehensive reports with:
   - Combined intelligence from both sources
   - Timestamped findings
   - Organized service information

## 📊 Sample Output

```
============================================================
 🔎 RECON TOTAL - SHODAN + NMAP
 By Pentester Caio | CHDEVSEC
============================================================

[+] Querying Shodan for IP: 8.8.8.8...

Organization: Google LLC
Country: United States
Operating System: N/A

Shodan Ports Found:
 - Port 53 | Service: Google Public DNS
 - Port 443 | Service: HTTPS

[+] Running Nmap scan on IP: 8.8.8.8...
[Nmap results...]

[+] Results saved to: recon_8_8_8_8_20240614_143022.txt
```

## ⚙️ Configuration

### Shodan API Setup
1. Register at [shodan.io](https://www.shodan.io/)
2. Get your free API key
3. Replace `SEU_TOKEN_API` in the script

### Nmap Parameters
Default scan: `-Pn -sV` (Skip ping, detect service versions)

Customize in script:
```python
["nmap", "-Pn", "-sV", "-sC", ip]  # Add script scanning
```

## 🛠️ Use Cases

- **Network Security Assessment**: Identify exposed services and potential vulnerabilities
- **Asset Discovery**: Map network infrastructure and service inventory  
- **Penetration Testing**: Gather reconnaissance data for security testing
- **Threat Intelligence**: Analyze target infrastructure and attack surface
- **Compliance Auditing**: Verify security controls and service exposure

## 📝 Requirements

- Python 3.6+
- Nmap installed and accessible in PATH
- Shodan API key (free tier available)
- Internet connection for Shodan queries

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| `Invalid API key` | Verify Shodan API key configuration |
| `Nmap timeout` | Increase timeout value or check target connectivity |
| `Command not found: nmap` | Install Nmap using system package manager |

## 🤝 Contributing

Contributions welcome! Please read our contributing guidelines and submit pull requests for any improvements.

## ⚠️ Legal Disclaimer

**FOR AUTHORIZED SECURITY TESTING ONLY**

This tool is designed for legitimate security professionals, researchers, and system administrators. Users must:

- ✅ Only scan systems you own or have explicit written permission to test
- ✅ Comply with all applicable local and international laws
- ✅ Follow responsible disclosure practices
- ❌ Never use for unauthorized access or malicious activities

**The developer assumes no liability for misuse of this tool. Users are solely responsible for ensuring legal and ethical usage.**

## 📊 Keywords

`network reconnaissance` `shodan api` `nmap scanner` `penetration testing` `security assessment` `network security` `port scanner` `vulnerability assessment` `cybersecurity tools` `infosec` `ethical hacking` `security research` `network mapping` `service discovery` `threat intelligence`

---

**⭐ Star this repo if you find it useful for your security research!**

**Developed by:** Pentester Caio | CHDEVSEC
