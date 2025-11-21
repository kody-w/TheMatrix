/**
 * NetworkGraph Visualizer
 * Force-directed graph showing nodes and relationships
 * Used for: Knowledge Synthesizer, System Designer
 * Pattern from: Technical Sophistication + Visual Impact strategies
 */

class NetworkGraphVisualizer {
  constructor(canvas, config) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.config = {
      inputNodes: config.inputNodes || 75,
      outputNodes: config.outputNodes || 200,
      connections: config.connections || 450,
      ...config
    };

    this.nodes = [];
    this.edges = [];
    this.animationId = null;
    this.isRunning = false;
  }

  initialize() {
    this.resizeCanvas();
    window.addEventListener('resize', () => this.resizeCanvas());

    this.createGraph();
    this.start();
  }

  resizeCanvas() {
    const container = this.canvas.parentElement;
    this.canvas.width = container.clientWidth;
    this.canvas.height = container.clientHeight;
  }

  createGraph() {
    const centerX = this.canvas.width / 2;
    const centerY = this.canvas.height / 2;
    const inputRadius = Math.min(this.canvas.width, this.canvas.height) * 0.2;
    const outputRadius = Math.min(this.canvas.width, this.canvas.height) * 0.35;

    // Create input nodes (papers) in inner circle
    for (let i = 0; i < this.config.inputNodes; i++) {
      const angle = (i / this.config.inputNodes) * Math.PI * 2;
      this.nodes.push({
        id: `input-${i}`,
        x: centerX + Math.cos(angle) * inputRadius,
        y: centerY + Math.sin(angle) * inputRadius,
        vx: 0,
        vy: 0,
        type: 'input',
        color: '#667eea',
        radius: 4
      });
    }

    // Create output nodes (articles) in outer circle
    for (let i = 0; i < this.config.outputNodes; i++) {
      const angle = (i / this.config.outputNodes) * Math.PI * 2;
      this.nodes.push({
        id: `output-${i}`,
        x: centerX + Math.cos(angle) * outputRadius,
        y: centerY + Math.sin(angle) * outputRadius,
        vx: 0,
        vy: 0,
        type: 'output',
        color: '#f093fb',
        radius: 3
      });
    }

    // Create connections
    const inputNodes = this.nodes.filter(n => n.type === 'input');
    const outputNodes = this.nodes.filter(n => n.type === 'output');

    for (let i = 0; i < this.config.connections; i++) {
      const source = inputNodes[Math.floor(Math.random() * inputNodes.length)];
      const target = outputNodes[Math.floor(Math.random() * outputNodes.length)];

      this.edges.push({
        source: source,
        target: target,
        opacity: 0.1 + Math.random() * 0.2
      });
    }
  }

  start() {
    this.isRunning = true;
    this.animate();
  }

  stop() {
    this.isRunning = false;
    if (this.animationId) {
      cancelAnimationFrame(this.animationId);
    }
  }

  animate() {
    if (!this.isRunning) return;

    // Clear canvas
    this.ctx.fillStyle = 'rgba(10, 14, 39, 0.1)';
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

    // Apply simple physics
    this.applyForces();

    // Draw edges
    this.drawEdges();

    // Draw nodes
    this.drawNodes();

    this.animationId = requestAnimationFrame(() => this.animate());
  }

  applyForces() {
    const centerX = this.canvas.width / 2;
    const centerY = this.canvas.height / 2;

    this.nodes.forEach(node => {
      // Gravity towards center
      const dx = centerX - node.x;
      const dy = centerY - node.y;
      const distance = Math.sqrt(dx * dx + dy * dy);

      if (distance > 0) {
        node.vx += (dx / distance) * 0.01;
        node.vy += (dy / distance) * 0.01;
      }

      // Apply velocity
      node.x += node.vx;
      node.y += node.vy;

      // Damping
      node.vx *= 0.95;
      node.vy *= 0.95;
    });
  }

  drawEdges() {
    this.ctx.strokeStyle = 'rgba(102, 126, 234, 0.15)';
    this.ctx.lineWidth = 0.5;

    this.edges.forEach(edge => {
      this.ctx.globalAlpha = edge.opacity;
      this.ctx.beginPath();
      this.ctx.moveTo(edge.source.x, edge.source.y);
      this.ctx.lineTo(edge.target.x, edge.target.y);
      this.ctx.stroke();
    });

    this.ctx.globalAlpha = 1;
  }

  drawNodes() {
    this.nodes.forEach(node => {
      this.ctx.fillStyle = node.color;
      this.ctx.beginPath();
      this.ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
      this.ctx.fill();

      // Glow effect
      const gradient = this.ctx.createRadialGradient(
        node.x, node.y, 0,
        node.x, node.y, node.radius * 2
      );
      gradient.addColorStop(0, node.color + '80');
      gradient.addColorStop(1, node.color + '00');

      this.ctx.fillStyle = gradient;
      this.ctx.beginPath();
      this.ctx.arc(node.x, node.y, node.radius * 2, 0, Math.PI * 2);
      this.ctx.fill();
    });
  }

  destroy() {
    this.stop();
    window.removeEventListener('resize', () => this.resizeCanvas());
  }
}

// Listen for demo-loaded event
document.addEventListener('demo-loaded', (e) => {
  if (e.detail.type === 'network-graph') {
    const visualizer = new NetworkGraphVisualizer(e.detail.canvas, e.detail.config);
    visualizer.initialize();
    e.detail.canvas.visualizer = visualizer;
  }
});
