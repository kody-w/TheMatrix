/**
 * The Matrix Cathedral Router
 * Manifest-driven demonstration gallery (Scalability Strategy)
 * With error handling (Production-Ready Strategy) and performance optimization (Performance Strategy)
 */

class Cathedral {
  constructor(manifest) {
    this.manifest = manifest;
    this.currentView = 'gallery';
    this.currentDemo = null;
    this.filterCategory = null;
    this.searchQuery = '';
    this.errorLog = [];
  }

  /**
   * Initialize cathedral system
   * @param {string} containerId - Container element ID
   */
  async initialize(containerId) {
    try {
      this.container = document.querySelector(containerId);
      if (!this.container) {
        throw new Error(`Container ${containerId} not found`);
      }

      // Setup navigation
      this.setupRouting();

      // Initial render
      await this.showGallery();

      console.log('✅ Cathedral initialized successfully');
    } catch (error) {
      this.handleError(error, 'Cathedral initialization');
    }
  }

  /**
   * Setup browser history and keyboard navigation
   */
  setupRouting() {
    // Browser back/forward
    window.addEventListener('popstate', async (e) => {
      if (e.state?.view === 'demo') {
        await this.showDemo(e.state.demoId, false);
      } else {
        await this.showGallery(false);
      }
    });

    // Keyboard shortcuts (UX Strategy)
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && this.currentView === 'demo') {
        window.history.back();
      }
    });
  }

  /**
   * Show demo gallery
   */
  async showGallery(updateHistory = true) {
    try {
      this.currentView = 'gallery';
      this.container.innerHTML = '';

      if (updateHistory) {
        window.history.pushState({ view: 'gallery' }, '', '#gallery');
      }

      // Create header
      const header = this.createHeader();
      this.container.appendChild(header);

      // Create gallery
      const gallery = this.createGallery();
      this.container.appendChild(gallery);

      // Setup event listeners
      this.attachGalleryListeners();

    } catch (error) {
      this.handleError(error, 'Gallery rendering');
    }
  }

  /**
   * Create cathedral header with search and filters
   */
  createHeader() {
    const header = document.createElement('header');
    header.className = 'cathedral-header';

    header.innerHTML = `
      <div class="cathedral-title">
        <h1>${this.manifest.cathedral.title}</h1>
        <p>${this.manifest.cathedral.subtitle}</p>
      </div>
      <div class="cathedral-controls">
        <input
          type="search"
          id="demo-search"
          placeholder="Search demonstrations..."
          class="search-input"
          autocomplete="off"
        >
        <div class="category-filters">
          <button class="filter-btn active" data-category="all">All</button>
          ${this.manifest.categories.map(cat => `
            <button class="filter-btn" data-category="${cat.id}">${cat.label}</button>
          `).join('')}
        </div>
      </div>
    `;

    return header;
  }

  /**
   * Create demo gallery grid
   */
  createGallery() {
    const gallery = document.createElement('div');
    gallery.className = 'demo-gallery';
    gallery.id = 'demo-gallery';

    const demos = this.getFilteredDemonstrations();

    if (demos.length === 0) {
      gallery.innerHTML = '<p class="no-results">No demonstrations match your search</p>';
      return gallery;
    }

    demos.forEach(demo => {
      const card = this.createDemoCard(demo);
      gallery.appendChild(card);
    });

    return gallery;
  }

  /**
   * Create individual demo card
   */
  createDemoCard(demo) {
    const category = this.manifest.categories.find(c => c.id === demo.category);

    const card = document.createElement('div');
    card.className = 'demo-card';
    card.dataset.demoId = demo.id;

    card.innerHTML = `
      <div class="demo-card-header">
        <h3>${demo.title}</h3>
        <span class="category-tag" style="background-color: ${category?.color || '#667eea'}">${category?.label || 'Demo'}</span>
      </div>

      <p class="demo-description">${demo.shortDescription}</p>

      <div class="demo-metrics">
        ${this.renderMetrics(demo.metrics)}
      </div>

      <button class="explore-btn">Explore →</button>
    `;

    return card;
  }

  /**
   * Render demo metrics
   */
  renderMetrics(metrics) {
    const metricEntries = Object.entries(metrics).slice(0, 4);

    return metricEntries.map(([key, value]) => `
      <div class="metric">
        <span class="metric-label">${this.formatMetricLabel(key)}</span>
        <span class="metric-value">${this.formatMetricValue(value)}</span>
      </div>
    `).join('');
  }

  formatMetricLabel(key) {
    return key
      .replace(/([A-Z])/g, ' $1')
      .replace(/^./, str => str.toUpperCase())
      .trim();
  }

  formatMetricValue(value) {
    if (typeof value === 'number') {
      if (value > 1000) {
        return value.toLocaleString();
      }
      if (value < 1) {
        return `${(value * 100).toFixed(1)}%`;
      }
      return value.toString();
    }
    return value;
  }

  /**
   * Attach event listeners to gallery
   */
  attachGalleryListeners() {
    // Search
    const searchInput = document.getElementById('demo-search');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        this.searchQuery = e.target.value.toLowerCase();
        this.updateGallery();
      });
    }

    // Category filters
    document.querySelectorAll('.filter-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        e.target.classList.add('active');
        this.filterCategory = e.target.dataset.category === 'all' ? null : e.target.dataset.category;
        this.updateGallery();
      });
    });

    // Demo cards
    document.querySelectorAll('.demo-card').forEach(card => {
      card.addEventListener('click', () => {
        const demoId = card.dataset.demoId;
        this.showDemo(demoId);
      });
    });
  }

  /**
   * Update gallery without full re-render
   */
  updateGallery() {
    const gallery = document.getElementById('demo-gallery');
    if (!gallery) return;

    gallery.innerHTML = '';

    const demos = this.getFilteredDemonstrations();

    if (demos.length === 0) {
      gallery.innerHTML = '<p class="no-results">No demonstrations match your search</p>';
      return;
    }

    demos.forEach(demo => {
      const card = this.createDemoCard(demo);
      gallery.appendChild(card);
    });

    // Re-attach listeners to new cards
    document.querySelectorAll('.demo-card').forEach(card => {
      card.addEventListener('click', () => {
        const demoId = card.dataset.demoId;
        this.showDemo(demoId);
      });
    });
  }

  /**
   * Get filtered demonstrations based on search and category
   */
  getFilteredDemonstrations() {
    return this.manifest.demonstrations.filter(demo => {
      // Filter by category
      if (this.filterCategory && demo.category !== this.filterCategory) {
        return false;
      }

      // Filter by search
      if (this.searchQuery) {
        const searchable = `${demo.title} ${demo.description} ${demo.shortDescription}`.toLowerCase();
        if (!searchable.includes(this.searchQuery)) {
          return false;
        }
      }

      // Only enabled demos
      return demo.enabled !== false;
    }).sort((a, b) => (a.order || 999) - (b.order || 999));
  }

  /**
   * Show individual demo
   */
  async showDemo(demoId, updateHistory = true) {
    try {
      const demo = this.manifest.demonstrations.find(d => d.id === demoId);
      if (!demo) {
        throw new Error(`Demo ${demoId} not found`);
      }

      this.currentView = 'demo';
      this.currentDemo = demo;

      if (updateHistory) {
        window.history.pushState(
          { view: 'demo', demoId: demoId },
          demo.title,
          `#demo/${demoId}`
        );
      }

      this.container.innerHTML = '';

      // Create demo view
      const demoView = document.createElement('div');
      demoView.className = 'demo-view active';

      // Top bar
      const topBar = document.createElement('div');
      topBar.className = 'demo-topbar';
      topBar.innerHTML = `
        <button class="back-btn">← Back to Gallery</button>
        <h2>${demo.title}</h2>
      `;
      demoView.appendChild(topBar);

      // Content area
      const content = document.createElement('div');
      content.className = 'demo-content';

      // Visualization
      const vizContainer = document.createElement('div');
      vizContainer.className = 'visualization-container';
      vizContainer.id = 'visualization';
      vizContainer.innerHTML = '<div class="loading">Loading demonstration...</div>';
      content.appendChild(vizContainer);

      // Side panel
      const sidePanel = this.createSidePanel(demo);
      content.appendChild(sidePanel);

      demoView.appendChild(content);
      this.container.appendChild(demoView);

      // Attach back button listener
      topBar.querySelector('.back-btn').addEventListener('click', () => {
        window.history.back();
      });

      // Load demo visualization
      await this.loadDemoVisualization(demo, vizContainer);

    } catch (error) {
      this.handleError(error, 'Demo loading');
    }
  }

  /**
   * Create side panel with demo information
   */
  createSidePanel(demo) {
    const panel = document.createElement('div');
    panel.className = 'demo-side-panel';

    panel.innerHTML = `
      <div class="panel-section">
        <h3>About</h3>
        <p>${demo.description}</p>
      </div>

      <div class="panel-section">
        <h3>Metrics</h3>
        <div class="demo-metrics">
          ${this.renderMetrics(demo.metrics)}
        </div>
      </div>

      <div class="panel-section">
        <h3>Visualization</h3>
        <p>Type: <strong>${demo.visualization.type}</strong></p>
      </div>
    `;

    return panel;
  }

  /**
   * Load and initialize demo visualization
   */
  async loadDemoVisualization(demo, container) {
    try {
      // Clear loading message
      container.innerHTML = '';

      // Create canvas for visualization
      const canvas = document.createElement('canvas');
      canvas.id = 'demo-canvas';
      canvas.width = container.clientWidth;
      canvas.height = container.clientHeight;
      container.appendChild(canvas);

      // Load appropriate visualizer based on type
      const vizType = demo.visualization.type;
      const vizConfig = demo.visualization.config;

      // Initialize visualization
      window.DEMO_CONFIG = { demo, config: vizConfig };

      // Import and initialize visualizer
      // This will be handled by the visualization patterns
      const event = new CustomEvent('demo-loaded', {
        detail: { type: vizType, config: vizConfig, canvas: canvas }
      });
      document.dispatchEvent(event);

    } catch (error) {
      container.innerHTML = `
        <div class="error-message">
          Failed to load demonstration: ${error.message}
        </div>
      `;
      this.handleError(error, 'Visualization loading');
    }
  }

  /**
   * Error handling (Production-Ready Strategy)
   */
  handleError(error, context) {
    const errorObj = {
      timestamp: Date.now(),
      message: error.message,
      stack: error.stack,
      context: context
    };

    this.errorLog.push(errorObj);
    console.error(`[Cathedral Error - ${context}]`, error);

    // Show user-friendly error
    if (this.container) {
      const errorDiv = document.createElement('div');
      errorDiv.className = 'error-message';
      errorDiv.textContent = `Error: ${error.message}`;
      this.container.insertBefore(errorDiv, this.container.firstChild);

      // Auto-remove after 5 seconds
      setTimeout(() => errorDiv.remove(), 5000);
    }
  }

  /**
   * Get error report
   */
  getErrorReport() {
    return {
      totalErrors: this.errorLog.length,
      recentErrors: this.errorLog.slice(-10)
    };
  }
}

// Initialize cathedral when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeCathedral);
} else {
  initializeCathedral();
}

async function initializeCathedral() {
  try {
    // Load manifest
    const response = await fetch('manifest.json');
    if (!response.ok) {
      throw new Error('Failed to load manifest');
    }

    const manifest = await response.json();

    // Create and initialize cathedral
    const cathedral = new Cathedral(manifest);
    await cathedral.initialize('#cathedral-root');

    // Make available globally for debugging
    window.cathedral = cathedral;

  } catch (error) {
    console.error('Failed to initialize cathedral:', error);
    document.body.innerHTML = `
      <div style="display: flex; align-items: center; justify-content: center; height: 100vh; background: #0a0e27; color: white; text-align: center; padding: 20px;">
        <div>
          <h1>Cathedral Initialization Failed</h1>
          <p style="color: #a0aec0; margin-top: 1rem;">Error: ${error.message}</p>
          <button onclick="location.reload()" style="margin-top: 2rem; padding: 0.75rem 1.5rem; background: #667eea; color: white; border: none; border-radius: 8px; cursor: pointer;">
            Try Again
          </button>
        </div>
      </div>
    `;
  }
}
