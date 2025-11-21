/**
 * CascadeFlow Visualizer
 * Particle system showing items flowing through sequential stages
 * Used for: The Great Migration
 * Pattern from: Scalability Strategy with Performance optimization
 */

class CascadeFlowVisualizer {
  constructor(canvas, config) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.config = {
      stages: config.stages || ['Input', 'Process', 'Output'],
      itemCount: config.itemCount || 100,
      duration: config.duration || 8000,
      colors: ['#667eea', '#999999', '#764ba2'],
      particleSize: 3,
      ...config
    };

    this.particles = [];
    this.startTime = null;
    this.animationId = null;
    this.isRunning = false;
  }

  /**
   * Initialize and start visualization
   */
  initialize() {
    this.resizeCanvas();
    window.addEventListener('resize', () => this.resizeCanvas());

    this.createParticles();
    this.start();
  }

  /**
   * Resize canvas to container
   */
  resizeCanvas() {
    const container = this.canvas.parentElement;
    this.canvas.width = container.clientWidth;
    this.canvas.height = container.clientHeight;
  }

  /**
   * Create particle system
   */
  createParticles() {
    const padding = 100;
    const usableHeight = this.canvas.height - (padding * 2);

    for (let i = 0; i < this.config.itemCount; i++) {
      this.particles.push({
        id: i,
        x: padding,
        y: padding + (Math.random() * usableHeight),
        baseY: padding + (Math.random() * usableHeight),
        stage: 0,
        progress: 0,
        speed: 0.8 + (Math.random() * 0.4), // Vary speed slightly
        size: this.config.particleSize,
        opacity: 0.6 + (Math.random() * 0.4)
      });
    }
  }

  /**
   * Start animation loop
   */
  start() {
    this.isRunning = true;
    this.startTime = Date.now();
    this.animate();
  }

  /**
   * Stop animation
   */
  stop() {
    this.isRunning = false;
    if (this.animationId) {
      cancelAnimationFrame(this.animationId);
    }
  }

  /**
   * Main animation loop
   */
  animate() {
    if (!this.isRunning) return;

    const elapsed = Date.now() - this.startTime;

    // Clear canvas with fade effect
    this.ctx.fillStyle = 'rgba(10, 14, 39, 0.15)';
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

    // Draw stage labels
    this.drawStageLabels();

    // Update and draw particles
    this.updateParticles(elapsed);
    this.drawParticles();

    // Continue animation
    this.animationId = requestAnimationFrame(() => this.animate());
  }

  /**
   * Draw stage labels
   */
  drawStageLabels() {
    const stageWidth = this.canvas.width / this.config.stages.length;
    const padding = 100;

    this.ctx.font = 'bold 16px -apple-system, sans-serif';
    this.ctx.textAlign = 'center';

    this.config.stages.forEach((stage, index) => {
      const x = padding + (stageWidth * index) + (stageWidth / 2);

      // Stage label
      this.ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
      this.ctx.fillText(stage, x, 50);

      // Vertical line
      this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
      this.ctx.lineWidth = 1;
      this.ctx.setLineDash([5, 5]);
      this.ctx.beginPath();
      this.ctx.moveTo(x, 80);
      this.ctx.lineTo(x, this.canvas.height - 80);
      this.ctx.stroke();
      this.ctx.setLineDash([]);
    });
  }

  /**
   * Update particle positions
   */
  updateParticles(elapsed) {
    const stageWidth = this.canvas.width / this.config.stages.length;
    const padding = 100;
    const progressFactor = (elapsed / this.config.duration);

    this.particles.forEach(particle => {
      // Calculate overall progress
      const overallProgress = progressFactor * particle.speed;
      const totalStages = this.config.stages.length;

      // Determine current stage and progress within stage
      particle.stage = Math.min(
        Math.floor(overallProgress * totalStages),
        totalStages - 1
      );
      particle.progress = (overallProgress * totalStages) % 1;

      // Calculate X position
      const stageX = padding + (stageWidth * particle.stage) + (stageWidth / 2);
      const nextStageX = padding + (stageWidth * (particle.stage + 1)) + (stageWidth / 2);

      if (particle.stage < totalStages - 1) {
        particle.x = stageX + ((nextStageX - stageX) * particle.progress);
      } else {
        particle.x = stageX;
      }

      // Slight Y drift
      particle.y = particle.baseY + Math.sin(elapsed * 0.001 + particle.id) * 10;

      // Keep within bounds
      particle.y = Math.max(100, Math.min(this.canvas.height - 100, particle.y));
    });
  }

  /**
   * Draw all particles
   */
  drawParticles() {
    this.particles.forEach(particle => {
      const colorIndex = Math.min(particle.stage, this.config.colors.length - 1);
      const color = this.config.colors[colorIndex];

      // Draw particle
      this.ctx.fillStyle = color;
      this.ctx.globalAlpha = particle.opacity;

      this.ctx.beginPath();
      this.ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
      this.ctx.fill();

      // Draw trail
      this.ctx.globalAlpha = particle.opacity * 0.3;
      this.ctx.beginPath();
      this.ctx.arc(
        particle.x - (particle.size * 2),
        particle.y,
        particle.size * 0.6,
        0,
        Math.PI * 2
      );
      this.ctx.fill();

      this.ctx.globalAlpha = 1;
    });
  }

  /**
   * Destroy visualizer
   */
  destroy() {
    this.stop();
    window.removeEventListener('resize', () => this.resizeCanvas());
  }
}

// Listen for demo-loaded event
document.addEventListener('demo-loaded', (e) => {
  if (e.detail.type === 'cascade-flow') {
    const visualizer = new CascadeFlowVisualizer(e.detail.canvas, e.detail.config);
    visualizer.initialize();

    // Store reference for cleanup
    e.detail.canvas.visualizer = visualizer;
  }
});
