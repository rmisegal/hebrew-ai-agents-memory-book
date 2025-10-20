# Project Planning Document
## Hebrew AI Agents Book - Complete Reorganization

**Last Updated:** October 20, 2025
**Project Status:** Phase 1 (50% Complete)

---

## Project Vision

Transform a draft Hebrew-language academic book about AI multi-agent systems into a **publication-ready masterpiece** that:
- Seamlessly integrates philosophy, ethics, practical implementation, and mathematics
- Reads as an original first edition (not a revision)
- Demonstrates state-of-the-art organization worthy of academic review
- Would pass scrutiny from a reader like Professor Yuval Noah Harari

**Book Title (Hebrew):** בינה מבוזרת: סוכנים אוטונומיים בעידן הבינה המלאכותית
**Book Title (English):** Distributed Intelligence: Autonomous Agents in the Age of AI

---

## Project Goals

### Primary Objectives
1. **Restructure** from 7 chapters to 6 with optimal ordering
2. **Eliminate** all content repetition and contradictions
3. **Complete** incomplete code in Appendix A
4. **Enhance** mathematical chapter with practical examples
5. **Standardize** Hebrew-English language mixing (100% CLS compliance)
6. **Achieve** clean LaTeX compilation with 0 errors

### Target Metrics
- **Page Count:** 24-28 pages (current: 26)
- **Chapter Count:** 6 (currently: 7)
- **Compilation Errors:** 0 (blocking)
- **Compilation Warnings:** ≤3 (acceptable)
- **Code Completeness:** 100% executable
- **CLS Compliance:** 100%

---

## Architecture

### Document Type
**Academic Book in Hebrew** with:
- Bidirectional text (Hebrew RTL, English LTR)
- Mathematical formulas
- Code listings (Python)
- Bibliography (IEEE style)
- Practical appendices

### Document Structure
```
Main Document (main.tex)
│
├── Front Matter
│   ├── Title page
│   ├── Abstract (Hebrew)
│   └── Table of Contents
│
├── Body (6 Chapters)
│   ├── Chapter 1: Introduction (Merged 1+2, NEW structure section)
│   ├── Chapter 2: Ethics & Security (Moved from old Ch6)
│   ├── Chapter 3: Gmail MCP Agent Implementation
│   ├── Chapter 4: Claude CLI Integration
│   ├── Chapter 5: MCP Protocol Deep Dive
│   └── Chapter 6: Mathematical Frameworks
│
├── Appendices (A-F)
│   ├── Appendix A: Manual implementation (gmail_mcp_server.py)
│   ├── Appendix B: Usage example (fetch_emails.py)
│   ├── Appendix C: Server documentation
│   ├── Appendix D: Manual requirements.txt
│   ├── Appendix E: SDK implementation (gmail_mcp_server_sdk.py)
│   └── Appendix F: SDK requirements.txt
│
└── Bibliography (IEEE style)
```

---

## Technology Stack

### Primary Tools

#### LaTeX System
- **Compiler:** LuaLaTeX (REQUIRED - NOT pdflatex)
- **Distribution:** MiKTeX
- **Main Packages:**
  - `polyglossia` - Multilingual support
  - `luabidi` - Bidirectional text
  - `fontspec` - Font management
  - `biblatex` with `biblatex-ieee` - Bibliography
  - `tcolorbox` + `listings` - Code display
  - `amsmath`, `amssymb` - Mathematics
  - `tikz-cd` - Diagrams
  - `hyperref` - PDF links

#### Custom Class
- **File:** `hebrew-academic-template.cls`
- **Purpose:** Defines CLS functions for Hebrew-English mixing
- **Key Functions:**
  - `\en{}` - Inline English text
  - `\num{}` - Numbers
  - `\hebyear{}` - Hebrew year format
  - `\hebrewsection{}`, `\hebrewsubsection{}` - Section headers
  - `pythonbox` environment - Code display with LTR + gray background

### Python Environment

#### Version Requirements
- **Manual Implementation (Appendix A):** Python 3.7+ compatible
- **SDK Implementation (Appendix E):** Python 3.10+ REQUIRED

#### Key Packages
- `google-api-python-client` - Gmail API
- `google-auth`, `google-auth-oauthlib` - OAuth 2.0
- `mcp>=1.2.0` - Model Context Protocol SDK (Python 3.10+ only)
- `python-dotenv` - Environment variables

### External Dependencies
- **Google Cloud Project** with Gmail API enabled
- **OAuth 2.0 credentials** (credentials.json)
- **Claude CLI** for agent orchestration

---

## Language Requirements

### Primary Language: Hebrew
- **Direction:** Right-to-Left (RTL)
- **Font:** David CLM (via Culmus fonts)
- **Encoding:** UTF-8

### Secondary Language: English
- **Direction:** Left-to-Right (LTR)
- **Font:** Times New Roman
- **Usage:** Technical terms, code, citations

### Hebrew-English Mixing Rules (CRITICAL)

**MUST use CLS functions - NO exceptions:**

| Type | Correct Syntax | Wrong Syntax |
|------|----------------|--------------|
| English words | `\en{Claude}` | `\textenglish{Claude}` ✗ |
| Numbers | `\num{100}` | `100` ✗ |
| Years | `\hebyear{2025}` | `2025` ✗ |
| Filenames | `\en{\texttt{main.py}}` | `\texttt{main.py}` ✗ |
| Bold Hebrew | `\textbf{Hebrew}` | `\texthebrew{\textbf{Hebrew}}` ✗ |

**Validation Command:**
```bash
grep -n "\\textenglish\|\\texthebrew" chapters/*.tex
# Should return zero results
```

---

## Code Display Standards

### Python Code (with comments)
```latex
\begin{english}
\begin{verbatim}
# Python code here
def function():
    return "value"
\end{verbatim}
\end{english}
```

### Python Code (simple, no complex comments)
```latex
\begin{pythonbox}
def function():
    return value
\end{pythonbox}
```

**NEVER use optional parameters:** `\begin{pythonbox}[Title]` causes compilation errors

### JSON/Config
```latex
\begin{english}
\begin{verbatim}
{
  "key": "value"
}
\end{verbatim}
\end{english}
```

---

## File Organization

### Directory Structure
```
Latech/
├── chapters/          # All LaTeX chapter and appendix files
├── claude_mem/        # Planning, tracking, and documentation
├── main.tex           # Main document
├── refs.bib           # Bibliography
├── *.cls              # Document class
└── main.pdf           # Compiled output
```

### Naming Conventions
- **Chapters:** `chapter1.tex` through `chapter6.tex` (target)
- **Appendices:** `appendixA.tex` through `appendixF.tex`
- **Draft files:** `chapter1_new.tex` (temporary during reorganization)

---

## Quality Standards

### The "Harari Standard"
Inspired by Yuval Noah Harari's writing principles:

1. **Narrative Flow:** Each chapter tells a story connecting to the next
2. **Historical Perspective:** Technology placed in historical context
3. **Clarity:** Non-experts understand 80%+ of content
4. **Critical Thinking:** Present trade-offs, not just benefits
5. **Progressive Complexity:** Each chapter builds on previous knowledge

### Content Requirements
- **Zero Repetition:** No paragraph repeats information
- **Forward References:** Explicit: "כפי שנראה בפרק X"
- **Back References:** Specific: "כפי שלמדנו בפרק Y"
- **First Mentions:** Include brief definition of every new term
- **Examples:** Abstract concepts grounded in concrete cases

### Technical Requirements
- **Compilation:** 0 errors (blocking), ≤3 warnings
- **Code:** 100% syntactically correct and executable
- **Citations:** IEEE format, complete references
- **Cross-references:** All internal links resolve

---

## Development Workflow

### Session Startup (MANDATORY)
1. Read `PLANNING.md` (this file)
2. Check `TASKS.md` for current status
3. Read `CLAUDE.md` for operational details
4. Verify clean compilation state

### During Work
1. Make incremental changes
2. Compile after EVERY file edit
3. Check CLS compliance with grep
4. Mark completed tasks in TASKS.md
5. Add discovered tasks to TASKS.md

### Before Committing Changes
1. Clean compilation (0 errors)
2. CLS compliance verified
3. Task marked complete with date
4. Testing completed (if code changes)

---

## Testing Strategy

### LaTeX Compilation Testing
```bash
# After every change
lualatex main.tex

# Before finalizing
bibtex main
lualatex main.tex
lualatex main.tex  # Second pass
```

**Expected Results:**
- Exit code: 0
- Errors: 0
- Warnings: ≤3
- Output: main.pdf (24-28 pages)

### Python Code Testing

#### SDK Implementation (Appendix E)
```bash
cd ../gmail-mcp-agent-sdk
venv\Scripts\activate  # Python 3.10+
python gmail_mcp_server_sdk.py
```

**Expected:** Server starts, no import errors

#### Manual Implementation (Appendix A)
Test after completing CSV export code
```bash
cd ../gmail-mcp-agent/
venv\Scripts\activate  # Python 3.7+
python gmail_mcp_server.py
```

**Expected:** Server starts, CSV export functions work

### Integration Testing
1. Start MCP server (Appendix E)
2. Start Claude CLI
3. Test tool discovery: `/tools`
4. Test email search and CSV export
5. Verify CSV file created in `csv/` directory
6. Check UTF-8-sig encoding

---

## Success Criteria

### Must-Have (Blocking)
- [ ] 6 chapters (not 7)
- [ ] Chapter 1 ≥40 lines with book structure
- [ ] Ethics is Chapter 2 (before implementation)
- [ ] Zero content repetition
- [ ] 100% CLS compliance
- [ ] Appendix A code complete
- [ ] Clean compilation (0 errors)
- [ ] All code examples executable

### Should-Have (Important)
- [ ] Abstract mentions dual approaches
- [ ] Math chapter has Gmail examples
- [ ] Python version warnings added
- [ ] Forward/back references explicit
- [ ] ≤3 compilation warnings
- [ ] 24-28 page PDF

### Nice-to-Have (Optional)
- [ ] Additional diagrams
- [ ] Extended examples
- [ ] Glossary of terms
- [ ] Generated index

---

## Risk Mitigation

### Known Risks
1. **LaTeX compilation errors** during reorganization
   - Mitigation: Compile after every change

2. **Breaking cross-references** when renaming chapters
   - Mitigation: Update all references systematically

3. **Introducing new repetitions** while removing old ones
   - Mitigation: Content diff review after each phase

4. **Code breaking** after modifications
   - Mitigation: Test execution before finalizing

### Backup Strategy
- Keep old chapter files until merge confirmed working
- Use descriptive temporary names: `chapter1_new.tex`
- Test compilation before deleting old files

---

## Dependencies

### External Resources Required
1. **Google Cloud Console Access**
   - Create project
   - Enable Gmail API
   - Generate OAuth credentials

2. **Python 3.10+ Installation** (for SDK)
   - Windows: Download from python.org
   - Use `py -3.13 -m venv venv` for venv creation

3. **LaTeX Distribution**
   - MiKTeX (Windows) or TeX Live (Linux)
   - LuaLaTeX compiler
   - Required packages installed

4. **Claude CLI**
   - Installed and configured
   - MCP server configuration in `~/.claude/config.json`

### Internal Dependencies (Chapter Order)
- Chapter 2 depends on Chapter 1 (foundations)
- Chapter 3 depends on Chapter 2 (ethical framework)
- Chapter 4 depends on Chapter 3 (implementation)
- Chapter 5 depends on Chapter 3-4 (practical experience)
- Chapter 6 depends on Chapter 3 (concrete example)

---

## Timeline

### Phase 1: Content Reorganization (~1 hour remaining)
**Status:** 50% complete
- ✅ Folder structure created
- ✅ Chapter 1 draft created
- ✅ Compilation tested
- 🔲 Ethics chapter moved
- 🔲 Math chapter renamed
- 🔲 Old files deleted

### Phase 2: Content Quality (~2 hours)
- Remove repetitions
- Add examples
- Complete code
- Update abstract

### Phase 3: Language Compliance (~1 hour)
- CLS audit
- Fix violations
- Verify compliance

### Phase 4: Validation (~2 hours)
- Compilation testing
- Code execution
- Harari review
- Quality report

### Phase 5: Documentation (~1 hour)
- Validation report
- Changelog
- Final proofreading

**Total Estimated:** 7 hours (3.5 hours remaining)

---

## Reference Documents

- **PRD.md** - Complete requirements specification
- **REORGANIZATION_PLAN.md** - Detailed chapter-by-chapter action plan
- **TASKS.md** - Living task list with completion tracking
- **CLAUDE.md** - Operational guide for Claude Code sessions

---

## Contact Information

**Project Owner:** Book Author
**Implementation:** Claude Code AI Assistant
**Quality Review:** Simulated "Harari Standard"

---

**Last Review:** October 20, 2025
**Next Review:** After Phase 1 completion
