/**
 * HierarchyTree Visualizer
 * Tree-like visualization for nested/hierarchical generation
 * Used for: Documentation Engine, Universe Architect
 * Pattern from: UX + Scalability strategies
 */

class HierarchyTreeVisualizer {
  constructor(canvas, config) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.config = {
      sourceFiles: config.sourceFiles || 3500,
      outputDocs: config.outputDocs || 400,
      categories: config.categories || 12,
      rootElement: config.rootElement || 1,
      generatedElements: config.generatedElements || 300,
      depth: config.depth || 5,
      ...config
    };

    this.nodes = [];
    this.startTime = null;
    this.animationId = null;
    this.isRunning = false;
  }

  initialize() {
    this.resizeCanvas();
    window.addEventListener('resize', () => this.resizeCanvas());

    this.createTree();
    this.start();
  }

  resizeCanvas() {
    const container = this.canvas.parentElement;
    this.canvas.width = container.clientWidth;
    this.canvas.height = container.clientHeight;
  }

  createTree() {
    const centerX = this.canvas.width / 2;
    const startY = 100;
    const levelHeight = (this.canvas.height - 200) / this.config.depth;

    // Create root
    this.nodes.push({
      id: 0,
      level: 0,
      x: centerX,
      y: startY,
      targetX: centerX,
      targetY: startY,
      parent: null,
      children: [],
      progress: 0,
      radius: 8,
      color: '#667eea'
    });

    // Generate tree structure
    let nodeId = 1;
    const maxNodes = this.config.generatedElements || this.config.outputDocs;
    const nodesPerLevel = Math.ceil(maxNodes / this.config.depth);

    for (let level = 1; level < this.config.depth; level++) {
      const prevLevelNodes = this.nodes.filter(n => n.level === level - 1);
      const childrenPerParent = Math.max(1, Math.floor(nodesPerLevel / prevLevelNodes.length));

      prevLevelNodes.forEach((parent, parentIndex) => {
        const siblings = Math.min(childrenPerParent, maxNodes - nodeId);

        for (let i = 0; i < siblings && nodeId < maxNodes; i++) {
          const siblingOffset = (i - siblings / 2) * 80;
          const x = parent.targetX + siblingOffset;
          const y = startY + (level * levelHeight);

          const node = {
            id: nodeId++,
            level: level,
            x: parent.x,
            y: parent.y,
            targetX: x,
            targetY: y,
            parent: parent,
            children: [],
            progress: 0,
            radius: Math.max(3, 8 - level),
            color: this.getColorForLevel(level)
          };

          parent.children.push(node);
          this.nodes.push(node);
        }
      });
    }
  }

  getColorForLevel(level) {
    const colors = ['#667eea', '#764ba2', '#f093fb', '#4facfe', '#00f2fe'];
    return colors[level % colors.length];
  }

  start() {
    this.isRunning = true;
    this.startTime = Date.now();
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

    const elapsed = Date.now() - this.startTime;
    const duration = 8000;
    const overallProgress = Math.min(elapsed / duration, 1);

    // Clear canvas
    this.ctx.fillStyle = 'rgba(10, 14, 39, 1)';
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

    // Update node positions
    this.updateNodes(overallProgress);

    // Draw connections
    this.drawConnections();

    // Draw nodes
    this.drawNodes();

    // Draw stats
    this.drawStats();

    this.animationId = requestAnimationFrame(() => this.animate());
  }

  updateNodes(overallProgress) {
    this.nodes.forEach(node => {
      // Calculate when this node should appear
      const nodeDelay = node.level * 0.15;
      const nodeProgress = Math.max(0, Math.min(1, (overallProgress - nodeDelay) / 0.3));

      node.progress = nodeProgress;

      // Animate position
      node.x = node.x + (node.targetX - node.x) * 0.1;
      node.y = node.y + (node.targetY - node.y) * 0.1;
    });
  }

  drawConnections() {
    this.ctx.strokeStyle = 'rgba(102, 126, 234, 0.2)';
    this.ctx.lineWidth = 1;

    this.nodes.forEach(node => {
      if (node.parent && node.progress > 0) {
        this.ctx.globalAlpha = node.progress;
        this.ctx.beginPath();
        this.ctx.moveTo(node.parent.x, node.parent.y);
        this.ctx.lineTo(node.x, node.y);
        this.ctx.stroke();
      }
    });

    this.ctx.globalAlpha = 1;
  }

  drawNodes() {
    this.nodes.forEach(node => {
      if (node.progress > 0) {
        this.ctx.globalAlpha = node.progress;

        // Draw node
        this.ctx.fillStyle = node.color;
        this.ctx.beginPath();
        this.ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
        this.ctx.fill();

        // Glow
        const gradient = this.ctx.createRadialGradient(
          node.x, node.y, 0,
          node.x, node.y, node.radius * 2
        );
        gradient.addColorStop(0, node.color + '60');
        gradient.addColorStop(1, node.color + '00');

        this.ctx.fillStyle = gradient;
        this.ctx.beginPath();
        this.ctx.arc(node.x, node.y, node.radius * 2, 0, Math.PI * 2);
        this.ctx.fill();
      }
    });

    this.ctx.globalAlpha = 1;
  }

  drawStats() {
    const visibleNodes = this.nodes.filter(n => n.progress > 0.5).length;

    this.ctx.fillStyle = '#ffffff';
    this.ctx.font = 'bold 16px -apple-system, sans-serif';
    this.ctx.textAlign = 'left';

    if (this.config.sourceFiles) {
      this.ctx.fillText(`Source Files: ${this.config.sourceFiles.toLocaleString()}`, 20, 30);
      this.ctx.fillText(`Generated Docs: ${visibleNodes}/${this.config.outputDocs}`, 20, 55);
      this.ctx.fillText(`Categories: ${this.config.categories}`, 20, 80);
    } else {
      this.ctx.fillText(`Root Elements: ${this.config.rootElement}`, 20, 30);
      this.ctx.fillText(`Generated: ${visibleNodes}/${this.config.generatedElements}`, 20, 55);
      this.ctx.fillText(`Depth: ${this.config.depth} levels`, 20, 80);
    }
  }

  destroy() {
    this.stop();
    window.removeEventListener('resize', () => this.resizeCanvas());
  }
}

// Listen for demo-loaded event
document.addEventListener('demo-loaded', (e) => {
  if (e.detail.type === 'hierarchy-tree') {
    const visualizer = new HierarchyTreeVisualizer(e.detail.canvas, e.detail.config);
    visualizer.initialize();
    e.detail.canvas.visualizer = visualizer;
  }
});
