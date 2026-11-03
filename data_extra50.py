# data_extra50.py - Additional 50 High-Yield Questions (Q251 - Q300)
# Expanding the bank to 300 questions for SWT301 (FPT University / ISTQB CTFL 4th Edition)

EXTRA_50_QUESTIONS = [
    # --- Chapter 1: Fundamentals of Testing (Q251 - Q255) ---
    {
        "id": "Q251",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.1 What is Testing?",
        "type": "Single",
        "question": "A developer runs their own code in debug mode with breakpoints to find out why a calculation outputs 0 instead of 100. Once the line is identified, the developer edits the code. Which activity is this?",
        "options": [
            "A. Dynamic Acceptance Testing",
            "B. Debugging (Locating and fixing the defect)",
            "C. Static Code Inspection",
            "D. Regression Test Execution"
        ],
        "answer": "B",
        "explanation": "Hành động đặt breakpoint, lần theo mã nguồn để tìm nguyên nhân gốc rễ và sửa code là Debugging (gỡ lỗi), một hoạt động thuộc về phát triển phần mềm, phân biệt với Testing (làm bộc lộ failure hoặc đánh giá chất lượng)."
    },
    {
        "id": "Q252",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.3 Seven Testing Principles",
        "type": "Single",
        "question": "A test manager notices that after testing for 3 weeks, new bugs are rarely found in the older modules, but when a new feature is deployed, 15 bugs appear immediately in that new module. Which principle explains why testing should focus extra effort on the new module?",
        "options": [
            "A. Defects cluster together (and Testing is context dependent)",
            "B. Absence-of-errors fallacy",
            "C. Exhaustive testing is possible on small modules",
            "D. Pesticide paradox only applies to databases"
        ],
        "answer": "A",
        "explanation": "Nguyên lý 'Defects cluster together': Các module mới hoặc có độ phức tạp cao thường tập trung phần lớn các lỗi phát sinh. Do đó tester cần phân bổ nỗ lực kiểm thử tập trung vào những cụm có mật độ lỗi cao."
    },
    {
        "id": "Q253",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.2 Why is Testing Necessary?",
        "type": "Single",
        "question": "Which of the following BEST illustrates an 'Environmental condition' causing a failure, where no software defect was present in the code itself?",
        "options": [
            "A. An off-by-one loop boundary condition.",
            "B. A solar flare induced cosmic ray flipping a memory bit in an unshielded server RAM, causing a parity error crash.",
            "C. An unhandled divide-by-zero exception in a pricing formula.",
            "D. A missing semicolon in a JavaScript function."
        ],
        "answer": "B",
        "explanation": "Tia vũ trụ gây lật bit trong thanh RAM là một điều kiện môi trường vật lý bên ngoài (environmental condition) gây ra failure, chứ không phải do lỗi trong mã nguồn phần mềm."
    },
    {
        "id": "Q254",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.4 Test Process",
        "type": "Single",
        "question": "During which activity of the test process are 'Test Charters' typically created?",
        "options": [
            "A. When planning and designing Exploratory Testing sessions.",
            "B. During automated compiler static checks.",
            "C. In formal hardware manufacturing.",
            "D. Only during contract renegotiation."
        ],
        "answer": "A",
        "explanation": "Test Charter (Hiến chương kiểm thử) được soạn thảo trong quá trình phân tích và thiết kế cho các phiên kiểm thử thăm dò (Exploratory Testing / Session-Based Test Management)."
    },
    {
        "id": "Q255",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.5 The Psychology of Testing",
        "type": "Single",
        "question": "When presenting defects to software developers, why should testers emphasize defects as neutral technical facts rather than personal mistakes?",
        "options": [
            "A. Because software developers are legally liable for fines.",
            "B. Because finding faults in someone's intellectual work can trigger defensive emotional reactions; objective communication fosters constructive collaboration.",
            "C. Because test reports are published directly in local newspapers.",
            "D. Because testers are not permitted to know developer names."
        ],
        "answer": "B",
        "explanation": "Báo cáo lỗi trung lập, khách quan, dựa trên sự thật (fact-focused) giúp loại bỏ tâm lý phòng thủ của lập trình viên, duy trì mối quan hệ hợp tác tích cực vì mục tiêu chất lượng chung."
    },

    # --- Chapter 2: Testing Throughout the SDLC (Q256 - Q260) ---
    {
        "id": "Q256",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.2 Test Levels",
        "type": "Single",
        "question": "In a continuous integration and continuous deployment (CI/CD) pipeline, automated unit and component integration tests are executed on every git commit. What is this practice called in modern software testing?",
        "options": [
            "A. Shift-Right Testing",
            "B. Continuous Testing (Shift-Left in CI/CD)",
            "C. Big Bang Waterfall Testing",
            "D. Operational Retest Phase"
        ],
        "answer": "B",
        "explanation": "Continuous Testing (Kiểm thử liên tục) trong CI/CD: Chạy các bài test tự động ngay khi có commit mới nhằm đưa việc kiểm thử về sớm nhất có thể trong chu trình phát triển (Shift-Left)."
    },
    {
        "id": "Q257",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.3 Test Types",
        "type": "Single",
        "question": "Testing an e-commerce checkout application to ensure that customer data remains confidential and resistant to unauthorized access complies with which ISO 25010 quality characteristic?",
        "options": [
            "A. Security",
            "B. Portability",
            "C. Usability",
            "D. Maintainability"
        ],
        "answer": "A",
        "explanation": "Đảm bảo tính bảo mật và quyền riêng tư của dữ liệu khách hàng chống lại các truy cập trái phép thuộc đặc tính Security (An toàn thông tin) theo tiêu chuẩn ISO/IEC 25010."
    },
    {
        "id": "Q258",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.3 Test Types",
        "type": "Single",
        "question": "What is the key difference between 'Confirmation Testing' and 'Regression Testing'?",
        "options": [
            "A. Confirmation testing tests whether a defect has been fixed; Regression testing checks whether the fix caused unintentional defects in unchanged code.",
            "B. Confirmation testing is automated; Regression testing is always manual.",
            "C. Regression testing is only done by end users; Confirmation testing is only done by developers.",
            "D. They are exact synonyms."
        ],
        "answer": "A",
        "explanation": "Confirmation testing (Re-testing) kiểm tra xem lỗi cũ đã được sửa hết chưa. Regression testing kiểm tra xem việc sửa đổi đó có vô tình làm hỏng các tính năng cũ đang chạy tốt hay không."
    },
    {
        "id": "Q259",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.2 Test Levels",
        "type": "Single",
        "question": "Which of the following is a key objective of 'Operational Acceptance Testing' (OAT)?",
        "options": [
            "A. Checking font sizes and button colors on mobile screens.",
            "B. Verifying disaster recovery, backup/restore procedures, performance monitoring, and failover capabilities.",
            "C. Verifying unit test code coverage in Java classes.",
            "D. Reviewing code formatting with Checkstyle."
        ],
        "answer": "B",
        "explanation": "Mục tiêu của OAT (Kiểm thử chấp nhận vận hành): Đảm bảo hệ thống có thể vận hành trơn tru và an toàn bởi đội ngũ SysAdmin/DevOps (kiểm tra sao lưu/phục hồi, khả năng chuyển đổi dự phòng failover, bảo mật vận hành)."
    },
    {
        "id": "Q260",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.4 Maintenance Testing",
        "type": "Single",
        "question": "When a company migrates an enterprise accounting system from an on-premise Oracle database to an AWS Aurora PostgreSQL database, what type of maintenance testing is ESSENTIAL?",
        "options": [
            "A. Testing data conversion, data integrity, and operational procedures on the new platform.",
            "B. Deleting all past financial data.",
            "C. Only testing CSS stylesheets on Android.",
            "D. Writing brand-new user stories for the old database."
        ],
        "answer": "A",
        "explanation": "Khi chuyển đổi nền tảng (Migration), kiểm thử bảo trì tập trung vào tính toàn vẹn dữ liệu (data integrity), chuyển đổi dữ liệu (data conversion), và kiểm tra hệ thống trên môi trường đích mới."
    },

    # --- Chapter 3: Static Testing (Q261 - Q265) ---
    {
        "id": "Q261",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "In a formal software inspection, what metric is typically calculated by dividing the total number of pages/lines reviewed by the total preparation time spent?",
        "options": [
            "A. Review Rate (Preparation speed / Review pace)",
            "B. Cyclomatic Density",
            "C. Defect Masking Coefficient",
            "D. Statement Branch Ratio"
        ],
        "answer": "A",
        "explanation": "Review Rate (Tốc độ review): Đo lường số trang hoặc số dòng code được xem xét trong một đơn vị thời gian (ví dụ 15 trang/giờ). Nếu tốc độ này quá nhanh, chất lượng phát hiện lỗi sẽ bị giảm sút."
    },
    {
        "id": "Q262",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.1 Static Testing Basics",
        "type": "Single",
        "question": "Which of the following statements regarding the ROI (Return on Investment) of static testing is TRUE?",
        "options": [
            "A. Static testing has negative ROI because it wastes developers' time.",
            "B. Static testing has very high ROI because discovering and fixing requirements/design defects early avoids massive rework costs during late dynamic testing or production.",
            "C. Static testing cannot reduce project costs.",
            "D. Static testing only provides value if 100% of code is rewritten."
        ],
        "answer": "B",
        "explanation": "Tỷ suất sinh lời (ROI) của Static Testing rất cao: Chi phí phát hiện và sửa một lỗi ở giai đoạn Requirement/Design bằng review rẻ hơn từ 10 đến 100 lần so với khi lỗi đó đã lọt tới System Test hoặc Production."
    },
    {
        "id": "Q263",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "Which review role is responsible for ensuring that the review meeting stays focused on the document rather than on personal opinions, and resolves interpersonal disputes?",
        "options": [
            "A. The Facilitator (Moderator)",
            "B. The Author",
            "C. The Scribe",
            "D. The System Administrator"
        ],
        "answer": "A",
        "explanation": "Facilitator (Moderator - Người điều phối) chịu trách nhiệm giữ cho cuộc họp tập trung vào tài liệu, ngăn ngừa xung đột cá nhân và đảm bảo buổi review diễn ra văn minh, hiệu quả."
    },
    {
        "id": "Q264",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.1 Static Testing Basics",
        "type": "Single",
        "question": "Can a linter (e.g., ESLint, SonarQube, Pylint) verify whether a business calculation meets the customer's true commercial expectations?",
        "options": [
            "A. Yes, linters understand business logic completely.",
            "B. No, linters check coding standards, syntax, and known structural flaws; validating customer business intent requires human review and dynamic testing.",
            "C. Yes, if configured in Java.",
            "D. Linters only work on physical network routers."
        ],
        "answer": "B",
        "explanation": "Linter và công cụ Static Analysis kiểm tra cú pháp, chuẩn viết mã và cấu trúc lỗi; chúng không thể hiểu được ý định nghiệp vụ (business intent) của khách hàng. Việc này cần sự tham gia của con người và dynamic testing."
    },
    {
        "id": "Q265",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "In Perspective-Based Reading (PBR), a reviewer adopting the 'Tester Perspective' will typically try to:",
        "options": [
            "A. Re-write the database schema from scratch.",
            "B. Draft acceptance test cases based on the requirements to verify whether the specification is clear, measurable, and testable.",
            "C. Negotiate the final sale price with the customer.",
            "D. Check server cooling vents."
        ],
        "answer": "B",
        "explanation": "Khi áp dụng góc nhìn của Tester (Tester Perspective) trong PBR: Người review sẽ thử thiết kế các test case nháp dựa trên tài liệu yêu cầu. Nếu không thể viết được test case thì chứng tỏ yêu cầu đó bị mơ hồ hoặc không thể kiểm thử được (untestable)."
    },

    # --- Chapter 4: Test Analysis & Design - Deep Practice (Q266 - Q285) ---
    {
        "id": "Q266",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Boundary Value Analysis",
        "type": "Single",
        "question": "A discount system accepts purchase amounts from $1.00 to $99.99 (inclusive, 2 decimal places). Using 2-value Boundary Value Analysis, which values should be tested around the upper boundary ($99.99)?",
        "options": [
            "A. $99.99 and $100.00",
            "B. $99.98, $99.99, $100.00",
            "C. $90.00 and $100.00",
            "D. $99.00 and $100.00"
        ],
        "answer": "A",
        "explanation": "Vì dữ liệu có độ chính xác 2 chữ số thập phân, bước nhảy nhỏ nhất là 0.01. Tại cận trên $99.99: Giá trị biên hợp lệ là $99.99 và giá trị kế cận ngay ngoài biên là $100.00 ($99.99 + 0.01). Hai giá trị cần test là $99.99 và $100.00."
    },
    {
        "id": "Q267",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Boundary Value Analysis",
        "type": "Single",
        "question": "For the same range [$1.00, $99.99] with 2 decimal precision, what are the 3-value boundary test values around the lower boundary ($1.00)?",
        "options": [
            "A. $0.99, $1.00, $1.01",
            "B. $0.00, $1.00, $2.00",
            "C. $0.90, $1.00, $1.10",
            "D. $1.00, $50.00, $99.99"
        ],
        "answer": "A",
        "explanation": "Kỹ thuật 3-value BVA chọn 3 giá trị tại mỗi biên: ngay dưới biên, tại biên, và ngay trên biên. Tại biên dưới $1.00 với độ chính xác 0.01: $0.99 (just below), $1.00 (boundary), $1.01 (just above)."
    },
    {
        "id": "Q268",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Equivalence Partitioning",
        "type": "Single",
        "question": "An insurance premium calculates risk based on two input variables:\n- Age: [18 to 65] (valid), <18 (invalid), >65 (invalid)\n- Smoker: Yes (valid), No (valid)\nWhat is the MINIMUM number of test cases to cover all valid equivalence partitions?",
        "options": [
            "A. 2 test cases",
            "B. 4 test cases",
            "C. 6 test cases",
            "D. 1 test case"
        ],
        "answer": "A",
        "explanation": "Có 1 phân vùng hợp lệ cho Age: [18, 65]. Có 2 phân vùng hợp lệ cho Smoker: Yes và No. Để bao phủ tất cả các phân vùng hợp lệ của cả 2 biến, chỉ cần tối thiểu 2 test cases kết hợp: TC1 (Age=30, Smoker=Yes) và TC2 (Age=40, Smoker=No)."
    },
    {
        "id": "Q269",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Equivalence Partitioning",
        "type": "Single",
        "question": "For the same insurance system (Age: 1 valid, 2 invalid; Smoker: 2 valid, 1 invalid [other inputs]), what is the MINIMUM number of test cases to test all INVALID equivalence partitions without error masking?",
        "options": [
            "A. 1 test case",
            "B. 3 test cases",
            "C. 6 test cases",
            "D. 8 test cases"
        ],
        "answer": "B",
        "explanation": "Có 2 phân vùng invalid cho Age (Age < 18 và Age > 65) và 1 phân vùng invalid cho Smoker (giá trị khác Yes/No). Theo nguyên tắc chống error masking, mỗi giá trị invalid phải được test riêng biệt với giá trị hợp lệ của biến kia. Do đó cần đúng 3 test cases: TC1 (Age=15, Smoker=Yes), TC2 (Age=70, Smoker=Yes), TC3 (Age=30, Smoker=Invalid)."
    },
    {
        "id": "Q270",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Decision Table Testing",
        "type": "Single",
        "question": "A hotel discount rule states:\n- Condition 1: Weekend stay (True/False)\n- Condition 2: Member of loyalty club (True/False)\nIf Weekend stay is False, NO DISCOUNT is granted regardless of loyalty club membership.\nHow many rules can be collapsed for the case Weekend = False?",
        "options": [
            "A. 2 rules can be collapsed into 1 rule (Weekend = False, Member = '-', Action = No discount)",
            "B. 4 rules",
            "C. Rules cannot be collapsed in hotel systems",
            "D. 0 rules"
        ],
        "answer": "A",
        "explanation": "Khi Weekend = False, dù Member là True hay False thì kết quả Action đều là 'No discount'. Do đó 2 cột (False, True) và (False, False) được gộp lại thành 1 cột duy nhất: Weekend = False, Member = '-' (Don't Care), Action = No discount."
    },
    {
        "id": "Q271",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: State Transition Testing",
        "type": "Single",
        "question": "A turnstile gate has two states: [Locked] and [Unlocked].\n- In [Locked], inserting a coin transitions to [Unlocked].\n- In [Locked], pushing the turnstile stays in [Locked].\n- In [Unlocked], pushing the turnstile transitions to [Locked].\n- In [Unlocked], inserting a coin stays in [Unlocked].\nHow many total transitions (including transitions to the same state) exist in this state machine?",
        "options": [
            "A. 2 transitions",
            "B. 4 transitions",
            "C. 8 transitions",
            "D. 1 transition"
        ],
        "answer": "B",
        "explanation": "Có 2 trạng thái và mỗi trạng thái có 2 sự kiện (Push và Coin), tổng cộng có 2 * 2 = 4 transitions: 1. Locked -> Coin -> Unlocked; 2. Locked -> Push -> Locked; 3. Unlocked -> Push -> Locked; 4. Unlocked -> Coin -> Unlocked."
    },
    {
        "id": "Q272",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: State Transition Testing",
        "type": "Single",
        "question": "What is '1-switch coverage' in State Transition Testing?",
        "options": [
            "A. Executing all valid sequences of two consecutive transitions (pairs of transitions).",
            "B. Executing only one test case.",
            "C. Turning off the computer switch once.",
            "D. Testing every state exactly once."
        ],
        "answer": "A",
        "explanation": "1-switch coverage (kiểm thử chuỗi 2 bước chuyển liên tiếp): Yêu cầu tất cả các cặp bước chuyển hợp lệ liên tiếp (sequences of two consecutive transitions) phải được thực thi ít nhất một lần. Mức độ bao phủ này sâu hơn 0-switch (chỉ test từng bước chuyển đơn lẻ)."
    },
    {
        "id": "Q273",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Statement Coverage",
        "type": "Single",
        "question": "Consider the code snippet:\n```java\nint compute(int x, int y) {\n    int res = 0;\n    if (x > 0 && y > 0) {\n        res = x + y;\n    }\n    return res;\n}\n```\nWhat input values of (x, y) will achieve 100% Statement Coverage with a SINGLE test case?",
        "options": [
            "A. x = 5, y = 10",
            "B. x = -5, y = 10",
            "C. x = 0, y = 0",
            "D. x = 5, y = -1"
        ],
        "answer": "A",
        "explanation": "Khi x = 5 và y = 10, biểu thức (x > 0 && y > 0) là True, dòng lệnh 'res = x + y;' bên trong if được thực thi. Như vậy 100% các dòng lệnh trong hàm đều được chạy qua chỉ với 1 test case duy nhất."
    },
    {
        "id": "Q274",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Decision Coverage",
        "type": "Single",
        "question": "For the same function:\n```java\nint compute(int x, int y) {\n    int res = 0;\n    if (x > 0 && y > 0) {\n        res = x + y;\n    }\n    return res;\n}\n```\nWhat is the MINIMUM number of test cases to achieve 100% Decision (Branch) Coverage?",
        "options": [
            "A. 1 test case",
            "B. 2 test cases (one where (x>0 && y>0) is True, one where it is False)",
            "C. 4 test cases",
            "D. 3 test cases"
        ],
        "answer": "B",
        "explanation": "Cấu trúc if có 2 kết quả nhánh: True và False. Cần tối thiểu 2 test cases: 1 test case làm cho điều kiện True (ví dụ x=1, y=1) và 1 test case làm cho điều kiện False (ví dụ x=-1, y=1)."
    },
    {
        "id": "Q275",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Modified Condition / Decision Coverage",
        "type": "Single",
        "question": "What is Modified Condition / Decision Coverage (MC/DC), commonly used in safety-critical avionics software (DO-178C)?",
        "options": [
            "A. A technique requiring that each individual condition within a decision is shown to independently affect the decision outcome.",
            "B. A technique where testers modify source code during testing.",
            "C. A tool used solely for database indexing.",
            "D. A black-box exploratory charter."
        ],
        "answer": "A",
        "explanation": "MC/DC (Modified Condition/Decision Coverage): Kỹ thuật White-box cao cấp bắt buộc trong phần mềm hàng không (chuẩn DO-178C Level A), yêu cầu chứng minh rằng mỗi điều kiện con đơn lẻ có thể độc lập làm thay đổi kết quả của toàn bộ biểu thức điều kiện quyết định."
    },
    {
        "id": "Q276",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Cyclomatic Complexity",
        "type": "Single",
        "question": "A method has 1 `while` loop, 2 independent `if` statements, and 1 `switch` statement with 3 `case` labels (and a default). What is the Cyclomatic Complexity V(G)?",
        "options": [
            "A. 7",
            "B. 6",
            "C. 4",
            "D. 9"
        ],
        "answer": "A",
        "explanation": "Công thức V(G) = Số điểm quyết định nhị phân + 1: 1 while loop = 1; 2 independent ifs = 2; switch với 3 case = 3 nhánh quyết định. Tổng số điểm quyết định P = 1 + 2 + 3 = 6. Do đó V(G) = P + 1 = 6 + 1 = 7."
    },
    {
        "id": "Q277",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Use Case Testing",
        "type": "Single",
        "question": "A tester designs test cases for an online banking transfer. Test Case 1 covers the 'Happy Path' (sufficient balance, valid OTP). Test Case 2 covers 'Invalid OTP entered twice'. Test Case 3 covers 'Transfer amount exceeds daily limit'. What technique is being applied?",
        "options": [
            "A. Use Case Testing (covering basic flow, alternate flow, and exception flows)",
            "B. Structural Statement Coverage",
            "C. Static Inspection",
            "D. Code Profiling"
        ],
        "answer": "A",
        "explanation": "Đây là kỹ thuật Use Case Testing: Thiết kế các test case bao phủ luồng chính (Main/Basic flow), luồng thay thế (Alternate flow) và luồng xử lý ngoại lệ (Exception flow) của ca sử dụng."
    },
    {
        "id": "Q278",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Path Testing",
        "type": "Single",
        "question": "In a program with 2 sequential, independent `if` statements (each having an `else` branch), how many total execution paths exist through the code?",
        "options": [
            "A. 2 paths",
            "B. 4 paths",
            "C. 8 paths",
            "D. 1 path"
        ],
        "answer": "B",
        "explanation": "Với 2 câu lệnh if-else tuần tự độc lập: If thứ nhất có 2 nhánh, If thứ hai có 2 nhánh. Tổng số đường đi khả dĩ xuyên qua chương trình là 2 * 2 = 4 đường đi: (True, True), (True, False), (False, True), (False, False)."
    },
    {
        "id": "Q279",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Decision Table Testing",
        "type": "Single",
        "question": "A login function has 2 conditions:\n1. Username correct? (Y/N)\n2. Password correct? (Y/N)\nAction: Grant access if both Y; otherwise Display error.\nHow many test cases are derived from the minimized decision table?",
        "options": [
            "A. 3 test cases: Rule 1 (Y, Y -> Access), Rule 2 (Y, N -> Error), Rule 3 (N, - -> Error)",
            "B. 10 test cases",
            "C. 1 test case",
            "D. 8 test cases"
        ],
        "answer": "A",
        "explanation": "Bảng đầy đủ có 4 cột: (Y,Y), (Y,N), (N,Y), (N,N). Khi Username = N, dù Password đúng hay sai đều báo lỗi Error, nên (N,Y) và (N,N) gộp thành (N, '-'). Vậy bảng rút gọn còn 3 test cases tối thiểu."
    },
    {
        "id": "Q280",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Boundary Value Analysis",
        "type": "Single",
        "question": "An input accepts calendar day of the month for February in a standard non-leap year (valid: 1 to 28). What are the 2-value boundary test values for day?",
        "options": [
            "A. 0, 1, 28, 29",
            "B. 1, 28",
            "C. -1, 0, 28, 31",
            "D. 0, 1, 2, 27, 28, 29"
        ],
        "answer": "A",
        "explanation": "Miền hợp lệ là [1, 28]. Áp dụng 2-value BVA: Biên dưới là 1 và kế cận ngoài là 0. Biên trên là 28 và kế cận ngoài là 29. Tập giá trị biên là {0, 1, 28, 29}."
    },
    {
        "id": "Q281",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.4 Experience-based Techniques",
        "type": "Single",
        "question": "A software tester tests a search engine by entering SQL injection strings (`' OR '1'='1`) and extremely long strings (100,000 characters) without looking at requirements. What experience-based technique is this?",
        "options": [
            "A. Error Guessing based on common attack patterns",
            "B. Formal Verification",
            "C. 100% Branch Coverage",
            "D. Static Architecture Review"
        ],
        "answer": "A",
        "explanation": "Tester sử dụng các mẫu tấn công và lỗi phổ biến trong quá khứ để đoán lỗi (Error Guessing), nhằm xem hệ thống có xử lý an toàn với các đầu vào độc hại hay không."
    },
    {
        "id": "Q282",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Statement vs Decision Coverage",
        "type": "Single",
        "question": "Why is Path Coverage rarely achievable in programs containing loops?",
        "options": [
            "A. Because loops can execute an arbitrarily large or infinite number of times, causing combinatorial explosion of possible execution paths.",
            "B. Because compilers do not allow loops to be tested.",
            "C. Because path testing is only applicable to HTML.",
            "D. Because path coverage does not require test cases."
        ],
        "answer": "A",
        "explanation": "Hiện tượng bùng nổ tổ hợp đường đi (combinatorial explosion): Một vòng lặp chạy từ 0 đến N lần sẽ nhân số lượng đường đi lên gấp hàng triệu lần, khiến việc đạt 100% Path Coverage trong thực tế là bất khả thi."
    },
    {
        "id": "Q283",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Equivalence Partitioning",
        "type": "Single",
        "question": "An employee leave booking system accepts leave duration from 0.5 days to 30.0 days in increments of 0.5 days (e.g., 0.5, 1.0, 1.5 ... 30.0). Which of the following is an INVALID equivalence partition?",
        "options": [
            "A. 1.3 days (invalid increment)",
            "B. 15.5 days",
            "C. 0.5 days",
            "D. 30.0 days"
        ],
        "answer": "A",
        "explanation": "Giá trị 1.3 ngày vi phạm quy tắc bước nhảy 0.5 ngày (invalid increment), thuộc phân vùng không hợp lệ."
    },
    {
        "id": "Q284",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Cyclomatic Complexity",
        "type": "Single",
        "question": "If Cyclomatic Complexity of a Java method is calculated as 15, what does this indicate according to software engineering best practices?",
        "options": [
            "A. The method is simple and easy to maintain.",
            "B. The method has high complexity, is difficult to test thoroughly, and should be refactored into smaller modular methods.",
            "C. The method has zero bugs.",
            "D. The method cannot be executed by the JVM."
        ],
        "answer": "B",
        "explanation": "Theo chuẩn McCabe, hàm có V(G) > 10 là hàm có độ phức tạp cao, tiềm ẩn nhiều lỗi và rất khó bảo trì; nên xem xét tái cấu trúc (refactor) chia nhỏ thành các hàm con."
    },
    {
        "id": "Q285",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.1 Categories of Test Techniques",
        "type": "Multiple",
        "question": "Which TWO of the following are specification-based (Black-box) test techniques? (Choose TWO options)",
        "options": [
            "A. Boundary Value Analysis",
            "B. Decision Coverage",
            "C. State Transition Testing",
            "D. Statement Testing",
            "E. Cyclomatic Complexity Calculation"
        ],
        "answer": "A, C",
        "explanation": "Boundary Value Analysis (BVA) và State Transition Testing là các kỹ thuật Black-box (dựa trên đặc tả). B, D, E là các kỹ thuật/chỉ số White-box."
    },

    # --- Chapter 5: Test Management & Risk (Q286 - Q295) ---
    {
        "id": "Q286",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.5 Risks and Testing",
        "type": "Single",
        "question": "In a medical heart-monitoring device, the probability of a data sync glitch is Low (2 out of 5), but if it occurs, the impact on patient health is Catastrophic (5 out of 5). What is the calculated Risk Priority Level?",
        "options": [
            "A. 10 (High Risk due to critical impact)",
            "B. 7",
            "C. 2.5",
            "D. 0"
        ],
        "answer": "A",
        "explanation": "Risk Level = Likelihood * Impact = 2 * 5 = 10. Dù xác suất thấp nhưng tác hại liên quan đến tính mạng bệnh nhân là thảm khốc, nên đây vẫn là rủi ro mức độ cao cần ưu tiên kiểm thử nghiêm ngặt."
    },
    {
        "id": "Q287",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.3 Test Monitoring and Control",
        "type": "Single",
        "question": "In software testing, what does an 'S-Curve' (Cumulative Test Execution Curve) visually represent over project duration?",
        "options": [
            "A. Slow progress initially, accelerating rapidly during main execution, and flattening out as exit criteria and test completion are reached.",
            "B. The salary curve of testers.",
            "C. Hardware memory usage.",
            "D. Internet bandwidth consumption."
        ],
        "answer": "A",
        "explanation": "Đường cong chữ S (S-Curve): Biểu đồ tích lũy tiến độ kiểm thử chuẩn - ban đầu tiến độ tăng chậm khi mới thiết lập môi trường, sau đó tăng tốc rất nhanh ở giai đoạn chạy test cao điểm, và thoải dần khi gần hoàn thành và hệ thống ổn định."
    },
    {
        "id": "Q288",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.6 Defect Management",
        "type": "Single",
        "question": "A tester logs a defect stating: 'The button does not work.' The developer rejects it as 'Not Reproducible'. What critical information was MISSING from the report?",
        "options": [
            "A. Detailed preconditions, exact step-by-step reproduction instructions, test data used, and actual vs expected results.",
            "B. The tester's phone number.",
            "C. A picture of the computer mouse.",
            "D. The brand of the developer's keyboard."
        ],
        "answer": "A",
        "explanation": "Báo cáo lỗi quá sơ sài không thể tái hiện được nếu thiếu: điều kiện tiên quyết (preconditions), các bước thực hiện tuần tự, dữ liệu đầu vào đã dùng và so sánh kết quả thực tế với kết quả mong đợi."
    },
    {
        "id": "Q289",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.2 Test Planning and Estimation",
        "type": "Single",
        "question": "What is the primary role of 'Definition of Ready' (DoR) in Agile Scrum testing?",
        "options": [
            "A. Ensuring that a User Story has clear acceptance criteria, sufficient detail, and testable requirements before the team agrees to pull it into a Sprint.",
            "B. Declaring that all developers are ready for lunch.",
            "C. Stating that the sprint backlog is completely deleted.",
            "D. Terminating the test manager."
        ],
        "answer": "A",
        "explanation": "Definition of Ready (DoR - Tiêu chí sẵn sàng): Đảm bảo rằng một User Story đã có đầy đủ tiêu chí chấp nhận (Acceptance Criteria), thông tin rõ ràng và có thể kiểm thử được trước khi nhóm nhận vào Sprint để phát triển."
    },
    {
        "id": "Q290",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.2 Test Planning and Estimation",
        "type": "Single",
        "question": "What is the primary difference between a Test Strategy and a Test Plan?",
        "options": [
            "A. A Test Strategy is organizational/project-independent describing general test approaches; a Test Plan is specific to a particular project detailing scope, schedule, and resources.",
            "B. A Test Plan is only for developers; a Test Strategy is only for clients.",
            "C. They are identical documents.",
            "D. Test Strategy is written only after testing finishes."
        ],
        "answer": "A",
        "explanation": "Test Strategy là định hướng chiến lược cấp cao (thường dùng chung cho nhiều dự án trong tổ chức); trong khi Test Plan là kế hoạch chi tiết cho một dự án/giai đoạn cụ thể (gồm nhân sự, lịch trình, phạm vi, ngân sách)."
    },
    {
        "id": "Q291",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.1 Test Organization",
        "type": "Single",
        "question": "What is a major risk if a software project employs ZERO independent testers and relies solely on developers testing their own code?",
        "options": [
            "A. Confirmation bias will lead developers to overlook defects caused by blind spots in their own assumptions.",
            "B. Testing will cost too much money.",
            "C. Code execution speed will drop by 50%.",
            "D. The compiler will refuse to build the project."
        ],
        "answer": "A",
        "explanation": "Nếu lập trình viên chỉ tự test code của mình: Thiên kiến xác nhận (Confirmation bias) khiến họ chỉ kiểm tra các trường hợp chạy đúng (happy path) và bỏ qua các giả định sai lầm của chính mình."
    },
    {
        "id": "Q292",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.6 Defect Management",
        "type": "Single",
        "question": "What happens when a defect report is marked as 'Deferred' by the change control board?",
        "options": [
            "A. The defect is acknowledged as a valid bug, but will not be fixed in the current release due to schedule, cost, or risk constraints.",
            "B. The defect is permanently erased from Jira history.",
            "C. The tester is penalized.",
            "D. The application is completely rewritten."
        ],
        "answer": "A",
        "explanation": "Trạng thái Deferred: Hội đồng quản lý thay đổi (CCB) thừa nhận lỗi là có thật, nhưng quyết định hoãn sửa sang các phiên bản sau vì thời gian gấp rút hoặc rủi ro sửa lỗi quá lớn."
    },
    {
        "id": "Q293",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.5 Risks and Testing",
        "type": "Single",
        "question": "Which of the following is an example of a Project Risk related to CONTRACTS?",
        "options": [
            "A. A third-party software library vendor breaches SLA agreements and fails to deliver the payment API on schedule.",
            "B. The mobile application crashes when internet is disconnected.",
            "C. The user enters an invalid credit card number.",
            "D. A division by zero error occurs in financial reporting."
        ],
        "answer": "A",
        "explanation": "Nhà cung cấp bên thứ ba vi phạm thỏa thuận hợp đồng SLA dẫn đến chậm tiến độ là rủi ro dự án liên quan đến hợp đồng/nhà thầu (Project Risk)."
    },
    {
        "id": "Q294",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.3 Test Monitoring and Control",
        "type": "Single",
        "question": "What does a high 'Defect Reopen Rate' typically indicate?",
        "options": [
            "A. Developers may be writing poor-quality bug fixes, or the root cause was not properly addressed, or regression occurred.",
            "B. Testers do not know how to run tests.",
            "C. The software has 100% test coverage.",
            "D. The compiler is malfunctioning."
        ],
        "answer": "A",
        "explanation": "Tỷ lệ Reopen bug cao (Defect Reopen Rate cao): Cho thấy chất lượng sửa lỗi của developer chưa tốt, chỉ sửa phần ngọn mà chưa giải quyết nguyên nhân gốc rễ, hoặc việc sửa lỗi gây ra lỗi mới."
    },
    {
        "id": "Q295",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.2 Test Planning and Estimation",
        "type": "Single",
        "question": "In test effort estimation, what does 'Estimation by Analogy' mean?",
        "options": [
            "A. Estimating effort for a new project based on actual effort spent on similar projects completed in the past.",
            "B. Guessing a random number between 1 and 100.",
            "C. Calculating the square root of code lines.",
            "D. Letting an AI write all code."
        ],
        "answer": "A",
        "explanation": "Ước lượng tương tự (Estimation by Analogy): Phương pháp ước lượng công sức cho dự án mới dựa trên việc so sánh và đối chiếu với dữ liệu thực tế từ các dự án tương đồng đã hoàn thành trong quá khứ."
    },

    # --- Chapter 6: Tool Support for Testing (Q296 - Q300) ---
    {
        "id": "Q296",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "What is the primary formula used to calculate Return on Investment (ROI) for a test automation initiative?",
        "options": [
            "A. ROI = (Net Benefits from Automation - Cost of Automation) / Cost of Automation * 100%",
            "B. ROI = Number of test cases * 100",
            "C. ROI = Server CPU usage * RAM size",
            "D. ROI = Number of bug tickets logged in Jira"
        ],
        "answer": "A",
        "explanation": "ROI của tự động hóa = (Lợi ích ròng thu được - Chi phí đầu tư cho tự động hóa) / Chi phí đầu tư cho tự động hóa * 100%. Lợi ích bao gồm số giờ manual tiết kiệm được, phát hiện lỗi sớm và rút ngắn chu kỳ release."
    },
    {
        "id": "Q297",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "Why is hardcoding test input data and expected results directly inside UI test scripts considered a POOR automation practice?",
        "options": [
            "A. Because whenever data changes, tester must manually modify code across multiple scripts, drastically increasing maintenance overhead.",
            "B. Because compilers refuse to run hardcoded strings.",
            "C. Because computers run out of disk space.",
            "D. Because ISO standards mandate SQL databases."
        ],
        "answer": "A",
        "explanation": "Hardcode dữ liệu vào script làm tăng chi phí bảo trì. Thay vào đó nên áp dụng Data-Driven Testing để tách dữ liệu ra các file bên ngoài (CSV, Excel, JSON)."
    },
    {
        "id": "Q298",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.2 Effective Use of Tools",
        "type": "Single",
        "question": "What should be done with test automation assets during the 'Test Completion' phase?",
        "options": [
            "A. Archive test scripts, test data, and execution results into version control and hand them over to maintenance teams with clear documentation.",
            "B. Delete all scripts to make room on the hard drive.",
            "C. Encrypt scripts and hide passwords.",
            "D. Print all scripts on paper and shred them."
        ],
        "answer": "A",
        "explanation": "Trong pha Kết thúc kiểm thử (Test Completion), các tài sản tự động hóa (scripts, test data, cấu hình) cần được lưu trữ cẩn thận vào hệ thống quản lý phiên bản (Git) và bàn giao đầy đủ cho đội ngũ vận hành/bảo trì."
    },
    {
        "id": "Q299",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "Which testing tool provides detailed memory leak analysis by tracking heap memory allocation and identifying un-freed pointers during execution?",
        "options": [
            "A. Dynamic Memory Analysis Tool (e.g., Valgrind, LeakCanary)",
            "B. Static Spell Checker",
            "C. Requirement Traceability Matrix Tool",
            "D. Bug Tracking Database"
        ],
        "answer": "A",
        "explanation": "Công cụ phân tích động bộ nhớ (như Valgrind, LeakCanary) theo dõi việc cấp phát bộ nhớ heap khi chương trình đang chạy để phát hiện các lỗi rò rỉ bộ nhớ (memory leaks) và con trỏ chưa được giải phóng."
    },
    {
        "id": "Q300",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.2 Effective Use of Tools",
        "type": "Single",
        "question": "What is the ultimate benefit of combining continuous automated testing with a robust Defect Tracking tool?",
        "options": [
            "A. Provides continuous quality visibility, rapid defect turnaround, and objective data for release go/no-go decisions.",
            "B. Completely eliminates the need to write software code.",
            "C. Guarantees that users will never file complaints.",
            "D. Replaces the need for database storage."
        ],
        "answer": "A",
        "explanation": "Sự kết hợp giữa kiểm thử tự động liên tục và công cụ theo dõi lỗi mang lại cái nhìn minh bạch liên tục về chất lượng phần mềm, giúp rút ngắn chu kỳ sửa lỗi và cung cấp số liệu khách quan giúp ban quản lý tự tin ra quyết định phát hành (release)."
    }
]
