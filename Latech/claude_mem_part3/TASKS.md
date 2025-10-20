# TASKS.md - Part 3 Conversion Task Tracker

## Phase 1: Analysis and Setup ⏳ IN PROGRESS

- [x] Read PDF completely (SkillsExplanations.pdf)
- [x] Create memory system directory (claude_mem_part3/)
- [x] Write PRD.md
- [x] Write CLAUDE.md
- [x] Write PLANNING.md
- [x] Write TASKS.md (this file)
- [ ] Extract all 21 footnote references from PDF
- [ ] Map PDF sections to chapter structure
- [ ] Identify specific cross-reference points
- [ ] Create reference extraction document

---

## Phase 2: Bibliography and Table Preparation ⏸️ PENDING

- [ ] Create REFERENCES_EXTRACTED.md with all 21 citations
- [ ] Add references 1-10 to refs.bib
- [ ] Add references 11-21 to refs.bib
- [ ] Check for duplicates with existing entries
- [ ] Run bibtex to verify clean compilation
- [ ] Convert comparison table (PDF page 3) to LaTeX
- [ ] Create chapters/skills_table_test.tex
- [ ] Test compile table in isolation
- [ ] Verify table renders correctly with Hebrew RTL
- [ ] Mark Phase 2 complete

---

## Phase 3: Chapter 14 - The Modular Mind ⏸️ PENDING

### Structure Planning
- [ ] Create chapters/chapter14.tex file
- [ ] Write chapter label and main section title
- [ ] Plan 4 subsections based on PDF Sections 1-2

### Content Writing
- [ ] Subsection 1.1: Context Crisis (15-20 lines)
  - [ ] Historical hook (Harari's imagined orders)
  - [ ] Context Rot concept from PDF
  - [ ] Cross-ref to Ch8 (Context Engineering)

- [ ] Subsection 1.2: Procedural Memory Need (10-15 lines)
  - [ ] Organizational knowledge concept
  - [ ] Skills as "digital onboarding manual"
  - [ ] Cross-ref to Ch10 (4-file system comparison)

- [ ] Subsection 1.3: Progressive Disclosure (15-20 lines)
  - [ ] 3-tier loading explanation
  - [ ] Token efficiency benefits
  - [ ] Cross-ref to Ch7 (external memory)

- [ ] Subsection 1.4: Skill Anatomy (10 lines)
  - [ ] SKILL.md structure
  - [ ] YAML front matter
  - [ ] Resources subdirectory

### Quality Checks
- [ ] All English wrapped in \en{}
- [ ] All numbers wrapped in \num{}
- [ ] All citations added
- [ ] Minimum 3 cross-references
- [ ] No \textenglish or \texthebrew
- [ ] Harari-style opening paragraph
- [ ] Run grep verification
- [ ] Mark Phase 3 complete

---

## Phase 4: Chapter 15 - Skills in Practice ⏸️ PENDING

### Structure Planning
- [ ] Create chapters/chapter15.tex file
- [ ] Write chapter label and main section title
- [ ] Plan 3 subsections based on PDF Sections 3-5

### Content Writing
- [ ] Subsection 3.1: Historical Comparison (20 lines)
  - [ ] vs Custom GPTs
  - [ ] vs Claude Projects
  - [ ] vs MCP Protocol
  - [ ] Include comparison table from Phase 2
  - [ ] Cross-ref to Ch4 (Claude CLI)

- [ ] Subsection 4.1: CLI Paths Mapping (15-20 lines)
  - [ ] Linux/WSL/Windows portability
  - [ ] Personal Skills paths (~/.claude/skills/)
  - [ ] Project Skills paths (./.claude/skills/)
  - [ ] Include path table
  - [ ] Cross-ref to Ch6 (modular architecture)

- [ ] Subsection 5.1: Practical Examples (20 lines)
  - [ ] webapp-testing Skill
  - [ ] document-skills (pdf, xlsx, docx, pptx)
  - [ ] data-aggregator example
  - [ ] Reference Appendix A
  - [ ] Cross-ref to Ch11 (knowledge management)

### Quality Checks
- [ ] All English wrapped in \en{}
- [ ] All numbers wrapped in \num{}
- [ ] Comparison table renders correctly
- [ ] Path table renders correctly
- [ ] Minimum 3 cross-references
- [ ] No \textenglish or \texthebrew
- [ ] Run grep verification
- [ ] Mark Phase 4 complete

---

## Phase 5: Chapter 16 - Dangers of Automation ⏸️ PENDING

### Structure Planning
- [ ] Create chapters/chapter16.tex file
- [ ] Write chapter label and main section title
- [ ] Plan 4 subsections based on PDF Section 6 + Summary

### Content Writing
- [ ] Subsection 6.1: Opaque Invocation (12-15 lines)
  - [ ] Model-invoked (not CLI-forced)
  - [ ] Control via description precision
  - [ ] Cognitive challenge
  - [ ] Cross-ref to Ch2 (security concerns)

- [ ] Subsection 6.2: Limitations (15 lines)
  - [ ] Conflict and confusion
  - [ ] Environment dependency
  - [ ] Security risks (arbitrary code execution)
  - [ ] Loading failures

- [ ] Subsection 6.3: Skill Atrophy (15-20 lines)
  - [ ] Expertise requires understanding
  - [ ] "Magic" vs mastery
  - [ ] Human expertise preservation
  - [ ] Force Multiplier (not replacement)
  - [ ] Cross-ref to Ch13 (cognitive partnership)
  - [ ] Cross-ref to Ch7 (memory vs automation)

- [ ] Subsection: Summary (10 lines)
  - [ ] Skills as paradigm shift
  - [ ] Modular file system architecture
  - [ ] Third pillar completion
  - [ ] Tie to Parts 1-2
  - [ ] Forward-looking statement

### Quality Checks
- [ ] All English wrapped in \en{}
- [ ] All numbers wrapped in \num{}
- [ ] Critical tone (Harari-style warnings)
- [ ] Minimum 3 cross-references
- [ ] No \textenglish or \texthebrew
- [ ] Ties to Ch13 conclusion
- [ ] Run grep verification
- [ ] Mark Phase 5 complete

---

## Phase 6: Integration - Update Existing Chapters ⏸️ PENDING

### Chapter 1 Update
- [ ] Read current chapter1.tex
- [ ] Locate Part 2 preview subsection (~line 95)
- [ ] Write Part 3 preview subsection (12-15 lines)
- [ ] Add cross-refs to Ch14-16
- [ ] Verify CLS compliance
- [ ] Test compile

### Chapter 4 Update
- [ ] Read current chapter4.tex
- [ ] Locate end of chapter (~line 85)
- [ ] Add forward reference to Ch14-15 (5-7 lines)
- [ ] Preview: Skills extend CLI capabilities
- [ ] Verify CLS compliance
- [ ] Test compile

### Chapter 10 Update
- [ ] Read current chapter10.tex
- [ ] Locate end of TASKS.md section (~line 88)
- [ ] Add note about Skills complementing 4-file system (5-7 lines)
- [ ] Explain: Memory (4 files) + Capabilities (Skills)
- [ ] Verify CLS compliance
- [ ] Test compile

### Chapter 13 Update
- [ ] Read current chapter13.tex
- [ ] Locate future directions subsection (~line 65)
- [ ] Add Skills as modular expertise (7-10 lines)
- [ ] Tie to Skill Atrophy warning from Ch16
- [ ] Verify CLS compliance
- [ ] Test compile

### Final Checks
- [ ] All 4 chapters compile cleanly
- [ ] Cross-references point correctly
- [ ] No CLS violations introduced
- [ ] Mark Phase 6 complete

---

## Phase 7: main.tex and Abstract Update ⏸️ PENDING

### main.tex Structure
- [ ] Read current main.tex
- [ ] Update version: \newcommand{\version}{\en{Version 5.0}}
- [ ] Update footer version string
- [ ] Add Part 3 division after Part 2
- [ ] Add \include{chapters/chapter14}
- [ ] Add \include{chapters/chapter15}
- [ ] Add \include{chapters/chapter16}

### Abstract Update
- [ ] Read current abstract
- [ ] Change "שני חלקים" → "שלושה חלקים משלימים"
- [ ] Add Part 3 description (2-3 sentences)
- [ ] Explain 3-part rationale (Architecture → Memory → Modularity)
- [ ] Verify Hebrew grammar and flow
- [ ] Check CLS compliance

### Verification
- [ ] Test compile main.tex
- [ ] Verify Part 3 appears in TOC
- [ ] Verify chapters numbered 14-16
- [ ] Mark Phase 7 complete

---

## Phase 8: Full Compilation and Testing ⏸️ PENDING

### Compilation Cycle
- [ ] Clean auxiliary files (rm *.aux *.toc *.out)
- [ ] Run: lualatex main.tex (first pass)
- [ ] Run: bibtex main
- [ ] Run: lualatex main.tex (second pass)
- [ ] Run: lualatex main.tex (third pass)
- [ ] Check for errors (must be 0)
- [ ] Check warnings (≤3 cosmetic)

### Citation Verification
- [ ] All Part 3 citations resolved
- [ ] No "?" in citations
- [ ] Bibliography includes new entries
- [ ] Run: grep "cite{" chapters/chapter14.tex chapter15.tex chapter16.tex
- [ ] Verify all cited keys exist in refs.bib

### Cross-Reference Verification
- [ ] All \ref{} commands resolve
- [ ] No "??" in cross-references
- [ ] Chapters numbered correctly (1-16)
- [ ] Part divisions appear correctly

### PDF Checks
- [ ] Open main.pdf
- [ ] Navigate to TOC
- [ ] Verify Part 3 listed
- [ ] Click Chapter 14 link (should jump correctly)
- [ ] Click Chapter 15 link
- [ ] Click Chapter 16 link
- [ ] Check page count (~70-75 pages)
- [ ] Verify tables render (Ch15 comparison table)
- [ ] Check Hebrew RTL direction
- [ ] Check English LTR inline
- [ ] Mark Phase 8 complete

---

## Phase 9: CLS Compliance Verification ⏸️ PENDING

### Automated Checks
- [ ] Run: grep -n "\\textenglish" chapters/chapter14.tex (expect 0 results)
- [ ] Run: grep -n "\\texthebrew" chapters/chapter14.tex (expect 0 results)
- [ ] Run: grep -n "\\textenglish" chapters/chapter15.tex (expect 0 results)
- [ ] Run: grep -n "\\texthebrew" chapters/chapter15.tex (expect 0 results)
- [ ] Run: grep -n "\\textenglish" chapters/chapter16.tex (expect 0 results)
- [ ] Run: grep -n "\\texthebrew" chapters/chapter16.tex (expect 0 results)

### English Wrapping Check
- [ ] Run: grep -n "[A-Z][a-z]\{3,\}" chapter14.tex | grep -v "\\en{"
- [ ] Review results, fix any unwrapped English
- [ ] Run: grep -n "[A-Z][a-z]\{3,\}" chapter15.tex | grep -v "\\en{"
- [ ] Review results, fix any unwrapped English
- [ ] Run: grep -n "[A-Z][a-z]\{3,\}" chapter16.tex | grep -v "\\en{"
- [ ] Review results, fix any unwrapped English

### Number Wrapping Check
- [ ] Manual review of chapter14.tex for unwrapped numbers
- [ ] Manual review of chapter15.tex for unwrapped numbers
- [ ] Manual review of chapter16.tex for unwrapped numbers
- [ ] Fix any violations

### Table Compliance
- [ ] Run: grep "\\begin{tabular}" chapter15.tex (expect 0 - should use rtltabular)
- [ ] Run: grep "\\begin{hebrewtable}" chapter15.tex (expect 1+)
- [ ] Verify all table cells use \hebcell{} or \encell{}

### Updated Chapters Check
- [ ] Check chapter1.tex for CLS violations
- [ ] Check chapter4.tex for CLS violations
- [ ] Check chapter10.tex for CLS violations
- [ ] Check chapter13.tex for CLS violations

### Recompile After Fixes
- [ ] If violations found, fix them
- [ ] Recompile: lualatex + bibtex + lualatex + lualatex
- [ ] Verify 0 errors
- [ ] Mark Phase 9 complete

---

## Phase 10: Full Book Coherence Review ⏸️ PENDING

### Chapter-by-Chapter Review

**Chapter 14**:
- [ ] Historical hook in opening? (Harari style)
- [ ] 80%+ accessible? (no unexplained jargon)
- [ ] Critical analysis present? (not just praise)
- [ ] Concrete examples? (not just abstract)
- [ ] Builds on Ch7-8 knowledge?
- [ ] Avoids repeating Ch10 content?

**Chapter 15**:
- [ ] Historical/practical context?
- [ ] Comparison table clear and useful?
- [ ] CLI paths explained accessibly?
- [ ] Practical examples concrete and relatable?
- [ ] Builds on Ch4 knowledge?
- [ ] Avoids repeating Ch11 content?

**Chapter 16**:
- [ ] Critical tone present? (warnings, not hype)
- [ ] Skill Atrophy concept clear?
- [ ] Ties to Ch13 partnership theme?
- [ ] Balances enthusiasm with caution?
- [ ] Builds on Ch2 ethics?
- [ ] Avoids repeating Ch7 automation discussion?

### Cross-Part Flow Review
- [ ] Read: Ch1 (intro) → Ch14 (Part 3 start)
  - [ ] Transition feels natural?
  - [ ] Part 3 preview in Ch1 sets expectations?

- [ ] Read: Ch13 (Part 2 end) → Ch14 (Part 3 start)
  - [ ] Thematic connection clear?
  - [ ] No jarring topic shift?

- [ ] Read: Ch4 (CLI) → Ch14-15 (Skills)
  - [ ] Forward reference helps?
  - [ ] Skills feel like natural CLI extension?

- [ ] Read: Ch10 (4-file) → Ch15 (Skills)
  - [ ] Complementary relationship clear?
  - [ ] Not redundant?

- [ ] Read: Ch16 (atrophy) → Ch13 (conclusion)
  - [ ] Warnings tie to partnership theme?
  - [ ] Consistent message about human expertise?

### Three-Pillar Clarity
- [ ] Part 1: Architecture pillar clear?
- [ ] Part 2: Memory pillar clear?
- [ ] Part 3: Modularity pillar clear?
- [ ] Three pillars feel integrated (not separate books)?
- [ ] Progression logical? (Architecture → Memory → Modularity)

### Information Repetition Check
- [ ] Skills vs 4-file system: different or redundant?
- [ ] Progressive Disclosure vs Context Engineering: distinguished?
- [ ] Skill Atrophy vs Ch13 partnership: reinforcing or repetitive?
- [ ] CLI paths vs Ch4 CLI: complementary or overlapping?

### Final Read-Through
- [ ] Read Chapters 1, 14, 15, 16 in sequence
- [ ] Note any jarring transitions
- [ ] Note any unclear connections
- [ ] Note any repetitive content
- [ ] Fix issues identified
- [ ] Mark Phase 10 complete

---

## Phase 11: README.md Update for Version 5.0 ⏸️ PENDING

### Header Updates
- [ ] Update version badge: 4.0 → 5.0
- [ ] Update pages badge: 55 → [actual from PDF]
- [ ] Update chapters badge: 13 → 16
- [ ] Update parts badge: 2 → 3
- [ ] Update metadata section (Version, Pages, Structure)

### Book Structure Section
- [ ] Add "Part 3: Skills and Modular Knowledge" header
- [ ] Add Chapter 14 description
- [ ] Add Chapter 15 description
- [ ] Add Chapter 16 description
- [ ] Verify Part 1 and Part 2 unchanged

### Quality Metrics Table
- [ ] Update Page Count row: 55 → [actual]
- [ ] Update Parts row: 2 → 3
- [ ] Update Chapters row: 13 → 16
- [ ] Update Bibliography row: 31 → ~52
- [ ] Verify other metrics still accurate

### Version History
- [ ] Add Version 5.0 section (before Version 4.0)
- [ ] List major expansion details
- [ ] List new content (3 chapters)
- [ ] List technical updates (21 refs, cross-refs)
- [ ] List quality improvements
- [ ] Include final metrics

### Learning Paths
- [ ] Update "For Beginners" path (add Ch14-15)
- [ ] Update "For Experienced Developers" path (add Ch15-16)
- [ ] Update "For Researchers" path (add Ch16)
- [ ] Update "For Memory System Practitioners" path (add Ch14)
- [ ] Add NEW "For Platform Engineers" path (Skills-focused)

### Citation Formats
- [ ] Update APA: Version 4.0 → 5.0
- [ ] Update pages: 55 → [actual]
- [ ] Update BibTeX: version, pages, chapters, parts fields

### Statistics Section
- [ ] Update Total Lines of Code: 15,000+ → [estimate 18,000+]
- [ ] Update LaTeX Source Files: 27+ → 30+
- [ ] Update Parts: 2 → 3
- [ ] Update Chapters: 13 → 16
- [ ] Update Bibliography Entries: 31 → ~52
- [ ] Update Development Time: 10 phases → 12 phases
- [ ] Update Compilation Tests: 30+ → 40+
- [ ] Update PDF Size: 570KB → [actual]
- [ ] Update Pages: 55 → [actual]

### Final Verification
- [ ] All badges correct
- [ ] All numbers consistent throughout
- [ ] No references to "2 parts" remaining
- [ ] Version 5.0 mentioned correctly
- [ ] Mark Phase 11 complete

---

## Phase 12: Git Commit and Tag v5.0 ⏸️ PENDING

### Pre-Commit Checks
- [ ] Run: git status (review all changed files)
- [ ] Verify main.pdf updated
- [ ] Verify no temporary files staged (.aux, .log, etc.)
- [ ] Verify README.md updated

### Stage Changes
- [ ] Run: git add Latech/chapters/chapter14.tex
- [ ] Run: git add Latech/chapters/chapter15.tex
- [ ] Run: git add Latech/chapters/chapter16.tex
- [ ] Run: git add Latech/chapters/chapter1.tex (updated)
- [ ] Run: git add Latech/chapters/chapter4.tex (updated)
- [ ] Run: git add Latech/chapters/chapter10.tex (updated)
- [ ] Run: git add Latech/chapters/chapter13.tex (updated)
- [ ] Run: git add Latech/main.tex (updated)
- [ ] Run: git add Latech/refs.bib (updated)
- [ ] Run: git add Latech/main.pdf (recompiled)
- [ ] Run: git add README.md (updated)
- [ ] Run: git add Latech/claude_mem_part3/ (memory files)

### Commit Message
- [ ] Draft comprehensive commit message
- [ ] Include: "Release Version 5.0 - Added Part 3"
- [ ] List: Major Expansion details
- [ ] List: New chapters (14-16)
- [ ] List: Updated chapters (1, 4, 10, 13)
- [ ] List: Technical updates (refs.bib, main.tex)
- [ ] List: Quality improvements
- [ ] List: Final metrics
- [ ] Include: Claude Code attribution
- [ ] Run: git commit with message

### Create Tag
- [ ] Draft annotated tag message
- [ ] Run: git tag -a v5.0 -m "[detailed message]"
- [ ] Verify tag created: git tag -l

### Push to GitHub
- [ ] Run: git push origin master
- [ ] Verify commit appears on GitHub
- [ ] Run: git push origin v5.0
- [ ] Verify tag appears on GitHub
- [ ] Check GitHub release page

### Final Verification
- [ ] Clone repo fresh (test)
- [ ] Compile from fresh clone
- [ ] Verify 0 errors
- [ ] Mark Phase 12 complete

---

## COMPLETION CRITERIA

**Part 3 Conversion is COMPLETE when**:
- [ ] All 12 phases marked complete
- [ ] 3 new chapters written (14, 15, 16)
- [ ] 4 existing chapters updated (1, 4, 10, 13)
- [ ] main.tex updated for Part 3
- [ ] refs.bib has ~52 entries
- [ ] Clean compilation (0 errors)
- [ ] 0 CLS violations
- [ ] 10+ cross-references between parts
- [ ] README.md updated for v5.0
- [ ] Git tagged and pushed v5.0
- [ ] Book reads as unified 3-part narrative
- [ ] Harari-style maintained throughout
- [ ] No information repetition
- [ ] Page count: 70-75 pages

---

## CURRENT STATUS

**Date**: October 20, 2025
**Phase**: 1 (Analysis and Setup)
**Status**: ⏳ IN PROGRESS
**Next Tasks**:
1. Extract 21 footnote references from PDF
2. Create REFERENCES_EXTRACTED.md
3. Finalize chapter division mapping
4. Move to Phase 2

**Last Updated**: Current session
