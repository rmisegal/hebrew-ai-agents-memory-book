# Project Guide: Hebrew AI Agents Book Reorganization

---

## 🚨 MANDATORY WORKFLOW - READ THIS FIRST 🚨

### Every New Claude Code Session MUST Follow This 4-Step Framework:

1. **Always read `PLANNING.md` at the start of every new conversation**
   - Understand project vision, architecture, and constraints
   - Review technology stack and requirements

2. **Check `TASKS.md` before starting your work**
   - See what's been completed
   - Identify the next task to work on
   - Understand task dependencies

3. **Mark completed tasks immediately**
   - Add completion date when you finish a task
   - Update task status in TASKS.md
   - This keeps the project synchronized

4. **Add any new tasks that you discover**
   - Projects evolve - new requirements emerge
   - Document new tasks in TASKS.md immediately
   - Maintain the living roadmap

**This framework ensures consistency across all sessions and prevents duplicate work.**

---

## Project Overview

**Book Title:** בינה מבוזרת: סוכנים אוטונומיים בעידן הבינה המלאכותית
**English Title:** Distributed Intelligence: Autonomous Agents in the Age of AI
**Current Status:** Phase 1 (50% complete) - Content reorganization in progress
**Document Version:** As of October 20, 2025

This is a **Hebrew-language academic book** about AI multi-agent systems with practical Gmail MCP agent implementation. The project is undergoing complete reorganization from 7 chapters to 6, with quality enhancements.

---

## Critical Project Constraints

### 1. LaTeX Compiler
- **MUST use LuaLaTeX** (NOT pdflatex, xelatex)
- Command: `lualatex main.tex`
- Then: `bibtex main && lualatex main.tex`

### 2. Hebrew-English Mixing (100% COMPLIANCE REQUIRED)
**Only use CLS functions from `hebrew-academic-template.cls`:**

| Content | Correct | WRONG ✗ |
|---------|---------|---------|
| English text | `\en{Claude}` | `\textenglish{Claude}` |
| Numbers | `\num{100}` | Plain `100` |
| Years | `\hebyear{2025}` | Plain `2025` |
| Filenames | `\en{\texttt{file.py}}` | `\texttt{file.py}` |
| Bold Hebrew | `\textbf{Hebrew}` | `\texthebrew{\textbf{Hebrew}}` |
| Code blocks | `\begin{pythonbox}` or `\begin{english}\begin{verbatim}` | Direct verbatim in Hebrew |

**Before ANY file edit:** Verify it follows these rules.
**After ANY edit:** Check compliance with grep:
```bash
grep -n "\\textenglish" chapters/*.tex  # Should return nothing
```

### 3. Python Code Display
- **Python code with comments:** Use `\begin{english}\begin{verbatim}...\end{verbatim}\end{english}`
- **Simple Python code:** Use `\begin{pythonbox}...\end{pythonbox}` (no optional parameters!)
- **JSON/config:** Use `\begin{english}\begin{verbatim}...\end{verbatim}\end{english}`

---

## Project File Structure

```
Latech/
├── chapters/                      # All content files
│   ├── chapter1.tex              # OLD brief intro (8 lines)
│   ├── chapter1_new.tex          # NEW merged chapter (DRAFT - ready to finalize)
│   ├── chapter2.tex              # OLD monolith chapter (to be merged)
│   ├── chapter3.tex              # Gmail agent (stays, minor updates)
│   ├── chapter4.tex              # Claude CLI (stays, add Python notice)
│   ├── chapter5.tex              # MCP protocol (remove redundant intro)
│   ├── chapter6.tex              # Ethics (MOVE to become new chapter2.tex)
│   ├── chapter7.tex              # Math (RENAME to chapter6.tex, add examples)
│   ├── appendixA.tex             # Manual impl - INCOMPLETE CSV code
│   ├── appendixB.tex - F.tex     # Complete appendices
│
├── claude_mem/                    # Planning and tracking documents
│   ├── CLAUDE.md                 # This file - project guide
│   ├── PLANNING.md               # Project vision and architecture
│   ├── TASKS.md                  # Task tracking (living document)
│   ├── PRD.md                    # Full requirements specification
│   └── REORGANIZATION_PLAN.md    # Detailed action plan
│
├── main.tex                       # Main document
├── hebrew-academic-template.cls   # CLS functions definition
├── refs.bib                       # Bibliography
└── main.pdf                       # Compiled output

Current: 26 pages compiled, 7 chapters
Target: 24-28 pages, 6 chapters, publication-ready
```

---

## New Chapter Structure (Target)

### Chapter 1: Introduction and Foundations [MERGED: Old 1+2+NEW]
- Subsection 1.1: From Cognitive Revolution to Digital Cooperation
- Subsection 1.2: Breaking the Monolith
- Subsection 1.3: Book Structure [NEW - explains what readers learn in each chapter]
- **Min Length:** 40 lines
- **Status:** Draft exists as `chapter1_new.tex`

### Chapter 2: Ethics, Privacy, Security [MOVED: Old Ch6]
- Must appear BEFORE implementation chapters
- Add forward reference: "בפרק 3 נראה כיצד עקרונות אלה מיושמים בפועל..."
- **Min Length:** 25 lines

### Chapter 3: Gmail MCP Agent [Old Ch3, minor updates]
- Add Python 3.10+ requirement notice
- Keep current length (~99 lines)

### Chapter 4: Claude CLI Integration [Old Ch4, minor updates]
- Add Python version note
- Add CSV verification steps
- **Min Length:** 20 lines (expand from 15)

### Chapter 5: MCP Protocol Deep Dive [Old Ch5, remove redundancy]
- **REMOVE:** Redundant MCP introduction
- **ADD:** "לאחר שראינו בפרק 3 את יישום MCP בפועל..."
- Keep comparison tables

### Chapter 6: Mathematical Frameworks [Old Ch7, add examples]
- **ADD:** Gmail agent concrete example mapping to graph/matrix
- **ADD:** "במערכת Gmail MCP שלנו (פרק 3), אם נתייחס לסוכן כצומת..."
- Keep current math (~30 lines)

---

## Critical Code Issues

### Appendix A: INCOMPLETE (MUST FIX)
**File:** `chapters/appendixA.tex`
**Problem:** CSV export code truncated at line 51-52
**Current state:**
```python
# Extract headers and write to CSV
# CODE MISSING HERE
```

**Required fix:** Complete the CSV export loop like in Appendix E:
```python
for msg in messages:
    msg_data = service.users().messages().get(
        userId='me', id=msg['id']
    ).execute()

    headers = msg_data.get('payload', {}).get('headers', [])
    date = next((h['value'] for h in headers if h['name'] == 'Date'), '')
    from_addr = next((h['value'] for h in headers if h['name'] == 'From'), '')
    subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '')

    writer.writerow([date, from_addr, subject])
```

---

## Testing and Validation

### After EVERY change:
```bash
cd "C:\25D\GeneralLearning\gmail_ai_agent_book_and_example\Latech"
lualatex main.tex
```

**Expected output:**
- 0 errors (BLOCKING if errors exist)
- ≤3 warnings (acceptable)
- Output: 24-28 pages

### Before finalizing:
```bash
bibtex main
lualatex main.tex
lualatex main.tex  # Second pass for references
```

---

## Common Pitfalls (AVOID THESE)

### ❌ DON'T:
1. Use `\textenglish{}` or `\texthebrew{}` - Use `\en{}` instead
2. Use plain numbers in Hebrew text - Use `\num{}`
3. Use optional parameters in pythonbox: `\begin{pythonbox}[Title]` - Causes errors
4. Put `#` comments in pythonbox - Use verbatim instead
5. Skip compilation testing after changes
6. Assume Python 3.9 works - MCP SDK needs 3.10+
7. **Skip reading PLANNING.md and TASKS.md at session start**

### ✅ DO:
1. **Read PLANNING.md at start of every session**
2. **Check TASKS.md before starting work**
3. **Mark tasks complete immediately with date**
4. **Add new discovered tasks to TASKS.md**
5. Compile after EVERY file change
6. Check CLS compliance with grep
7. Test code execution before finalizing

---

## Quick Reference Commands

### Compilation:
```bash
cd "C:\25D\GeneralLearning\gmail_ai_agent_book_and_example\Latech"
lualatex main.tex
bibtex main
lualatex main.tex
```

### CLS Compliance Check:
```bash
grep -n "\\textenglish" chapters/*.tex
grep -n "\\texthebrew" chapters/*.tex
# Both should return nothing
```

### View Task Status:
```bash
cat claude_mem/TASKS.md | grep -E "^\- \[" | head -20
```

---

## Session Startup Checklist

When starting a new Claude Code session on this project:

1. [ ] **Read `claude_mem/PLANNING.md` completely**
2. [ ] **Check `claude_mem/TASKS.md` for current status**
3. [ ] Read this CLAUDE.md file
4. [ ] Test compilation: `lualatex main.tex` to verify clean state
5. [ ] Identify next uncompleted task from TASKS.md
6. [ ] Before editing: verify file follows CLS conventions
7. [ ] After editing: compile to test
8. [ ] **Mark task complete in TASKS.md with date**
9. [ ] **Add any new tasks discovered to TASKS.md**

---

## Key Documents Reference

- **PLANNING.md** (`claude_mem/PLANNING.md`) - **READ FIRST** - Project vision and architecture
- **TASKS.md** (`claude_mem/TASKS.md`) - **CHECK BEFORE WORK** - Task tracking and status
- **PRD.md** (`claude_mem/PRD.md`) - Full requirements specification
- **REORGANIZATION_PLAN.md** (`claude_mem/REORGANIZATION_PLAN.md`) - Detailed chapter-by-chapter plan
- **This file** (`CLAUDE.md`) - Operational guide for Claude Code sessions

---

## Version History

- **v1.1** (October 20, 2025) - Added 4-step framework, moved to claude_mem/
- **v1.0** (October 20, 2025) - Initial CLAUDE.md created from PRD.md
  - Phase 1: 50% complete (folder structure, draft Chapter 1, compilation tested)

---

**Remember:** This is a publication-quality academic book in Hebrew. Treat it with the same rigor as submitting to an academic press. The "Harari Standard" means every sentence should flow naturally, every concept should build on the previous, and the reader should feel they're reading an original masterpiece, not a revision.

**Current Priority:** Complete Phase 1 reorganization (get from 7 chapters to 6 in correct order).
