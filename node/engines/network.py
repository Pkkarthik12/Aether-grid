import threading
import time
import random

class NetworkEngine(threading.Thread):
    def __init__(self, callback=None):
        super().__init__()
        self.callback = callback
        self.running = True
        self.daemon = True

    def run(self):
        while self.running:
            # Simulate scanning WiFi signals
            # In a real scenario, this would use scapy to sniff 802.11 beacons
            networks = [
                {"ssid": "Aether-Secure-01", "rssi": random.randint(-60, -30), "chan": 1},
                {"ssid": "Unknown-Device", "rssi": random.randint(-90, -70), "chan": 6},
                {"ssid": "Home-WiFi", "rssi": random.randint(-50, -40), "chan": 11},
            ]
            
            # Anomaly detection logic
            for net in networks:
                if net["rssi"] > -40 and net["ssid"] == "Unknown-Device":
                    # Rogue signal detected (too strong for unknown)
                    if self.callback:
                        self.callback({
                            "type": "network_anomaly",
                            "severity": "high",
                            "details": f"High power rogue signal: {net['ssid']} at {net['rssi']}dBm"
                        })

            if self.callback:
                self.callback({
                    "type": "network_scan",
                    "networks": networks
                })

            time.sleep(2.0)

    def stop(self):
        self.running = False
