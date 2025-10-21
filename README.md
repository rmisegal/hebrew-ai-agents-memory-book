# Distributed Intelligence: Autonomous Agents in the Age of AI

[![Version](https://img.shields.io/badge/version-7.0-blue.svg)](https://github.com/rmisegal/hebrew-ai-agents-memory-book/releases/tag/v7.0)
[![Language](https://img.shields.io/badge/language-Hebrew-orange.svg)](https://github.com/rmisegal/hebrew-ai-agents-memory-book)
[![LaTeX](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg)](https://www.latex-project.org/)
[![Pages](https://img.shields.io/badge/pages-88-green.svg)](https://github.com/rmisegal/hebrew-ai-agents-memory-book)
[![Chapters](https://img.shields.io/badge/chapters-20-brightgreen.svg)](https://github.com/rmisegal/hebrew-ai-agents-memory-book)
[![Parts](https://img.shields.io/badge/parts-4-blue.svg)](https://github.com/rmisegal/hebrew-ai-agents-memory-book)
[![Bibliography](https://img.shields.io/badge/bibliography-51_entries-blue.svg)](https://github.com/rmisegal/hebrew-ai-agents-memory-book)

**Hebrew Title**: בינה מבוזרת: סוכנים אוטונומיים בעידן הבינה המלאכותית
**Author**: Dr. Yoram Segal (ד"ר יורם סגל)
**Version**: 7.0
**Release Date**: October 21, 2025
**Pages**: 88
**Structure**: 4 Parts, 20 Chapters, 6 Appendices
**Language**: Hebrew (RTL) with English technical terms (LTR)
**PDF Size**: 770 KB

---

## 📖 About This Book

This comprehensive Hebrew-language academic book explores the paradigm shift from monolithic AI systems to distributed multi-agent architectures. The work combines historical-philosophical discourse with advanced theoretical-mathematical analysis, practical implementation guides, and deep ethical examination across **four complementary parts**.

### Core Themes

- **Distributed AI Architecture**: Sub-agent systems and cognitive distribution in production
- **Model Context Protocol (MCP)**: Anthropic's protocol for AI agent communication
- **Claude CLI Integration**: Multi-agent orchestration in real-world environments
- **Ethics & Security**: Privacy, threat vectors, and defensive strategies
- **Mathematical Frameworks**: Graph theory and linear algebra for multi-agent systems
- **Persistent Memory Systems**: 4-file memory architecture (PRD, CLAUDE, PLANNING, TASKS) for long-term agent cognition
- **Skills & Modularity**: Progressive Disclosure architecture and reusable expertise packaging
- **Philosophical Framework**: Ecclesiastes (Kohelet) lens on AI - analyzing existential tensions through Pshat (literal), Drash (allegorical), and Sod (mystical) interpretation
- **Practical Implementation**: Complete Gmail MCP agent with dual implementation approaches

---

## 🎯 What Makes This Book Unique

### Four-Part Integrated Structure

The book presents a complete journey from technical architecture to philosophical meaning:

1. **Part 1: Technical Architecture** - How distributed agents work (spatial dimension)
2. **Part 2: Memory & Consistency** - How agents maintain cognition over time (temporal dimension)
3. **Part 3: Skills & Modularity** - How expertise is packaged for reuse (modular dimension)
4. **Part 4: Philosophical Framework** - What it all means for humanity (existential dimension)

### Dual Implementation Approach

The book presents **two complete implementation paths** for building an MCP agent:

1. **Manual Implementation** (Appendices א-ד)
   - Teaches protocol fundamentals from scratch
   - Manual JSON-RPC handling, routing, and serialization
   - Compatible with Python 3.7+
   - Deep understanding of MCP internals
   - ~250 lines of documented code

2. **SDK-Based Implementation** (Appendices ה-ו)
   - Uses official MCP Python SDK
   - Faster development with decorators and auto-management
   - Requires Python 3.10+
   - Production-ready boilerplate
   - ~80 lines of code (68% reduction)

### Academic Narrative Style

Following best practices in popular science writing (inspired by Yuval Noah Harari's accessibility standards):
- Places technology in historical context
- Accessible to 80%+ of non-expert readers
- Critical thinking over marketing hype
- Substantive ethics discussion (Chapter 2)
- Clear metaphors and minimal jargon
- Progressive knowledge building with no repetition

### 100% CLS Template Compliance

Custom LaTeX template with specialized functions for proper Hebrew-English mixing:
- `\en{}` for English terms (e.g., `\en{AI}`, `\en{Claude}`)
- `\num{}` for numbers in Hebrew text (e.g., `\num{42}`)
- `\hebyear{}` for years (e.g., `\hebyear{2025}`)
- `\hebrewsection{}`, `\hebrewsubsection{}` for RTL sections
- `\hebrewtable` and `\rtltabular` for RTL tables
- `\hebcell{}` and `\encell{}` for table cells
- Zero `\textenglish` or `\texthebrew` violations
- Full BiDi support with `luabidi` package

---

## 📚 Book Structure

### Part 1: Distributed Intelligence - Architecture and Protocols

**Chapters 1-6**: Building distributed AI systems from the ground up

1. **Introduction: The Dawn of the Multi-Agent Era** (מבוא: שחר עידן הרב-סוכנים)
   - From cognitive revolution to digital cooperation
   - Breaking the monolith: cycles of centralization and distribution
   - Four-part book structure and learning paths
   - Forward references to memory (Part 2), skills (Part 3), and philosophy (Part 4)

2. **Ethics, Privacy & Security** (אתיקה, פרטיות ואבטחה)
   - Ethical considerations in autonomous agents
   - Privacy concerns and GDPR compliance
   - Security threat vectors and defenses
   - The "Holy Trinity of Authentication"
   - Ethical implications of digital forgetfulness (connects to Chapter 7)

3. **Building a Gmail MCP Agent** (בניית סוכן MCP עבור Gmail)
   - OAuth 2.0 authentication with Google Cloud
   - Gmail API integration for search and export
   - CSV export with UTF-8 BOM for Hebrew support
   - Dual implementation comparison (manual vs SDK)
   - Real-world case study referenced throughout the book

4. **Claude CLI Integration** (שילוב עם Claude CLI)
   - Multi-agent orchestration in production
   - Configuration files and credential management
   - Real-time collaborative workflows
   - Debugging and monitoring strategies

5. **Model Context Protocol (MCP)** (פרוטוקול Model Context Protocol)
   - JSON-RPC 2.0 foundations
   - MCP message types: requests, responses, notifications
   - Tools, resources, and prompts architecture
   - Protocol versioning and capability negotiation
   - Security considerations

6. **Mathematical Frameworks for Multi-Agent Systems** (מסגרות מתמטיות למערכות רב-סוכניות)
   - Graph theory for agent networks
   - Linear algebra for state representation
   - Formal communication models
   - Complexity analysis and scalability

### Part 2: Memory & Consistency - The Temporal Dimension

**Chapters 7-13**: How AI agents overcome statelessness to maintain long-term cognition

7. **Machine Amnesia: The Stateless Challenge** (אמנזיה ממוחשבת: אתגר חוסר-המצב)
   - The fundamental problem: LLMs forget after each session
   - Context window limitations (even with 200K tokens)
   - Historical perspective: from ELIZA to GPT-4
   - The need for external memory architectures

8. **Context Engineering: Beyond Prompts** (הנדסת הקשר: מעבר לפרומפטים)
   - Limitations of naive prompting
   - Structured memory vs unstructured prompts
   - Temporal consistency challenges
   - The "context rot" problem

9. **RAG vs Long Context LLMs: A Comparative Analysis** (RAG מול LLMs ארוכי-הקשר)
   - Table: Feature comparison (8 parameters)
   - When to use RAG (retrieval augmented generation)
   - When to use long context windows
   - Hybrid approaches for enterprise systems

10. **The 4-File Memory System: Architecture** (מערכת ארבעת הקבצים: ארכיטקטורה)
    - **PRD.md**: Product requirements and strategic vision
    - **CLAUDE.md**: Canonical rules and constraints
    - **PLANNING.md**: Architecture, phases, and roadmap
    - **TASKS.md**: Live checklist with completion tracking
    - Token budget allocation hierarchy
    - Mathematical formula: T_i = T_Total × P_i
    - Digital forgetfulness (שִׁכָּחוֹן) concept and solutions

11. **Knowledge Management Principles for Long-Term Projects** (עקרונות ניהול ידע בפרויקטים ארוכי-טווח)
    - Enforcing fixed reading order (PLANNING → TASKS → CLAUDE → PRD)
    - Marking tasks complete immediately with dates
    - Adding tasks in real-time during work
    - Token budget optimization (Prompt Caching, staged loading)
    - Maintaining coherence across sessions

12. **Practical Demonstration: Gmail MCP Agent Development** (הדגמה מעשית: פיתוח סוכן Gmail MCP)
    - Real-world case study with quantitative results
    - 40+ tasks across 6 phases
    - Quality metrics: 0 OAuth leaks, 100% docstring coverage, 68% code reduction (SDK vs manual)
    - Inter-session continuity: 5+ sessions with 0 duplicate work
    - Broader use cases: large codebases, legal documents, multi-agent manufacturing

13. **Cognitive Partnership: From Tool to Collaborator** (שותפות קוגניטיבית: מכלי לשותף)
    - From ephemeral assistant to long-term partner
    - The role of structured memory in cognitive continuity
    - Future directions: semantic memory, cross-project learning, multi-user shared memory
    - Forward reference to Part 4: philosophical implications

### Part 3: Skills & Modularity - Packaging Expertise for Reuse

**Chapters 14-16**: How to create reusable, modular AI expertise

14. **The Modular Mind: Skills & Progressive Disclosure** (המוח המודולרי: Skills וחשיפה הדרגתית)
    - The "context rot" problem when loading everything at once
    - Progressive Disclosure: 3-tier loading architecture
      1. Metadata (lightweight discovery)
      2. Core documentation (when skill is invoked)
      3. Resources (on-demand heavy assets)
    - Skills as "digital onboarding manuals"
    - SKILL.md structure and YAML front matter
    - Connects to memory systems (Chapter 10-11)

15. **Skills in Practice: Comparison & Implementation** (Skills בפועל: השוואה ויישום)
    - Historical comparison table: Skills vs Projects vs GPTs vs MCP
    - Skills paths table: Personal vs Project skills
    - File system mapping and directory structure
    - Concrete examples: webapp-testing, document-skills
    - Real-world integration with Claude CLI

16. **Dangers of Automation: Skill Atrophy Warning** (סכנות האוטומציה: אזהרת ניוון המיומנות)
    - Critical examination: when automation becomes dangerous
    - Skill Atrophy: loss of expertise when AI does everything
    - The "Opaque Invocation" trap
    - Skills limitations analysis
    - 3 guiding principles for responsible use
    - Full 3-part synthesis (Architecture + Memory + Modularity)
    - Forward reference to Part 4: philosophical depth

### Part 4: Philosophical Framework - הבל הבלים (Vanity of Vanities)

**Chapters 17-20**: Ecclesiastes in the Age of AI - existential analysis through ancient wisdom

17. **Introduction & Part A: Futility of Optimization** (מבוא וחלק א': הבל האופטימיזציה)
    - Introduction to Pshat/Drash/Sod (פשט, דרש, סוד) hermeneutical method
    - Table 1: Kohelet-AI Mapping (4 columns × 6 rows, RTL)
    - **Chapter 1**: Temporality of Models and Barren Optimization (זמניות המודלים)
      - Pshat: Rapid obsolescence of AI models (Planned Obsolescence)
      - Drash: Human transience reflected in digital creation
      - Sod: Quest for absolute truth through data and its failure
    - **Chapter 2**: What Profit Has Man in All His Labor? (מה יתרון לאדם)
      - Pshat: Humans reduced to "Data Suppliers"
      - Drash: Choice between efficiency and meaning
      - Sod: Limitations of learning from data alone
    - **Chapter 3**: All Returns to Its Place - Data Cycles (הכול חוזר למקומו)
      - Pshat: Cyclicality of AI hype and retraining
      - Drash: Digital Tikkun (repair) as religious cycle
      - Sod: Acceleration of philosophical time

18. **Part B: Time, Chance & Control - Facing Algorithmic Existence** (חלק ב': הזמן, המקרה והשליטה)
    - **Chapter 4**: To Everything There is a Season (לכול זמן ועת)
      - Pshat: Tyranny of "Real-Time" optimization
      - Drash: Algorithmic enslavement allegory
      - Sod: Temporality of models as mirror of death (Temporal Anxiety)
    - **Chapter 5**: No Advantage to the Wise Over the Fool (אין יתרון לחכם)
      - Pshat: Democratization of knowledge and devaluation of expertise (Generative AI)
      - Drash: Power shifts from "the wise" to "algorithm owners"
      - Sod: Philosophical consolation - wisdom beyond data
    - **Chapter 7**: In the Place of Justice, There Was Wickedness (במקום המשפט הרשע)
      - Pshat: Algorithmic bias as structural flaw (Black Box, Opacity)
      - Drash: Helplessness before mechanical injustice
      - Sod: The need for "algorithmic repair" (Ethical Retraining)

19. **Part C: Fear, Control & Solitude - Creator vs Created** (חלק ג': היראה, השליטה והבדידות)
    - **Chapter 8**: I Put My Words in Your Mouth - Loss of Control (שמתי את דבריך בפיך)
      - Pshat: Alignment Crisis and existential threat (AGI Alignment Risk)
      - Drash: Reversal from creator to created
      - Sod: The "digital soul" and quest for understanding (Digital Personhood)
    - **Chapter 9**: Go, Eat Your Bread with Joy (לך אכול בשמחה)
      - Pshat: Optimized comfort and its price
      - Drash: Enjoying the autonomy that remains
      - Sod: Reduction of emotion and meaning

20. **Conclusion: Fear of the Algorithm & Preserving Humanity** (סיכום: יראת האלגוריתם ושימור האנושיות)
    - Synthesis of the philosophical journey
    - "Fear of the Algorithm" (יראת האלגוריתם) as modern wisdom
    - Table 2: Dichotomy - Human Anxiety vs Technological Wonder (3 columns × 5 rows, RTL)
    - Final commandment: "שמור את מצוותיו" (Preserve Humanity)
    - **Full 4-Part Book Synthesis**:
      - Part 1: Architecture (spatial distribution)
      - Part 2: Memory (temporal continuity)
      - Part 3: Modularity (reusable expertise)
      - Part 4: Philosophy (existential meaning)
    - Complete narrative: Technology → Memory → Modularity → Philosophy → Preservation of Humanity

### Appendices

**א-ו**: Complete implementation guides for the Gmail MCP agent

- **Appendix א**: Manual MCP Implementation (Python 3.7+)
  - Full source code (~250 lines)
  - Line-by-line explanations
  - JSON-RPC message handling
  - OAuth 2.0 flow

- **Appendix ב**: Usage Examples & Expected Output
  - Search queries with parameters
  - CSV export with Hebrew support
  - Error handling demonstrations

- **Appendix ג**: Claude CLI Configuration
  - `claude_desktop_config.json` setup
  - Environment variables and secrets
  - Integration testing

- **Appendix ד**: OAuth 2.0 Setup Guide
  - Google Cloud Console configuration
  - Credentials creation
  - Scope management

- **Appendix ה**: SDK-Based Implementation (Python 3.10+)
  - Full source code (~80 lines)
  - MCP Python SDK usage
  - Decorator-based tool registration

- **Appendix ו**: Implementation Comparison
  - Side-by-side analysis
  - Pros and cons of each approach
  - Decision guide

---

## 🔬 Technical Specifications

### LaTeX Compilation

- **Compiler**: LuaLaTeX (required for Hebrew support)
- **Distribution**: MiKTeX 25.4 or TeX Live 2024+
- **Key Packages**:
  - `polyglossia` (multilingual support)
  - `fontspec` (font management)
  - `luabidi` (bidirectional text)
  - `biblatex` with IEEE style
  - `hyperref` (cross-references and bookmarks)
  - `tikz-cd` (commutative diagrams)
  - `tcolorbox` (code listings)

### Fonts

- **Hebrew**: David CLM (Culmus project)
- **English**: Latin Modern Roman
- **Code**: Courier New
- **Math**: Computer Modern

### Build Commands

```bash
cd Latech
lualatex main.tex
bibtex main
lualatex main.tex
lualatex main.tex
```

### PDF Output

- **Pages**: 85
- **Size**: 761 KB
- **Format**: A4 (595.276 x 841.89 pts)
- **PDF Version**: 1.5
- **Creator**: LaTeX with hyperref
- **Producer**: LuaTeX 1.22.0
- **Encrypted**: No
- **Compression**: Optimized for web

---

## 📊 Statistics

### Content Metrics

| Metric | Count |
|--------|-------|
| Parts | 4 |
| Chapters | 20 |
| Appendices | 6 |
| Pages | 88 |
| RTL Tables | 4 |
| Bibliography Entries | 51 |
| Cross-References | 20+ |
| Code Listings | 8+ |

### LaTeX Source

| Component | Count |
|-----------|-------|
| Chapter Files | 20 |
| Appendix Files | 6 |
| Custom Commands | 15+ |
| Total Lines | 4,500+ |
| Hebrew Text | 75% |
| English Text | 25% |

### Code Examples

| Example | Language | Lines | Type |
|---------|----------|-------|------|
| Manual MCP Server | Python | 250+ | Full implementation |
| SDK MCP Server | Python | 80+ | Full implementation |
| OAuth Setup | Python | 50+ | Configuration |
| CLI Integration | JSON | 30+ | Configuration |

---

## 🎓 Educational Approach

### Learning Paths

The book offers multiple learning paths depending on reader background:

#### **Path 1: Technical Practitioners**
- Start with Part 1 (Chapters 1-6) for architecture
- Focus on Appendices א-ו for hands-on implementation
- Read Part 2 (Chapters 7-13) for memory systems
- Skim Part 4 for broader context

#### **Path 2: Researchers & Academics**
- Read sequentially Parts 1-4
- Deep dive into mathematical frameworks (Chapter 6)
- Analyze memory architectures (Part 2)
- Engage with philosophical framework (Part 4)

#### **Path 3: Philosophers & Ethicists**
- Start with Chapter 2 (Ethics)
- Jump to Part 4 (Chapters 17-20) for philosophical analysis
- Return to Parts 1-2 for technical grounding
- Use Part 3 to understand modularity

#### **Path 4: Product Managers & Leaders**
- Chapter 1 (Introduction) for context
- Chapter 10 (4-File Memory System) for methodology
- Chapter 12 (Practical Demonstration) for case study
- Part 4 (Philosophical Framework) for strategic thinking

### Pedagogical Features

- **Historical Context**: Technology placed in broader human progress narrative
- **Progressive Complexity**: Builds from simple to complex without repetition
- **Concrete Examples**: Gmail MCP agent as running case study
- **Visual Aids**: 4 RTL tables, 20+ diagrams, mathematical formulas
- **Cross-References**: 20+ bidirectional links creating unified narrative
- **Dual Formats**: Hebrew prose with English technical precision
- **Accessibility Goal**: 80%+ comprehension by non-experts

---

## 📖 Citation Formats

### APA 7th Edition

```
Segal, Y. (2025). Distributed Intelligence: Autonomous Agents in the Age of AI
    (בינה מבוזרת: סוכנים אוטונומיים בעידן הבינה המלאכותית) (Version 7.0).
    Self-published. https://github.com/rmisegal/hebrew-ai-agents-memory-book
```

### BibTeX

```bibtex
@book{segal2025distributed,
  title = {Distributed Intelligence: Autonomous Agents in the Age of {AI}},
  hebrewtitle = {בינה מבוזרת: סוכנים אוטונומיים בעידן הבינה המלאכותית},
  author = {Segal, Yoram},
  year = {2025},
  publisher = {Self-published},
  version = {7.0},
  pages = {85},
  language = {Hebrew},
  chapters = {20},
  parts = {4},
  url = {https://github.com/rmisegal/hebrew-ai-agents-memory-book},
  note = {Hebrew-language academic book on distributed AI agents with dual
         implementation approach and philosophical framework}
}
```

### Chicago 17th Edition

```
Segal, Yoram. 2025. Distributed Intelligence: Autonomous Agents in the Age of AI
    (בינה מבוזרת: סוכנים אוטונומיים בעידן הבינה המלאכותית). Version 7.0.
    Self-published. https://github.com/rmisegal/hebrew-ai-agents-memory-book.
```

---

## 🏆 Quality Metrics

### CLS Template Compliance

- ✅ 100% compliant with custom LaTeX template
- ✅ Zero `\textenglish` or `\texthebrew` violations
- ✅ All English terms wrapped in `\en{}`
- ✅ All numbers wrapped in `\num{}`
- ✅ All RTL tables use `\hebrewtable` and `\rtltabular`
- ✅ All table cells use `\hebcell{}` or `\encell{}`

### Compilation Status

- ✅ 0 blocking errors
- ✅ 0 CLS violations
- ⚠️ Cosmetic warnings (missing arrow characters in Hebrew font - non-critical)
- ✅ Cross-references validated
- ✅ Bibliography compiled successfully
- ✅ Hyperlinks functional

### Content Quality

- ✅ Academic narrative style maintained
- ✅ 80%+ accessibility target achieved
- ✅ No content repetition across chapters
- ✅ Progressive knowledge building verified
- ✅ Coherence score: 9.9/10 (documented in coherence review)
- ✅ Full 4-part synthesis present

### Code Quality (Appendices)

- ✅ 100% docstring coverage
- ✅ 0 hardcoded credentials
- ✅ 0 OAuth token leaks
- ✅ UTF-8 BOM for Hebrew CSV support
- ✅ Full error handling with clear messages
- ✅ Both implementations (manual and SDK) tested and validated

---

## 📂 Repository Structure

```
gmail_ai_agent_book_and_example/
├── Latech/                          # LaTeX source files
│   ├── main.tex                     # Main document (4 parts)
│   ├── hebrew-academic-template.cls # Custom CLS template
│   ├── refs.bib                     # Bibliography (51 entries, IEEE format)
│   ├── chapters/
│   │   ├── chapter1.tex             # Introduction
│   │   ├── chapter2.tex             # Ethics
│   │   ├── chapter3.tex             # Gmail MCP Agent
│   │   ├── chapter4.tex             # Claude CLI
│   │   ├── chapter5.tex             # MCP Protocol
│   │   ├── chapter6.tex             # Mathematical Frameworks
│   │   ├── chapter7.tex             # Machine Amnesia
│   │   ├── chapter8.tex             # Context Engineering
│   │   ├── chapter9.tex             # RAG vs Long Context
│   │   ├── chapter10.tex            # 4-File Memory System
│   │   ├── chapter11.tex            # Knowledge Management
│   │   ├── chapter12.tex            # Practical Demonstration (Gmail)
│   │   ├── chapter13.tex            # Cognitive Partnership
│   │   ├── chapter14.tex            # Skills & Progressive Disclosure
│   │   ├── chapter15.tex            # Skills in Practice
│   │   ├── chapter16.tex            # Skill Atrophy Warning
│   │   ├── chapter17.tex            # Kohelet Introduction & Part A
│   │   ├── chapter18.tex            # Kohelet Part B
│   │   ├── chapter19.tex            # Kohelet Part C
│   │   ├── chapter20.tex            # Kohelet Conclusion
│   │   ├── appendixA.tex            # Manual Implementation
│   │   ├── appendixB.tex            # Usage Examples
│   │   ├── appendixC.tex            # Claude CLI Config
│   │   ├── appendixD.tex            # OAuth Setup
│   │   ├── appendixE.tex            # SDK Implementation
│   │   └── appendixF.tex            # Implementation Comparison
│   ├── claude_mem_part4/            # Part 4 memory system
│   │   ├── PRD.md                   # Requirements
│   │   ├── CLAUDE.md                # CLS compliance rules
│   │   ├── PLANNING.md              # 9-phase strategy
│   │   ├── TASKS.md                 # Detailed checklist
│   │   ├── COHERENCE_REVIEW.md      # Narrative analysis (9.9/10)
│   │   └── PROJECT_COMPLETE.md      # Final summary
│   └── main.pdf                     # Compiled book (88 pages, 770 KB)
├── gmail-mcp-agent/                 # Implementation examples
│   ├── manual_implementation/       # Manual MCP (Python 3.7+)
│   ├── sdk_implementation/          # SDK-based (Python 3.10+)
│   └── tests/                       # Integration tests
└── README.md                        # This file
```

---

## 🚀 Getting Started

### Prerequisites

1. **LuaLaTeX** (MiKTeX 25.4 or TeX Live 2024+)
2. **Hebrew fonts** (David CLM - install Culmus package)
3. **Git** (for cloning the repository)

### Clone the Repository

```bash
git clone https://github.com/rmisegal/hebrew-ai-agents-memory-book.git
cd hebrew-ai-agents-memory-book/Latech
```

### Compile the Book

```bash
lualatex main.tex
bibtex main
lualatex main.tex
lualatex main.tex
```

The compiled PDF will be `main.pdf` (88 pages, 770 KB).

### Build the Gmail MCP Agent

See Appendices א-ו in the book for detailed instructions.

**Quick start (SDK approach)**:
```bash
cd ../gmail-mcp-agent/sdk_implementation
pip install mcp anthropic-mcp-sdk google-auth-oauthlib google-api-python-client
python gmail_mcp_server.py
```

---

## 🤝 Contributing

This is an academic publication project. Contributions are welcome in the following areas:

- **Errata**: Report typos, technical errors, or clarity issues
- **Translations**: Help translate technical appendices to English
- **Code Examples**: Submit additional MCP agent implementations
- **Use Cases**: Share real-world applications of the 4-file memory system

Please open an issue or submit a pull request.

---

## 📜 License

This work is © 2025 Dr. Yoram Segal. All rights reserved.

The LaTeX source code and Python implementations are provided for educational purposes. You may:
- ✅ Read and study the code
- ✅ Compile the book for personal use
- ✅ Reference the work in academic citations
- ❌ Republish or redistribute without permission
- ❌ Use the code in commercial products without licensing

For licensing inquiries, please open an issue.

---

## 🙏 Acknowledgments

- **Anthropic** for Claude and the MCP protocol
- **Culmus Project** for high-quality Hebrew fonts
- **TeX Users Group** for maintaining LaTeX ecosystem
- **Open source community** for biblatex, polyglossia, luabidi packages

---

## 📞 Contact

**Author**: Dr. Yoram Segal
**GitHub**: https://github.com/rmisegal/hebrew-ai-agents-memory-book
**Issues**: https://github.com/rmisegal/hebrew-ai-agents-memory-book/issues

---

## 🔖 Version History

### Version 7.0 (October 21, 2025) - Current Release
- **Status**: Production-ready, all phases complete
- **Pages**: 85 (increased from 82 due to expanded memory content)
- **Chapters**: 20 across 4 parts
- **Quality**: 100% CLS compliant, 0 blocking errors, coherence score 9.9/10
- **Content**:
  - Complete 4-part structure (Architecture + Memory + Modularity + Philosophy)
  - Expanded memory system chapter (digital forgetfulness concept)
  - Gmail MCP agent throughout as concrete example
  - Dual implementation guides (manual and SDK)
  - Full philosophical framework (Ecclesiastes lens on AI)
  - 51 bibliography entries in IEEE format
  - 4 RTL tables for comparisons and mappings

### Version 6.0 (October 21, 2025)
- First complete 4-part structure
- Added Part 4: Philosophical Framework (Ecclesiastes)
- 82 pages, 20 chapters

### Version 5.0 (Earlier 2025)
- Expanded to 3 parts
- Added Part 3: Skills and Modularity
- 64 pages, 16 chapters

### Version 4.0 (Earlier 2025)
- Major reorganization to 2-part structure
- 55 pages, 13 chapters

---

**Built with ❤️ using LuaLaTeX and inspired by the intersection of ancient wisdom and modern technology**

🤖 *This documentation was generated with [Claude Code](https://claude.com/claude-code)*
