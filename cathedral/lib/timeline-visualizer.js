/**
 * Timeline Visualizer
 * Process orchestration showing parallel execution over time
 * Used for: Automation Orchestrator
 * Pattern from: Production-Ready + Simplicity strategies
 */

class TimelineVisualizer {
  constructor(canvas, config) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.config = {
      processes: config.processes || 50,
      artifacts: config.artifacts || 300,
      parallelism: config.parallelism || 16,
      duration: 10000,
      ...config
    };

    this.processes = [];
    this.startTime = null;
    this.animationId = null;
    this.isRunning = false;
  }

  initialize() {
    this.resizeCanvas();
    window.addEventListener('resize', () => this.resizeCanvas());

    this.createProcesses();
    this.start();
  }

  resizeCanvas() {
    const container = this.canvas.parentElement;
    this.canvas.width = container.clientWidth;
    this.canvas.height = container.clientHeight;
  }

  createProcesses() {
    const laneHeight = this.canvas.height / this.config.parallelism;

    for (let i = 0; i < this.config.processes; i++) {
      const lane = i % this.config.parallelism;
      const startTime = Math.random() * 0.3; // Start within first 30%
      const duration = 0.1 + Math.random() * 0.2; // 10-30% of total time

      this.processes.push({
        id: i,
        lane: lane,
        startTime: startTime,
        duration: duration,
        progress: 0,
        status: 'pending', // pending, running, complete
        artifactsCreated: Math.floor(Math.random() * 10) + 1
      });
    }
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
    const overallProgress = Math.min((elapsed / this.config.duration), 1);

    // Clear canvas
    this.ctx.fillStyle = 'rgba(10, 14, 39, 1)';
    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

    // Draw lane lines
    this.drawLanes();

    // Update and draw processes
    this.updateProcesses(overallProgress);
    this.drawProcesses();

    // Draw metrics
    this.drawMetrics(overallProgress);

    this.animationId = requestAnimationFrame(() => this.animate());
  }

  drawLanes() {
    const laneHeight = this.canvas.height / this.config.parallelism;

    this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.05)';
    this.ctx.lineWidth = 1;

    for (let i = 0; i <= this.config.parallelism; i++) {
      const y = i * laneHeight;
      this.ctx.beginPath();
      this.ctx.moveTo(0, y);
      this.ctx.lineTo(this.canvas.width, y);
      this.ctx.stroke();
    }
  }

  updateProcesses(overallProgress) {
    this.processes.forEach(process => {
      const processEnd = process.startTime + process.duration;

      if (overallProgress < process.startTime) {
        process.status = 'pending';
        process.progress = 0;
      } else if (overallProgress >= processEnd) {
        process.status = 'complete';
        process.progress = 1;
      } else {
        process.status = 'running';
        process.progress = (overallProgress - process.startTime) / process.duration;
      }
    });
  }

  drawProcesses() {
    const laneHeight = this.canvas.height / this.config.parallelism;
    const barHeight = laneHeight * 0.6;
    const padding = 50;
    const timelineWidth = this.canvas.width - padding * 2;

    this.processes.forEach(process => {
      const x = padding + (process.startTime * timelineWidth);
      const width = Math.max(process.duration * timelineWidth * process.progress, 2);
      const y = (process.lane * laneHeight) + (laneHeight - barHeight) / 2;

      // Determine color by status
      let color;
      if (process.status === 'pending') {
        color = 'rgba(160, 174, 192, 0.3)';
      } else if (process.status === 'running') {
        color = '#667eea';
      } else {
        color = '#48bb78';
      }

      // Draw process bar
      this.ctx.fillStyle = color;
      this.ctx.fillRect(x, y, width, barHeight);

      // Draw glow for running processes
      if (process.status === 'running') {
        this.ctx.shadowBlur = 10;
        this.ctx.shadowColor = color;
        this.ctx.fillRect(x, y, width, barHeight);
        this.ctx.shadowBlur = 0;
      }
    });
  }

  drawMetrics(overallProgress) {
    const completed = this.processes.filter(p => p.status === 'complete').length;
    const running = this.processes.filter(p => p.status === 'running').length;
    const totalArtifacts = this.processes
      .filter(p => p.status === 'complete')
      .reduce((sum, p) => sum + p.artifactsCreated, 0);

    this.ctx.fillStyle = '#ffffff';
    this.ctx.font = 'bold 16px -apple-system, sans-serif';
    this.ctx.textAlign = 'left';

    this.ctx.fillText(`Progress: ${Math.floor(overallProgress * 100)}%`, 20, 30);
    this.ctx.fillText(`Completed: ${completed}/${this.config.processes}`, 20, 55);
    this.ctx.fillText(`Running: ${running}`, 20, 80);
    this.ctx.fillText(`Artifacts: ${totalArtifacts}`, 20, 105);
  }

  destroy() {
    this.stop();
    window.removeEventListener('resize', () => this.resizeCanvas());
  }
}

// Listen for demo-loaded event
document.addEventListener('demo-loaded', (e) => {
  if (e.detail.type === 'timeline') {
    const visualizer = new TimelineVisualizer(e.detail.canvas, e.detail.config);
    visualizer.initialize();
    e.detail.canvas.visualizer = visualizer;
  }
});
