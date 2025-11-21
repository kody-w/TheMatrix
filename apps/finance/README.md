# Finance Applications

**Category**: Investment & Portfolio Management Tools

This directory contains financial planning and investment management applications built with The Matrix framework.

---

## Applications

### Portfolio Steward
**File**: `portfolio-steward.html`
**Size**: 1,947 lines
**Description**: Comprehensive investment management platform

**Features**:
- 📊 Real-time portfolio tracking and visualization
- 📈 Interactive charts powered by Chart.js
- 🎨 3D data visualizations using Three.js
- 💰 Asset allocation analysis
- 📱 Mobile-responsive design
- 🌈 Modern gradient UI with glassmorphism
- 💾 Local-first data storage

**Technologies**:
- Three.js for 3D visualizations
- Chart.js for financial charts
- LocalStorage for data persistence
- Responsive CSS Grid/Flexbox layout

**Use Cases**:
- Personal investment tracking
- Portfolio performance monitoring
- Asset allocation planning
- Investment decision support
- Financial goal tracking

---

## Architecture

All finance apps follow The Matrix principles:

- ✅ **Self-Contained**: Complete HTML files with embedded CSS/JavaScript
- ✅ **Local-First**: Data stored in browser, no backend required
- ✅ **CDN Dependencies**: Uses CDN resources for Chart.js and Three.js (no build process)
- ✅ **Offline-Capable**: Works without network once loaded
- ✅ **Mobile-Friendly**: Responsive design for all devices
- ✅ **Privacy-Focused**: All data stays local

---

## Usage

### Opening Applications

Simply open any HTML file in a modern web browser:

```bash
# Open Portfolio Steward
open portfolio-steward.html

# Or via HTTP server
python3 -m http.server 8000
# Navigate to http://localhost:8000/portfolio-steward.html
```

### Data Persistence

All apps use browser LocalStorage for data persistence:
- Data persists across browser sessions
- No server or database required
- Export/import functionality included
- Clear data option for privacy

---

## Development

### Adding New Finance Apps

Follow The Matrix app development patterns:

1. **Self-contained HTML file** - All code in one file
2. **CDN dependencies allowed** - For chart libraries, visualization tools
3. **Local-first data** - Use LocalStorage or IndexedDB
4. **Responsive design** - Mobile-first approach
5. **Modern UI** - Gradient backgrounds, glassmorphism, smooth animations

### Financial Data Security

**Important**: These apps are demonstration tools:
- ⚠️ Not financial advice
- ⚠️ Use at your own risk
- ⚠️ Always consult financial professionals
- ⚠️ Data stored locally (clear browser data to delete)

---

## Future Applications (Planned)

- **Budget Tracker** - Personal expense management
- **Retirement Calculator** - Long-term financial planning
- **Crypto Portfolio** - Cryptocurrency tracking
- **Tax Estimator** - Income tax calculation tools
- **Loan Calculator** - Mortgage and loan analysis
- **Investment Screener** - Stock/fund screening tools

---

## Contributing

To add new finance applications:

1. Create self-contained HTML file in this directory
2. Follow existing app patterns (Portfolio Steward as reference)
3. Test in multiple browsers
4. Add to this README with description
5. Run configuration generator:
   ```bash
   python3 scripts/generate-apps-config.py
   ```

---

## Resources

**Financial Data APIs** (for future integration):
- Alpha Vantage - Stock market data
- CoinGecko - Cryptocurrency prices
- Yahoo Finance - Market data
- IEX Cloud - Real-time financial data

**Charting Libraries** (currently used):
- Chart.js - Beautiful charts and graphs
- Three.js - 3D data visualization
- D3.js - Advanced data visualization (potential)

---

## License

MIT License - See repository root LICENSE file

---

**Last Updated**: 2025-11-21 by Portfolio Steward Agent
**Category Status**: Active Development
**Total Apps**: 2
