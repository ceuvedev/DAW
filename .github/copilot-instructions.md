# Copilot Instructions for DAW Course Repository

## Repository Overview
This is a **Desarrollo de Aplicaciones Web (DAW)** course workspace containing coursework, notes, and practical exercises across multiple web development subjects. It's organized by subject folders rather than a single project.

## Architecture & Folder Structure

### Subject Areas (Primary Organization)
- **Lenguaje de marcas/** - HTML/CSS markup exercises and projects
  - `tasques/` - Individual exercises (exercici1-15) with incremental complexity
  - `js/` - JavaScript practice files (practica1.js, practica3.js)
  - `practica_final_U2/` - Final unit projects combining HTML/CSS/JS

- **Programación/** - Python exercises and scripting
  - Files follow `tema{N}.py` naming (tema2, tema3, tema4)
  - Individual exercises with `activitat.py`, `basket.py`, etc.

- **BD/** - Database (Base de Datos) coursework

- **IPO 1/** - UI Programming (Interfaz de Usuario)

- **Entornos de desarrollo/** - Development environments setup and Python basics

- **Other folders** - Inglés profesional, Sistemas informáticos, Projecte intermodular

## Key Conventions & Patterns

### HTML/CSS Projects
- **File organization**: Each `exerciciN/` folder contains complete exercise with `index.html` (or `.htm`) and optional `style.css`
- **Comments structure**: Exercises use numbered HTML comments for sections:
  ```html
  <!-- 1a parte del ejercicio -->
  <!-- 2da parte del ejercicio -->
  <!-- 3a parte del ejercicio -->
  ```
- **CSS approach**: Inline styles or external stylesheets; uses RGB color values, semantic selectors
- **Language**: Spanish comments and user-facing content (mixed with English in some exercises)

### JavaScript Files
- Use `"use strict";` at the top of practice files
- Type checking pattern: `typeof num !== 'number' && Number.isNaN(num)` for validation
- Console functions are used for output (though `print()` appears in exercises - may indicate teaching tool context)

### Python Exercises
- **Naming**: Exercise comments reference unit and exercise number (`# Exercici 5 - UD2`)
- **Language mix**: Code comments in Catalan/Spanish (`Dona'm`, `Dis-me`)
- **Input/output**: Console-based with `input()` and `print()`
- **No external dependencies**: Pure Python exercises

## Development Workflows

### For Markup Exercises
1. Open HTML file in browser to test
2. Modify HTML structure in `indexN.html`
3. Update related `style.css`
4. Check semantic structure and CSS selectors

### For Python Exercises
1. Run with `python3 filename.py`
2. Follow interactive console input prompts
3. Exercises are self-contained (no imports or dependencies)

### For JavaScript Practice
1. Files may require browser execution or Node.js
2. Strict mode enforced for type safety
3. Basic validation patterns expected

## File Naming Conventions
- HTML exercises: `exerciciN/index.html` (or `.htm`)
- Python files: `temaX.py`, `activitat.py`, `basket.py`
- JavaScript: `practicaN.js`
- Styling: `style.css` collocated with HTML
- Task documentation: `tasques/` subdirectories contain work

## When Editing
- **Preserve folder structure** - each exercise is self-contained in its directory
- **Language consistency** - maintain Spanish comments matching existing code
- **Semantic HTML** - use proper heading hierarchy and sectioning elements
- **Testing context** - many exercises are learning exercises (may have intentional imperfections)
- **No build system** - these are raw HTML/CSS/JavaScript files, not compiled/bundled

## Cross-Subject Integration
- **Projecte intermodular/** - Final capstone project integrating multiple subjects (Entrega_1 folder structure)
- Reference exercises from other subjects when implementing integrated features
