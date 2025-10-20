# PRD: Part 3 - Skills and Modular Knowledge Architecture

## Product Vision

Add Part 3 to the Hebrew AI Agents book, covering Claude CLI's "Skills" feature as the third pillar of distributed AI intelligence:
- **Part 1**: Distributed Intelligence - Architecture and Protocols (Chapters 1-6)
- **Part 2**: Memory and Consistency - Engineering Persistent Cognition (Chapters 7-13)
- **Part 3**: Skills and Modular Knowledge - Packaging Expertise for AI Agents (NEW)

## Source Material

**Primary Source**: `C:\25D\GeneralLearning\Videos\Skills\SkillsExplanations.pdf`
- 6 pages of Hebrew content about Claude CLI Skills
- Academic style, similar to Parts 1-2
- Contains technical examples, tables, code snippets

## Core Requirements

### 1. Chapter Structure Analysis

From the PDF, identify natural chapter divisions based on:
- Section 1: Introduction - From Context Crisis to Cognitive Revolution
  - 1.1: Context Anxiety and Context Rot
  - 1.2: Need for Procedural Memory
  - 1.3: Skills as New Imagined Order

- Section 2: Progressive Disclosure Architecture
  - 2.1: Core Principle
  - 2.2: Anatomical Structure of Skills
  - 2.3: Best Practices for Writing Skills

- Section 3: Skills vs Historical Agents (Paradigmatic Comparison)
  - 3.1: vs Custom GPTs and Claude Projects
  - 3.2: Transition to MCP Protocol

- Section 4: Digital Territory Mapping - Skills Paths in CLI
  - 4.1: Cross-OS Portability
  - 4.2: Personal Skills Location
  - 4.3: Project Skills Location

- Section 5: Practice and Implementation
  - 5.1: Conceptual Example
  - 5.2: Practical Examples (Code Skills)

- Section 6: Dangers and Control
  - 6.1: Autonomous Invocation Trap
  - 6.2: Limitations and Weaknesses
  - 6.3: Skill Atrophy Illusion

- Appendix A: Code Snippets

**Proposed Chapter Division** (3-4 chapters):
- Chapter 14: The Modular Mind - Skills and Progressive Disclosure
- Chapter 15: Skills in Practice - CLI Mapping and Implementation
- Chapter 16: Dangers of Automation - Skill Atrophy and Human Expertise

### 2. Content Requirements

**Must maintain**:
- 100% CLS compliance (all `\en{}`, `\num{}`, `\hebrewsection{}` functions)
- Harari-style narrative (80%+ accessibility, historical context)
- Hebrew RTL with English LTR inline mixing
- Academic rigor with practical examples

**Must add**:
- Cross-references to Parts 1-2 (especially Ch4 Claude CLI, Ch7-8 Memory, Ch9 RAG vs LC-LLMs)
- Connection to 4-file memory system (Ch10-11)
- Tie Skills to distributed intelligence theme (Ch1, Ch6 graph theory)

**Must update**:
- Chapter 1 introduction to mention Part 3
- main.tex abstract to explain 3-part structure
- refs.bib with new citations from PDF (21 footnotes to extract)

### 3. Quality Standards

**CLS Functions Only**:
- Hebrew text: `\hebrewsection{}`, `\hebrewsubsection{}`
- English inline: `\en{}`
- Numbers: `\num{}`
- Years: `\hebyear{}`
- Table cells: `\hebcell{}`, `\encell{}`
- Headers: `\hebheader{}`, `\enheader{}`

**No Forbidden Commands**:
- ❌ `\textenglish{}`
- ❌ `\texthebrew{}`
- ❌ Direct English/numbers without wrappers

**Table Requirements**:
- Use `hebrewtable` environment
- Use `rtltabular` for complex tables
- See existing tables in Ch9 for reference

### 4. Integration Requirements

**Update Chapter 1** (Introduction):
- Add Part 3 preview subsection (after Part 2 preview)
- Mention Skills as third pillar of distributed cognition
- ~10-15 lines

**Update main.tex**:
- Add Part 3 division: `\part{Skills and Modular Knowledge - Packaging Expertise}`
- Update abstract to explain 3-part structure rationale
- Update version to 5.0
- Include new chapter files

**Cross-Reference Network**:
- From Part 1 to Part 3: Ch4 (Claude CLI) → Ch14 (Skills intro)
- From Part 2 to Part 3: Ch10 (4-file system) → Ch15 (Skills as complementary)
- From Part 3 to Part 1: Ch14 → Ch1 (distributed intelligence)
- From Part 3 to Part 2: Ch16 → Ch7 (memory vs automation)

### 5. Bibliography Extraction

Extract all 21 footnote references from PDF and add to refs.bib:
- References 1-21 from the PDF
- Follow existing BibTeX format
- Add `keywords = {english}` tag
- Remove any duplicates

### 6. Final Deliverables

**LaTeX Files** (new):
- `chapters/chapter14.tex` - The Modular Mind
- `chapters/chapter15.tex` - Skills in Practice
- `chapters/chapter16.tex` - Dangers of Automation

**Updated Files**:
- `chapters/chapter1.tex` - Add Part 3 preview
- `main.tex` - Part 3 division, abstract update, version 5.0
- `refs.bib` - Add 21 new references
- `README.md` - Update for Version 5.0

**Compilation Target**:
- Pages: ~70-75 (from 55)
- Structure: 3 parts, 16 chapters, 6 appendices
- Compilation: 0 errors
- CLS Compliance: 100%

### 7. Success Criteria

1. ✅ All PDF content converted to LaTeX with CLS compliance
2. ✅ Harari-style narrative maintained throughout
3. ✅ No information repetition between sections
4. ✅ Each new section builds on previous knowledge
5. ✅ Cross-references create unified 3-part narrative
6. ✅ Full book coherence (reads as one book, not 3 separate parts)
7. ✅ Clean compilation (0 errors)
8. ✅ All citations resolved

## Version Target

**Version 5.0**:
- 3 parts
- 16 chapters (6 + 7 + 3)
- 6 appendices
- ~70-75 pages
- 40+ bibliography entries

## Timeline

Phase-by-phase conversion following Part 2 methodology.
