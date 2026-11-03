# build_all.py - Generates all learning materials for 300 questions with keyboard navigation

import os
import json
import data_ch1
import data_ch2
import data_ch3
import data_ch4
import data_ch5
import data_ch6
import data_extra50

BASE_DIR = r"C:\Users\ASUS\.gemini\antigravity\scratch\SWT301_Exam_Preparation"

all_questions = (
    data_ch1.CH1_QUESTIONS +
    data_ch2.CH2_QUESTIONS +
    data_ch3.CH3_QUESTIONS +
    data_ch4.CH4_QUESTIONS +
    data_ch5.CH5_QUESTIONS +
    data_ch6.CH6_QUESTIONS +
    data_extra50.EXTRA_50_QUESTIONS
)

print(f"Loaded {len(all_questions)} questions in total.")

# 1. Save questions.json
json_path = os.path.join(BASE_DIR, "questions.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)
print(f"Saved: {json_path}")

# 2. Build SWT301_Full_Question_Bank_300.md
md_300_path = os.path.join(BASE_DIR, "SWT301_Full_Question_Bank_300.md")

chapters = [
    ("Chapter 1: Fundamentals of Testing", [q for q in all_questions if q["chapter"].startswith("Chapter 1")]),
    ("Chapter 2: Testing Throughout the SDLC", [q for q in all_questions if q["chapter"].startswith("Chapter 2")]),
    ("Chapter 3: Static Testing", [q for q in all_questions if q["chapter"].startswith("Chapter 3")]),
    ("Chapter 4: Test Analysis and Design (Dynamic Techniques)", [q for q in all_questions if q["chapter"].startswith("Chapter 4")]),
    ("Chapter 5: Test Management", [q for q in all_questions if q["chapter"].startswith("Chapter 5")]),
    ("Chapter 6: Tool Support for Testing", [q for q in all_questions if q["chapter"].startswith("Chapter 6")]),
]

full_md_lines = [
    "# TÀI LIỆU ÔN TẬP TOÀN DIỆN MÔN SWT301 (SOFTWARE TESTING) - FPT UNIVERSITY",
    "## NGUỒN TÀI LIỆU CHUẨN: Foundations of Software Testing: ISTQB Certification (4th Edition)",
    "### DÀNH CHO: QUIZ, PROGRESS TEST 3 VÀ FINAL EXAM (SEB / EOS FORMAT) - TRỌN BỘ 300 CÂU HỎI",
    "",
    "> **Mục tiêu bộ tài liệu:** Cung cấp ngân hàng trọn vẹn 300 câu hỏi trắc nghiệm chuẩn hóa (ABCD, ABCDE, Multiple-select và Scenario tính toán) bám sát tuyệt đối 6 chương của giáo trình *Foundations of Software Testing 4th Edition* và cấu trúc đề thi SEB tại Đại học FPT. Mỗi câu hỏi đều có giải thích chi tiết bằng tiếng Việt kết hợp thuật ngữ chuẩn ISTQB tiếng Anh.",
    "",
    "---",
    "",
    "## MỤC LỤC BỘ 300 CÂU HỎI",
]

for ch_title, ch_qs in chapters:
    full_md_lines.append(f"- **{ch_title}:** {len(ch_qs)} câu hỏi (Từ `{ch_qs[0]['id']}` đến `{ch_qs[-1]['id']}`)")

full_md_lines.extend([
    "",
    "---",
    ""
])

for ch_title, ch_qs in chapters:
    full_md_lines.append(f"## {ch_title.upper()}")
    full_md_lines.append(f"*Tổng số: {len(ch_qs)} câu hỏi (Từ {ch_qs[0]['id']} đến {ch_qs[-1]['id']})*")
    full_md_lines.append("")
    
    for q in ch_qs:
        full_md_lines.append(f"### {q['id']}. [{q['topic']}] ({'Chọn nhiều đáp án' if q['type'] == 'Multiple' else 'Chọn 1 đáp án đúng'})")
        full_md_lines.append("")
        full_md_lines.append(q["question"])
        full_md_lines.append("")
        for opt in q["options"]:
            full_md_lines.append(f"- **{opt[:2]}** {opt[3:]}")
        full_md_lines.append("")
        full_md_lines.append("<details>")
        full_md_lines.append(f"<summary>👉 <b>Xem đáp án & giải thích chi tiết ({q['id']})</b></summary>")
        full_md_lines.append("")
        full_md_lines.append(f"- **ĐÁP ÁN ĐÚNG:** `{q['answer']}`")
        full_md_lines.append(f"- **GIẢI THÍCH:** {q['explanation']}")
        full_md_lines.append("</details>")
        full_md_lines.append("")
        full_md_lines.append("---")
        full_md_lines.append("")

with open(md_300_path, "w", encoding="utf-8") as f:
    f.write("\n".join(full_md_lines))
print(f"Saved: {md_300_path}")

md_250_path = os.path.join(BASE_DIR, "SWT301_Full_Question_Bank_250.md")
with open(md_250_path, "w", encoding="utf-8") as f:
    f.write("\n".join(full_md_lines))
print(f"Updated: {md_250_path}")

# 3. Build PT3_Targeted_Review_Ch4_5_6.md (180 Questions!)
pt3_path = os.path.join(BASE_DIR, "PT3_Targeted_Review_Ch4_5_6.md")
pt3_qs = [q for q in all_questions if q["chapter"].startswith(("Chapter 4", "Chapter 5", "Chapter 6"))]

pt3_lines = [
    "# TRỌNG TÂM ÔN THI PROGRESS TEST 3 (PT3) - MÔN SWT301",
    "## PHẠM VI TRỌNG TÂM: CHAPTER 4 (TECHNIQUES) + CHAPTER 5 (MANAGEMENT) + CHAPTER 6 (TOOLS)",
    f"### TỔNG SỐ: {len(pt3_qs)} CÂU HỎI CHUYÊN SÂU (BÀI TẬP TÍNH TOÁN, ĐỘ PHỦ, RỦI RO, TOOL AUTOMATION)",
    "",
    "> **Lưu ý đặc biệt cho PT3:** Đề thi Progress Test 3 thường có tỷ trọng câu hỏi bài tập tính toán và áp dụng rất cao, đặc biệt là các dạng:",
    "> 1. **Equivalence Partitioning & Boundary Value Analysis (2-value vs 3-value):** Xác định số phân vùng, các giá trị biên (số nguyên, số thực, ngày tháng), và số test case tối thiểu không bị error masking.",
    "> 2. **Decision Table Testing:** Đếm số quy tắc 2^N, rút gọn bảng (collapsing rules với '-') và suy ra số test case tối thiểu.",
    "> 3. **State Transition Testing:** Tính độ bao phủ 0-switch (1-transition coverage), 1-switch coverage, nhận biết invalid transitions.",
    "> 4. **White-box Statement & Decision Coverage:** Tính số test case tối thiểu để đạt 100% Statement / Decision coverage cho các đoạn code if-else, while, switch; tính Cyclomatic Complexity V(G) = E - N + 2P = P + 1.",
    "> 5. **Risk Analysis:** Tính mức độ rủi ro Risk Level = Likelihood * Impact và thứ tự ưu tiên kiểm thử.",
    "> 6. **Defect Management & Review / Tools:** Phân biệt Severity vs Priority, trạng thái bug lifecycle, mục tiêu của Pilot Project và các rủi ro của Test Automation.",
    "",
    "---",
    "",
    "## BẢNG CÔNG THỨC VÀ QUY TẮC VÀNG CHO BÀI TẬP TÍNH TOÁN (CHEAT SHEET)",
    "",
    "| Kỹ thuật / Chỉ số | Công thức / Quy tắc tính nhanh | Ví dụ kinh điển trong đề thi |",
    "| :--- | :--- | :--- |",
    "| **2-value BVA (cho đoạn [min, max])** | Mỗi biên có 2 điểm: {min-1, min} và {max, max+1} | Miền [1, 50] -> Điểm biên là: 0, 1, 50, 51 |",
    "| **3-value BVA (cho đoạn [min, max])** | Mỗi biên có 3 điểm: {min-1, min, min+1} và {max-1, max, max+1} | Miền [1, 50] -> Điểm biên là: 0, 1, 2, 49, 50, 51 |",
    "| **Số cột Decision Table đầy đủ** | $2^N$ với $N$ là số điều kiện nhị phân độc lập (True/False) | 3 điều kiện nhị phân -> $2^3 = 8$ rules (cột) |",
    "| **0-switch Transition Coverage** | $(\\text{Số transition đã test} / \\text{Tổng số valid transition}) \\times 100\\%$ | Có 6 transition, đã chạy 5 transition -> Coverage = 83.33% |",
    "| **Statement Coverage** | $(\\text{Số statement đã chạy} / \\text{Tổng số executable statement}) \\times 100\\%$ | `if (x>10) print('Hi')`: x=15 bao phủ 100% statement (1 test case) |",
    "| **Decision / Branch Coverage** | $(\\text{Số decision outcomes đã chạy} / \\text{Tổng số outcomes}) \\times 100\\%$ | Cần chạy cả nhánh True và False (tối thiểu 2 test cases cho 1 if) |",
    "| **Mối quan hệ Statement & Decision** | 100% Decision Coverage $\\implies$ 100% Statement Coverage. Chiều ngược lại **KHÔNG ĐÚNG** | 100% Statement có thể chỉ đạt 50% Decision coverage nếu chỉ có nhánh True |",
    "| **Cyclomatic Complexity $V(G)$** | 1. $V(G) = E - N + 2P$<br>2. $V(G) = P + 1$ ($P$ là số decision nodes)<br>3. $V(G) = \\text{Miền kín} + 1$ | 3 câu lệnh if độc lập -> $P=3 \\implies V(G) = 3 + 1 = 4$ |",
    "| **Risk Level (Mức độ rủi ro)** | $\\text{Risk Level} = \\text{Likelihood} \\times \\text{Impact}$ | Likelihood = 4, Impact = 5 -> Risk = 20 (ưu tiên test trước) |",
    "| **Defect Density** | $\\text{Defect Density} = \\text{Số lỗi} / \\text{Quy mô (KLOC / FPs)}$ | 50 lỗi trong 10.000 dòng code -> 5 lỗi / KLOC |",
    "",
    "---",
    "",
    f"## NGÂN HÀNG {len(pt3_qs)} CÂU HỎI LUYỆN TẬP CHUYÊN SÂU CHO PT3 (Từ {pt3_qs[0]['id']} đến {pt3_qs[-1]['id']})",
    ""
]

for q in pt3_qs:
    pt3_lines.append(f"### {q['id']}. [{q['chapter']} - {q['topic']}] ({'Chọn nhiều đáp án' if q['type'] == 'Multiple' else 'Chọn 1 đáp án đúng'})")
    pt3_lines.append("")
    pt3_lines.append(q["question"])
    pt3_lines.append("")
    for opt in q["options"]:
        pt3_lines.append(f"- **{opt[:2]}** {opt[3:]}")
    pt3_lines.append("")
    pt3_lines.append("<details>")
    pt3_lines.append(f"<summary>👉 <b>Xem đáp án & giải thích ({q['id']})</b></summary>")
    pt3_lines.append("")
    pt3_lines.append(f"- **ĐÁP ÁN ĐÚNG:** `{q['answer']}`")
    pt3_lines.append(f"- **GIẢI THÍCH:** {q['explanation']}")
    pt3_lines.append("</details>")
    pt3_lines.append("")
    pt3_lines.append("---")
    pt3_lines.append("")

with open(pt3_path, "w", encoding="utf-8") as f:
    f.write("\n".join(pt3_lines))
print(f"Saved: {pt3_path}")

# 4. Build quiz_practice.html with full keyboard navigation (Arrows, Enter, A/B/C/D)
html_path = os.path.join(BASE_DIR, "quiz_practice.html")
questions_json_str = json.dumps(all_questions, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SWT301 Exam Practice - FPT University (ISTQB CTFL 4th Ed) - 300 Questions</title>
    <style>
        :root {{
            --bg-color: #f8fafc;
            --card-bg: #ffffff;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --primary: #2563eb;
            --primary-hover: #1d4ed8;
            --success: #16a34a;
            --danger: #dc2626;
            --warning: #d97706;
            --border: #e2e8f0;
            --code-bg: #f1f5f9;
        }}
        [data-theme="dark"] {{
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --primary: #3b82f6;
            --primary-hover: #60a5fa;
            --border: #334155;
            --code-bg: #090d16;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            line-height: 1.6;
            padding: 20px;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
        }}
        header {{
            background: var(--card-bg);
            padding: 24px;
            border-radius: 12px;
            border: 1px solid var(--border);
            margin-bottom: 20px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        }}
        .header-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
        }}
        h1 {{ font-size: 1.5rem; color: var(--primary); }}
        .badge {{
            background: #dbeafe;
            color: #1e40af;
            padding: 4px 10px;
            border-radius: 9999px;
            font-size: 0.85rem;
            font-weight: 600;
        }}
        .controls {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 16px;
            align-items: center;
        }}
        select, button {{
            padding: 8px 14px;
            border-radius: 8px;
            border: 1px solid var(--border);
            background: var(--card-bg);
            color: var(--text-main);
            font-size: 0.9rem;
            cursor: pointer;
            transition: all 0.2s;
        }}
        button.primary {{
            background: var(--primary);
            color: white;
            border: none;
            font-weight: 600;
        }}
        button.primary:hover {{ background: var(--primary-hover); }}
        .shortcuts-bar {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            align-items: center;
            margin-top: 14px;
            font-size: 0.82rem;
            color: var(--text-muted);
            background: var(--code-bg);
            padding: 8px 14px;
            border-radius: 8px;
            border: 1px dashed var(--border);
        }}
        .kbd {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 4px;
            padding: 2px 6px;
            font-family: monospace;
            font-weight: 700;
            color: var(--primary);
            box-shadow: 0 1px 1px rgba(0,0,0,0.1);
        }}
        .stats-bar {{
            display: flex;
            justify-content: space-between;
            background: var(--code-bg);
            padding: 12px 18px;
            border-radius: 8px;
            margin: 16px 0;
            font-size: 0.9rem;
            font-weight: 500;
        }}
        .card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.03);
        }}
        .q-meta {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 12px;
            font-size: 0.85rem;
            color: var(--text-muted);
        }}
        .q-text {{
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 18px;
            white-space: pre-wrap;
        }}
        pre {{
            background: var(--code-bg);
            padding: 12px;
            border-radius: 6px;
            overflow-x: auto;
            font-size: 0.9rem;
            margin: 10px 0;
            border: 1px solid var(--border);
        }}
        .options {{
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 20px;
        }}
        .opt-btn {{
            display: flex;
            align-items: flex-start;
            gap: 12px;
            padding: 12px 16px;
            border: 1px solid var(--border);
            border-radius: 8px;
            background: var(--card-bg);
            cursor: pointer;
            text-align: left;
            font-size: 0.95rem;
            transition: all 0.15s;
        }}
        .opt-btn:hover:not(.disabled) {{
            border-color: var(--primary);
            background: #eff6ff;
        }}
        .opt-btn.selected {{
            border-color: var(--primary);
            background: #dbeafe;
            font-weight: 600;
        }}
        .opt-btn.correct {{
            border-color: var(--success) !important;
            background: #dcfce7 !important;
            color: #14532d !important;
            font-weight: 600;
        }}
        .opt-btn.incorrect {{
            border-color: var(--danger) !important;
            background: #fee2e2 !important;
            color: #7f1d1d !important;
        }}
        .explanation-box {{
            display: none;
            background: #f0fdf4;
            border-left: 4px solid var(--success);
            padding: 16px;
            border-radius: 6px;
            margin-top: 16px;
            font-size: 0.92rem;
            color: #166534;
        }}
        [data-theme="dark"] .explanation-box {{
            background: #064e3b;
            color: #a7f3d0;
        }}
        .nav-buttons {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 24px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="header-top">
                <div>
                    <h1>SWT301 Quiz & Exam Practice (300 Questions)</h1>
                    <p style="color: var(--text-muted); font-size: 0.9rem;">FPT University | ISTQB Foundation 4th Edition</p>
                </div>
                <div style="display: flex; gap: 8px; align-items: center;">
                    <span class="badge" id="exam-badge">Full 300 Questions</span>
                    <button id="theme-btn" onclick="toggleTheme()">🌓 Dark/Light</button>
                </div>
            </div>
            <div class="controls">
                <label><b>Lọc theo phạm vi:</b></label>
                <select id="chapter-filter" onchange="filterQuestions()">
                    <option value="ALL">Toàn bộ 300 câu hỏi (Chương 1 - 6)</option>
                    <option value="PT3" selected>Trọng tâm Progress Test 3 (Chương 4, 5, 6: 180 câu)</option>
                    <option value="CH1">Chương 1: Fundamentals of Testing (40 câu)</option>
                    <option value="CH2">Chương 2: Testing Throughout SDLC (40 câu)</option>
                    <option value="CH3">Chương 3: Static Testing (40 câu)</option>
                    <option value="CH4">Chương 4: Test Techniques & Coverage (85 câu)</option>
                    <option value="CH5">Chương 5: Test Management & Risk (55 câu)</option>
                    <option value="CH6">Chương 6: Tool Support for Testing (40 câu)</option>
                    <option value="MOCK60">Mô phỏng Final Exam 60 phút (60 câu chuẩn SEB)</option>
                </select>
                <button onclick="resetPractice()">Làm lại từ đầu</button>
            </div>
            <div class="shortcuts-bar">
                <span>⚡ <b>Phím tắt:</b></span>
                <span><span class="kbd">➡ Mũi tên phải</span>: Câu tiếp</span>
                <span><span class="kbd">⬅ Mũi tên trái</span>: Câu trước</span>
                <span><span class="kbd">Enter</span>: Kiểm tra đáp án</span>
                <span><span class="kbd">A</span> <span class="kbd">B</span> <span class="kbd">C</span> <span class="kbd">D</span>: Chọn đáp án</span>
            </div>
        </header>

        <div class="stats-bar">
            <div>Câu hỏi: <span id="q-idx" style="font-weight: 700; color: var(--primary);">1</span> / <span id="q-total">180</span></div>
            <div>Đúng: <span id="score-correct" style="color: var(--success); font-weight: 700;">0</span></div>
            <div>Sai: <span id="score-wrong" style="color: var(--danger); font-weight: 700;">0</span></div>
            <div>Tỷ lệ: <span id="score-pct" style="font-weight: 700;">0%</span></div>
        </div>

        <div class="card" id="question-card">
            <div class="q-meta">
                <span id="q-chapter">Chapter 4</span>
                <span id="q-type" class="badge">Single Choice</span>
            </div>
            <div class="q-text" id="q-text">Đang tải câu hỏi...</div>
            <div class="options" id="options-container"></div>
            
            <div style="display: flex; gap: 10px; margin-top: 10px;">
                <button id="submit-btn" class="primary" onclick="submitAnswer()">Kiểm tra đáp án (Enter)</button>
                <button id="hint-btn" onclick="toggleExplanation()">Xem giải thích</button>
            </div>

            <div class="explanation-box" id="explanation-box">
                <b>ĐÁP ÁN: <span id="correct-ans-label"></span></b>
                <p id="explanation-text" style="margin-top: 6px;"></p>
            </div>
        </div>

        <div class="nav-buttons">
            <button onclick="prevQuestion()">⬅ Câu trước (Phím ⬅)</button>
            <button onclick="nextQuestion()" class="primary">Câu tiếp theo ➡ (Phím ➡)</button>
        </div>
    </div>

    <script>
        const rawQuestions = {questions_json_str};
        let activeQuestions = [];
        let currentIndex = 0;
        let selectedOptions = new Set();
        let userAnswers = {{}};
        let correctCount = 0;
        let wrongCount = 0;

        function init() {{
            filterQuestions();
            setupKeyboardNavigation();
        }}

        function setupKeyboardNavigation() {{
            document.addEventListener('keydown', function(e) {{
                // Do not trigger shortcuts if user is focusing a select or form input
                if (e.target.tagName === 'SELECT' || e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {{
                    return;
                }}

                if (e.key === 'ArrowRight') {{
                    e.preventDefault();
                    nextQuestion();
                }} else if (e.key === 'ArrowLeft') {{
                    e.preventDefault();
                    prevQuestion();
                }} else if (e.key === 'Enter') {{
                    e.preventDefault();
                    const q = activeQuestions[currentIndex];
                    if (!userAnswers[q.id]) {{
                        submitAnswer();
                    }} else {{
                        nextQuestion();
                    }}
                }} else if (['a', 'A', '1'].includes(e.key)) {{
                    selectOption('A', activeQuestions[currentIndex].type === 'Multiple');
                }} else if (['b', 'B', '2'].includes(e.key)) {{
                    selectOption('B', activeQuestions[currentIndex].type === 'Multiple');
                }} else if (['c', 'C', '3'].includes(e.key)) {{
                    selectOption('C', activeQuestions[currentIndex].type === 'Multiple');
                }} else if (['d', 'D', '4'].includes(e.key)) {{
                    selectOption('D', activeQuestions[currentIndex].type === 'Multiple');
                }} else if (['e', 'E', '5'].includes(e.key)) {{
                    selectOption('E', activeQuestions[currentIndex].type === 'Multiple');
                }}
            }});
        }}

        function toggleTheme() {{
            const isDark = document.body.getAttribute('data-theme') === 'dark';
            document.body.setAttribute('data-theme', isDark ? 'light' : 'dark');
        }}

        function filterQuestions() {{
            const val = document.getElementById('chapter-filter').value;
            if (val === 'ALL') {{
                activeQuestions = [...rawQuestions];
            }} else if (val === 'PT3') {{
                activeQuestions = rawQuestions.filter(q => q.chapter.startsWith('Chapter 4') || q.chapter.startsWith('Chapter 5') || q.chapter.startsWith('Chapter 6'));
            }} else if (val === 'CH1') {{
                activeQuestions = rawQuestions.filter(q => q.chapter.startsWith('Chapter 1'));
            }} else if (val === 'CH2') {{
                activeQuestions = rawQuestions.filter(q => q.chapter.startsWith('Chapter 2'));
            }} else if (val === 'CH3') {{
                activeQuestions = rawQuestions.filter(q => q.chapter.startsWith('Chapter 3'));
            }} else if (val === 'CH4') {{
                activeQuestions = rawQuestions.filter(q => q.chapter.startsWith('Chapter 4'));
            }} else if (val === 'CH5') {{
                activeQuestions = rawQuestions.filter(q => q.chapter.startsWith('Chapter 5'));
            }} else if (val === 'CH6') {{
                activeQuestions = rawQuestions.filter(q => q.chapter.startsWith('Chapter 6'));
            }} else if (val === 'MOCK60') {{
                // 60 representative questions
                activeQuestions = rawQuestions.filter((q, idx) => idx % 5 === 0).slice(0, 60);
            }}
            currentIndex = 0;
            userAnswers = {{}};
            correctCount = 0;
            wrongCount = 0;
            updateStats();
            renderQuestion();
        }}

        function renderQuestion() {{
            if (activeQuestions.length === 0) return;
            const q = activeQuestions[currentIndex];
            document.getElementById('q-idx').innerText = currentIndex + 1;
            document.getElementById('q-total').innerText = activeQuestions.length;
            document.getElementById('q-chapter').innerText = q.id + " | " + q.chapter + " - " + q.topic;
            document.getElementById('q-type').innerText = q.type === 'Multiple' ? 'Chọn nhiều đáp án' : 'Chọn 1 đáp án';
            document.getElementById('q-text').innerText = q.question;

            selectedOptions.clear();
            const container = document.getElementById('options-container');
            container.innerHTML = '';

            const expBox = document.getElementById('explanation-box');
            expBox.style.display = 'none';

            q.options.forEach(opt => {{
                const letter = opt.substring(0, 1);
                const btn = document.createElement('div');
                btn.className = 'opt-btn';
                btn.id = 'opt-' + letter;
                btn.innerHTML = '<b>' + letter + '.</b> <span>' + opt.substring(3) + '</span>';
                btn.onclick = () => selectOption(letter, q.type === 'Multiple');
                container.appendChild(btn);
            }});

            // Check if already answered
            if (userAnswers[q.id]) {{
                showAnswerResults(userAnswers[q.id]);
            }}
        }}

        function selectOption(letter, isMultiple) {{
            const q = activeQuestions[currentIndex];
            if (userAnswers[q.id]) return; // already submitted

            if (!isMultiple) {{
                selectedOptions.clear();
                selectedOptions.add(letter);
            }} else {{
                if (selectedOptions.has(letter)) selectedOptions.delete(letter);
                else selectedOptions.add(letter);
            }}

            const qOptions = q.options.map(o => o.substring(0, 1));
            qOptions.forEach(l => {{
                const el = document.getElementById('opt-' + l);
                if (el) {{
                    if (selectedOptions.has(l)) el.classList.add('selected');
                    else el.classList.remove('selected');
                }}
            }});
        }}

        function submitAnswer() {{
            const q = activeQuestions[currentIndex];
            if (userAnswers[q.id]) return; // already submitted
            if (selectedOptions.size === 0) {{
                alert('Vui lòng chọn ít nhất một đáp án trước khi bấm Enter hoặc kiểm tra!');
                return;
            }}
            const chosen = Array.from(selectedOptions).sort().join(', ');
            userAnswers[q.id] = chosen;
            showAnswerResults(chosen);

            const isCorrect = chosen.replace(/\\s/g, '') === q.answer.replace(/\\s/g, '');
            if (isCorrect) correctCount++;
            else wrongCount++;
            updateStats();
        }}

        function showAnswerResults(chosen) {{
            const q = activeQuestions[currentIndex];
            const correctSet = new Set(q.answer.split(',').map(s => s.trim()));
            const chosenSet = new Set(chosen.split(',').map(s => s.trim()));

            q.options.map(o => o.substring(0, 1)).forEach(l => {{
                const el = document.getElementById('opt-' + l);
                if (!el) return;
                el.classList.add('disabled');
                if (correctSet.has(l)) {{
                    el.classList.add('correct');
                }} else if (chosenSet.has(l)) {{
                    el.classList.add('incorrect');
                }}
            }});

            document.getElementById('correct-ans-label').innerText = q.answer;
            document.getElementById('explanation-text').innerText = q.explanation;
            document.getElementById('explanation-box').style.display = 'block';
        }}

        function toggleExplanation() {{
            const q = activeQuestions[currentIndex];
            document.getElementById('correct-ans-label').innerText = q.answer;
            document.getElementById('explanation-text').innerText = q.explanation;
            const exp = document.getElementById('explanation-box');
            exp.style.display = exp.style.display === 'block' ? 'none' : 'block';
        }}

        function updateStats() {{
            document.getElementById('score-correct').innerText = correctCount;
            document.getElementById('score-wrong').innerText = wrongCount;
            const totalAnswered = correctCount + wrongCount;
            const pct = totalAnswered > 0 ? Math.round((correctCount / totalAnswered) * 100) : 0;
            document.getElementById('score-pct').innerText = pct + '%';
        }}

        function prevQuestion() {{
            if (currentIndex > 0) {{
                currentIndex--;
                renderQuestion();
            }}
        }}

        function nextQuestion() {{
            if (currentIndex < activeQuestions.length - 1) {{
                currentIndex++;
                renderQuestion();
            }}
        }}

        function resetPractice() {{
            if (confirm('Bạn có chắc muốn làm lại từ câu số 1 không?')) {{
                filterQuestions();
            }}
        }}

        window.onload = init;
    </script>
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Saved: {html_path}")
print("BUILD COMPLETED WITH KEYBOARD NAVIGATION!")
