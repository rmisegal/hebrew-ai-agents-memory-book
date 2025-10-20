# Table Analysis: RAG vs Long Context LLMs Comparison
## Phase 2, Milestone 2.1 - Table Structure Analysis

**Date:** October 20, 2025
**Source:** ClaudeMemHebChapter.pdf, Section 3.2.3 (Pages 4-5)
**Status:** ✅ COMPLETE

---

## PDF Table Location

**Section:** 3.2.3 ניתוח השוואתי: RAG לעומת Long Context LLMs
**Pages:** 4-5
**Title:** "סיכום השוואתי של דינמיקת המערכת RAG לעומת Long Context LLMs"

---

## Table Structure Extracted from PDF

### Column Headers (RTL - Right to Left)

| Visual Position | Hebrew Header | English Equivalent |
|----------------|---------------|-------------------|
| Right (Column 3) | **מאפיין** | Feature/Characteristic |
| Middle (Column 2) | **Retrieval-Augmented Generation (RAG)** | RAG |
| Left (Column 1) | **Long Context LLMs (LC-LLMs)** | Long Context LLMs |

### Table Rows (7 rows total)

**Row 1: מקור ידע (Knowledge Source)**
- **מאפיין:** מקור ידע
- **RAG:** לא-פרמטרי, חיצוני, נתונים דינמיים (מסד נתונים וקטורי/גרף).
- **LC-LLMs:** פרמטרי (משקולות מאומנות) + חלון הקשר גדול (נתוני In-Context).

**Row 2: סקיילביליות (Scalability)**
- **מאפיין:** סקיילביליות
- **RAG:** גבוהה במיוחד (טריליוני אסימונים); סקיילביליות בלתי תלויה בגודל המודל.
- **LC-LLMs:** מוגבלת על ידי מורכבות ה-Attention; מוגבלת למקסימום חלון ההקשר הנוכחי.

**Row 3: עלות ויעילות (Cost and Efficiency)**
- **מאפיין:** עלות ויעילות
- **RAG:** חסכוני מאוד באמצעות אחזור סלקטיבי; משתמש במשאבים ביעילות.
- **LC-LLMs:** דרישות חישוביות גבוהות לעיבוד חלון ההקשר הגדול כולו בכל שאילתה.

**Row 4: התאמה לנתונים (Data Suitability)**
- **מאפיין:** התאמה לנתונים
- **RAG:** מצטיין בנתונים מקוטעים, דינמיים, מיוחדים או דלילים (למשל, מאגרי קוד, דיאלוג).
- **LC-LLMs:** מתאים יותר להקשרים צפופים, מובנים היטב ועקביים (למשל, ספרים, מסמכים מובנים).

---

## CLS Table Functions (from hebrew-academic-template.cls)

### Key Functions for Mixed Hebrew-English Tables

#### 1. **Table Environment**
```latex
\begin{hebrewtable}[H]
\caption{Table caption with \en{English} terms}
\centering
\begin{rtltabular}{|m{width1}|m{width2}|m{width3}|}
% Table content
\end{rtltabular}
\end{hebrewtable}
```

#### 2. **Column Specification**
- **MUST use `m{width}` (not `p{width}`)** for vertical centering
- **Reverse order:** Columns written RTL (rightmost first in code)
- Example: `{|m{5cm}|m{5cm}|m{3cm}|}` = [Right column | Middle | Left]

#### 3. **Header Row Functions**

**For Hebrew headers with English terms:**
```latex
\textbf{\hebheader{Hebrew text \en{English}}}
```

**For pure English headers:**
```latex
\textbf{\enheader{English Text}}
```

#### 4. **Data Cell Functions**

**For Hebrew cells with mixed content:**
```latex
\hebcell{Hebrew text \en{English terms} more Hebrew}
```

**For pure English cells:**
```latex
\encell{English text or formulas}
```

**Key Rules:**
- ✅ DO: `\hebcell{Hebrew \en{RAG} text}`
- ❌ DON'T: `\hebcell{Hebrew \en{ RAG } text}` (no spaces inside `\en{}`)
- ✅ DO: `\en{In-Context}`
- ❌ DON'T: Split English terms: `\en{In}-\en{Context}`

#### 5. **Numbers in Tables**
- **Always use `\num{}` for numbers in Hebrew cells:**
  - ✅ `\hebcell{גבוהה במיוחד (\en{טריליוני} אסימונים)}`
  - For standalone numbers: wrap in `\en{}` for LTR display

---

## LaTeX Conversion Strategy

### Column Order (RTL)

**Visual Layout (what reader sees):**
```
┌────────────────┬─────────────────────────────┬─────────────────────────────┐
│    מאפיין      │            RAG             │      Long Context LLMs      │
│   (Right)     │          (Middle)          │          (Left)            │
└────────────────┴─────────────────────────────┴─────────────────────────────┘
```

**LaTeX Code Order (how we write it):**
```latex
\begin{rtltabular}{|m{3cm}|m{5.5cm}|m{5.5cm}|}
\hline
\textbf{\hebheader{מאפיין}} & \textbf{\enheader{Retrieval-Augmented Generation (RAG)}} & \textbf{\enheader{Long Context LLMs (LC-LLMs)}} \\
\hline
% Column 3 (right) & Column 2 (middle) & Column 1 (left)
```

### Cell Content Pattern

**Row 1 (Knowledge Source):**
```latex
\hebcell{מקור ידע} &
\hebcell{לא-פרמטרי, חיצוני, נתונים דינמיים (מסד נתונים וקטורי/גרף).} &
\hebcell{פרמטרי (משקולות מאומנות) + חלון הקשר גדול (נתוני \en{In-Context}).} \\
\hline
```

**Key Observations:**
- מאפיין column: Pure Hebrew → `\hebcell{}`
- RAG column: Mixed Hebrew with English terms → `\hebcell{Hebrew \en{English}}`
- LC-LLMs column: Mixed Hebrew with English terms → `\hebcell{Hebrew \en{English}}`

---

## Complete Table Dimensions

### Recommended Column Widths

Based on content analysis:

| Column | Content Type | Width | Justification |
|--------|--------------|-------|---------------|
| מאפיין (Right) | Pure Hebrew, short | `m{3cm}` | Feature names are 2-5 words |
| RAG (Middle) | Mixed, medium-long | `m{5.5cm}` | Descriptions 15-30 words |
| LC-LLMs (Left) | Mixed, medium-long | `m{5.5cm}` | Descriptions 15-30 words |

**Total width:** 3cm + 5.5cm + 5.5cm = 14cm (fits within A4 margins)

---

## English Terms Requiring `\en{}` Wrapper

From the PDF table content:

### Terms in RAG Column:
- In-Context (appears in Row 1: "נתוני In-Context")
- Attention (appears in Row 2)
- Note: Many terms already in English parentheses in original

### Terms in LC-LLMs Column:
- In-Context
- Attention
- All abbreviated terms already in English

### Numbers:
- No explicit numbers in this table (just descriptive text)
- References like "20" in superscript are citations, not table content

---

## Citation Handling

The PDF table includes superscript citation numbers (e.g., ²⁰, ²²).

**LaTeX Approach:**
- Use `\cite{key}` or manual superscript: `\textsuperscript{\num{20}}`
- For this test table, we'll **omit citations** initially
- Add citations in Chapter 9 integration phase

---

## Complete Row Content (Extracted)

### Row 1: מקור ידע
- מאפיין: מקור ידע
- RAG: לא-פרמטרי, חיצוני, נתונים דינמיים (מסד נתונים וקטורי/גרף).
- LC-LLMs: פרמטרי (משקולות מאומנות) + חלון הקשר גדול (נתוני In-Context).

### Row 2: סקיילביליות
- מאפיין: סקיילביליות
- RAG: גבוהה במיוחד (טריליוני אסימונים); סקיילביליות בלתי תלויה בגודל המודל.
- LC-LLMs: מוגבלת על ידי מורכבות ה-Attention; מוגבלת למקסימום חלון ההקשר הנוכחי.

### Row 3: עלות ויעילות
- מאפיין: עלות ויעילות
- RAG: חסכוני מאוד באמצעות אחזור סלקטיבי; משתמש במשאבים ביעילות.
- LC-LLMs: דרישות חישוביות גבוהות לעיבוד חלון ההקשר הגדול כולו בכל שאילתה.

### Row 4: התאמה לנתונים
- מאפיין: התאמה לנתונים
- RAG: מצטיין בנתונים מקוטעים, דינמיים, מיוחדים או דלילים (למשל, מאגרי קוד, דיאלוג).
- LC-LLMs: מתאים יותר להקשרים צפופים, מובנים היטב ועקביים (למשל, ספרים, מסמכים מובנים).

---

## Critical CLS Compliance Rules

### ✅ DO (Correct Usage):

1. **Column spec:** `{|m{3cm}|m{5.5cm}|m{5.5cm}|}` (all `m{}` type)
2. **Headers:** `\textbf{\hebheader{מאפיין}}` (Hebrew) or `\textbf{\enheader{RAG}}` (English)
3. **Hebrew cells:** `\hebcell{Hebrew text}`
4. **Mixed cells:** `\hebcell{Hebrew \en{English} more Hebrew}`
5. **Pure English cells:** `\encell{English text}` (if any)
6. **No spaces in \en{}:** `\en{In-Context}` not `\en{ In-Context }`
7. **Hyphens with English:** `\en{In-Context}` not `\en{In}-\en{Context}`

### ❌ DON'T (Wrong Usage):

1. ❌ `p{width}` columns (use `m{width}` only)
2. ❌ `\textenglish{}` or `\texthebrew{}` (forbidden by CLS rules)
3. ❌ Plain numbers without `\num{}` or `\en{}`
4. ❌ Spaces inside `\en{}`: `\en{ text }`
5. ❌ Mixed cell without `\hebcell{}` wrapper
6. ❌ Using `\begin{english}` for individual cells (use `\en{}` instead)

---

## Next Steps (Milestone 2.2)

1. ✅ Table structure analyzed
2. ✅ CLS functions documented
3. ✅ Column widths determined
4. ⏳ **NEXT:** Create `chapters/table_test.tex` with complete table
5. ⏳ Test compilation: `lualatex main.tex`
6. ⏳ Verify rendering: Check RTL column order, Hebrew alignment, English inline
7. ⏳ Fix any issues before integrating into Chapter 9

---

## Test Table Template (Ready to Code)

```latex
\begin{hebrewtable}[H]
\caption{השוואה: \en{RAG} לעומת \en{Long Context LLMs}}
\centering
\begin{rtltabular}{|m{3cm}|m{5.5cm}|m{5.5cm}|}
\hline
\textbf{\hebheader{מאפיין}} &
\textbf{\enheader{Retrieval-Augmented Generation (RAG)}} &
\textbf{\enheader{Long Context LLMs (LC-LLMs)}} \\
\hline
% Row 1: מקור ידע
\hebcell{מקור ידע} &
\hebcell{לא-פרמטרי, חיצוני, נתונים דינמיים (מסד נתונים וקטורי/גרף).} &
\hebcell{פרמטרי (משקולות מאומנות) + חלון הקשר גדול (נתוני \en{In-Context}).} \\
\hline
% ... more rows ...
\end{rtltabular}
\end{hebrewtable}
```

---

**Analysis Status:** ✅ COMPLETE
**Milestone 2.1:** COMPLETE
**Ready for Milestone 2.2:** Create test file

**Completion Date:** October 20, 2025
