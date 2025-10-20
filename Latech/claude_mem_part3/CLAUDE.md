# CLAUDE.md - Part 3 Conversion Rules

## CRITICAL: READ FIRST - EVERY SESSION

**Priority Order** (MUST follow in every session):
1. Read PLANNING.md first
2. Read TASKS.md immediately after
3. Read this file (CLAUDE.md) before starting work
4. Read PRD.md for context

## CLS Template Compliance - ABSOLUTE RULES

### ✅ ALLOWED Commands (USE THESE ONLY)

**Hebrew Sections**:
```latex
\hebrewsection{כותרת}
\hebrewsubsection{תת-כותרת}
```

**English Inline**:
```latex
\en{English text}
\en{CLI}
\en{Skills}
\en{Progressive Disclosure}
```

**Numbers in Hebrew Text**:
```latex
\num{42}
\num{1.5}
\num{200,000}
```

**Years**:
```latex
\hebyear{2025}
```

**Table Functions**:
```latex
\begin{hebrewtable}[H]
\caption{כותרת הטבלה}
\begin{rtltabular}{|m{3cm}|m{5cm}|}
\hline
\hebheader{כותרת עברית} & \enheader{English Header} \\
\hline
\hebcell{תוכן עברי} & \encell{English content} \\
\hline
\end{rtltabular}
\end{hebrewtable}
```

**Lists**:
```latex
\begin{itemize}
  \item פריט ראשון
  \item פריט שני עם \en{English}
\end{itemize}

\begin{enumerate}
  \item \textbf{כותרת מודגשת}: תיאור
\end{enumerate}
```

**References**:
```latex
בפרק~\ref{sec:chapter1}
\cite{anthropic2025skills}
```

### ❌ FORBIDDEN Commands (NEVER USE)

```latex
\textenglish{...}  ❌ USE \en{} INSTEAD
\texthebrew{...}   ❌ NOT NEEDED (default is Hebrew)
123                ❌ USE \num{123} INSTEAD
2025               ❌ USE \hebyear{2025} FOR YEARS
Plain English text ❌ MUST BE WRAPPED IN \en{}
```

### Verification Commands

Before finalizing ANY chapter:
```bash
# Check for forbidden commands
grep -n "\\textenglish\|\\texthebrew" chapter14.tex
grep -n "\\textbf{[0-9]}" chapter14.tex

# Check for unwrapped English
grep -n "[A-Z][a-z]*" chapter14.tex | grep -v "\\en{"

# Check for unwrapped numbers
grep -oP '\b\d+\b' chapter14.tex | head -20
```

## Harari-Style Narrative Rules

### Required Elements

1. **Historical Hook** (first paragraph):
   - Connect to human history (like writing invention in Ch7)
   - Example from PDF: "האדם המודרני פיתח 'סדרים מדומיינים' כדי לשתף פעולה"

2. **80%+ Accessibility**:
   - Avoid jargon without explanation
   - Use metaphors and analogies
   - Progressive complexity (simple → complex)

3. **Critical Thinking**:
   - Not marketing hype
   - Acknowledge limitations (Section 6 in PDF is excellent)
   - Balance: benefits AND dangers

4. **Concrete Examples**:
   - Every abstract concept needs example
   - PDF provides: webapp-testing, document-skills, data-aggregator

### Structure Per Chapter

```
1. Opening: Historical/philosophical context (2-3 paragraphs)
2. Core Concept: Technical explanation with Hebrew-first, English inline
3. Practical Example: Concrete use case
4. Critical Analysis: Limitations, trade-offs
5. Connection: Tie to previous chapters
```

## Cross-Reference Strategy

### Mandatory Connections

**From Part 3 to Part 1**:
- Ch14 → Ch1 (distributed intelligence paradigm)
- Ch14 → Ch4 (Claude CLI integration)
- Ch15 → Ch6 (modular architecture, graph theory analogy)

**From Part 3 to Part 2**:
- Ch14 → Ch7 (external memory vs Skills)
- Ch14 → Ch8 (Progressive Disclosure vs Context Engineering)
- Ch15 → Ch10 (Skills complement 4-file system)
- Ch16 → Ch11 (knowledge management principles)
- Ch16 → Ch13 (cognitive partnership, human expertise preservation)

**From Part 1 to Part 3** (UPDATE EXISTING):
- Ch1 (introduction) → Add Part 3 preview
- Ch4 (Claude CLI) → Add forward reference to Ch14-15

**From Part 2 to Part 3** (UPDATE EXISTING):
- Ch10 (4-file system) → Add note about Skills as complementary
- Ch13 (conclusion) → Expand to mention Skills

### Cross-Reference Format

```latex
כפי שראינו בפרק~\num{1}, הארכיטקטורה המבוזרת...

בחלק~\num{2} (פרקים~\num{7}–\num{13}) דנו בזיכרון החיצוני...

נושא זה יורחב בפרק~\num{14} כאשר נדון ב\en{-Skills}.
```

## Bibliography Extraction Rules

### From PDF Footnotes

**Extraction Process**:
1. Read PDF carefully, note all footnotes (1-21)
2. Extract: Author, Title, Year, URL (if applicable)
3. Create BibTeX entries in refs.bib

**Format Template**:
```bibtex
@misc{anthropic2025skills,
  author = {{Anthropic}},
  title = {Skills in Claude Code: Modular Expertise Packaging},
  howpublished = {\emph{Anthropic Documentation}},
  year = {2025},
  url = {https://...},
  note = {Online; accessed Oct. 20, 2025},
  keywords = {english}
}

@article{author2024topic,
  author = {Last, First and Second, Name},
  title = {Article Title},
  journal = {Journal Name},
  year = {2024},
  volume = {10},
  pages = {123--145},
  keywords = {english}
}
```

**Check for Duplicates**:
- Before adding, search refs.bib for similar titles
- Some references might already exist from Parts 1-2

## Table Conversion Rules

### PDF Table (Page 3)

**Original** (Hebrew/English mixed):
```
מאפיין | Claude Skills | Claude Projects | Custom GPTs | MCP
מטרת העל | אריזת מומחיות... | ניהול קונטקסט... | ...
```

**LaTeX Conversion**:
```latex
\begin{hebrewtable}[H]
\caption{מודלים להפצת ידע ומומחיות בסביבות \en{AI}}
\label{tab:skills_comparison}
\centering
\begin{rtltabular}{|m{2.5cm}|m{3cm}|m{3cm}|m{3cm}|m{2.5cm}|}
\hline
\hebheader{מאפיין} &
\enheader{Claude Skills (CLI)} &
\enheader{Claude Projects (Web/CLI)} &
\enheader{Custom GPTs (OpenAI)} &
\enheader{MCP} \\
\hline
\hebcell{מטרת העל} &
\hebcell{אריזת מומחיות פרוצדורלית וקוד ניתנים לשימוש חוזר.} &
\hebcell{ניהול קונטקסט נרחב, מסמכי יסוד (\en{Artifacts}) ו-\en{Data Room}.} &
\hebcell{משימות נישתיות ואינטראקציה מבוססת \en{API}.} &
\hebcell{רישום פורמלי של כלים חיצוניים (\en{APIs}).} \\
\hline
... (continue for all rows)
\end{rtltabular}
\end{hebrewtable}
```

**Reference in Text**:
```latex
כפי שמוצג בטבלה~\ref{tab:skills_comparison}, ההבדל המרכזי בין \en{Skills} ל\en{-Claude Projects}...
```

## Code Block Handling

### From Appendix A

**YAML Front Matter**:
```latex
\begin{latin}
\begin{verbatim}
name: Data Aggregator for Project X
description: |
  Aggregates and standardizes CSV data files...
allowed-tools: [...]
\end{verbatim}
\end{latin}
```

**Inline Code References**:
```latex
קובץ ה\en{-\texttt{SKILL.md}} כולל...
```

## Chapter Division from PDF

### Recommended Structure

**Chapter 14: המוח המודולרי - Skills וחשיפה הדרגתית**
- Content: Sections 1-2 from PDF
- Length: ~40-50 lines LaTeX
- Focus: Introduction, Progressive Disclosure architecture
- Historical hook: Imagined orders (Harari reference from PDF)

**Chapter 15: Skills בפועל - מיפוי נתיבים ויישום**
- Content: Sections 3-5 from PDF
- Length: ~50-60 lines LaTeX
- Focus: Comparison tables, CLI paths, practical examples
- Includes: Table conversion, code examples

**Chapter 16: סכנות האוטומציה - ניוון מיומנות ושמירת המומחיות**
- Content: Section 6 from PDF + Summary
- Length: ~40-50 lines LaTeX
- Focus: Skill Atrophy, limitations, human expertise
- Critical tone: Harari-style warnings

**Total**: ~130-160 lines = 3 chapters (similar to Part 2 chapters)

## File Naming Convention

```
chapters/chapter14.tex
chapters/chapter15.tex
chapters/chapter16.tex
```

**Inside each file**:
```latex
\hebrewsection{כותרת הפרק}
\label{sec:chapter14}

\hebrewsubsection{תת-כותרת ראשונה}
...
```

## Update Strategy for Existing Chapters

### Chapter 1 Update

**Location**: After Part 2 preview (around line 90)

**Add**:
```latex
\hebrewsubsection{חלק ג: \en{Skills} וארכיטקטורת הידע המודולרי}

\textbf{חלק ג} של הספר (פרקים~\num{14}–\num{16}) משלים את התמונה:
כיצד ניתן לארוז מומחיות פרוצדורלית ליחידות מודולריות הניתנות לשימוש חוזר?
\en{Skills} ב\en{-Claude Code} מייצגים את השלב הבא של הקוגניציה המבוזרת:
לא רק זיכרון חיצוני (חלק~\num{2}), אלא גם \textbf{יכולות ניתנות להרחבה}.

בחלק זה נדון בעקרון \en{Progressive Disclosure} (חשיפה הדרגתית),
נבחן כיצד \en{Skills} משתלבים עם המערכות שראינו בחלקים הקודמים,
ונעמוד על הסכנות הטמונות באוטומציה יתר – תופעת "ניוון המיומנות" (\en{Skill Atrophy}).
```

### main.tex Abstract Update

**Old** (Version 4.0):
```latex
\begin{abstract}
...ספר זה בוחן לעומק שינוי פרדיגמה זה במבנה של שני חלקים...
```

**New** (Version 5.0):
```latex
\begin{abstract}
בעשור האחרון אנו עדים למעבר מפרדיגמת בינה מלאכותית יחידה למערכות
המורכבות מצוות של סוכנים מתמחים. ספר זה בוחן לעומק שינוי פרדיגמה זה
במבנה של \textbf{שלושה חלקים משלימים}:

\textbf{חלק א'} (פרקים~\num{1}–\num{6}) עוסק בארכיטקטורת הקוגניציה המבוזרת
(תת-סוכנים) וכיצד פלטפורמות דוגמת \en{Claude CLI} ופרוטוקול \en{MCP}
מאפשרים שיתוף פעולה חלק בין סוכנים מרובים.

\textbf{חלק ב'} (פרקים~\num{7}–\num{13}) עובר לממד הקוגניטיבי: כיצד סוכנים
שומרים על זיכרון, עקביות ורציפות לאורך זמן באמצעות מערכות זיכרון חיצוניות
מובנות (ארבעת הקבצים: \en{\texttt{PRD.md}}, \en{\texttt{CLAUDE.md}},
\en{\texttt{PLANNING.md}}, \en{\texttt{TASKS.md}}).

\textbf{חלק ג'} (פרקים~\num{14}–\num{16}) משלים את התמונה: כיצד ניתן לארוז
מומחיות פרוצדורלית ליחידות מודולריות (\en{Skills}) הניתנות לשימוש חוזר?
נדון בעקרון \en{Progressive Disclosure}, נבחן את היתרונות של ארכיטקטורה
מבוססת תיקיות קבצים, ונעמוד על הסכנות הטמונות באוטומציה יתר.

נעסוק גם בהיבטי אתיקה, פרטיות וסיכונים הכרוכים בסוכני \en{AI}, ונדגים את
הדיון באמצעות מקרה מבחן מעשי – סוכן לחילוץ מידע מ\en{-Gmail}. הספר מציג
\textbf{שני מסלולי יישום}: גישה ידנית מלאה (נספחים א–ד) המלמדת את יסודות
הפרוטוקול, וגישה מבוססת \en{MCP Python SDK} (נספחים ה–ו, דורשת
\en{Python 3.10+}) המציעה פיתוח מהיר יותר.

שילוב זה של פרספקטיבה בין-תחומית, עומק טכני, דיון היסטורי-פילוסופי וניתוח
מתמטי ברמת מחקר מתקדמת, נועד להעניק לקורא הבנה רחבה ומעמיקה של הדור
החדש של סוכני הבינה המלאכותית – מארכיטקטורה לזיכרון ומודולריות, ומכלי
רגעי לשותפות קוגניטיבית ארוכת-טווח המבוססת על מומחיות ניתנת לאריזה.
\end{abstract}
```

## Quality Checklist (Before Completion)

### Per-Chapter Checklist

- [ ] All Hebrew sections use `\hebrewsection{}`, `\hebrewsubsection{}`
- [ ] All English text wrapped in `\en{}`
- [ ] All numbers wrapped in `\num{}`
- [ ] No `\textenglish{}` or `\texthebrew{}` commands
- [ ] All tables use `hebrewtable` + `rtltabular`
- [ ] All table cells use `\hebcell{}` or `\encell{}`
- [ ] All citations use `\cite{}`
- [ ] At least 2-3 cross-references to other chapters
- [ ] Historical hook in opening paragraph
- [ ] Concrete examples for abstract concepts
- [ ] Harari-style critical analysis (not just praise)

### Full-Book Checklist

- [ ] Chapter 1 updated with Part 3 preview
- [ ] main.tex abstract explains 3-part structure
- [ ] main.tex includes Part 3 division
- [ ] main.tex includes chapter14.tex, chapter15.tex, chapter16.tex
- [ ] main.tex version updated to 5.0
- [ ] refs.bib has all 21 new references
- [ ] refs.bib has no duplicates
- [ ] All cross-references resolve (compile twice to verify)
- [ ] No information repetition between chapters
- [ ] Coherent narrative flow (Parts 1→2→3 feel unified)
- [ ] README.md updated for Version 5.0

## Common Pitfalls (AVOID)

1. **❌ Copying English text without `\en{}`**:
   ```latex
   BAD:  Progressive Disclosure היא...
   GOOD: \en{Progressive Disclosure} היא...
   ```

2. **❌ Using numbers directly**:
   ```latex
   BAD:  200,000 אסימונים
   GOOD: \num{200,000} אסימונים
   ```

3. **❌ Forgetting table wrappers**:
   ```latex
   BAD:  \begin{tabular}... (wrong environment)
   GOOD: \begin{hebrewtable}[H]...\begin{rtltabular}...
   ```

4. **❌ Creating orphan chapters** (no connections):
   - ALWAYS add cross-references
   - ALWAYS tie to previous chapters

5. **❌ Marketing language** (violates Harari style):
   ```latex
   BAD:  Skills הם הפתרון המושלם...
   GOOD: Skills מציעים יתרון משמעותי, אך טומנים בחובם סכנות...
   ```

## Success Metrics

**This Part 3 conversion is SUCCESSFUL when**:
1. ✅ 0 compilation errors
2. ✅ 0 CLS violations (verified with grep)
3. ✅ All 21 PDF references in refs.bib
4. ✅ Reader cannot tell Parts 1-2-3 were written at different times
5. ✅ Every chapter has cross-references
6. ✅ Harari-style narrative maintained
7. ✅ Total pages: 70-75

---

**REMEMBER**: Read PLANNING.md and TASKS.md FIRST in every session!
