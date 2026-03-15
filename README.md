# 🛡 SOC AI Security Agent

🚨 A lightweight **AI-powered Security Operations Center (SOC) investigation platform** built with **Python and FastAPI**.

This system acts like a **virtual security analyst**, helping users investigate suspicious:

- IP addresses  
- URLs / links  
- file hashes  
- network ports  

through an **automated investigation workflow and an interactive dashboard**.

The goal of this project is to **make cybersecurity investigation simple and accessible even for non-technical users**, helping them understand potential threats before they cause harm.

---

# 📸 Dashboard Preview

## Security Dashboard

![Dashboard](screenshots/dashboard.png)

## Investigation Example

![Investigation](screenshots/investigation.png)

## Activity History

![Activity](screenshots/activity.png)

---

# 🚀 Project Overview

People often encounter suspicious things like:

- unknown links in emails  
- suspicious IP addresses  
- potentially malicious files  
- unusual network activity  

Most users **do not know how to investigate these safely**.

This project demonstrates how an **AI-driven investigation agent** can automate these security checks and provide **clear explanations and guidance**.

Users can simply enter commands such as:

```
8.8.8.8
https://example.com
port scan 127.0.0.1
investigate https://example.com
```

The AI agent automatically **detects the user’s intent and runs the appropriate investigation tools.**

---

# 🧠 How the AI Agent Works

The system follows a simplified **SOC investigation workflow**:

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

Each investigation may trigger multiple security checks such as:

- IP reputation analysis  
- URL risk analysis  
- DNS resolution  
- port scanning  
- incident response guidance  

---

# 🔎 Key Features

## Automated Security Investigation

The AI agent automatically detects the investigation type and runs the correct security tools.

Examples:

| Command | Action |
|--------|--------|
| `8.8.8.8` | IP reputation analysis |
| `https://example.com` | URL security scan |
| `port scan 127.0.0.1` | local port scanning |
| `investigate domain.com` | multi-step investigation |
| `I clicked this link` | incident response guidance |

---

## Threat Intelligence Analysis

The system evaluates risk using a **custom threat scoring engine**.

Threat indicators include:

- malicious reputation reports  
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

The web dashboard provides a **simple SOC-style interface** including:

- threat alerts  
- investigation history  
- recent activity monitoring  
- investigation results  
- automated security guidance  

This helps users quickly understand **whether something is safe or potentially dangerous**.

---

## Multi-Tool Security Engine

The platform integrates several security investigation tools:

| Tool | Purpose |
|------|--------|
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
|-----------|------------|
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

This project currently focuses on demonstrating **SOC automation concepts and AI-assisted investigations**.

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

# 👨‍💻 Authors

**Vishwa Patel**  
**Heenaba Chauhan**

Cybersecurity students passionate about:

- SOC automation  
- threat intelligence  
- AI-driven security tools  
- network security research  

---

# 💡 Project Goal

To demonstrate how **AI-powered investigation tools can help everyday users understand and respond to potential cybersecurity threats**, even without advanced technical knowledge.