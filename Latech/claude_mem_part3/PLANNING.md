# PLANNING.md - Part 3 Conversion Strategy

## Executive Summary

Add Part 3 to the Hebrew AI Agents book, converting 6-page PDF about Claude CLI Skills into 3 new LaTeX chapters (14-16), with full CLS compliance and Harari-style narrative.

**Target**: Version 5.0 (3 parts, 16 chapters, ~70-75 pages)

## Phase Breakdown

### Phase 1: Analysis and Setup ✅ IN PROGRESS
**Goal**: Deep understanding of PDF structure and content

**Tasks**:
1. ✅ Read PDF completely (DONE)
2. ✅ Create memory system (PRD, CLAUDE, PLANNING, TASKS)
3. ⏳ Extract all 21 footnote references
4. ⏳ Map PDF sections to LaTeX chapters
5. ⏳ Identify cross-reference points to Parts 1-2

**Deliverables**:
- Memory files created
- Reference list extracted
- Chapter division finalized

**Duration**: Current session

---

### Phase 2: Bibliography and Table Preparation
**Goal**: Prepare supporting materials before chapter writing

**Tasks**:
1. Add 21 new references to refs.bib
2. Check for duplicates with existing 31 entries
3. Convert PDF comparison table (page 3) to LaTeX rtltabular format
4. Create test compilation of table in isolation (like table_test.tex from Part 2)
5. Verify table renders correctly

**Deliverables**:
- `refs.bib` updated (~52 total entries)
- `chapters/skills_table_test.tex` (table test file)
- Clean bibtex compilation

**Duration**: 1 work session

---

### Phase 3: Chapter 14 - The Modular Mind
**Goal**: Convert PDF Sections 1-2 to LaTeX

**Content**:
- Section 1: Introduction (Context Crisis, Procedural Memory, Skills as Imagined Order)
- Section 2: Progressive Disclosure Architecture (Core Principle, Skill Anatomy, Best Practices)

**Structure**:
```latex
\hebrewsection{המוח המודולרי: \en{Skills} וארכיטקטורת החשיפה ההדרגתית}
\label{sec:chapter14}

\hebrewsubsection{ממשבר הקונטקסט למהפכה הקוגניטיבית}
% Content from 1.1: Context Anxiety, Context Rot
% Historical hook: Harari's "imagined orders"
% ~15-20 lines

\hebrewsubsection{הצורך בזיכרון פרוצדורלי וארגוני}
% Content from 1.2-1.3
% Connect to Ch10 (4-file system) - both are procedural knowledge
% ~10-15 lines

\hebrewsubsection{עקרון החשיפה ההדרגתית (\en{Progressive Disclosure})}
% Content from 2.1-2.2
% Explain 3-tier loading (Metadata → Core Docs → Resources)
% ~15-20 lines

\hebrewsubsection{המבנה האנטומי של \en{Skill}}
% Content from 2.2
% SKILL.md structure, YAML front matter
% ~10 lines
```

**Cross-References**:
- To Ch1: Distributed intelligence paradigm
- To Ch7: External memory (Skills vs memory files)
- To Ch8: Progressive Disclosure vs Context Engineering
- To Ch10: Procedural knowledge packaging

**Length**: ~50-55 lines

**Duration**: 1 work session

---

### Phase 4: Chapter 15 - Skills in Practice
**Goal**: Convert PDF Sections 3-5 to LaTeX

**Content**:
- Section 3: Comparison (vs Custom GPTs, Projects, MCP)
- Section 4: CLI paths (Linux/WSL/Windows)
- Section 5: Practical examples (webapp-testing, data-aggregator)

**Structure**:
```latex
\hebrewsection{\en{Skills} בפועל: השוואה, מיפוי ויישום}
\label{sec:chapter15}

\hebrewsubsection{\en{Skills} לעומת הסוכנים ההיסטוריים}
% Content from 3.1-3.2
% Include comparison table (from Phase 2)
% Compare to Custom GPTs, Claude Projects, MCP
% ~20 lines

\hebrewsubsection{מיפוי הטריטוריה הדיגיטלית: נתיבי \en{Skills} ב\en{-CLI}}
% Content from 4.1-4.3
% Personal vs Project Skills
% Linux/WSL/Windows paths
% Include path table
% ~15-20 lines

\hebrewsubsection{דוגמאות מעשיות: אוטומציה וקוד}
% Content from 5.1-5.2
% webapp-testing Skill example
% document-skills (pdf, xlsx, docx)
% Reference to Appendix A
% ~20 lines
```

**Cross-References**:
- To Ch4: Claude CLI integration
- To Ch6: Modular architecture (graph nodes analogy)
- To Ch11: Knowledge management principles

**Length**: ~55-60 lines

**Duration**: 1 work session

---

### Phase 5: Chapter 16 - Dangers of Automation
**Goal**: Convert PDF Section 6 + Summary to LaTeX

**Content**:
- Section 6: Opaque Invocation, Limitations, Skill Atrophy
- Summary: Future of modular knowledge

**Structure**:
```latex
\hebrewsection{סכנות האוטומציה: ניוון מיומנות ושמירת המומחיות}
\label{sec:chapter16}

\hebrewsubsection{המלכודת של ההפעלה האוטונומית}
% Content from 6.1
% Model-invoked (not user-forced)
% Control via description precision
% ~12-15 lines

\hebrewsubsection{חסרונות ונקודות תורפה}
% Content from 6.2
% Conflicts, environment dependency, security
% Code execution risks
% ~15 lines

\hebrewsubsection{אשליית המומחיות: הסכנה הקוגניטיבית}
% Content from 6.3
% Skill Atrophy concept
% Human expertise preservation
% Connect to Ch13 (cognitive partnership)
% ~15-20 lines

\hebrewsubsection{סיכום: עתיד הידע המודולרי}
% PDF Summary section
% Tie to Parts 1-2
% Skills as third pillar
% ~10 lines
```

**Cross-References**:
- To Ch2: Ethics and security concerns
- To Ch7: Memory vs automation
- To Ch11: Knowledge management (avoiding duplication)
- To Ch13: Cognitive partnership, human-machine collaboration

**Length**: ~52-60 lines

**Duration**: 1 work session

---

### Phase 6: Integration - Update Existing Chapters
**Goal**: Add Part 3 references to Parts 1-2

**Updates**:

**1. Chapter 1 (Introduction)**:
- Location: After Part 2 preview (~line 95)
- Add: Part 3 preview subsection (~12-15 lines)
- Mention: Skills as third pillar, modularity, Skill Atrophy warning

**2. Chapter 4 (Claude CLI Integration)**:
- Location: End of chapter (~line 85)
- Add: Forward reference to Ch14-15 (~5-7 lines)
- Preview: Skills extend CLI capabilities

**3. Chapter 10 (Four Pillars)**:
- Location: End of TASKS.md section (~line 88)
- Add: Note about Skills as complementary (~5-7 lines)
- Connection: 4-file system (memory) + Skills (capabilities)

**4. Chapter 13 (Conclusion)**:
- Location: Future directions subsection (~line 65)
- Add: Skills as modular expertise packaging (~7-10 lines)
- Tie: To Skill Atrophy warning from Ch16

**Duration**: 1 work session

---

### Phase 7: main.tex and Abstract Update
**Goal**: Update document structure for Part 3

**Changes**:

**1. Version Update**:
```latex
\newcommand{\version}{\en{Version 5.0}}
```

**2. Add Part 3 Division**:
```latex
\part{\en{Skills} וארכיטקטורת הידע המודולרי - אריזת מומחיות}
% Part 3: Skills and Modular Knowledge - Packaging Expertise

\include{chapters/chapter14}
\include{chapters/chapter15}
\include{chapters/chapter16}
```

**3. Update Abstract**:
- Change "שני חלקים" → "שלושה חלקים משלימים"
- Add Part 3 description (2-3 sentences)
- Explain 3-part rationale (Architecture → Memory → Modularity)

**4. Update Footer**:
- Version 5.0 in footer

**Duration**: 1 work session

---

### Phase 8: Full Compilation and Testing
**Goal**: Verify everything works

**Process**:
1. Full compilation cycle:
   ```bash
   lualatex main.tex
   bibtex main
   lualatex main.tex
   lualatex main.tex
   ```

2. Verify:
   - 0 errors
   - All citations resolved
   - All cross-references resolved
   - Page count: ~70-75 pages

3. PDF checks:
   - Part 3 appears in TOC
   - Chapters 14-16 numbered correctly
   - Tables render properly
   - Hebrew RTL + English LTR correct

**Duration**: 1 work session

---

### Phase 9: CLS Compliance Verification
**Goal**: 100% CLS compliance check

**Verification Commands**:
```bash
cd chapters

# Check for forbidden commands
grep -n "\\textenglish\|\\texthebrew" chapter14.tex chapter15.tex chapter16.tex

# Check for unwrapped English
grep -n "[A-Z][a-z]\{3,\}" chapter14.tex | grep -v "\\en{" | head -20

# Check for unwrapped numbers (basic)
grep -oP '(?<!\\num\{)\b\d+\b' chapter14.tex | head -20

# Check table compliance
grep -n "\\begin{tabular}" chapter14.tex chapter15.tex chapter16.tex  # Should be EMPTY
grep -n "\\begin{hebrewtable}" chapter15.tex  # Should find comparison table

# Check all chapters updated
grep -n "פרק.*16\|chapter16" chapter1.tex chapter13.tex
```

**Fix any violations** before proceeding.

**Duration**: 1 work session

---

### Phase 10: Full Book Coherence Review
**Goal**: Harari-style narrative audit

**Review Questions**:

**Per Chapter**:
1. Does it start with historical/philosophical hook?
2. Is it 80%+ accessible (no unexplained jargon)?
3. Does it include critical analysis (not just praise)?
4. Are abstract concepts supported by concrete examples?
5. Does it build on previous chapters' knowledge?
6. Does it avoid repeating information from earlier chapters?

**Cross-Part**:
1. Does Part 3 feel like natural continuation of Parts 1-2?
2. Are the three pillars clear? (Architecture → Memory → Modularity)
3. Do cross-references create unified narrative?
4. Is there a clear progression of complexity? (Part 1 → Part 2 → Part 3)

**Read-Through**:
- Read Chapters 1, 14, 15, 16, 13 in sequence
- Check narrative flow
- Ensure no jarring transitions

**Duration**: 1 work session

---

### Phase 11: README.md Update for Version 5.0
**Goal**: Update project documentation

**Updates**:

**1. Header Badges**:
- Version: 4.0 → 5.0
- Pages: 55 → ~72 (update after compilation)
- Chapters: 13 → 16
- Parts: 2 → 3

**2. Book Structure**:
- Add Part 3 section
- List Chapters 14-16 with descriptions

**3. Quality Metrics**:
- Update table for Version 5.0
- Pages: ~72
- Chapters: 16
- Parts: 3
- Bibliography: ~52 entries

**4. Version History**:
- Add Version 5.0 entry
- List major additions:
  - Part 3 added (Skills and Modular Knowledge)
  - 3 new chapters
  - 21 new bibliography entries
  - Cross-references between all 3 parts

**5. Learning Paths**:
- Update all 4 paths to include Part 3 chapters
- Add "For Platform Engineers" path (Skills-focused)

**6. Statistics**:
- Update LOC count
- Update file count (27+ → 30+)
- Update page count
- Update bibliography count

**Duration**: 1 work session

---

### Phase 12: Git Commit and Tag v5.0
**Goal**: Release Version 5.0

**Process**:
1. Stage all changes:
   ```bash
   git add .
   ```

2. Commit with detailed message (similar to v4.0)

3. Create annotated tag:
   ```bash
   git tag -a v5.0 -m "Version 5.0 - Added Part 3..."
   ```

4. Push:
   ```bash
   git push origin master
   git push origin v5.0
   ```

**Duration**: 1 work session

---

## Phase Dependencies

```
Phase 1 (Analysis) ✅
    ↓
Phase 2 (Bibliography + Tables)
    ↓
Phase 3 (Ch14) ← Phase 2 complete
    ↓
Phase 4 (Ch15) ← Phase 2 complete (needs table)
    ↓
Phase 5 (Ch16)
    ↓
Phase 6 (Update Ch1, 4, 10, 13) ← Phases 3-5 complete
    ↓
Phase 7 (main.tex update) ← Phase 6 complete
    ↓
Phase 8 (Compilation) ← Phase 7 complete
    ↓
Phase 9 (CLS Verification) ← Phase 8 clean
    ↓
Phase 10 (Coherence Review) ← Phase 9 clean
    ↓
Phase 11 (README update) ← Phase 10 clean
    ↓
Phase 12 (Git release) ← Phase 11 complete
```

## Risk Mitigation

### Risk 1: PDF Content Doesn't Align with Book Style
**Mitigation**:
- Rewrite sections to match Harari narrative
- Add historical hooks where missing
- Convert technical jargon to accessible language
- Add critical analysis to balance enthusiasm

### Risk 2: CLS Violations Creep In
**Mitigation**:
- Run verification grep after EVERY chapter
- Use existing chapters as templates
- Never copy-paste PDF text directly
- Always wrap English in `\en{}`

### Risk 3: Information Repetition Across Parts
**Mitigation**:
- Check each concept against Parts 1-2
- If concept exists, REFERENCE it, don't repeat
- Example: "כפי שראינו בפרק 8, עקרון החשיפה ההדרגתית..."

### Risk 4: Weak Cross-References (Parts feel disconnected)
**Mitigation**:
- Minimum 3 cross-refs per new chapter
- Update 4 existing chapters (Ch1, 4, 10, 13)
- Phase 10 coherence review catches gaps

### Risk 5: Table Rendering Issues
**Mitigation**:
- Phase 2 creates isolated table test
- Verify before integrating into Ch15
- Use Ch9 table as template

## Success Criteria

**Phase Complete When**:
- [ ] All 3 chapters written (14, 15, 16)
- [ ] All 4 existing chapters updated (1, 4, 10, 13)
- [ ] main.tex updated (Part 3, abstract, version 5.0)
- [ ] refs.bib has ~52 entries (31 old + 21 new)
- [ ] Clean compilation (0 errors)
- [ ] 0 CLS violations
- [ ] 10+ cross-references between parts
- [ ] README.md updated
- [ ] Git tagged v5.0

**Book Quality When**:
- [ ] Reader cannot tell Parts 1-2-3 written separately
- [ ] Harari-style narrative throughout
- [ ] No information repetition
- [ ] Progressive complexity (each chapter builds on previous)
- [ ] 3-pillar structure clear (Architecture → Memory → Modularity)

## Estimated Timeline

- **Phase 1**: Current session (✅ IN PROGRESS)
- **Phase 2**: 1 session
- **Phases 3-5**: 3 sessions (1 chapter each)
- **Phase 6**: 1 session
- **Phase 7**: 1 session
- **Phases 8-9**: 1 session
- **Phase 10**: 1 session
- **Phases 11-12**: 1 session

**Total**: ~10 work sessions

## Current Status

**NOW**: Phase 1 - Analysis and Setup
**NEXT**: Extract 21 references, finalize chapter division
**THEN**: Phase 2 - Bibliography and tables

---

**REMEMBER**: This plan is READ FIRST in every session along with TASKS.md!
