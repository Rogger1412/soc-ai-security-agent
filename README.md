# 🛡 SOC AI Security Agent

🚨 A lightweight AI-powered Security Operations Center (SOC) investigation platform built with **FastAPI and Python**.

This system acts as a simplified **AI security analyst**, capable of investigating suspicious:

- IP addresses
- URLs
- file hashes
- network ports

through an automated investigation workflow and an interactive dashboard.

---

# 📸 Dashboard Preview

## Security Dashboard

![Dashboard](/screenshots/dashboard.png)

## Investigation Example

![Investigation](/screenshots/investigation.png)

## Activity History

![Activity](/screenshots/activity.png)

---

# 🚀 Project Overview

Security analysts frequently investigate indicators such as:

- suspicious IP addresses
- unknown URLs
- malicious file hashes
- exposed network services

This project demonstrates how an **AI-driven investigation agent** can automate these tasks by coordinating multiple security tools into a structured investigation pipeline.

Users can simply type commands like:

```
8.8.8.8
https://example.com
port scan 127.0.0.1
investigate https://example.com
```

The AI agent then **detects the intent and runs the appropriate investigation tools automatically.**

---

# 🧠 How the AI Agent Works

The system follows a simplified **SOC investigation pipeline**:

```
User Input
   ↓
Intent Detection
   ↓
Target Extraction
   ↓
Investigation Planner
   ↓
Tool Execution Engine
   ↓
Threat Scoring
   ↓
AI Explanation
   ↓
Investigation Report
```

Each investigation may trigger multiple security tools such as:

- IP reputation analysis
- URL risk analysis
- DNS resolution
- port scanning
- incident response guidance

---

# 🔎 Features

## Automated Security Investigation

The agent automatically detects the investigation type and runs the appropriate security tools.

Examples:

| Command | Action |
|------|------|
| `8.8.8.8` | IP reputation analysis |
| `https://example.com` | URL risk analysis |
| `port scan 127.0.0.1` | local port scanning |
| `investigate domain.com` | multi-step investigation |
| `I clicked this link` | incident response guidance |

---

## Threat Intelligence Analysis

The system evaluates risk using a **custom threat scoring engine**.

Threat indicators include:

- malicious reports
- suspicious open ports
- risky services
- malware hash detections

Results are categorized as:

```
LOW
MEDIUM
HIGH
```

---

## SOC Investigation Dashboard

The web dashboard provides a simplified SOC-style interface including:

- threat alerts
- investigation history
- recent activity tracking
- investigation results
- automated security guidance

---

## Multi-Tool Security Engine

The platform integrates several security investigation tools:

| Tool | Purpose |
|-----|------|
| IP Scanner | reputation analysis |
| URL Scanner | phishing / malware detection |
| Port Scanner | network exposure discovery |
| Hash Scanner | malware hash lookup |
| Domain Resolver | domain → IP mapping |

---

## Investigation Memory

The system stores investigation history including:

- timestamp
- investigation target
- investigation type
- threat score
- severity level

This simulates a simplified **SOC case tracking system**.

---

## Report Export

Investigations can be exported as structured reports for documentation and incident response workflows.

---

# 🏗 Architecture

```
Frontend Dashboard
        ↓
FastAPI Backend API
        ↓
AI Security Agent
        ↓
Investigation Planner
        ↓
Tool Execution Engine
        ↓
Security Scanners
        ↓
Threat Scoring Engine
        ↓
Response Builder
        ↓
Database Logging
```

---

# 🖥 Technology Stack

| Component | Technology |
|------|------|
| Backend | FastAPI |
| Frontend | HTML / CSS / JavaScript |
| Language | Python |
| Database | SQLite |
| Security Tools | Custom scanners |
| Architecture | Modular AI Agent |

---

# 🧪 Example Investigation

User input:

```
investigate https://example.com
```

Agent workflow:

```
URL Scan
   ↓
Domain Resolution
   ↓
IP Reputation Analysis
   ↓
Port Scan
   ↓
Threat Scoring
   ↓
Investigation Report
```

---

# ⚠ Limitations

This project focuses on demonstrating **SOC automation concepts**.

Future improvements may include:

- VirusTotal integration
- Shodan intelligence integration
- real threat intelligence feeds
- malware sandbox analysis
- automated threat correlation

---

# 🔮 Future Improvements

Planned enhancements include:

- real threat intelligence APIs
- IOC correlation graphs
- automated threat hunting workflows
- machine learning threat scoring
- full SOC case management

---

# 🎯 Educational Purpose

This project demonstrates key cybersecurity concepts including:

- SOC automation
- threat intelligence analysis
- incident response workflows
- network security scanning
- AI-assisted investigation systems

---

# 📚 Skills Demonstrated

- Python security tool development
- FastAPI backend engineering
- AI agent workflow design
- cybersecurity investigation automation
- security dashboard development
- threat scoring algorithms

---

# 👨‍💻 Author

**Vishwa Patel And Heenaba Chauhan**

Cybersecurity students passionate about:
- SOC automation
- threat intelligence
- AI-driven security tooling
- network security research

---