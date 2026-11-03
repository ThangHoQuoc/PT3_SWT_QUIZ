# ÔN THI SWT301 - PROGRESS TEST 3 & FINAL EXAM (ĐẠI HỌC FPT)
## NGÂN HÀNG 300 CÂU HỎI TRẮC NGHIỆM CHUẨN SEB (ISTQB CTFL 4TH EDITION)

Tài liệu ôn thi toàn diện môn **SWT301 (Software Testing)** bám sát 100% giáo trình tham khảo:
📖 **Foundations of Software Testing: ISTQB Certification (4th Edition)** - *Rex Black, Dorothy Graham, Erik van Veenendaal*.

---

### 🌟 TÍNH NĂNG NỔI BẬT

1. **Ứng dụng Web Quiz thực hành (`quiz_practice.html`):**
   - Mở trực tiếp trên mọi trình duyệt (Chrome, Edge, Cốc Cốc, Safari) mà không cần cài đặt server.
   - Hỗ trợ **Phím tắt điều hướng nhanh**:
     * ➡ **Mũi tên phải**: Chuyển ngay sang câu tiếp theo.
     * ⬅ **Mũi tên trái**: Quay lại câu trước đó.
     * **Enter**: Kiểm tra đáp án ngay lập tức (không cần dùng chuột). Nếu đã trả lời xong, bấm Enter sẽ tự động chuyển sang câu tiếp theo.
     * **Phím A, B, C, D (hoặc 1, 2, 3, 4)**: Chọn nhanh đáp án tương ứng.
   - Chế độ chấm điểm tức thì, lọc theo từng chương hoặc trọng tâm PT3 (180 câu), hỗ trợ Dark/Light Mode.

2. **Tài liệu Markdown chuẩn hóa:**
   - **`PT3_Targeted_Review_Ch4_5_6.md`**: 180 câu hỏi trọng tâm cho Progress Test 3 (Chapters 4, 5, 6) kèm Bảng công thức vàng (Cheat Sheet) cho các bài toán tính toán biên, độ phủ dòng lệnh/nhánh, Cyclomatic complexity, Decision table và rủi ro.
   - **`SWT301_Full_Question_Bank_300.md`**: Trọn bộ 300 câu hỏi 6 chương có thẻ ẩn/hiện đáp án và lời giải chi tiết.
   - **`Final_Exam_Comprehensive_Mock.md`**: Đề thi thử Final Exam 60 câu / 60 phút mô phỏng chính xác cấu trúc thi SEB/EOS của Đại học FPT kèm phiếu đáp án ở cuối.
   - **`questions.json`**: Dữ liệu có cấu trúc để import vào Quizlet/Anki.

---

### 📂 CẤU TRÚC THƯ MỤC REPOSITORY

```text
├── quiz_practice.html              # Ứng dụng Web Quiz 300 câu (có phím tắt Enter, Mũi tên, A/B/C/D)
├── PT3_Targeted_Review_Ch4_5_6.md   # Tài liệu trọng tâm ôn Progress Test 3 (180 câu + Cheat Sheet)
├── SWT301_Full_Question_Bank_300.md # Ngân hàng 300 câu hỏi toàn bộ 6 chương (kèm lời giải chi tiết)
├── Final_Exam_Comprehensive_Mock.md # Đề thi thử Final Exam chuẩn SEB (60 câu / 60 phút)
├── questions.json                  # File dữ liệu JSON chuẩn hóa
├── build_all.py                    # Script Python tự động sinh toàn bộ tài liệu & web app
├── data_ch1.py -> data_ch6.py      # Dữ liệu 6 chương theo ISTQB CTFL 4th Edition
└── data_extra50.py                 # Dữ liệu 50 câu hỏi nâng cao & bài tập kịch bản
```

---

### 📊 PHÂN BỔ 300 CÂU HỎI THEO CHƯƠNG

* **Chương 1: Fundamentals of Testing (40 câu):** 7 nguyên lý kiểm thử, phân biệt Error - Defect - Failure, quy trình kiểm thử.
* **Chương 2: Testing Throughout the SDLC (40 câu):** V-model, Agile, các cấp độ Unit/Integration/System/Acceptance, Regression testing.
* **Chương 3: Static Testing (40 câu):** Static vs Dynamic, quy trình Review, phân biệt Inspection - Walkthrough - Technical Review.
* **Chương 4: Test Analysis and Design (85 câu):** Bài tập tính toán BVA 2-value/3-value, Equivalence Partitioning, Decision Table, State Transition, Statement & Decision Coverage, Cyclomatic Complexity $V(G)$.
* **Chương 5: Test Management & Risk (55 câu):** Quản lý rủi ro $\text{Risk} = \text{Likelihood} \times \text{Impact}$, Test Plan IEEE 829, ước lượng Wideband Delphi, vòng đời Defect.
* **Chương 6: Tool Support for Testing (40 câu):** Phân loại tool, Data-driven vs Keyword-driven, rủi ro automation, mục tiêu Pilot project.

---

Chúc các bạn ôn tập tốt và đạt điểm số tối đa trong kỳ thi môn SWT301!
