# AGENT BRIEFING: Pokemon Battle Assistant Ultimate Upgrade

**Mission:** Build comprehensive Pokemon GO PvP toolkit
**Agents:** 10 outcome-generator agents (parallel execution)
**Timeline:** 45 minutes
**Output:** 10 feature modules for integration

---

## PROJECT CONTEXT

### Current State
- Single HTML file (1.6MB) with basic rankings browser
- Uses only rankings directory from pvpoke/pvpoke GitHub repo
- Coverage: ~5% of available data
- Features: 1 (file browser only)

### Target State
- Comprehensive PvP toolkit with 10 feature modules
- Uses full gamemaster.json (1.68MB) with all Pokemon/move data
- Coverage: 100% of pvpoke data
- Features: 10 (complete battle assistant)

### Data Source
**pvpoke/pvpoke GitHub repository:** https://github.com/pvpoke/pvpoke

**Key files:**
- `src/data/gamemaster.json` - All Pokemon and move data (1.68MB)
- `src/js/GameMaster.js` - Data loading logic
- `src/js/battle/` - Battle simulation modules
- `src/data/rankings/` - Pre-calculated rankings

---

## DATA SCHEMAS

### Pokemon Object
```javascript
{
  dex: 1,                                    // Pokedex number
  speciesName: "Bulbasaur",                  // Display name
  speciesId: "bulbasaur",                    // Unique ID
  baseStats: { atk: 118, def: 111, hp: 128 }, // Base stats
  types: ["grass", "poison"],                // Type array
  fastMoves: ["vine_whip", "tackle"],        // Available fast moves
  chargedMoves: ["power_whip", "sludge_bomb", "seed_bomb"], // Charged moves
  eliteMoves: [],                            // Legacy/exclusive moves
  tags: ["starter"],                         // Classification tags
  released: true,                            // Availability
  family: {                                  // Evolution family
    id: "bulbasaur",
    evolutions: ["ivysaur", "venusaur"]
  },
  buddyDistance: 3,                          // Km per candy
  thirdMoveCost: 10000,                      // Stardust for 2nd charged move
  defaultIVs: {                              // Recommended IVs per league
    cp500: { level: 15.5, ivs: { atk: 0, def: 15, hp: 15 } },
    cp1500: { level: 29, ivs: { atk: 0, def: 15, hp: 14 } },
    cp2500: { level: 40, ivs: { atk: 0, def: 15, hp: 15 } }
  },
  level25CP: 987                             // CP at level 25
}
```

### Move Object
```javascript
{
  moveId: "vine_whip",       // Unique ID
  name: "Vine Whip",         // Display name
  type: "grass",             // Move type
  power: 5,                  // Base damage
  energy: 4,                 // Energy gained (fast) or cost (charged)
  duration: 1,               // Animation duration
  turns: 2,                  // PvP turns
  archetype: "fast",         // "fast" or "charged"
  buffs: null,               // Stat changes (if applicable)
  buffApplyChance: 0,        // Buff probability
  buffTarget: "self"         // "self" or "opponent"
}
```

### Type Effectiveness Matrix
```javascript
{
  normal: { rock: 0.625, ghost: 0.390625, steel: 0.625, ... },
  fire: { fire: 0.625, water: 0.625, grass: 1.6, ice: 1.6, bug: 1.6, ... },
  water: { fire: 1.6, water: 0.625, grass: 0.625, ground: 1.6, ... },
  // ... (18 types total)
}
```

---

## TECHNICAL REQUIREMENTS

### UI Framework
- **Style:** Dark theme matching existing assistant (dark blue/purple background)
- **Layout:** Tabbed interface with 10 tabs (one per feature)
- **Components:** Shared Pokemon cards, stat displays, move selectors
- **Responsive:** Mobile-friendly grid layouts
- **No external dependencies:** Pure HTML/CSS/JavaScript

### Code Patterns
```javascript
// Pokemon card component example
function createPokemonCard(pokemon) {
  return `
    <div class="pokemon-card" data-id="${pokemon.speciesId}">
      <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokemon.dex}.png" />
      <h3>${pokemon.speciesName}</h3>
      <div class="types">
        ${pokemon.types.map(t => `<span class="type type-${t}">${t}</span>`).join('')}
      </div>
      <div class="stats">
        <span>ATK: ${pokemon.baseStats.atk}</span>
        <span>DEF: ${pokemon.baseStats.def}</span>
        <span>HP: ${pokemon.baseStats.hp}</span>
      </div>
    </div>
  `;
}
```

### Data Loading
```javascript
// Load gamemaster.json data
async function loadGameMaster() {
  const response = await fetch('https://raw.githubusercontent.com/pvpoke/pvpoke/master/src/data/gamemaster.json');
  const data = await response.json();
  return {
    pokemon: data.pokemon,
    moves: data.moves
  };
}
```

---

## WORK PACKAGES

Each agent builds ONE feature module. All modules share the same data source and UI patterns.

### Package 1: Pokemon Database Browser
**Features:**
- Grid view of all Pokemon (1000+) with sprites
- Search by name, filter by type/generation/tags
- Sort by stats, CP, dex number
- Pokemon detail modal (stats, moves, evolution chain)
- Type effectiveness for selected Pokemon
- Comparison tool (2-3 Pokemon side-by-side)

**Deliverable:** `pokemon-browser.html` (standalone module)

---

### Package 2: Move Database & Calculator
**Features:**
- Complete move list (fast + charged)
- Move details: damage, energy, duration, DPT, EPT, DPE
- Filter by type, archetype
- Sort by damage, energy efficiency
- Move comparison tool
- Type effectiveness multipliers
- Best moves per type chart

**Deliverable:** `move-database.html` (standalone module)

---

### Package 3: Battle Simulator Engine
**Features:**
- 1v1 Pokemon battle simulator
- Pokemon selection with move customization
- Real-time battle visualization
- Fast move cycling, energy tracking
- Charged move execution with shields
- HP tracking, turn counter
- Battle log with move history
- Optimal move sequence suggester

**Deliverable:** `battle-simulator.html` (standalone module)

---

### Package 4: IV Calculator & Optimizer
**Features:**
- IV input interface (ATK/DEF/HP: 0-15)
- Level slider (1-50)
- CP calculator
- Stat product calculation
- League rank checker (Great/Ultra/Master)
- IV spread optimizer (find #1 rank)
- Breakpoint calculator
- Power-up cost estimator

**Deliverable:** `iv-calculator.html` (standalone module)

---

### Package 5: Team Builder & Analyzer
**Features:**
- 3-Pokemon team selector
- Type coverage heatmap (18 types)
- Weakness/resistance analysis
- Threat score vs common meta Pokemon
- Team synergy calculator
- Safe swap identifier
- Counter suggestions
- Export team composition

**Deliverable:** `team-builder.html` (standalone module)

---

### Package 6: Rankings Viewer Enhanced
**Features:**
- League selector (Great/Ultra/Master/Custom)
- Meta selector (all available metas)
- Filter by type, role, generation
- Sort by score, consistency, TDO, bulk
- Pokemon preview on hover
- Move suggestions for top Pokemon
- Export to CSV
- Favorite Pokemon lists

**Deliverable:** `rankings-enhanced.html` (standalone module)

---

### Package 7: Type Effectiveness Matrix
**Features:**
- 18×18 interactive type chart
- Click cell to see multiplier details
- Single-type lookup
- Dual-type calculator
- Coverage checker (what types does my Pokemon/team hit?)
- Best offensive/defensive types
- Triple resistance finder (0.244x)
- STAB calculator

**Deliverable:** `type-chart.html` (standalone module)

---

### Package 8: Meta Analysis Dashboard
**Features:**
- Current meta snapshot (top 20 per league)
- Usage statistics chart
- Trending up/down Pokemon
- Team archetypes (common cores)
- Spice picks (off-meta but effective)
- Win rate correlations
- Move usage stats
- Shield usage patterns

**Deliverable:** `meta-dashboard.html` (standalone module)

---

### Package 9: Training Battle Mode
**Features:**
- Practice battles vs AI (Easy/Medium/Hard)
- Energy management training
- Shield baiting scenarios
- Fast move counting practice
- Type coverage challenges
- Battle metrics tracking
- Hints and tips
- Progress tracking

**Deliverable:** `training-mode.html` (standalone module)

---

### Package 10: Advanced Tools Suite
**Features:**
- Breakpoint finder (IV thresholds for damage)
- Bulkpoint calculator (survive specific moves)
- Energy advantage simulator
- CMP checker (attack stat tiebreaker)
- Shadow vs Normal comparison
- Mega evolution planner
- Lucky trade IV estimator
- Stardust ROI calculator

**Deliverable:** `advanced-tools.html` (standalone module)

---

## SUCCESS CRITERIA

Each module must:
- ✅ Be a standalone HTML file (can run independently)
- ✅ Use consistent dark theme styling
- ✅ Load gamemaster.json data from pvpoke GitHub
- ✅ Include all features listed in package description
- ✅ Be mobile-responsive
- ✅ Have clear UI with intuitive controls
- ✅ Include inline documentation/help text
- ✅ Handle errors gracefully
- ✅ Use shared component patterns (Pokemon cards, stat displays)
- ✅ Be ready for integration into unified app

---

## INTEGRATION NOTES

After all 10 modules are built, an integrator agent will:
1. Combine all modules into tabbed interface
2. Unify data loading (load gamemaster.json once)
3. Share state across tabs (e.g., selected Pokemon)
4. Create unified navigation
5. Optimize file size (dedupe code)

Each agent should focus ONLY on their assigned package. Don't worry about integration - that's the integrator's job.

---

## REFERENCE MATERIALS

- pvpoke repo: https://github.com/pvpoke/pvpoke
- gamemaster.json: https://raw.githubusercontent.com/pvpoke/pvpoke/master/src/data/gamemaster.json
- Existing assistant: Pokemon Battle Assistant.html (for styling reference)
- PokeAPI sprites: https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{dex}.png

---

**Agent Instructions:**
1. Read this briefing completely
2. Fetch gamemaster.json to understand data structure
3. Build your assigned feature module
4. Test all functionality
5. Deliver standalone HTML file
6. Report completion with feature summary

**Timeline:** Complete within 45 minutes
**Quality bar:** Production-ready, fully functional, user-friendly

GO GO GO! 🚀
