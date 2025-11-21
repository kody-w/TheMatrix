# Pokemon Battle Assistant Suite

A comprehensive collection of Pokemon GO battle tools and utilities for competitive PvP analysis.

## Overview

This directory contains multiple specialized Pokemon battle tools, each designed for specific aspects of competitive Pokemon GO gameplay. All tools are standalone HTML applications that work entirely in the browser with no backend requirements.

## Tool Variants

### Core Battle Assistants

#### pokemon-battle-assistant-v1.html
- **Purpose**: Original battle assistant with comprehensive feature set
- **Size**: ~1.6MB (includes extensive Pokemon data)
- **Features**:
  - Real-time battle tracking
  - Type effectiveness calculator
  - Move database integration
  - IV analysis
  - Team composition suggestions
- **Best For**: Players who want the full suite in one app
- **Data**: Embedded Pokemon database

#### pokemon-battle-assistant-v2.html
- **Purpose**: Enhanced version with improved UI and performance
- **Size**: ~49KB (optimized, uses external data sources)
- **Features**:
  - Modern responsive UI
  - Faster load times
  - Cloud data integration
  - Enhanced battle simulations
  - Meta analysis dashboard
- **Best For**: Mobile users and those wanting faster performance
- **Data**: Loads from external APIs

### Specialized Tools

#### battle-simulator.html
**Purpose**: Advanced battle simulation engine
- Simulate battles between any Pokemon matchups
- Test different move sets and strategies
- Analyze damage calculations
- View energy generation and timing
- Export simulation results
**Use Case**: Testing specific matchups before live battles

#### iv-calculator.html
**Purpose**: Individual Value (IV) calculator and optimizer
- Calculate exact IVs from in-game stats
- Optimize IVs for specific leagues (Great, Ultra, Master)
- Rank spreads by stat product
- CP evolution calculator
- Bulk IV checking
**Use Case**: Determining which Pokemon to power up

#### meta-dashboard.html
**Purpose**: Meta-game analysis and tracking
- Current meta rankings by league
- Usage statistics
- Trend analysis over time
- Counter picks for popular Pokemon
- Team composition insights
**Use Case**: Staying current with competitive meta

#### move-database.html
**Purpose**: Comprehensive move reference
- All fast and charged moves
- Damage, energy, and duration data
- Type effectiveness multipliers
- Move availability by Pokemon
- DPS and EPS calculations
**Use Case**: Learning move stats and availability

#### pokemon-browser.html
**Purpose**: Pokemon database explorer
- Browse all available Pokemon
- Filter by type, stats, moves
- View base stats and CP ranges
- Check evolution chains
- Search and sort capabilities
**Use Case**: Researching Pokemon for team building

#### rankings-enhanced.html
**Purpose**: Enhanced PvP rankings viewer
- Rankings for Great, Ultra, and Master leagues
- Filter by type and role
- Compare Pokemon side-by-side
- View optimal IV spreads
- Export rankings data
**Use Case**: Finding top performers for each league

#### team-builder.html
**Purpose**: Team composition and analysis tool
- Build teams of 6 Pokemon
- Analyze type coverage
- Identify weaknesses
- Suggest counters
- Save and load teams
**Use Case**: Creating balanced competitive teams

#### training-mode.html
**Purpose**: Battle practice and skill training
- Practice fast move timing
- Learn charge move baiting
- Shield management drills
- Switch timing exercises
- Performance tracking
**Use Case**: Improving mechanical battle skills

#### type-chart.html
**Purpose**: Type effectiveness reference matrix
- Complete type matchup chart
- Quick effectiveness lookups
- Dual-type calculations
- STAB bonus information
- Visual color coding
**Use Case**: Quick reference during team building

## Feature Comparison

| Tool | Battle Sim | IV Calc | Meta | Database | Team Build | Rankings | Training |
|------|-----------|---------|------|----------|------------|----------|----------|
| **Offline** | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ |
| **Mobile** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Size** | ~43KB | ~42KB | ~37KB | ~38KB | ~47KB | ~46KB | ~77KB |
| **Data Source** | Embedded | Calc | API | Embedded | Embedded | API | Embedded |

## Which Tool Should I Use?

### For Complete Beginners
Start with **pokemon-battle-assistant-v2.html** - it has the most user-friendly interface and provides guided workflows.

### For Competitive Players
Use **meta-dashboard.html** + **team-builder.html** + **battle-simulator.html** for complete competitive analysis.

### For Team Building
1. **rankings-enhanced.html** - Find top performers
2. **team-builder.html** - Create balanced teams
3. **battle-simulator.html** - Test matchups

### For IV Optimization
**iv-calculator.html** is the dedicated tool with the most comprehensive IV features.

### For Quick Reference
- **type-chart.html** for type matchups
- **move-database.html** for move stats
- **pokemon-browser.html** for Pokemon lookup

## Data Sources

### Embedded Data (Works Offline)
- pokemon-battle-assistant-v1.html
- battle-simulator.html
- iv-calculator.html
- move-database.html
- pokemon-browser.html
- team-builder.html
- training-mode.html
- type-chart.html

### External APIs (Requires Internet)
- pokemon-battle-assistant-v2.html
- meta-dashboard.html
- rankings-enhanced.html

## Development History

### Version 1 (Original)
- Comprehensive all-in-one tool
- Large file size due to embedded data
- Full offline functionality
- Rich feature set

### Version 2 (Enhanced)
- Modernized UI with responsive design
- Smaller file size using external data
- Improved performance
- Enhanced visualizations
- Better mobile experience

### Specialized Tools
Created to provide focused functionality for specific use cases while maintaining smaller file sizes and faster load times.

## Technical Details

### Technologies Used
- Pure HTML/CSS/JavaScript (no frameworks)
- Local storage for saving preferences
- Canvas for visualizations
- Responsive design for mobile support

### Browser Compatibility
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

### File Size Optimization
- Version 1: ~1.6MB (full data embedded)
- Version 2: ~49KB (external data)
- Specialized tools: 35-80KB each

## Usage Tips

1. **Bookmark Your Favorites**: Each tool is standalone, so bookmark the ones you use most
2. **Use Multiple Tools**: Open several tools in tabs for comprehensive analysis
3. **Save Your Data**: Most tools support local storage to save your preferences and teams
4. **Mobile Access**: All tools work on mobile devices - add to home screen for app-like experience
5. **Offline Use**: Download v1 or specialized tools for offline battle tournaments

## Future Enhancements

Potential improvements being considered:
- PWA (Progressive Web App) support for better offline experience
- Data sync between tools
- Team sharing and import/export
- Battle log analysis
- Integration with Pokemon GO screenshots
- IV scanning from screenshots
- Automated team suggestions based on meta

## Contributing

These tools are part of The Matrix framework. To contribute:
1. Test thoroughly before submitting changes
2. Maintain standalone functionality (no external dependencies)
3. Keep file sizes optimized
4. Ensure mobile compatibility
5. Document all features

## License

Part of The Matrix - MIT License

## Support

For issues or feature requests, see the main Matrix repository documentation.

---

**Choose the right tool for your needs and dominate the competitive Pokemon GO scene!**
