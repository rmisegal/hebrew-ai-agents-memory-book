# Project Guide: Hebrew AI Agents Book - Part 2 Integration
## Memory and Consistency - Engineering Persistent Cognition

---

## 🚨 MANDATORY WORKFLOW - READ THIS FIRST 🚨

### Every New Claude Code Session MUST Follow This 4-Step Framework:

1. **Always read `PLANNING.md` at the start of every new conversation**
   - Understand Part 2 integration strategy
   - Review chapter mapping from PDF to LaTeX
   - Understand cross-reference requirements

2. **Check `TASKS.md` before starting your work**
   - See what's been completed in Part 2 conversion
   - Identify the next chapter to convert
   - Understand dependencies (e.g., bibliography before chapters)

3. **Mark completed tasks immediately**
   - Add completion date when you finish a task
   - Update task status in TASKS.md
   - This keeps Part 1 and Part 2 work synchronized

4. **Add any new tasks that you discover**
   - PDF conversion may reveal unexpected needs
   - Document new tasks in TASKS.md immediately
   - Maintain the living roadmap

**This framework ensures consistency across all sessions and prevents duplicate work.**

---

## Project Overview

**Book Title:** בינה מבוזרת: סוכנים אוטונומיים בעידן הבינה המלאכותית
**English Title:** Distributed Intelligence: Autonomous Agents in the Age of AI
**Current Phase:** Part 2 Integration (Version 4.0 expansion from 3.0)
**Document Date:** October 20, 2025

This is a **Hebrew-language academic book** expanding from 1 part (6 chapters, MCP agents) to **2 parts** (13 chapters total):
- **Part 1:** Distributed AI architecture, MCP protocol, Gmail agent (existing, minor updates)
- **Part 2:** AI agent memory systems, context engineering, cognitive partnership (NEW from PDF)

---

## Critical Project Constraints

### 1. LaTeX Compiler
- **MUST use LuaLaTeX** (NOT pdflatex, xelatex)
- Command: `lualatex main.tex`
- Then: `bibtex main && lualatex main.tex && lualatex main.tex`

### 2. Hebrew-English Mixing (100% COMPLIANCE REQUIRED)
**Only use CLS functions from `hebrew-academic-template.cls`:**

| Content | Correct | WRONG ✗ |
|---------|---------|---------||
| English text | `\en{Claude Code}` | `\textenglish{Claude Code}` |
| Numbers | `\num{23}` | Plain `23` |
| Years | `\hebyear{2025}` | Plain `2025` |
| Filenames | `\en{\texttt{PRD.md}}` | `\texttt{PRD.md}` |
| Bold Hebrew | `\textbf{זיכרון}` | `\texthebrew{\textbf{זיכרון}}` |
| Bold English | `\textbf{\en{MCP}}` | `\textbf{MCP}` |
| Code blocks | `\begin{english}\begin{verbatim}` | Direct verbatim in Hebrew |
| Math numbers | `\num{100}` in matrices | Plain `100` |

**Before ANY file edit:** Verify it follows these rules.
**After ANY edit:** Check compliance with grep:
```bash
grep -n "\\textenglish" chapters/*.tex  # Should return nothing
grep -n "\\texthebrew" chapters/*.tex   # Should return nothing
```

### 3. Python Code Display (From Part 1, Still Applies)
- **Python code with comments:** Use `\begin{english}\begin{verbatim}...\end{verbatim}\end{english}`
- **Simple Python code:** Use `\begin{pythonbox}...\end{pythonbox}` (no optional parameters!)
- **JSON/config:** Use `\begin{english}\begin{verbatim}...\end{verbatim}\end{english}`

### 4. Harari-Style Narrative (MANDATORY FOR PART 2)
Every chapter in Part 2 must follow Professor Yuval Noah Harari's standard:

✅ **DO:**
1. **Start with historical context** - Example: Chapter 7 begins with invention of writing
2. **Use accessible language** - 80%+ of readers should understand without technical background
3. **Define every technical term immediately** - Don't assume knowledge
4. **Use metaphors and analogies** - Make abstract concepts concrete
5. **Discuss limitations and trade-offs** - Critical thinking, not marketing hype
6. **Provide substantive examples** - Every concept needs a real-world illustration
7. **Answer "why this matters"** - Every chapter should have a "מדוע זה משנה?" moment

❌ **DON'T:**
1. Use jargon without explanation
2. Make marketing claims without evidence
3. Repeat content from other chapters - use forward references instead
4. Write in academic "lecture" style - narrative storytelling is key
5. Assume readers have read specific papers or documentation

**Example of Harari Style (from PDF Chapter 7):**
```
מאז ומעולם, הקפיצה הקוגניטיבית הגדולה ביותר של האנושות לא נבעה משיפור
הזיכרון הביולוגי עצמו, אלא מהיכולת להנדס "זיכרון חוץ-גופי". המצאת הכתב,
הפיכת סיפורים לארכיונים ממלכתיים וחקיקת חוקות על גבי לוחות אבן, יצרו את
הבסיס לציוויליזציה על ידי אחסון ידע מחוץ למוחו של אדם יחיד.
```

This paragraph:
- Starts with deep history ("מאז ומעולם")
- Uses metaphor ("זיכרון חוץ-גופי")
- Connects ancient technology (writing) to modern concept (external memory)
- Accessible to non-experts
- Sets up the "why this matters" (foundation of civilization)

---

## Part 2 Specific Constraints

### 1. Source Material: PDF Structure
**File:** `C:\25D\GeneralLearning\Videos\add_mem_to_claude_code\ClaudeMemHebChapter.pdf`
**Pages:** 9
**Language:** Hebrew with English technical terms
**Author:** Dr. Yoram Segal
**Date:** October 2025

**7 Main Sections (to become Chapters 7-13):**
1. Introduction: Machine Amnesia (האמנזיה של המכונה)
2. Context Engineering Foundations (הנדסת קונטקסט)
3. Architectural Distinction (ההבחנה הארכיטקטונית)
4. Four Pillars of Consistency (ארבעת עמודי הזיכרון)
5. Knowledge Management Principles (ניהול ידע בפרויקטים)
6. Demonstration and Impact (הדגמה והשפעות רוחב)
7. Conclusion: Cognitive Partnership (שותפות קוגניטיבית)

### 2. Chapter Structure Standard

Each Part 2 chapter MUST include:

1. **\hebrewsection{Chapter Title}**
   - Use `\hebrewsection{}` for main chapter title
   - NO manual numbering - LaTeX auto-numbers from 7

2. **Opening Paragraph (Historical/Conceptual Hook)**
   - 3-5 lines establishing context
   - Harari-style narrative opening
   - Example: "לפני שנבין את X, עלינו לחזור ל..."

3. **\hebrewsubsection{} for Major Sections**
   - 2-4 subsections per chapter
   - Each subsection = one main idea
   - Clear logical progression

4. **Forward/Backward References**
   - At least 1 reference to Part 1 (Chapters 1-6)
   - At least 1 reference within Part 2 (if applicable)
   - Format: "כפי שראינו בפרק \num{3}..." or "בפרק \num{10} נעמיק ב..."

5. **Closing Paragraph (Bridge to Next Chapter)**
   - 2-3 lines transitioning to next topic
   - Example: "לאחר שהבנו X, נוכל כעת לבחון Y בפרק הבא..."

6. **Minimum Length:**
   - Chapter 7-9: 35-55 lines each
   - Chapter 10: 60-70 lines (longest, covers 4 pillars)
   - Chapter 11-13: 30-50 lines each

### 3. Cross-Reference Requirements

#### Forward References (Part 1 → Part 2)
**MUST ADD to existing chapters:**

**Chapter 1 (Introduction):**
- Add 5-8 lines at the end
- Preview Part 2: "בחלק השני של הספר (פרקים \num{7}-\num{13}) נצלול לממד הקוגניטיבי..."
- Explain why memory matters for distributed agents

**Chapter 4 (Claude CLI):**
- Add 2-3 lines referencing Chapter 10
- Example: "מנגנוני הזיכרון המאפשרים שימור הקשר בין הפעלות יידונו בפרק \num{10}..."

**Chapter 6 (Math):**
- Add 2-3 lines referencing Chapter 13
- Example: "המסגרת המתמטית למדידת עקביות קוגניטיבית תורחב בפרק \num{13}..."

#### Backward References (Part 2 → Part 1)
**MUST INCLUDE in new chapters:**

**Chapter 7:**
- Reference Chapter 3 (Gmail agent): "בפרק \num{3} ראינו כיצד בונים סוכן \en{MCP}; כעת נבין כיצד הוא זוכר..."

**Chapter 9:**
- Reference Chapter 5 (MCP protocol): "הארכיטקטורה שתוארה בפרק \num{5} מהווה בסיס להבנת..."

**Chapter 10:**
- Reference Chapter 2 (Ethics): "ארבעת הקבצים שנדונו כאן ממחישים את העקרונות האתיים מפרק \num{2}..."

### 4. Table Conversion (Critical)

The PDF contains a **comparison table** (Section 3.2.3):
- **Columns:** מאפיין | RAG | Long Context LLMs
- **Rows:** ~8-10 features compared
- **Challenge:** Mixed Hebrew (row headers) and English (technical terms)

**LaTeX Conversion Requirements:**
```latex
\begin{english}
\begin{tabular}{|r|p{5cm}|p{5cm}|}
\hline
\textbf{מאפיין} & \textbf{\en{RAG}} & \textbf{\en{Long Context LLMs}} \\
\hline
זמן תגובה & \en{Retrieval latency: 100-500ms} & \en{Inference only: 50-200ms} \\
\hline
דיוק & ... & ... \\
\hline
\end{tabular}
\end{english}
```

**Rules:**
- Wrap entire table in `\begin{english}...\end{english}` for RTL flow
- Use `\en{}` for English technical terms in cells
- Hebrew text directly in cells (no `\texthebrew{}`)
- Use `\num{}` for numbers in cells

### 5. Bibliography Integration (23 New References)

The PDF cites 23 sources. You MUST:

1. **Extract citations from PDF**
   - Numbered [1] through [23]
   - Some are papers, some are documentation URLs

2. **Add to refs.bib in BibLaTeX format**
   - Use unique cite keys: `@article{segal2025memory, ...}`
   - Distinguish from Part 1 refs: `@manual{anthropic2025mcp, ...}`

3. **Hebrew/English field handling:**
   ```bibtex
   @article{example_hebrew,
     title = {כותרת בעברית},
     author = {סגל, יורם},
     year = {2025},
     language = {Hebrew}
   }

   @article{example_english,
     title = {English Title},
     author = {Smith, John},
     year = {2024},
     language = {English}
   }
   ```

4. **Cite in chapters:**
   - Use `\cite{key}` in Hebrew text
   - Example: "כפי שמתואר במחקר~\cite{segal2025memory}, מערכות זיכרון..."

---

## Project File Structure

```
Latech/
├── main.tex                           # UPDATE: Add \part{} divisions
├── hebrew-academic-template.cls       # Unchanged
├── refs.bib                           # UPDATE: +23 new references
├── main.pdf                           # OUTPUT: ~50-58 pages (2 parts)
│
├── chapters/                          # All content
│   ├── chapter1.tex                   # UPDATE: Add Part 2 preview (5-8 lines)
│   ├── chapter2.tex                   # UNCHANGED (Ethics)
│   ├── chapter3.tex                   # UNCHANGED (Gmail agent)
│   ├── chapter4.tex                   # UPDATE: Add Chapter 10 reference (2-3 lines)
│   ├── chapter5.tex                   # UNCHANGED (MCP protocol)
│   ├── chapter6.tex                   # UPDATE: Add Chapter 13 reference (2-3 lines)
│   │
│   ├── chapter7.tex                   # NEW: Machine Amnesia
│   ├── chapter8.tex                   # NEW: Context Engineering
│   ├── chapter9.tex                   # NEW: Architectural Distinction
│   ├── chapter10.tex                  # NEW: Four Pillars (longest chapter)
│   ├── chapter11.tex                  # NEW: Knowledge Management
│   ├── chapter12.tex                  # NEW: Demonstration
│   ├── chapter13.tex                  # NEW: Cognitive Partnership
│   │
│   ├── appendixA.tex - appendixF.tex  # UNCHANGED (Code examples)
│
├── claude_mem/                        # Part 1 memory (ARCHIVED - READ ONLY)
│   ├── CLAUDE.md
│   ├── PLANNING.md
│   ├── TASKS.md
│   └── PRD.md
│
└── claude_mem_part2/                  # Part 2 memory (ACTIVE - READ/WRITE)
    ├── PRD.md                         # ✅ Created
    ├── CLAUDE.md                      # ✅ This file
    ├── PLANNING.md                    # ⏳ To be created next
    └── TASKS.md                       # ⏳ To be created after PLANNING.md
```

---

## New Chapter Structure (Target)

### Part 1: בינה מבוזרת - ארכיטקטורה ופרוטוקולים
*Distributed Intelligence - Architecture and Protocols*

| Chapter | Title | Status | Lines | Updates Needed |
|---------|-------|--------|-------|----------------|
| 1 | מבוא: שחר עידן הרב-סוכנים | ⏳ Minor update | ~50 → ~58 | Add Part 2 preview (8 lines) |
| 2 | אתיקה, פרטיות ואבטחה | ✅ No changes | ~25 | None |
| 3 | בניית סוכן MCP עבור Gmail | ✅ No changes | ~99 | None |
| 4 | שילוב עם Claude CLI | ⏳ Minor update | ~15 → ~18 | Add Chapter 10 reference (3 lines) |
| 5 | צלילת עומק לפרוטוקול MCP | ✅ No changes | ~12 | None |
| 6 | מבנים מתמטיים | ⏳ Minor update | ~30 → ~33 | Add Chapter 13 reference (3 lines) |

**Target Pages:** 27-30 (currently 27, will expand slightly with cross-refs)

### Part 2: זיכרון ועקביות - מהנדסת קוגניציה מתמשכת
*Memory and Consistency - Engineering Persistent Cognition*

| Chapter | Title | Source PDF | Status | Est. Lines |
|---------|-------|------------|--------|------------|
| 7 | האמנזיה של המכונה | Section 1.1-1.2 | ⏳ To convert | 35-40 |
| 8 | הנדסת קונטקסט | Section 2.1-2.3 | ⏳ To convert | 40-45 |
| 9 | ההבחנה הארכיטקטונית | Section 3.1-3.2 | ⏳ To convert | 50-55 |
| 10 | ארבעת עמודי הזיכרון | Section 4.1-4.4 | ⏳ To convert | 60-70 |
| 11 | ניהול ידע בפרויקטים | Section 5 | ⏳ To convert | 45-50 |
| 12 | הדגמה מעשית | Section 6 | ⏳ To convert | 35-40 |
| 13 | שותפות קוגניטיבית | Section 7 | ⏳ To convert | 30-35 |

**Target Pages:** 24-28

---

## Testing and Validation

### After EVERY change:
```bash
cd "C:\25D\GeneralLearning\gmail_ai_agent_book_and_example\Latech"
lualatex main.tex
```

**Expected output:**
- 0 errors (BLOCKING if errors exist)
- ≤3 warnings (acceptable, usually font or spacing cosmetic issues)
- Output pages:
  - After Part 1 updates: ~28-30 pages
  - After Part 2 Chapter 7: ~32-35 pages
  - After Part 2 Chapter 10: ~42-45 pages
  - Final with all 13 chapters: 50-58 pages

### Before finalizing Part 2:
```bash
bibtex main
lualatex main.tex
lualatex main.tex  # Second pass for cross-references
```

### CLS Compliance Check (Run after each new chapter):
```bash
grep -n "\\textenglish" chapters/chapter7.tex chapters/chapter8.tex chapters/chapter9.tex chapters/chapter10.tex chapters/chapter11.tex chapters/chapter12.tex chapters/chapter13.tex
# Should return NOTHING

grep -n "\\texthebrew" chapters/chapter7.tex chapters/chapter8.tex chapters/chapter9.tex chapters/chapter10.tex chapters/chapter11.tex chapters/chapter12.tex chapters/chapter13.tex
# Should return NOTHING
```

---

## Common Pitfalls (AVOID THESE IN PART 2)

### ❌ DON'T:

1. **Use `\textenglish{}` or `\texthebrew{}`** - Use `\en{}` and direct Hebrew text instead
2. **Use plain numbers in Hebrew text** - Always use `\num{23}`
3. **Copy-paste from PDF without CLS conversion** - PDF may have plain numbers and English terms
4. **Repeat content from Part 1** - Use forward/backward references instead
5. **Skip Harari-style opening** - Every chapter needs historical/conceptual hook
6. **Write in "academic lecture" style** - Narrative storytelling, not bullet points
7. **Forget to compile after each chapter** - Compile immediately to catch errors early
8. **Use optional parameters in pythonbox** - `\begin{pythonbox}[Title]` causes errors
9. **Put `#` comments in pythonbox** - Use `\begin{english}\begin{verbatim}` instead
10. **Skip cross-references** - Every chapter needs at least 1 reference to another chapter
11. **Translate PDF literally** - Adapt for narrative flow, add context where needed
12. **Assume readers remember Part 1 details** - Briefly recap key concepts when referenced
13. **Skip reading PLANNING.md and TASKS.md at session start** - Critical for context

### ✅ DO:

1. **Read PLANNING.md at start of every session** - Understand chapter mapping and cross-reference strategy
2. **Check TASKS.md before starting work** - Know what's been done and what's next
3. **Mark tasks complete immediately with date** - Keep TASKS.md current
4. **Add new discovered tasks to TASKS.md** - Document new requirements as they emerge
5. **Compile after EVERY chapter creation** - Don't wait until all chapters are done
6. **Check CLS compliance with grep after each chapter** - Automated verification
7. **Test cross-references resolve** - Look for "undefined reference" warnings
8. **Read Part 1 chapters before writing Part 2** - Understand style, tone, and content to reference
9. **Use `\en{}` for ALL English terms** - Even single words like "MCP" or "RAG"
10. **Start each chapter with Harari-style hook** - Historical context or philosophical question
11. **End each chapter with bridge to next** - Smooth transitions between chapters
12. **Provide concrete examples** - Abstract concepts need real-world illustrations
13. **Answer "why this matters"** - Every chapter should have clear practical implications
14. **Use metaphors and analogies** - Make technical concepts accessible

---

## Quick Reference Commands

### Compilation:
```bash
cd "C:\25D\GeneralLearning\gmail_ai_agent_book_and_example\Latech"

# Quick compile (after each chapter):
lualatex main.tex

# Full compile (before finalizing):
lualatex main.tex
bibtex main
lualatex main.tex
lualatex main.tex
```

### CLS Compliance Check:
```bash
# Check all Part 2 chapters:
grep -n "\\textenglish" chapters/chapter{7..13}.tex
grep -n "\\texthebrew" chapters/chapter{7..13}.tex
# Both should return nothing

# Check updated Part 1 chapters:
grep -n "\\textenglish" chapters/chapter1.tex chapters/chapter4.tex chapters/chapter6.tex
grep -n "\\texthebrew" chapters/chapter1.tex chapters/chapter4.tex chapters/chapter6.tex
# Both should return nothing
```

### View Task Status:
```bash
cat claude_mem_part2/TASKS.md | grep -E "^\\- \\[" | head -30
```

### Count Pages:
```bash
pdfinfo main.pdf | grep Pages
```

---

## Session Startup Checklist

When starting a new Claude Code session on Part 2:

1. [ ] **Read `claude_mem_part2/PLANNING.md` completely**
2. [ ] **Check `claude_mem_part2/TASKS.md` for current status**
3. [ ] Read this CLAUDE.md file (you're reading it now)
4. [ ] Test compilation: `lualatex main.tex` to verify clean state
5. [ ] Identify next uncompleted task from TASKS.md
6. [ ] If converting a chapter, re-read the relevant PDF section
7. [ ] Before editing: verify existing chapters follow CLS conventions (learn from them)
8. [ ] After creating new chapter: compile immediately to test
9. [ ] **Mark task complete in TASKS.md with date**
10. [ ] **Add any new tasks discovered to TASKS.md**

---

## Quality Standards (The Harari Test)

Every Part 2 chapter must pass these subjective quality checks:

### 1. Accessibility Test
- Can an intelligent high school graduate understand this chapter?
- Are all technical terms defined immediately upon first use?
- Do metaphors and analogies clarify abstract concepts?

### 2. Narrative Flow Test
- Does the chapter tell a story, or just list facts?
- Does the opening hook the reader emotionally or intellectually?
- Does the closing create anticipation for the next chapter?

### 3. Uniqueness Test
- Does this chapter provide information not found elsewhere in the book?
- If it references another chapter, does it add new insights rather than repeat?
- Does every paragraph contribute to the chapter's unique thesis?

### 4. Practical Value Test
- After reading, can the reader apply this knowledge?
- Are there concrete examples they can relate to?
- Is there a clear "why this matters" takeaway?

### 5. Critical Thinking Test
- Does the chapter discuss limitations and trade-offs?
- Does it present multiple perspectives (e.g., RAG vs Long Context)?
- Does it avoid marketing hype and unsubstantiated claims?

### 6. Integration Test
- Does the chapter feel like a natural continuation of the book?
- Do cross-references enrich understanding without causing confusion?
- Does Part 2 complement Part 1 without redundancy?

**If any chapter fails these tests, revise before moving to the next chapter.**

---

## Version History

- **v1.0** (October 20, 2025) - Initial CLAUDE.md created for Part 2 integration
  - Based on Part 1 CLAUDE.md structure
  - Added Part 2 specific requirements
  - Added Harari-style narrative standards
  - Added table conversion guidelines
  - Added chapter structure standards
  - Added cross-reference requirements

---

## Key Documents Reference

**Part 2 Memory (Active):**
- **PLANNING.md** (`claude_mem_part2/PLANNING.md`) - **READ FIRST** - Technical architecture
- **TASKS.md** (`claude_mem_part2/TASKS.md`) - **CHECK BEFORE WORK** - Task tracking
- **PRD.md** (`claude_mem_part2/PRD.md`) - Strategic requirements
- **This file** (`CLAUDE.md`) - Operational guide for Part 2 work

**Part 1 Memory (Archived - Read Only):**
- `claude_mem/CLAUDE.md` - Part 1 workflow guide (reference for style)
- `claude_mem/PLANNING.md` - Part 1 architecture (reference for context)
- `claude_mem/TASKS.md` - Part 1 completed tasks (reference for what was done)
- `claude_mem/PRD.md` - Part 1 requirements (reference for scope)

**Source Material:**
- `C:\25D\GeneralLearning\Videos\add_mem_to_claude_code\ClaudeMemHebChapter.pdf` - 9 pages, 7 sections

---

**Remember:** This is a publication-quality academic book in Hebrew. Part 2 must match Part 1's Harari standard: every sentence should flow naturally, every concept should build on the previous, and the reader should feel they're reading an original masterpiece, not a conversion from a PDF.

**Current Priority:** Create PLANNING.md and TASKS.md, then begin systematic PDF-to-LaTeX conversion starting with Chapter 7.

**Final Goal:** A seamless 50-58 page book where a reader starting at Chapter 1 can read continuously through Chapter 13 without noticing that Part 2 was added later. The division into 2 parts should feel intentional and pedagogically sound, not arbitrary.
