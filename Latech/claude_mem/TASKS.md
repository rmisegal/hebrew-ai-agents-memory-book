# Project Tasks - Hebrew AI Agents Book Reorganization

**Last Updated:** October 20, 2025
**Current Phase:** Phase 1 (50% Complete)

---

## How to Use This File

- [ ] **Uncompleted task** - Not started yet
- [x] **Completed task** - Done (with completion date)
- **Mark tasks complete IMMEDIATELY when finished**
- **Add completion date in format: (✓ 2025-10-20)**
- **Add new discovered tasks at the bottom of relevant section**
- **This is a LIVING document - update it constantly**

---

## PHASE 1: Content Reorganization
**Goal:** Restructure from 7 chapters to 6 in correct order
**Priority:** CRITICAL
**Estimated Time:** 1 hour total (0.5 hour remaining)

### Milestone 1.1: Project Setup
- [x] Create organized folder structure (chapters/, claude_mem/) (✓ 2025-10-20)
- [x] Move all chapter files to chapters/ subdirectory (✓ 2025-10-20)
- [x] Move planning documents to claude_mem/ (✓ 2025-10-20)
- [x] Update main.tex to use chapters/ paths (✓ 2025-10-20)
- [x] Test compilation with new folder structure (✓ 2025-10-20)
- [x] Create CLAUDE.md with 4-step framework (✓ 2025-10-20)
- [x] Create PLANNING.md (✓ 2025-10-20)
- [x] Create TASKS.md (✓ 2025-10-20)

### Milestone 1.2: Chapter 1 Finalization ✅ COMPLETE
- [x] Create draft merged Chapter 1 (chapter1_new.tex) (✓ 2025-10-20)
- [x] Review chapter1_new.tex for completeness (✓ 2025-10-20)
- [x] Verify all 3 subsections are present and complete (✓ 2025-10-20)
- [x] Check CLS compliance in chapter1_new.tex (✓ 2025-10-20)
- [x] Verify line count ≥40 lines (✓ 2025-10-20)
- [x] Replace old chapter1.tex with chapter1_new.tex (✓ 2025-10-20)
- [x] Delete or archive chapter1_new.tex after merge (✓ 2025-10-20)

### Milestone 1.3: Chapter Reorganization ✅ COMPLETE
- [x] Read current chapters/chapter6.tex (Ethics) (✓ 2025-10-20)
- [x] Create new chapters/chapter2.tex from old chapter6.tex (✓ 2025-10-20)
- [x] Add intro paragraph to new Chapter 2: "לפני שניגש לבניית סוכנים..." (✓ 2025-10-20)
- [x] Add forward reference to Chapter 3 authentication (✓ 2025-10-20)
- [x] Verify new Chapter 2 compiles successfully (✓ 2025-10-20)
- [x] Update chapter number references in new Chapter 2 (✓ 2025-10-20)
- [x] Test compilation after Chapter 2 creation (✓ 2025-10-20)

### Milestone 1.4: Chapter Renaming
- [ ] Create backup of chapters/chapter7.tex (Math)
- [ ] Rename chapters/chapter7.tex → chapters/chapter6_new.tex (temporary)
- [ ] Update chapter references in renamed file
- [ ] Test compilation with renamed file
- [ ] Finalize rename to chapters/chapter6.tex

### Milestone 1.5: Reference Updates
- [ ] Review chapters/chapter3.tex for chapter number references
- [ ] Review chapters/chapter4.tex for chapter number references
- [ ] Review chapters/chapter5.tex for chapter number references
- [ ] Update any references to old chapter numbers
- [ ] Update intro paragraph in Chapter 5 to reference Chapter 3
- [ ] Test compilation after reference updates

### Milestone 1.6: File Cleanup
- [ ] Verify new 6-chapter structure compiles successfully
- [ ] Delete or archive old chapters/chapter1.tex
- [ ] Delete or archive old chapters/chapter2.tex
- [ ] Delete or archive old chapters/chapter6.tex (now Chapter 2)
- [ ] Delete or archive old chapters/chapter7.tex (now Chapter 6)
- [ ] Update main.tex to include only 6 chapters
- [ ] Final compilation test with 6-chapter structure

### Milestone 1.7: Phase 1 Validation
- [ ] Run full compilation: lualatex → bibtex → lualatex × 2
- [ ] Verify 0 errors (BLOCKING if errors exist)
- [ ] Verify ≤3 warnings
- [ ] Verify PDF is 24-28 pages
- [ ] Verify Table of Contents shows 6 chapters in correct order
- [ ] Visual review of PDF for obvious issues
- [ ] Mark Phase 1 as COMPLETE

---

## PHASE 2: Content Quality Enhancement
**Goal:** Eliminate repetitions, complete code, add examples
**Priority:** HIGH
**Estimated Time:** 2 hours

### Milestone 2.1: Remove Repetitions
- [ ] Read Chapter 5 (MCP Protocol) completely
- [ ] Identify redundant MCP introduction in Chapter 5
- [ ] Rewrite Chapter 5 intro to reference Chapter 3
- [ ] Add text: "לאחר שראינו בפרק 3 את יישום MCP בפועל..."
- [ ] Remove duplicate protocol definition
- [ ] Keep unique comparison content
- [ ] Test compilation after Chapter 5 edits

### Milestone 2.2: Complete Appendix A Code
- [ ] Read chapters/appendixA.tex completely
- [ ] Locate truncated CSV export code (around line 51)
- [ ] Write complete CSV export loop implementation
- [ ] Add header extraction logic (Date, From, Subject)
- [ ] Add csv.writer.writerow() calls
- [ ] Verify code matches Appendix E structure (but manual style)
- [ ] Test LaTeX compilation of updated Appendix A
- [ ] Test Python execution of completed code (if possible)

### Milestone 2.3: Enhance Mathematical Chapter
- [ ] Read Chapter 6 (Mathematics) completely
- [ ] Identify abstract examples that need grounding
- [ ] Add opening paragraph connecting to Chapters 3-5
- [ ] Add Gmail agent example for graph representation
- [ ] Add text: "במערכת Gmail MCP שלנו (פרק 3), אם נתייחס לסוכן כצומת..."
- [ ] Add practical application note for matrix analysis
- [ ] Map mathematical concepts to Gmail agent data flow
- [ ] Test compilation after Chapter 6 edits

### Milestone 2.4: Add Python Version Notices
- [ ] Read Chapter 3 (Gmail Agent) completely
- [ ] Add Python 3.10+ requirement notice for SDK approach
- [ ] Clarify which appendices use which Python version
- [ ] Read Chapter 4 (Claude CLI) completely
- [ ] Add Python version note for SDK users
- [ ] Read chapters/appendixE.tex
- [ ] Add version notice at top: "דרישת גרסה: Python 3.10 ומעלה"
- [ ] Test compilation after all notices added

### Milestone 2.5: Update Abstract
- [ ] Read current abstract in main.tex
- [ ] Identify what's missing (dual approaches, Python requirements)
- [ ] Draft new abstract text mentioning manual + SDK approaches
- [ ] Add text about two implementation paths
- [ ] Keep abstract length 150-200 words (Hebrew)
- [ ] Update abstract in main.tex
- [ ] Test compilation after abstract update

### Milestone 2.6: Add Forward References
- [ ] Review Chapter 2 (Ethics) for forward reference to Chapter 3
- [ ] Add explicit reference: "בפרק 3 נראה כיצד עקרונות אלה מיושמים..."
- [ ] Review other chapters for missing forward references
- [ ] Add forward references where appropriate
- [ ] Test compilation after reference additions

### Milestone 2.7: Phase 2 Validation
- [ ] Run full compilation test
- [ ] Verify 0 errors, ≤3 warnings
- [ ] Content review: check for any remaining repetitions
- [ ] Verify all code examples are complete
- [ ] Verify abstract accurately reflects book content
- [ ] Mark Phase 2 as COMPLETE

---

## PHASE 3: Language and Format Compliance
**Goal:** 100% CLS function compliance for Hebrew-English mixing
**Priority:** HIGH
**Estimated Time:** 1 hour

### Milestone 3.1: CLS Compliance Audit
- [ ] Run grep search for `\textenglish` in all chapters
- [ ] Run grep search for `\texthebrew` in all chapters
- [ ] List all violations found
- [ ] Create fix plan for each violation

### Milestone 3.2: Fix Language Mixing Violations
- [ ] Fix `\textenglish{}` → `\en{}` in Chapter 1
- [ ] Fix `\textenglish{}` → `\en{}` in Chapter 2
- [ ] Fix `\textenglish{}` → `\en{}` in Chapter 3
- [ ] Fix `\textenglish{}` → `\en{}` in Chapter 4
- [ ] Fix `\textenglish{}` → `\en{}` in Chapter 5
- [ ] Fix `\textenglish{}` → `\en{}` in Chapter 6
- [ ] Test compilation after each chapter fix

### Milestone 3.3: Fix Number Formatting
- [ ] Audit all chapters for plain numbers in Hebrew text
- [ ] Replace plain numbers with `\num{}` in Chapter 1
- [ ] Replace plain numbers with `\num{}` in Chapter 2
- [ ] Replace plain numbers with `\num{}` in Chapter 3
- [ ] Replace plain numbers with `\num{}` in Chapter 4
- [ ] Replace plain numbers with `\num{}` in Chapter 5
- [ ] Replace plain numbers with `\num{}` in Chapter 6
- [ ] Test compilation after fixes

### Milestone 3.4: Fix Year Formatting
- [ ] Audit all chapters for plain years
- [ ] Replace plain years with `\hebyear{}` in all chapters
- [ ] Test compilation after fixes

### Milestone 3.5: Fix Code Block Formatting
- [ ] Review all appendices for code block formatting
- [ ] Verify no optional parameters in `\begin{pythonbox}`
- [ ] Verify complex code uses `\begin{english}\begin{verbatim}`
- [ ] Verify JSON uses verbatim (not pythonbox)
- [ ] Fix any code block violations
- [ ] Test compilation after fixes

### Milestone 3.6: Phase 3 Validation
- [ ] Run final CLS compliance check: `grep -n "\\textenglish\|\\texthebrew" chapters/*.tex`
- [ ] Verify zero results from grep search
- [ ] Run full compilation test
- [ ] Verify 0 errors, ≤3 warnings
- [ ] Visual PDF review for formatting issues
- [ ] Mark Phase 3 as COMPLETE

---

## PHASE 4: Validation and Testing
**Goal:** Ensure everything works and reads well
**Priority:** CRITICAL
**Estimated Time:** 2 hours

### Milestone 4.1: LaTeX Compilation Validation
- [ ] Clean all auxiliary files: `rm -f *.aux *.log *.out`
- [ ] Run: `lualatex main.tex`
- [ ] Verify: 0 errors (BLOCKING)
- [ ] Run: `bibtex main`
- [ ] Verify: No bibtex errors
- [ ] Run: `lualatex main.tex` (second pass)
- [ ] Run: `lualatex main.tex` (third pass for references)
- [ ] Verify: All cross-references resolved
- [ ] Verify: PDF generated successfully
- [ ] Verify: PDF is 24-28 pages
- [ ] Check: ≤3 warnings (acceptable)

### Milestone 4.2: Code Execution Testing
- [ ] Navigate to gmail-mcp-agent-sdk directory
- [ ] Activate Python 3.10+ venv
- [ ] Run: `python gmail_mcp_server_sdk.py`
- [ ] Verify: Server starts without import errors
- [ ] Verify: No Python syntax errors
- [ ] Test: OAuth flow (if credentials available)
- [ ] Test: CSV export functionality (if possible)
- [ ] Navigate to manual implementation directory
- [ ] Test manual implementation code (after Appendix A completion)

### Milestone 4.3: Content Quality Review
- [ ] Read entire book PDF cover-to-cover
- [ ] Check: Does each chapter connect to the next?
- [ ] Check: Are "why this matters" moments clear?
- [ ] Check: Is there intellectual progression?
- [ ] Check: Are abstract concepts grounded in examples?
- [ ] Check: Zero content repetition found?
- [ ] Check: Each chapter introduces 2-3 new concepts?
- [ ] Check: Forward references are explicit?
- [ ] Check: Back references are specific?
- [ ] Check: First mention of terms include definitions?

### Milestone 4.4: Technical Accuracy Review
- [ ] Verify: All code is syntactically correct
- [ ] Verify: Package versions are compatible
- [ ] Verify: OAuth setup instructions are accurate
- [ ] Verify: Mathematical notation is consistent
- [ ] Verify: MCP protocol description matches spec
- [ ] Verify: All imports are included in code
- [ ] Verify: No placeholder comments without implementation

### Milestone 4.5: "Harari Standard" Narrative Review
- [ ] Historical perspective: Technology in historical context?
- [ ] Clarity: Can non-expert understand 80%+?
- [ ] Critical thinking: Trade-offs presented, not just benefits?
- [ ] Ethics chapter: Substantive, not perfunctory?
- [ ] Avoid marketing language: No vendor hype?
- [ ] Metaphors: Consistent and helpful?
- [ ] Jargon: Minimized or well-explained?

### Milestone 4.6: Structural Validation
- [ ] Verify: Chapter dependency matrix is correct
- [ ] Chapter 2 depends on Chapter 1? ✓
- [ ] Chapter 3 depends on Chapters 1-2? ✓
- [ ] Chapter 4 depends on Chapter 3? ✓
- [ ] Chapter 5 depends on Chapters 3-4? ✓
- [ ] Chapter 6 depends on Chapter 3? ✓
- [ ] All "Provides To" references are explicit in text?

### Milestone 4.7: Generate Validation Report
- [ ] Create VALIDATION_REPORT.md in claude_mem/
- [ ] Document: All tests performed
- [ ] Document: All issues found and fixed
- [ ] Document: Compilation statistics
- [ ] Document: Code execution results
- [ ] Document: Quality review scores
- [ ] Document: Final metrics (pages, chapters, warnings)
- [ ] Mark Phase 4 as COMPLETE

---

## PHASE 5: Final Documentation and Polish
**Goal:** Complete project documentation and final review
**Priority:** MEDIUM
**Estimated Time:** 1 hour

### Milestone 5.1: Create Changelog
- [ ] Create CHANGELOG.md in claude_mem/
- [ ] Document: All structural changes (7→6 chapters)
- [ ] Document: All content changes (repetitions removed, etc.)
- [ ] Document: All code completions (Appendix A)
- [ ] Document: All formatting fixes (CLS compliance)
- [ ] Document: Version history
- [ ] Document: Breaking changes (if any)

### Milestone 5.2: Final Proofreading
- [ ] Proofread Chapter 1 for typos
- [ ] Proofread Chapter 2 for typos
- [ ] Proofread Chapter 3 for typos
- [ ] Proofread Chapter 4 for typos
- [ ] Proofread Chapter 5 for typos
- [ ] Proofread Chapter 6 for typos
- [ ] Proofread all appendices for typos
- [ ] Check bibliography for completeness
- [ ] Check all URLs and references work

### Milestone 5.3: Generate Final PDF
- [ ] Clean all auxiliary files
- [ ] Run complete build: lualatex → bibtex → lualatex × 2
- [ ] Verify 0 errors, ≤3 warnings
- [ ] Generate final main.pdf
- [ ] Verify PDF quality (fonts, images, layout)
- [ ] Archive final PDF with date stamp

### Milestone 5.4: Update Project Documentation
- [ ] Update PLANNING.md with final status
- [ ] Update TASKS.md with all completed tasks
- [ ] Update CLAUDE.md with any lessons learned
- [ ] Update PRD.md Phase status to 100% complete
- [ ] Verify all documentation is consistent

### Milestone 5.5: Archive and Backup
- [ ] Create archive of old chapter files (if not already done)
- [ ] Create backup of final working version
- [ ] Document: File locations and structure
- [ ] Document: Setup instructions for future work

### Milestone 5.6: Project Completion
- [ ] Review: All must-have criteria met?
- [ ] Review: All should-have criteria met?
- [ ] Review: Documentation complete?
- [ ] Review: Tests passed?
- [ ] Final sign-off: Project COMPLETE
- [ ] Mark Phase 5 as COMPLETE

---

## NEW TASKS (Discovered During Implementation)

### Add tasks here as they are discovered:

- [ ] (Example format: Task description - add date when added)

---

## COMPLETED PHASES SUMMARY

### Phase 1: Content Reorganization
- **Status:** 50% Complete
- **Started:** 2025-10-20
- **Completed:** _In Progress_
- **Notes:** Folder structure complete, Chapter 1 draft ready, compilation tested

### Phase 2: Content Quality Enhancement
- **Status:** Not Started
- **Started:** _Pending_
- **Completed:** _Pending_

### Phase 3: Language Compliance
- **Status:** Not Started
- **Started:** _Pending_
- **Completed:** _Pending_

### Phase 4: Validation
- **Status:** Not Started
- **Started:** _Pending_
- **Completed:** _Pending_

### Phase 5: Documentation
- **Status:** Not Started
- **Started:** _Pending_
- **Completed:** _Pending_

---

## OVERALL PROJECT STATUS

**Total Tasks:** ~150
**Completed Tasks:** ~13
**Completion Percentage:** ~9%
**Current Phase:** Phase 1 (Milestone 1.2: 85% complete, 1 task remaining)
**Blocking Issues:** None
**Next Critical Task:** Delete/archive chapter1_new.tex, then begin Milestone 1.3 (Chapter Reorganization)

---

**Last Updated:** October 20, 2025 by Claude Code
**Next Review:** After Phase 1 completion
