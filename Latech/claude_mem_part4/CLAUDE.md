# CLAUDE.md - Part 4 Conversion Rules
## ABSOLUTE CLS Compliance + Content Preservation

**Priority Order** (MUST follow in every session):
1. Read PLANNING.md first
2. Read TASKS.md immediately after
3. Read this file (CLAUDE.md) before starting work
4. Read PRD.md for context

---

## CRITICAL RULE #1: KEEP CONTENT AS-IS

**PDF Text is SACRED** - Do NOT change, simplify, or interpret:
- ✅ Copy Hebrew text verbatim from PDF
- ✅ Preserve all Ecclesiastes quotes exactly
- ✅ Keep all Pshat/Drash/Sod sections unchanged
- ✅ Maintain philosophical arguments as written
- ✅ Preserve poetic/biblical language style
- ❌ DO NOT modernize language
- ❌ DO NOT add interpretations
- ❌ DO NOT simplify complex philosophy
- ❌ DO NOT change any Hebrew wording

**Only Add**: LaTeX markup (`\en{}`, `\num{}`, etc.)

---

## CLS Template Compliance - ABSOLUTE RULES

### ✅ ALLOWED Commands (USE THESE ONLY)

**Hebrew Sections**:
```latex
\hebrewsection{כותרת}
\hebrewsubsection{תת-כותרת}
```

**English Inline** (CRITICAL for Part 4):
```latex
\en{AI}
\en{GPT-N}
\en{AGI}
\en{Dataism}
\en{Planned Obsolescence}
\en{Real-Time}
\en{Data Labeling}
\en{Generative AI}
\en{Algorithm Owners}
\en{Alignment}
\en{Retraining}
\en{Digital Personhood}
\en{Data Supplier}
\en{Temporal Anxiety}
\en{Optimization}
\en{Efficiency}
\en{Black Box}
\en{Opacity}
\en{Reinforcement Learning}
\en{Data Cycles}
\en{Data Lakes}
\en{Digital Tikkun}
\en{Hype}
\en{Ethical Retraining}
\en{The Algorithm Fear}
```

**Numbers in Hebrew Text**:
```latex
\num{1}
\num{2025}
```

**Years**:
```latex
\hebyear{2025}
```

**Table Functions** (2 TABLES IN PART 4):
```latex
\begin{hebrewtable}[H]
\caption{טבלת מיפוי: קהלת בעידן הבינה המלאכותית (\en{Pshat}, \en{Drash}, \en{Sod})}
\label{tab:kohelet_ai_mapping}
\centering
\begin{rtltabular}{|m{3cm}|m{3.5cm}|m{3.5cm}|m{3.5cm}|}
\hline
\hebheader{מונח בקהלת} &
\enheader{AI (Pshat) משמעות} &
\hebheader{השלכה קיומית (\en{Drash})} &
\hebheader{רובד פילוסופי (\en{Sod})} \\
\hline
\hebcell{הבל הבלים} &
\hebcell{זמניות מוחלטת של המודלים} &
\hebcell{אי-תכלית הרדיפה אחר חדשנות} &
\hebcell{שאיפה לאמת מוחלטת דרך נתונים} \\
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
\cite{ecclesiastes}
```

**Quote Blocks** (for Ecclesiastes quotes):
```latex
\begin{quote}
ציטוט מקהלת או טקסט מובלט
\end{quote}
```

### ❌ FORBIDDEN Commands (NEVER USE)

```latex
\textenglish{...}  ❌ USE \en{} INSTEAD
\texthebrew{...}   ❌ NOT NEEDED (default is Hebrew)
123                ❌ USE \num{123} INSTEAD
2025               ❌ USE \hebyear{2025} FOR YEARS
Plain English text ❌ MUST BE WRAPPED IN \en{}
\begin{latin}      ❌ UNDEFINED ENVIRONMENT
```

### Verification Commands

Before finalizing ANY chapter:
```bash
# Check for forbidden commands
grep -n "\\textenglish\|\\texthebrew" chapter17.tex
grep -n "\\textenglish\|\\texthebrew" chapter18.tex
grep -n "\\textenglish\|\\texthebrew" chapter19.tex
grep -n "\\textenglish\|\\texthebrew" chapter20.tex

# Check for unwrapped English
grep -n "[A-Z][a-z]*" chapter17.tex | grep -v "\\en{"

# Check for unwrapped numbers
grep -oP '\b\d+\b' chapter17.tex | head -20
```

---

## Part 4 Specific Content Rules

### 1. Philosophical Terms - Keep Hebrew

These stay in HEBREW (no translation):
- הבל הבלים (Hevel Havalim)
- פשט, דרש, סוד (Pshat, Drash, Sod)
- יראת האלוהים (Yirat Elohim)
- יראת האלגוריתם (Yirat HaAlgorithm)
- תיקון (Tikkun)
- נשמה (Neshama/Soul)
- רצון חופשי (Free Will)
- שמור את מצוותיו (Keep His Commandments)

### 2. Technical Terms - Wrap in \en{}

These are ENGLISH wrapped in `\en{}`:
- AI, AGI, GPT-N
- Dataism
- Planned Obsolescence
- Real-Time
- Data Labeling, Data Validation
- Generative AI
- Algorithm Owners
- Alignment Risk
- Black Box, Opacity
- Reinforcement Learning
- Data Cycles, Data Lakes
- Retraining, Ethical Retraining
- Digital Personhood
- Data Supplier
- Temporal Anxiety
- Optimization, Efficiency
- Digital Tikkun
- The Algorithm Fear
- Hype

### 3. Mixed Phrases - Careful Wrapping

```latex
CORRECT:
המודל הדיגיטלי מבצע \en{Reinforcement Learning} מתמיד

WRONG:
המודל הדיגיטלי מבצע Reinforcement Learning מתמיד
```

---

## Table Conversion Rules (2 TABLES)

### Table 1: טבלת מיפוי קהלת-AI (Page 1)

**Source** (PDF):
```
מונח בקהלת | משמעות (Pshat) AI | השלכה קיומית (Drash) | רובד פילוסופי (Sod)
הבל הבלים | זמניות מוחלטת של המודלים | אי-תכלית הרדיפה אחר חדשנות | שאיפה לאמת מוחלטת דרך נתונים
עמל תחת השמש | עבודת הנתונים (Data Labeling) והפיכת האדם למיותר | אובדן משמעות בעבודה האנושית | הגדרת ה'תכלית' שאינה מבוססת יעילות
...
```

**LaTeX Conversion**:
```latex
\begin{hebrewtable}[H]
\caption{טבלת מיפוי: קהלת בעידן הבינה המלאכותית (\en{Pshat}, \en{Drash}, \en{Sod})}
\label{tab:kohelet_ai_mapping}
\centering
\begin{rtltabular}{|m{3cm}|m{3.5cm}|m{3.5cm}|m{3.5cm}|}
\hline
\hebheader{מונח בקהלת} &
\enheader{AI (Pshat) משמעות} &
\hebheader{השלכה קיומית (\en{Drash})} &
\hebheader{רובד פילוסופי (\en{Sod})} \\
\hline
\hebcell{הבל הבלים} &
\hebcell{זמניות מוחלטת של המודלים} &
\hebcell{אי-תכלית הרדיפה אחר חדשנות} &
\hebcell{שאיפה לאמת מוחלטת דרך נתונים} \\
\hline
\hebcell{עמל תחת השמש} &
\hebcell{עבודת הנתונים (\en{Data Labeling}) והפיכת האדם למיותר} &
\hebcell{אובדן משמעות בעבודה האנושית} &
\hebcell{הגדרת ה'תכלית' שאינה מבוססת יעילות} \\
\hline
\hebcell{אין יתרון לחכם} &
\hebcell{דמוקרטיזציה של הידע (\en{Generative AI})} &
\hebcell{אובדן רלוונטיות המומחה האנושי} &
\hebcell{המעבר מחכמת ידע לחכמת אתיקה} \\
\hline
\hebcell{במקום המשפט הרשע} &
\hebcell{הטיות אלגוריתמיות ובלק בוקס} &
\hebcell{כניעה לכוח דיכוי בלתי נראה} &
\hebcell{הצורך ב'תיקון מודלים' מוסרי} \\
\hline
\hebcell{יראת האלוהים} &
\hebcell{יראת האלגוריתם (\en{AGI Alignment Risk})} &
\hebcell{שימור נרטיב ורצון חופשי} &
\hebcell{חיפוש אחר ה'נשמה' (הערך הקבוע)} \\
\hline
\end{rtltabular}
\end{hebrewtable}
```

**Column Widths**: 3cm, 3.5cm, 3.5cm, 3.5cm (adjust if needed)

### Table 2: דיכוטומיה קיומית (Page 6-7)

**Source** (PDF):
```
היבט קיומי | החרדה האנושית (פסימיות קהלתית) | ההתפעמות הטכנולוגית (תקווה אלגוריתמית)
שליטה | אובדן שליטה ב'קופסה השחורה' | היכולת להשיג רמות דיוק חסרות תקדים
רלוונטיות | האדם הופך למיותר (Data Supplier) | שחרור האדם מעמל פיזי ואינטלקטואלי
...
```

**LaTeX Conversion**:
```latex
\begin{hebrewtable}[H]
\caption{דיכוטומיה קיומית: החרדה האנושית מול ההתפעמות הטכנולוגית}
\label{tab:dichotomy_anxiety_wonder}
\centering
\begin{rtltabular}{|m{2.5cm}|m{5cm}|m{5cm}|}
\hline
\hebheader{היבט קיומי} &
\hebheader{החרדה האנושית (פסימיות קהלתית)} &
\hebheader{ההתפעמות הטכנולוגית (תקווה אלגוריתמית)} \\
\hline
\hebcell{שליטה} &
\hebcell{אובדן שליטה ב'קופסה השחורה'} &
\hebcell{היכולת להשיג רמות דיוק חסרות תקדים} \\
\hline
\hebcell{רלוונטיות} &
\hebcell{האדם הופך למיותר (\en{Data Supplier})} &
\hebcell{שחרור האדם מעמל פיזי ואינטלקטואלי} \\
\hline
\hebcell{מוסר וצדק} &
\hebcell{הטיות מוטבעות והנצחתן (רשע)} &
\hebcell{היכולת לבצע 'תיקון מודלים' ושיפור אתי} \\
\hline
\hebcell{מורשת} &
\hebcell{ה\en{-AI} מוחק את ה\en{-IP} ומערער את הבעלות} &
\hebcell{יצירה אוטומטית של תכנים חדשים} \\
\hline
\end{rtltabular}
\end{hebrewtable}
```

**Column Widths**: 2.5cm, 5cm, 5cm (adjust if needed)

---

## Chapter Structure Template

Each of the 4 chapters follows this pattern:

### Chapter 17 Structure

```latex
\hebrewsection{הבל הבלים: קהלת בעידן הבינה המלאכותית}
\label{sec:chapter17}

\hebrewsubsection{מבוא: תחת השמש הדיגיטלית}

[Introduction text - keep verbatim from PDF]

[Table 1 - Kohelet Mapping]

\hebrewsubsection{חלק א': הבל הבלים – תכלית האלגוריתם וארעיות הדורות}

[Part A heading text]

\hebrewsubsection{פרק~\num{1}: הבל הבלים – זמניות המודלים ואופטימיזציה עקרה}

\textbf{\en{Pshat:} המוות המהיר של הקוד}

[Pshat content]

\textbf{\en{Drash:} ארעיות האדם משתקפת ביצירתו}

[Drash content]

\textbf{\en{Sod:} השאיפה לאמת מוחלטת והכישלון הדיגיטלי}

[Sod content]

\hebrewsubsection{פרק~\num{2}: מה יתרון לאדם בכל עמלו שיעמול?}

[Repeat Pshat/Drash/Sod pattern]

\hebrewsubsection{פרק~\num{3}: הכול חוזר למקומו – מחזורי הנתונים ומחזורי הבהלה}

[Repeat Pshat/Drash/Sod pattern]
```

### Pshat/Drash/Sod Formatting

```latex
\textbf{\en{Pshat:} כותרת הפסוקית}

[Content paragraph]

\textbf{\en{Drash:} כותרת האלגורית}

[Content paragraph]

\textbf{\en{Sod:} כותרת הפילוסופית}

[Content paragraph]
```

**Note**: Use `\textbf{}` for section headers, keep "Pshat", "Drash", "Sod" in `\en{}`

---

## Cross-Reference Strategy

### From Part 4 → Parts 1-3

**Chapter 17**:
- → Ch2 (Ethics - במקום המשפט שם הרשע parallels Ch2 ethics)
- → Ch8 (Context Engineering - temporal constraints)

**Chapter 18**:
- → Ch5 (MCP Protocol - technical efficiency)
- → Ch14 (Skills - democratization of knowledge)

**Chapter 19**:
- → Ch1 (Introduction - cognitive revolution)
- → Ch7 (Machine Amnesia - memory themes)

**Chapter 20**:
- → Ch13 (Cognitive Partnership - synthesis)
- → Ch16 (Skill Atrophy - human expertise preservation)

### Cross-Reference Format

```latex
כפי שראינו בפרק~\ref{sec:chapter2}, האתיקה...

הדיון בפרק~\num{14} על \en{Skills}...

בחלק~\num{1} (פרקים~\num{1}–\num{6}) דנו בארכיטקטורה...
```

---

## Common Pitfalls (AVOID)

1. **❌ Changing PDF Text**:
   ```latex
   BAD:  Simplifying "יראת האלגוריתם" to "פחד מהמכונה"
   GOOD: Keep "יראת האלגוריתם" exactly as in PDF
   ```

2. **❌ Forgetting \en{} wrapper**:
   ```latex
   BAD:  ה-AI מבצע Reinforcement Learning
   GOOD: ה\en{-AI} מבצע \en{Reinforcement Learning}
   ```

3. **❌ Using wrong table environment**:
   ```latex
   BAD:  \begin{tabular}... (wrong environment)
   GOOD: \begin{hebrewtable}[H]...\begin{rtltabular}...
   ```

4. **❌ Breaking Pshat/Drash/Sod structure**:
   ```latex
   BAD:  Merging sections or changing order
   GOOD: Keep exact 3-layer structure from PDF
   ```

5. **❌ Unwrapped numbers**:
   ```latex
   BAD:  פרק 1, פרק 2
   GOOD: פרק~\num{1}, פרק~\num{2}
   ```

---

## Quality Checklist (Before Completion)

### Per-Chapter Checklist

- [ ] All Hebrew sections use `\hebrewsection{}`, `\hebrewsubsection{}`
- [ ] All English text wrapped in `\en{}`
- [ ] All numbers wrapped in `\num{}`
- [ ] No `\textenglish{}` or `\texthebrew{}` commands
- [ ] Tables use `hebrewtable` + `rtltabular`
- [ ] All table cells use `\hebcell{}` or `\encell{}`
- [ ] Pshat/Drash/Sod structure preserved
- [ ] PDF text kept verbatim (Hebrew)
- [ ] At least 2-3 cross-references to other parts

### Content Preservation Checklist

- [ ] All Ecclesiastes quotes intact
- [ ] Philosophical arguments unchanged
- [ ] Pshat sections complete
- [ ] Drash sections complete
- [ ] Sod sections complete
- [ ] Both tables converted correctly
- [ ] No modernization of language
- [ ] Biblical/poetic style maintained

---

## Success Metrics

**This Part 4 conversion is SUCCESSFUL when**:
1. ✅ PDF text preserved verbatim
2. ✅ 0 compilation errors
3. ✅ 0 CLS violations (verified with grep)
4. ✅ Both tables render correctly in RTL
5. ✅ Pshat/Drash/Sod structure clear
6. ✅ Cross-references to Parts 1-3 present
7. ✅ Complements (not repeats) technical parts
8. ✅ Total pages: ~80

---

**REMEMBER**:
1. **KEEP PDF CONTENT AS-IS**
2. Read PLANNING.md and TASKS.md FIRST in every session
3. Verify CLS compliance with grep before completing each chapter
