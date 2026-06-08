# Aether-Grid

**Decentralized ML Swarm Intelligence Framework** — A high-level, engineer-grade platform for coordinating autonomous edge nodes with real-time vision, network security monitoring, and 3D visualization.

```
   ▄▄▄▄▀ ▄███▄   ▄███▄   █  █▀ ▄███▄   █▄▄▄▄ ▄▀  ▄███▄   █  █▀ 
▀▀▀ █    █▀   ▀  █▀   ▀  █▄█   █▀   ▀  █  ▄▀ █   █▀   ▀  █▄█   
    █    ██▄▄    ██▄▄    █▀▄   ██▄▄    █▀▀▌  █   ██▄▄    █▀▄   
   █     █▄   ▄▀ █▄   ▄▀ █  █  █▄   ▄▀ █  █  █   █▄   ▄▀ █  █  
  ▀      ▀███▀   ▀███▀     █   ▀███▀     █   █   ▀███▀     █   
                          ▀             ▀    ▀            ▀    
```

## 🏗️ Architecture

Aether-Grid is built on a modular, multi-language stack designed for low latency and high scalability:

- **Aether-Core (Go):** The central nervous system. A high-performance WebSocket hub that routes telemetry, alerts, and commands across the swarm.
- **Aether-Node (Python):** The edge intelligence. Runs YOLOv8 for object detection and Scapy-based RF scanning for anomaly detection.
- **Aether-Dash (React + Three.js):** The situational awareness interface. A WebGL-powered 3D dashboard visualizing the swarm's state in real-time.
- **Aether-CLI (Go):** The developer's command center for managing deployments and model synchronization.

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.13+ (for local node development)
- Go 1.24+ (for core/cli development)

### Launch the Stack
```bash
docker-compose up --build
```
1. Open the Dashboard: `http://localhost:5173`
2. Core API: `ws://localhost:8080/ws`

## 🛡️ Network Security & AI
Aether-Grid nodes don't just "see"—they listen.
- **Vision Engine:** Real-time object classification using YOLOv8n.
- **NetSec Engine:** Continuous monitoring of the RF spectrum to detect rogue access points or signal jamming attempts.
- **Swarm Sync:** Decentralized state propagation ensures all nodes are aware of detected threats.

## 🛠️ Monorepo Layout
- `/core`: Go WebSocket hub.
- `/node`: Python edge node software.
- `/dash`: React/Three.js 3D dashboard.
- `/cli`: Go-based command line interface.
- `/docs`: Detailed architectural specifications.

## 📜 License
MIT
