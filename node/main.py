import json
import time
import websocket
import threading
from engines.vision import VisionEngine
from engines.network import NetworkEngine

class AetherNode:
    def __init__(self, core_url="ws://localhost:8080/ws"):
        self.core_url = core_url
        self.ws = None
        self.node_id = None
        self.running = True

    def on_message(self, ws, message):
        data = json.loads(message)
        # Handle commands from Core if any
        pass

    def on_error(self, ws, error):
        print(f"WS Error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        print("### WS Closed ###")

    def on_open(self, ws):
        print("Connected to Aether-Core")

    def send_telemetry(self, payload):
        if self.ws and self.ws.sock and self.ws.sock.connected:
            message = {
                "type": "telemetry",
                "source_id": self.node_id,
                "payload": payload,
                "timestamp": int(time.time())
            }
            self.ws.send(json.dumps(message))

    def vision_callback(self, detections):
        self.send_telemetry({
            "module": "vision",
            "detections": detections
        })

    def network_callback(self, data):
        self.send_telemetry({
            "module": "network",
            "data": data
        })

    def start(self):
        # Start engines
        self.vision = VisionEngine(callback=self.vision_callback)
        self.network = NetworkEngine(callback=self.network_callback)
        
        self.vision.start()
        self.network.start()

        # Start WebSocket
        # websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            self.core_url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        
        # Run WS in a separate thread to allow main thread to handle lifecycle
        ws_thread = threading.Thread(target=self.ws.run_forever)
        ws_thread.daemon = True
        ws_thread.start()

        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.running = False
        self.vision.stop()
        self.network.stop()
        if self.ws:
            self.ws.close()

if __name__ == "__main__":
    node = AetherNode()
    node.start()
