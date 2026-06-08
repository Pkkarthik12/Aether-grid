import { useRef, useState, useEffect } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, Grid, Text, PerspectiveCamera } from '@react-three/drei';
import * as THREE from 'three';

interface NodeData {
  id: string;
  position: [number, number, number];
  status: 'nominal' | 'alert';
  lastSeen: number;
}

function Node({ data }: { data: NodeData }) {
  const meshRef = useRef<THREE.Mesh>(null);
  
  return (
    <group position={data.position}>
      <mesh ref={meshRef}>
        <sphereGeometry args={[0.5, 32, 32]} />
        <meshStandardMaterial color={data.status === 'alert' ? 'red' : '#00ff00'} />
      </mesh>
      <Text
        position={[0, 1, 0]}
        fontSize={0.5}
        color="white"
        anchorX="center"
        anchorY="middle"
      >
        {data.id.slice(0, 8)}
      </Text>
    </group>
  );
}

export default function SwarmScene({ nodes }: { nodes: Record<string, NodeData> }) {
  return (
    <div style={{ width: '100%', height: '80vh', background: '#111' }}>
      <Canvas shadows>
        <PerspectiveCamera makeDefault position={[10, 10, 10]} />
        <OrbitControls />
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} intensity={1} castShadow />
        
        <Grid 
          infiniteGrid 
          sectionSize={10} 
          sectionThickness={1} 
          sectionColor="#333" 
          gridSize={20} 
          cellColor="#222"
        />
        
        {Object.values(nodes).map((node) => (
          <Node key={node.id} data={node} />
        ))}
      </Canvas>
    </div>
  );
}
