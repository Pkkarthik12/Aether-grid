import { useState, useEffect } from 'react';
import SwarmScene from './components/SwarmScene';
import { Activity, ShieldAlert, Cpu, Network } from 'lucide-react';
import './App.css';

interface NodeData {
  id: string;
  position: [number, number, number];
  status: 'nominal' | 'alert';
  lastSeen: number;
}

function App() {
  const [nodes, setNodes] = useState<Record<string, NodeData>>({});
  const [alerts, setAlerts] = useState<any[]>([]);

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8080/ws');

    ws.onmessage = (event) => {
      const msg = JSON.parse(event.data);
      if (msg.type === 'telemetry') {
        setNodes(prev => {
          const node = prev[msg.source_id] || {
            id: msg.source_id,
            position: [Math.random() * 10 - 5, 0, Math.random() * 10 - 5],
            status: 'nominal',
            lastSeen: Date.now()
          };

          // Update status if network anomaly detected
          if (msg.payload.module === 'network' && msg.payload.data.type === 'network_anomaly') {
            node.status = 'alert';
            setAlerts(a => [{ id: Date.now(), msg: msg.payload.data.details }, ...a].slice(0, 5));
          }

          return { ...prev, [msg.source_id]: { ...node, lastSeen: Date.now() } };
        });
      }
    };

    return () => ws.close();
  }, []);

  return (
    <div className="aether-dash">
      <header>
        <h1><Activity color="#00ff00" /> AETHER-GRID <span className="status-badge">SWARM LIVE</span></h1>
      </header>

      <main>
        <div className="control-panel">
          <section className="stats">
            <div className="stat-card">
              <Cpu />
              <h3>Active Nodes</h3>
              <p>{Object.keys(nodes).length}</p>
            </div>
            <div className="stat-card">
              <Network />
              <h3>RF Status</h3>
              <p className={alerts.length > 0 ? 'text-alert' : 'text-ok'}>
                {alerts.length > 0 ? 'ANOMALY' : 'SECURE'}
              </p>
            </div>
          </section>

          <section className="alerts">
            <h3><ShieldAlert color="red" /> Security Alerts</h3>
            <ul>
              {alerts.map(a => (
                <li key={a.id}>{a.msg}</li>
              ))}
              {alerts.length === 0 && <li>No active threats</li>}
            </ul>
          </section>
        </div>

        <div className="scene-container">
          <SwarmScene nodes={nodes} />
        </div>
      </main>
    </div>
  );
}

export default App;
