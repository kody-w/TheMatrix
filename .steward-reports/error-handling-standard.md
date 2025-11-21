# Standard Error Handling Pattern for HTML Apps

## Overview
This document defines the standard error handling pattern applied to all Matrix HTML applications during Phase 4 code quality improvements.

## Pattern Implementation

### Global Error Handler
Add to the beginning of every `<script>` section:

```javascript
// Global error handler
window.onerror = function(msg, url, lineNo, columnNo, error) {
    console.error('Error: ' + msg + '\nURL: ' + url + '\nLine: ' + lineNo);
    // User-friendly error notification
    const statsEl = document.getElementById('stats'); // Adapt to app's status element
    if (statsEl) {
        statsEl.innerHTML = '<span style="color: #ff4444;">⚠️ An error occurred. Check console for details.</span>';
    }
    return false;
};

// Promise rejection handler
window.addEventListener('unhandledrejection', function(event) {
    console.error('Unhandled promise rejection:', event.reason);
});
```

### Function-Level Error Handling
Wrap critical functions with try-catch:

```javascript
async function criticalFunction() {
    try {
        // Critical operations
        const result = await someOperation();
        return result;
    } catch (error) {
        console.error('Function failed:', error);
        // Graceful degradation
        return defaultValue;
    }
}
```

## Applied To

### Phase 4 - Completed Implementations

1. **index.html** (main gateway)
   - Global error handler with visual notifications
   - Promise rejection handling
   - Status: ✅ Complete

2. **apps-gallery.html** (app browser)
   - Global error handler
   - Enhanced loadApps() with validation
   - Error handling in filterByCategory()
   - Error handling in searchApps()
   - Error handling in openApp()
   - Status: ✅ Complete

### Recommended for Future Phases

High-priority files for error handling:
- pokemon-battle-assistant-v1.html (23,756 lines - complex game logic)
- windows95-emulator.html (21,153 lines - complex emulation)
- wristAI.html (6,633 lines - AI interface)
- Copilot_Companion.html (6,439 lines - AI assistant)
- NexusWorlds.html (6,177 lines - complex 3D game)

## Benefits

- ✅ Prevents white screen of death
- ✅ User-friendly error messages
- ✅ Console logging for debugging
- ✅ Graceful degradation
- ✅ Production-ready error handling

## JSDoc Documentation Pattern

### Standard Function Documentation

```javascript
/**
 * Function description
 * @async (if async)
 * @param {type} paramName - Parameter description
 * @returns {type} Return value description
 * @throws {Error} Error conditions (if applicable)
 * @example
 * functionName(exampleInput)
 */
function functionName(paramName) {
    // implementation
}
```

### Applied To

1. **apps-gallery.html**
   - loadApps() - Complete JSDoc with @async, @returns, @throws, @example
   - filterByCategory() - Complete JSDoc with @param, @example
   - searchApps() - Complete JSDoc with @param, @example
   - openApp() - Complete JSDoc with @param, @example

## Code Quality Metrics

### apps-gallery.html Improvements
- Error handling functions: 5
- JSDoc documented functions: 4
- Error recovery paths: 3
- User-facing error messages: 2

### index.html Improvements
- Error handling functions: 1 (global)
- Promise rejection handling: 1
- Visual error notifications: 1

## Next Steps

For future steward runs:
1. Apply error handling pattern to top 10 complex HTML apps
2. Add JSDoc to all public functions in complex apps
3. Implement retry logic for network operations
4. Add error tracking/analytics (optional)

---

Generated: 2025-11-20
Phase: 4 (Code Quality)
Steward: Autonomous Code Improvement Agent
