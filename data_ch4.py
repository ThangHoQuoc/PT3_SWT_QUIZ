# data_ch4.py - Chapter 4: Test Analysis and Design (65 Questions)

CH4_QUESTIONS = [
    {
        "id": "Q106",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.1 Categories of Test Techniques",
        "type": "Single",
        "question": "Which of the following BEST characterizes Black-box (specification-based) test techniques?",
        "options": [
            "A. Test cases are derived from the internal source code and control flow logic.",
            "B. Test cases are derived from analysis of the specified behavior and requirements of the software without reference to its internal structure.",
            "C. Test cases are created solely based on the personal intuition and gut feelings of the developer.",
            "D. Test cases are generated automatically by compilers."
        ],
        "answer": "B",
        "explanation": "Black-box test techniques (kỹ thuật hộp đen / dựa trên đặc tả): Test cases được thiết kế dựa trên yêu cầu, đặc tả chức năng và hành vi của hệ thống mà không cần biết hay can thiệp vào cấu trúc mã nguồn bên trong."
    },
    {
        "id": "Q107",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Equivalence Partitioning",
        "type": "Single",
        "question": "An input field accepts an integer age for purchasing a child ticket: valid age is between 3 and 12 (inclusive). Which of the following correctly identifies all the equivalence partitions for this input?",
        "options": [
            "A. One valid partition: [3, 12]; Two invalid partitions: age < 3 and age > 12.",
            "B. One valid partition: [3, 12]; One invalid partition: age != 7.",
            "C. Two valid partitions: [3, 7] and [8, 12]; No invalid partitions.",
            "D. Infinite valid partitions."
        ],
        "answer": "A",
        "explanation": "Với miền giá trị tuổi hợp lệ từ 3 đến 12 (bao gồm cả 3 và 12): Có 1 phân vùng tương đương hợp lệ là [3, 12] và 2 phân vùng tương đương không hợp lệ là age < 3 (ví dụ 2) và age > 12 (ví dụ 13)."
    },
    {
        "id": "Q108",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Equivalence Partitioning",
        "type": "Single",
        "question": "Why should invalid equivalence partitions be tested SEPARATELY rather than combined into a single test case?",
        "options": [
            "A. To save execution time.",
            "B. To avoid error masking, where one invalid input hides the failure or prevents the evaluation of another invalid input.",
            "C. Because test automation tools cannot accept more than one input value.",
            "D. It is an optional guideline with no technical justification."
        ],
        "answer": "B",
        "explanation": "Hiện tượng che giấu lỗi (Error Masking): Nếu kết hợp nhiều giá trị không hợp lệ trong cùng 1 test case, hệ thống có thể từ chối ngay ở trường đầu tiên và không kiểm tra trường thứ hai, làm che giấu lỗi tiềm ẩn ở trường thứ hai. Do đó mỗi giá trị invalid cần được test riêng lẻ."
    },
    {
        "id": "Q109",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Boundary Value Analysis",
        "type": "Single",
        "question": "A system accepts an order quantity between 1 and 50 units (inclusive). Using 2-value Boundary Value Analysis (BVA), which set of test input values is required?",
        "options": [
            "A. 0, 1, 50, 51",
            "B. 1, 25, 50",
            "C. 0, 1, 2, 49, 50, 51",
            "D. -1, 0, 50, 100"
        ],
        "answer": "A",
        "explanation": "Trong kỹ thuật 2-value BVA (phân tích giá trị biên 2 điểm): Với miền hợp lệ [1, 50], các giá trị biên là cận dưới và giá trị ngay ngoài cận dưới (1 và 0), cùng với cận trên và giá trị ngay ngoài cận trên (50 và 51). Tập giá trị là {0, 1, 50, 51}."
    },
    {
        "id": "Q110",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Boundary Value Analysis",
        "type": "Single",
        "question": "Using 3-value Boundary Value Analysis (BVA) for the integer range [10, 100], which values should be selected for the lower boundary (around 10)?",
        "options": [
            "A. 9, 10, 11",
            "B. 10, 100",
            "C. 8, 9, 10",
            "D. 9, 10"
        ],
        "answer": "A",
        "explanation": "3-value BVA chọn 3 giá trị tại mỗi biên: giá trị tại biên, giá trị ngay dưới biên và giá trị ngay trên biên. Tại biên dưới 10, ba giá trị là: 9 (just below), 10 (boundary), 11 (just above)."
    },
    {
        "id": "Q111",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Equivalence Partitioning",
        "type": "Single",
        "question": "A student grading module gives:\n- Grade A for score 85 to 100\n- Grade B for score 70 to 84\n- Grade C for score 50 to 69\n- Grade F for score 0 to 49\nScores below 0 or above 100 are rejected as invalid.\nWhat is the MINIMUM number of test cases required to achieve 100% Equivalence Partitioning coverage?",
        "options": [
            "A. 4 test cases",
            "B. 5 test cases",
            "C. 6 test cases",
            "D. 8 test cases"
        ],
        "answer": "C",
        "explanation": "Có 4 phân vùng hợp lệ: [85, 100], [70, 84], [50, 69], [0, 49] và 2 phân vùng không hợp lệ: score < 0 và score > 100. Tổng cộng có 6 phân vùng tương đương. Để đạt 100% EP coverage, cần tối thiểu 6 test cases (mỗi test case đại diện cho 1 phân vùng)."
    },
    {
        "id": "Q112",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Decision Table Testing",
        "type": "Single",
        "question": "A decision table has 3 independent binary (True/False) conditions. How many total columns (combinations/rules) does the fully expanded truth table contain?",
        "options": [
            "A. 3",
            "B. 6",
            "C. 8",
            "D. 9"
        ],
        "answer": "C",
        "explanation": "Với N điều kiện nhị phân độc lập, số lượng cột (rules/tổ hợp) tối đa là 2^N. Với N = 3 điều kiện: 2^3 = 8 cột."
    },
    {
        "id": "Q113",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Decision Table Testing",
        "type": "Single",
        "question": "In a Decision Table, what does a dash ('-') or 'N/A' (Don't Care) in a condition row indicate?",
        "options": [
            "A. The condition is impossible to test.",
            "B. The value of this condition does not affect the outcome/action for that rule.",
            "C. The test case failed during execution.",
            "D. The developer forgot to implement the feature."
        ],
        "answer": "B",
        "explanation": "Dấu gạch ngang ('-') hoặc Don't Care trong bảng quyết định thể hiện rằng giá trị của điều kiện đó (dù là True hay False) đều không làm thay đổi hành động (action) sinh ra của quy tắc đó. Nó cho phép gộp 2 cột thành 1."
    },
    {
        "id": "Q114",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: State Transition Testing",
        "type": "Single",
        "question": "In State Transition Testing, what is '0-switch coverage' (also known as branch transition coverage)?",
        "options": [
            "A. Testing every state only once without triggering transitions.",
            "B. Testing all valid individual transitions between states at least once.",
            "C. Testing all sequences of two consecutive transitions.",
            "D. Executing zero tests on the state machine."
        ],
        "answer": "B",
        "explanation": "0-switch coverage (hay 1-transition coverage) yêu cầu mọi bước chuyển trạng thái hợp lệ đơn lẻ (single valid transition) phải được thực thi ít nhất một lần. 1-switch coverage là kiểm tra chuỗi 2 bước chuyển liên tiếp."
    },
    {
        "id": "Q115",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: State Transition Testing",
        "type": "Single",
        "question": "An online shopping order has the following states: [Cart] -> [Checkout] -> [Paid] -> [Shipped] -> [Delivered]. A customer in [Cart] state attempts to click 'Delivered'. What does this scenario represent in State Transition Testing?",
        "options": [
            "A. A valid 0-switch transition",
            "B. An invalid (disallowed) transition test case",
            "C. A circular loop transition",
            "D. A white-box branch coverage metric"
        ],
        "answer": "B",
        "explanation": "Việc cố gắng chuyển từ trạng thái [Cart] thẳng sang [Delivered] là một bước chuyển không hợp lệ (Invalid / Disallowed Transition). Kiểm tra các bước chuyển không hợp lệ là một phần quan trọng của State Transition Testing nhằm xác minh hệ thống có bắt lỗi và ngăn chặn hành vi sai trái hay không."
    },
    {
        "id": "Q116",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Use Case Testing",
        "type": "Single",
        "question": "When designing test cases from a Use Case specification, which path is TYPICALLY tested first?",
        "options": [
            "A. The exception flow when server loses power.",
            "B. The basic (main success/happy) flow representing normal, error-free execution.",
            "C. The database rollback scenario.",
            "D. The boundary timeout flow."
        ],
        "answer": "B",
        "explanation": "Khi thiết kế test case từ Use Case, luồng cơ bản (Basic flow / Happy path / Main success scenario) mô tả quá trình thực hiện thông suốt, thành công và không gặp lỗi luôn được ưu tiên kiểm tra đầu tiên."
    },
    {
        "id": "Q117",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Statement Coverage",
        "type": "Single",
        "question": "Consider the following pseudocode snippet:\n```\n1: Read(x);\n2: if (x > 10) {\n3:     print(\"Large\");\n4: }\n5: print(\"Done\");\n```\nWhat is the MINIMUM number of test cases required to achieve 100% Statement Coverage?",
        "options": [
            "A. 1 test case (e.g., x = 15)",
            "B. 2 test cases (e.g., x = 15 and x = 5)",
            "C. 3 test cases",
            "D. 0 test cases"
        ],
        "answer": "A",
        "explanation": "Để đạt 100% Statement Coverage (bao phủ tất cả dòng lệnh): Chỉ cần chạy 1 test case với x = 15 (x > 10 là True). Khi đó dòng 1, 2, 3, 4, 5 đều được thực thi. Do đó số test case tối thiểu là 1."
    },
    {
        "id": "Q118",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Decision Coverage",
        "type": "Single",
        "question": "Consider the exact same pseudocode snippet:\n```\n1: Read(x);\n2: if (x > 10) {\n3:     print(\"Large\");\n4: }\n5: print(\"Done\");\n```\nWhat is the MINIMUM number of test cases required to achieve 100% Decision (Branch) Coverage?",
        "options": [
            "A. 1 test case",
            "B. 2 test cases (e.g., x = 15 [True] and x = 5 [False])",
            "C. 3 test cases",
            "D. 4 test cases"
        ],
        "answer": "B",
        "explanation": "Cấu trúc 'if (x > 10)' có 2 kết quả quyết định (decision outcomes): True và False. Để đạt 100% Decision Coverage, phải thực thi cả 2 nhánh True và False. Cần tối thiểu 2 test cases: 1 test case cho True (ví dụ x = 15) và 1 test case cho False (ví dụ x = 5)."
    },
    {
        "id": "Q119",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Coverage Relationships",
        "type": "Single",
        "question": "Which of the following statements correctly expresses the relationship between Statement Coverage and Decision Coverage?",
        "options": [
            "A. 100% Statement Coverage guarantees 100% Decision Coverage.",
            "B. 100% Decision Coverage guarantees 100% Statement Coverage, but 100% Statement Coverage does NOT guarantee 100% Decision Coverage.",
            "C. There is no relationship between Statement Coverage and Decision Coverage.",
            "D. Decision Coverage can never exceed 50%."
        ],
        "answer": "B",
        "explanation": "Định lý cốt lõi trong White-box testing: Đạt 100% Decision Coverage luôn luôn đảm bảo đạt 100% Statement Coverage. Tuy nhiên, chiều ngược lại KHÔNG đúng: 100% Statement Coverage KHÔNG đảm bảo 100% Decision Coverage (như ví dụ với câu lệnh if đơn không có else)."
    },
    {
        "id": "Q120",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Cyclomatic Complexity",
        "type": "Single",
        "question": "A control flow graph of a method has 9 edges (E), 7 nodes (N), and 1 connected component (P = 1). What is the McCabe Cyclomatic Complexity V(G)?",
        "options": [
            "A. 2",
            "B. 4",
            "C. 9",
            "D. 16"
        ],
        "answer": "B",
        "explanation": "Công thức tính Cyclomatic Complexity của McCabe: V(G) = E - N + 2P. Ở đây E = 9, N = 7, P = 1. Ta có: V(G) = 9 - 7 + 2(1) = 2 + 2 = 4."
    },
    {
        "id": "Q121",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Cyclomatic Complexity",
        "type": "Single",
        "question": "A Java method contains 3 independent simple 'if' statements and no loops or switch blocks. Using the predicate formula V(G) = P + 1 (where P is the number of decision points), what is the Cyclomatic Complexity?",
        "options": [
            "A. 3",
            "B. 4",
            "C. 7",
            "D. 8"
        ],
        "answer": "B",
        "explanation": "Với mỗi điểm quyết định nhị phân (decision point/predicate node), P = 3. Độ phức tạp Cyclomatic V(G) = P + 1 = 3 + 1 = 4. Đây cũng là số đường đi độc lập tuyến tính (basis paths) tối đa trong hàm."
    },
    {
        "id": "Q122",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.4 Experience-based Techniques",
        "type": "Single",
        "question": "A veteran tester anticipates that users will likely enter blank spaces, special characters ($#@!), or paste 10,000 characters into the username box because similar bugs occurred in three past projects. Which testing technique is being applied?",
        "options": [
            "A. Decision Table Testing",
            "B. Error Guessing",
            "C. Finite State Testing",
            "D. Statement Testing"
        ],
        "answer": "B",
        "explanation": "Error Guessing (Đoán lỗi): Kỹ thuật dựa trên kinh nghiệm, kiến thức về các lỗi phổ biến trong quá khứ và trực giác của tester để dự đoán những lỗi mà developer dễ mắc phải."
    },
    {
        "id": "Q123",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.4 Experience-based Techniques",
        "type": "Single",
        "question": "What is the key characteristic of Exploratory Testing?",
        "options": [
            "A. Test cases are fully documented and frozen six months prior to execution.",
            "B. Test design, test execution, test logging, and learning are performed concurrently during time-boxed sessions.",
            "C. Testing is executed completely at random by an automated bot without human oversight.",
            "D. It requires 100% white-box branch coverage."
        ],
        "answer": "B",
        "explanation": "Exploratory Testing (Kiểm thử thăm dò): Quá trình học hỏi (learning), thiết kế kiểm thử (test design), thực thi (execution) và ghi chép (logging) diễn ra đồng thời (concurrently) trong các phiên có giới hạn thời gian (time-boxed sessions) dựa trên test charter."
    },
    {
        "id": "Q124",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.4 Experience-based Techniques",
        "type": "Single",
        "question": "In Session-Based Test Management (SBTM) for exploratory testing, what document guides the tester by specifying the mission and scope of the test session?",
        "options": [
            "A. Test Policy",
            "B. Test Charter",
            "C. Test Script",
            "D. Defect Density Matrix"
        ],
        "answer": "B",
        "explanation": "Test Charter (Hiến chương kiểm thử) xác định mục tiêu (mission), phạm vi (scope) và các rủi ro trọng tâm cần khám phá trong một phiên kiểm thử thăm dò (time-box thường kéo dài từ 60 đến 120 phút)."
    },
    {
        "id": "Q125",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Boundary Value Analysis",
        "type": "Single",
        "question": "A system calculates shipping rates based on weight W in kilograms:\n- 0 < W <= 5: $10\n- 5 < W <= 20: $25\n- 20 < W <= 50: $50\nWeights <= 0 or > 50 are invalid.\nUsing 2-value Boundary Value Analysis, which values should test the boundary between the first and second valid partitions around W = 5?",
        "options": [
            "A. 5 and 6 (or 5.0 and 5.1 for decimals)",
            "B. 0 and 50",
            "C. 1 and 20",
            "D. 4 and 6"
        ],
        "answer": "A",
        "explanation": "Tại ranh giới giữa 2 khoảng (0, 5] và (5, 20]: Biên là 5 (thuộc phân vùng 1) và giá trị ngay sát trên 5 (ví dụ 6 nếu là số nguyên, hoặc 5.1 nếu là số thập phân) thuộc phân vùng 2."
    },
    {
        "id": "Q126",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Decision Table Testing",
        "type": "Single",
        "question": "Consider a decision table for a banking loan with 4 binary conditions:\n1. Employed (Y/N)\n2. Credit Score > 700 (Y/N)\n3. Existing Debt < $10,000 (Y/N)\n4. Collateral Available (Y/N)\nIf no rules can be collapsed, how many test cases are required for full decision table coverage?",
        "options": [
            "A. 4",
            "B. 8",
            "C. 16",
            "D. 32"
        ],
        "answer": "C",
        "explanation": "Số quy tắc (cột) đầy đủ khi có 4 điều kiện nhị phân độc lập là 2^4 = 16 quy tắc tương ứng 16 test cases."
    },
    {
        "id": "Q127",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Decision Coverage",
        "type": "Single",
        "question": "Consider the following code snippet:\n```\nif (A && B) {\n    executeAction1();\n} else {\n    executeAction2();\n}\n```\nTo achieve 100% Decision (Branch) Coverage, which of the following pairs of test inputs (A, B) is SUFFICIENT?",
        "options": [
            "A. Test 1: (A=True, B=True) -> True branch; Test 2: (A=False, B=True) -> False branch",
            "B. Test 1: (A=True, B=False); Test 2: (A=False, B=True)",
            "C. Test 1: (A=True, B=True); Test 2: (A=True, B=True)",
            "D. Only 4 test cases can achieve Decision Coverage."
        ],
        "answer": "A",
        "explanation": "Decision Coverage chỉ quan tâm đến toàn bộ biểu thức điều kiện (A && B) trả về True hay False: Cần 1 test case làm (A && B) = True (chính là A=True, B=True) và 1 test case làm (A && B) = False (ví dụ A=False, B=True). Như vậy chỉ cần 2 test cases là đủ 100% Decision Coverage."
    },
    {
        "id": "Q128",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Statement Coverage",
        "type": "Single",
        "question": "Consider this code:\n```\nint discount = 0;\nif (isMember) {\n    discount = 10;\n}\nif (couponCodeValid) {\n    discount += 5;\n}\nreturn discount;\n```\nWhat is the MINIMUM number of test cases required to achieve 100% Statement Coverage?",
        "options": [
            "A. 1 test case: (isMember = True, couponCodeValid = True)",
            "B. 2 test cases",
            "C. 4 test cases",
            "D. 3 test cases"
        ],
        "answer": "A",
        "explanation": "Chỉ cần 1 test case với cả hai điều kiện đều True: isMember = True và couponCodeValid = True. Khi đó cả hai khối lệnh bên trong if đều được thực thi, đảm bảo 100% các dòng lệnh trong hàm đều được chạy qua."
    },
    {
        "id": "Q129",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Decision Coverage",
        "type": "Single",
        "question": "For the same code:\n```\nint discount = 0;\nif (isMember) {\n    discount = 10;\n}\nif (couponCodeValid) {\n    discount += 5;\n}\nreturn discount;\n```\nWhat is the MINIMUM number of test cases required to achieve 100% Decision Coverage?",
        "options": [
            "A. 1 test case",
            "B. 2 test cases: Test 1 (True, True) and Test 2 (False, False)",
            "C. 4 test cases",
            "D. 3 test cases"
        ],
        "answer": "B",
        "explanation": "Có 2 câu lệnh if độc lập, mỗi if có 2 nhánh True và False (tổng cộng 4 nhánh: If1-True, If1-False, If2-True, If2-False). Cần tối thiểu 2 test cases: Test 1 (isMember=True, couponCodeValid=True) bao phủ If1-True và If2-True; Test 2 (isMember=False, couponCodeValid=False) bao phủ If1-False và If2-False. Tổng cộng 2 test cases đạt 100% Decision Coverage."
    },
    {
        "id": "Q130",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Equivalence Partitioning",
        "type": "Single",
        "question": "A PIN code for a debit card must consist of EXACTLY 4 numeric digits. Which of the following represents an INVALID equivalence partition?",
        "options": [
            "A. '1234'",
            "B. '9081'",
            "C. '123' (3 digits) or '12345' (5 digits)",
            "D. '0000'"
        ],
        "answer": "C",
        "explanation": "PIN hợp lệ gồm đúng 4 chữ số. Phân vùng không hợp lệ (Invalid Partition) bao gồm: ít hơn 4 chữ số (ví dụ '123'), nhiều hơn 4 chữ số (ví dụ '12345'), hoặc chứa ký tự không phải số (ví dụ '12A4')."
    },
    {
        "id": "Q131",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Use Case Testing",
        "type": "Single",
        "question": "In Use Case Testing, what is an 'Extension' or 'Alternative Flow'?",
        "options": [
            "A. The path where everything works perfectly without variation.",
            "B. A path describing alternative ways of achieving the goal or optional user behaviors.",
            "C. A compiler plug-in used to build Java code.",
            "D. The physical internet cable connected to the computer."
        ],
        "answer": "B",
        "explanation": "Alternative Flow (Luồng thay thế / mở rộng) mô tả các nhánh rẽ khác để hoàn thành mục tiêu hoặc các hành vi tùy chọn của người dùng (ví dụ: thanh toán bằng thẻ tín dụng thay vì thanh toán bằng ví điện tử)."
    },
    {
        "id": "Q132",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: State Transition Testing",
        "type": "Single",
        "question": "In a state transition diagram with 4 states and 6 transitions, a test suite exercises 5 of the 6 transitions. What is the 0-switch transition coverage?",
        "options": [
            "A. 50%",
            "B. 83.33%",
            "C. 100%",
            "D. 75%"
        ],
        "answer": "B",
        "explanation": "Độ bao phủ chuyển trạng thái 0-switch = (Số transition được thực thi / Tổng số transition) * 100% = (5 / 6) * 100% = 83.33%."
    },
    {
        "id": "Q133",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Statement vs Decision Coverage",
        "type": "Single",
        "question": "A test suite achieves 100% Statement Coverage on a module containing 4 'if-then' statements (without 'else'). What is the MINIMUM possible Decision Coverage that this test suite could have achieved?",
        "options": [
            "A. 100%",
            "B. 50%",
            "C. 0%",
            "D. 25%"
        ],
        "answer": "B",
        "explanation": "Nếu test case làm cho cả 4 câu lệnh if đều rơi vào nhánh True, tất cả dòng lệnh đều được thực thi (đạt 100% Statement Coverage). Tuy nhiên, cả 4 nhánh False đều chưa được thực thi lần nào. Vì có 8 nhánh quyết định (4 True + 4 False) mà mới chạy 4 nhánh True, nên Decision Coverage tối thiểu có thể chỉ là 4/8 = 50%."
    },
    {
        "id": "Q134",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Decision Table Testing",
        "type": "Single",
        "question": "Two rules in a decision table have identical actions. Rule 1 requires Condition A = True, Condition B = True. Rule 2 requires Condition A = True, Condition B = False. How can these two rules be simplified (collapsed)?",
        "options": [
            "A. By deleting Condition A.",
            "B. By merging them into a single rule with Condition A = True and Condition B = '-' (Don't Care).",
            "C. They cannot be simplified.",
            "D. By setting Action = False."
        ],
        "answer": "B",
        "explanation": "Vì khi Condition A = True thì dù Condition B là True hay False thì kết quả Action đều giống hệt nhau, ta có thể gộp (collapse) 2 rule này thành 1 rule duy nhất: Condition A = True, Condition B = '-' (Don't Care)."
    },
    {
        "id": "Q135",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.4 Experience-based Techniques",
        "type": "Single",
        "question": "When is Exploratory Testing MOST USEFUL and effective?",
        "options": [
            "A. When specifications are scarce or poorly documented, and when rapid feedback is required under tight schedules.",
            "B. When automated testing is legally mandated to be 100% repeatable.",
            "C. When testers have zero domain knowledge and zero software experience.",
            "D. When no software has been written yet."
        ],
        "answer": "A",
        "explanation": "Exploratory testing phát huy hiệu quả cao nhất khi tài liệu đặc tả thiếu thốn hoặc sơ sài, thời gian gấp rút cần phản hồi nhanh, hoặc dùng để bổ trợ sau khi đã chạy xong các test case formal nhằm tìm thêm các lỗi bất ngờ."
    },
    {
        "id": "Q136",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.1 Categories of Test Techniques",
        "type": "Multiple",
        "question": "Which TWO of the following are classified as White-box test techniques? (Choose TWO options)",
        "options": [
            "A. Statement Testing",
            "B. Equivalence Partitioning",
            "C. Decision (Branch) Testing",
            "D. State Transition Testing",
            "E. Use Case Testing"
        ],
        "answer": "A, C",
        "explanation": "Statement Testing và Decision Testing là các kỹ thuật White-box (dựa trên cấu trúc mã nguồn). B, D, E là các kỹ thuật Black-box (dựa trên đặc tả)."
    },
    {
        "id": "Q137",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.1 Categories of Test Techniques",
        "type": "Multiple",
        "question": "Which TWO of the following are Experience-based test techniques? (Choose TWO options)",
        "options": [
            "A. Error Guessing",
            "B. Boundary Value Analysis",
            "C. Exploratory Testing",
            "D. Decision Table Testing",
            "E. Cyclomatic Complexity Analysis"
        ],
        "answer": "A, C",
        "explanation": "Error Guessing và Exploratory Testing là các kỹ thuật kiểm thử dựa trên kinh nghiệm (Experience-based techniques)."
    },
    {
        "id": "Q138",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Equivalence Partitioning",
        "type": "Single",
        "question": "A bonus salary calculation specifies:\n- Employees with tenure 0 to < 2 years: 0% bonus\n- Employees with tenure 2 to < 5 years: 10% bonus\n- Employees with tenure 5 to 10 years: 20% bonus\nNegative tenure is invalid. How many valid equivalence partitions exist?",
        "options": [
            "A. 1",
            "B. 2",
            "C. 3",
            "D. 4"
        ],
        "answer": "C",
        "explanation": "Có 3 phân vùng hợp lệ: [0, 2), [2, 5), và [5, 10]. Phân vùng < 0 hoặc > 10 là không hợp lệ."
    },
    {
        "id": "Q139",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Statement Coverage",
        "type": "Single",
        "question": "A program contains 20 executable statements. A single test case executes 15 of these statements. What is the Statement Coverage percentage?",
        "options": [
            "A. 50%",
            "B. 75%",
            "C. 80%",
            "D. 100%"
        ],
        "answer": "B",
        "explanation": "Statement Coverage = (Số câu lệnh đã thực thi / Tổng số câu lệnh) * 100% = (15 / 20) * 100% = 75%."
    },
    {
        "id": "Q140",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Decision Coverage",
        "type": "Single",
        "question": "A program contains 6 decision points (each having 2 outcomes: True and False). A test suite executes 9 of the 12 possible decision outcomes. What is the Decision Coverage?",
        "options": [
            "A. 50%",
            "B. 75%",
            "C. 90%",
            "D. 66.7%"
        ],
        "answer": "B",
        "explanation": "Tổng số decision outcomes = 6 * 2 = 12. Số outcomes đã thực thi = 9. Decision Coverage = (9 / 12) * 100% = 75%."
    },
    {
        "id": "Q141",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Boundary Value Analysis",
        "type": "Single",
        "question": "A field accepts a string whose length must be between 5 and 20 characters. What string lengths represent the 2-value boundary values?",
        "options": [
            "A. 4, 5, 20, 21",
            "B. 5, 20",
            "C. 0, 5, 20, 100",
            "D. 4, 5, 6, 19, 20, 21"
        ],
        "answer": "A",
        "explanation": "Độ dài chuỗi hợp lệ L trong khoảng [5, 20]. Áp dụng 2-value BVA: Giá trị biên dưới là 5 và giá trị kế cận ngoài là 4. Giá trị biên trên là 20 và giá trị kế cận ngoài là 21. Tập giá trị biên cần test độ dài là {4, 5, 20, 21}."
    },
    {
        "id": "Q142",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: State Transition Testing",
        "type": "Single",
        "question": "An authentication system allows up to 3 failed login attempts before locking an account. The states are: [Unlocked], [Locked]. The events are: 'Valid password' and 'Invalid password'. Which test case will transition the state from [Unlocked] to [Locked]?",
        "options": [
            "A. Enter 1 invalid password then 1 valid password.",
            "B. Enter 3 consecutive invalid passwords.",
            "C. Enter 1 valid password.",
            "D. Leave the password field blank once."
        ],
        "answer": "B",
        "explanation": "Theo đặc tả máy trạng thái, điều kiện bảo vệ (guard condition) để chuyển từ Unlocked sang Locked là số lần nhập sai liên tiếp đạt ngưỡng 3 lần (3 consecutive invalid passwords)."
    },
    {
        "id": "Q143",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Cyclomatic Complexity",
        "type": "Single",
        "question": "What does Cyclomatic Complexity represent in terms of white-box testing?",
        "options": [
            "A. The total number of bugs found in the code.",
            "B. The upper bound for the number of linearly independent paths needed to achieve 100% branch/decision coverage.",
            "C. The execution time of the program in milliseconds.",
            "D. The number of developers needed to maintain the software."
        ],
        "answer": "B",
        "explanation": "Độ phức tạp Cyclomatic (McCabe) cung cấp giới hạn trên cho số lượng đường đi độc lập tuyến tính (basis paths) cần thiết trong đồ thị luồng điều khiển để đạt được độ bao phủ nhánh hoàn chỉnh."
    },
    {
        "id": "Q144",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.4 Experience-based Techniques",
        "type": "Single",
        "question": "What is 'Checklist-based Testing'?",
        "options": [
            "A. An experience-based technique where testers design, implement, and execute tests to cover test conditions found in a checklist.",
            "B. Writing random code in a text file.",
            "C. Only checking if the computer monitor is plugged in.",
            "D. An automated technique that executes all database tables."
        ],
        "answer": "A",
        "explanation": "Checklist-based testing: Kỹ thuật kiểm thử dựa trên kinh nghiệm, trong đó tester dựa vào một danh sách các mục cần kiểm tra (checklist - đúc kết từ kinh nghiệm, chuẩn chất lượng, hoặc lỗi hay gặp) để thiết kế và thực thi test."
    },
    {
        "id": "Q145",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Decision Table Testing",
        "type": "Single",
        "question": "In a Decision Table, conditions represent ______ and actions represent ______.",
        "options": [
            "A. Outputs; Inputs",
            "B. Inputs or system states; Outputs or system responses",
            "C. Developers; Testers",
            "D. Bugs; Fixes"
        ],
        "answer": "B",
        "explanation": "Trong Bảng quyết định (Decision Table): Các hàng Conditions (Điều kiện) đại diện cho các đầu vào (inputs) hoặc trạng thái hệ thống; các hàng Actions (Hành động) đại diện cho các đầu ra (outputs) hoặc phản hồi của hệ thống."
    },
    {
        "id": "Q146",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Statement Coverage",
        "type": "Single",
        "question": "Given the code:\n```\nif (temperature > 37.5) {\n    alertPatient();\n    logRecord();\n}\n```\nIf a tester runs one test with temperature = 36.0, what is the statement coverage achieved?",
        "options": [
            "A. 100%",
            "B. 33.3%",
            "C. 0%",
            "D. 50%"
        ],
        "answer": "B",
        "explanation": "Khi temperature = 36.0, điều kiện 'if (temperature > 37.5)' là False. Khối lệnh bên trong gồm alertPatient() và logRecord() bị bỏ qua. Chỉ có dòng lệnh kiểm tra điều kiện if được thực thi. Trong 3 câu lệnh có thể thực thi, chỉ 1 được chạy -> độ bao phủ dòng lệnh đạt xấp xỉ 33.3%."
    },
    {
        "id": "Q147",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Use Case Testing",
        "type": "Single",
        "question": "Which of the following is an example of an 'Exception Flow' in a Use Case for withdrawing cash from an ATM?",
        "options": [
            "A. User inserts card, enters correct PIN, and receives cash.",
            "B. User requests an amount greater than the ATM's available cash balance, and the transaction is cancelled with an error message.",
            "C. User chooses to print a receipt after cash withdrawal.",
            "D. User selects English instead of Vietnamese."
        ],
        "answer": "B",
        "explanation": "Exception Flow (Luồng ngoại lệ) mô tả tình huống lỗi ngăn cản Actor đạt được mục tiêu chính (ví dụ: máy ATM hết tiền, tài khoản không đủ số dư, thẻ bị khóa)."
    },
    {
        "id": "Q148",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Equivalence Partitioning",
        "type": "Single",
        "question": "An online store accepts coupon codes with the following rule: code must be either 'SAVE10', 'SAVE20', or 'FREESHIP'. Any other string is invalid. How many equivalence partitions are there?",
        "options": [
            "A. 1 valid partition, 1 invalid partition",
            "B. 3 valid partitions ('SAVE10', 'SAVE20', 'FREESHIP') and 1 invalid partition (any other string)",
            "C. Infinite valid partitions",
            "D. 2 valid partitions and 0 invalid partitions"
        ],
        "answer": "B",
        "explanation": "Vì mỗi mã giảm giá hợp lệ mang lại một mức giảm giá khác nhau ('SAVE10' giảm 10%, 'SAVE20' giảm 20%, 'FREESHIP' miễn phí vận chuyển), mỗi mã hợp lệ là một phân vùng riêng biệt (3 valid partitions). Bất kỳ chuỗi nào khác là phân vùng không hợp lệ (1 invalid partition). Tổng cộng 4 phân vùng."
    },
    {
        "id": "Q149",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Control Flow Graphs",
        "type": "Single",
        "question": "In a Control Flow Graph (CFG), what do NODES and EDGES represent?",
        "options": [
            "A. Nodes represent test cases, edges represent bug reports.",
            "B. Nodes represent one or more sequential statements; edges represent transfers of control (branches) between nodes.",
            "C. Nodes represent programmers, edges represent network cables.",
            "D. Nodes represent database tables, edges represent foreign keys."
        ],
        "answer": "B",
        "explanation": "Trong Đồ thị luồng điều khiển (Control Flow Graph): Nodes (Đỉnh) đại diện cho một khối các câu lệnh thực thi tuần tự; Edges (Cạnh nối) đại diện cho luồng chuyển giao điều khiển giữa các đỉnh (các nhánh rẽ True/False)."
    },
    {
        "id": "Q150",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Boundary Value Analysis",
        "type": "Single",
        "question": "A speed camera issues a ticket if car speed is strictly greater than 60 km/h (speed > 60). Drivers traveling at or below 60 km/h are not ticketed. What are the 2-value boundary test values for integer speeds around the boundary?",
        "options": [
            "A. 59 and 60",
            "B. 60 and 61",
            "C. 60 and 100",
            "D. 0 and 60"
        ],
        "answer": "B",
        "explanation": "Ranh giới là 60: Với speed = 60 km/h (không bị phạt - Valid/No ticket); với speed = 61 km/h (bị phạt - Valid/Ticket). Hai giá trị biên liền kề là 60 và 61."
    },
    {
        "id": "Q151",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Decision Coverage",
        "type": "Single",
        "question": "Why is 100% Decision Coverage considered STRONGER than 100% Statement Coverage?",
        "options": [
            "A. Because Decision Coverage requires fewer test cases.",
            "B. Because Decision Coverage exercises both the True and False outcomes of all decisions, thereby guaranteeing that every statement is also executed.",
            "C. Because Decision Coverage does not require access to code.",
            "D. Because compilers automatically enforce Decision Coverage."
        ],
        "answer": "B",
        "explanation": "Decision Coverage mạnh hơn Statement Coverage vì nó buộc phải kiểm tra tất cả các kết quả rẽ nhánh (cả True và False). Khi tất cả các nhánh rẽ đều được đi qua thì mọi câu lệnh nằm trong các nhánh đó chắc chắn đều được thực thi."
    },
    {
        "id": "Q152",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Decision Table Testing",
        "type": "Single",
        "question": "A movie theater offers a discount if: (Age < 18 OR Student = Yes) AND LoyaltyMember = Yes. How many total combinations of these three conditions exist in a full truth table?",
        "options": [
            "A. 3",
            "B. 6",
            "C. 8",
            "D. 12"
        ],
        "answer": "C",
        "explanation": "Có 3 điều kiện nhị phân (Age < 18, Student, LoyaltyMember). Tổng số tổ hợp trong bảng chân trị đầy đủ là 2^3 = 8 cột."
    },
    {
        "id": "Q153",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Cyclomatic Complexity",
        "type": "Single",
        "question": "If a control flow graph divides the plane into 5 enclosed regions (R) plus 1 external infinite region, what is its Cyclomatic Complexity?",
        "options": [
            "A. 5",
            "B. 6",
            "C. 7",
            "D. 12"
        ],
        "answer": "B",
        "explanation": "Theo định lý đồ thị phẳng của McCabe, Cyclomatic Complexity V(G) = Số miền kín (enclosed regions) + 1 miền vô hạn bên ngoài = 5 + 1 = 6."
    },
    {
        "id": "Q154",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: State Transition Testing",
        "type": "Single",
        "question": "What is a 'State Table' in State Transition Testing?",
        "options": [
            "A. A table listing employee salaries by US state.",
            "B. A matrix showing the current states on one axis, events on the other axis, and the resulting next states (and actions) in the cells.",
            "C. A database table storing system crashes.",
            "D. A Gantt chart for scheduling testing sprints."
        ],
        "answer": "B",
        "explanation": "State Table (Bảng trạng thái): Một bảng ma trận biểu diễn trạng thái hiện tại (hàng), các sự kiện kích hoạt (cột), và ô giao nhau chứa trạng thái tiếp theo cùng hành động tương ứng. Các ô trống trong bảng chỉ ra các bước chuyển không hợp lệ (invalid transitions)."
    },
    {
        "id": "Q155",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.4 Experience-based Techniques",
        "type": "Single",
        "question": "A tester with 10 years of experience in testing e-commerce checkouts focuses their manual tests on race conditions when two users purchase the last available stock item simultaneously. What technique is this?",
        "options": [
            "A. Error Guessing based on domain expertise",
            "B. 100% Statement Coverage",
            "C. Cyclomatic Boundary Reduction",
            "D. Static Linting"
        ],
        "answer": "A",
        "explanation": "Tester dựa trên kinh nghiệm chuyên sâu về domain thương mại điện tử để nhắm vào lỗi tranh chấp tài nguyên (race condition) - đây là kỹ thuật Error Guessing (Đoán lỗi dựa trên kinh nghiệm)."
    },
    {
        "id": "Q156",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.1 Categories of Test Techniques",
        "type": "Single",
        "question": "Which category of test technique derives test cases from an analysis of the software's internal architecture, code structure, or data flow?",
        "options": [
            "A. Black-box techniques",
            "B. White-box (Structure-based) techniques",
            "C. Specification-based techniques",
            "D. Random monkey testing"
        ],
        "answer": "B",
        "explanation": "White-box techniques (Kỹ thuật hộp trắng / dựa trên cấu trúc) thiết kế test cases dựa trên phân tích cấu trúc bên trong phần mềm, mã nguồn, luồng điều khiển và luồng dữ liệu."
    },
    {
        "id": "Q157",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Boundary Value Analysis",
        "type": "Single",
        "question": "When is Boundary Value Analysis (BVA) APPLICABLE?",
        "options": [
            "A. Only on un-ordered qualitative descriptions like favorite color.",
            "B. On ordered numeric or sequential data where boundaries between partitions exist.",
            "C. Exclusively on hardware wiring diagrams.",
            "D. Only when testing non-functional usability."
        ],
        "answer": "B",
        "explanation": "BVA chỉ có thể áp dụng trên các dữ liệu có thứ tự (ordered data - như số nguyên, số thực, ngày tháng, độ dài chuỗi) nơi mà các ranh giới giữa các phân vùng có thể xác định rõ ràng."
    },
    {
        "id": "Q158",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Loop Testing",
        "type": "Single",
        "question": "When testing a simple loop of maximum N iterations, which boundary values should typically be tested?",
        "options": [
            "A. Skip loop entirely (0 iterations), 1 iteration, 2 iterations, typical iterations, N-1 iterations, N iterations, and attempt N+1 iterations.",
            "B. Only test 100,000 iterations.",
            "C. Loops should never be tested dynamically.",
            "D. Test 1 iteration only."
        ],
        "answer": "A",
        "explanation": "Kỹ thuật kiểm thử vòng lặp (Loop testing) tiêu chuẩn kiểm tra các biên: không chạy vòng lặp (0 lần), 1 lần, 2 lần, số lần điển hình ở giữa, N-1 lần, N lần (cận trên), và N+1 lần (nếu có thể)."
    },
    {
        "id": "Q159",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Equivalence Partitioning",
        "type": "Single",
        "question": "A web form accepts credit card types: Visa, MasterCard, and American Express. Any other credit card type is rejected. How many valid and invalid equivalence partitions are there?",
        "options": [
            "A. 1 valid partition, 1 invalid partition",
            "B. 3 valid partitions (Visa, MasterCard, Amex) and 1 invalid partition (any other card)",
            "C. 3 valid partitions and 3 invalid partitions",
            "D. Infinite valid partitions"
        ],
        "answer": "B",
        "explanation": "Có 3 giá trị hợp lệ riêng biệt được chấp nhận (3 valid partitions) và tất cả các loại thẻ khác gộp lại thành 1 phân vùng không hợp lệ (1 invalid partition)."
    },
    {
        "id": "Q160",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Path Testing",
        "type": "Single",
        "question": "What is an 'Independent Path' in a control flow graph?",
        "options": [
            "A. A path that has no edges.",
            "B. Any path through the code that introduces at least one new edge that is not part of any previously defined path.",
            "C. A path that never executes any statements.",
            "D. A test case written by an external vendor."
        ],
        "answer": "B",
        "explanation": "Đường đi độc lập (Independent Path / Basis Path) là một đường đi xuyên qua đồ thị luồng điều khiển từ điểm bắt đầu đến điểm kết thúc mà chứa ít nhất một cạnh nối (edge) chưa từng xuất hiện trong các đường đi đã xác định trước đó."
    },
    {
        "id": "Q161",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Use Case Testing",
        "type": "Single",
        "question": "Who is an 'Actor' in the context of Use Case Testing?",
        "options": [
            "A. A Hollywood movie celebrity.",
            "B. A person, external system, or hardware device that interacts with the system to achieve a specific goal.",
            "C. The developer who wrote the unit test.",
            "D. The relational database schema."
        ],
        "answer": "B",
        "explanation": "Trong Use Case, Actor (Tác nhân) là người dùng, hệ thống bên ngoài hoặc thiết bị phần cứng tương tác với hệ thống đang kiểm thử để thực hiện một mục tiêu cụ thể."
    },
    {
        "id": "Q162",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Branch Coverage Calculation",
        "type": "Single",
        "question": "Consider a C function with a 'switch(x)' statement containing 4 'case' blocks and 1 'default' block. How many branch outcomes must be executed to achieve 100% Decision (Branch) Coverage for this switch?",
        "options": [
            "A. 1",
            "B. 4",
            "C. 5",
            "D. 10"
        ],
        "answer": "C",
        "explanation": "Cấu trúc switch có 4 nhánh case và 1 nhánh default -> tổng cộng có 5 nhánh rẽ độc lập. Để đạt 100% Branch Coverage, cần kiểm thử cả 5 nhánh (5 test cases)."
    },
    {
        "id": "Q163",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Decision Table Testing",
        "type": "Single",
        "question": "Why is Decision Table Testing particularly valuable for testing complex business logic?",
        "options": [
            "A. Because it generates source code automatically.",
            "B. Because it systematically reveals combinations of conditions that might otherwise be overlooked or missing in specifications.",
            "C. Because it proves that the software has 0 bugs.",
            "D. Because it replaces the need for performance testing."
        ],
        "answer": "B",
        "explanation": "Bảng quyết định cực kỳ hữu ích với logic nghiệp vụ phức tạp vì nó liệt kê có hệ thống mọi tổ hợp điều kiện, giúp phát hiện ngay các kịch bản bị bỏ sót hoặc mâu thuẫn trong tài liệu đặc tả."
    },
    {
        "id": "Q164",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.4 Experience-based Techniques",
        "type": "Single",
        "question": "What is the primary drawback of relying EXCLUSIVELY on experience-based test techniques?",
        "options": [
            "A. They are too formal and require too much paperwork.",
            "B. Test coverage is subjective, unpredictable, difficult to quantify, and heavily dependent on individual tester skill.",
            "C. They can only be executed by automated test robots.",
            "D. They guarantee 100% statement coverage."
        ],
        "answer": "B",
        "explanation": "Nhược điểm lớn nhất của kỹ thuật dựa trên kinh nghiệm: Độ bao phủ kiểm thử mang tính chủ quan, khó đo lường chính xác bằng số liệu, và phụ thuộc quá nhiều vào năng lực cá nhân của người test."
    },
    {
        "id": "Q165",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: State Transition Testing",
        "type": "Single",
        "question": "In a state diagram, what triggers a 'Transition' from one state to another?",
        "options": [
            "A. An Event (optionally accompanied by a guard condition and an action)",
            "B. A compiler warning",
            "C. A Jira sprint retro meeting",
            "D. An increase in server temperature"
        ],
        "answer": "A",
        "explanation": "Một bước chuyển trạng thái (Transition) được kích hoạt bởi một Sự kiện (Event/Input), có thể đi kèm Điều kiện bảo vệ (Guard condition) và sinh ra một Hành động (Action)."
    },
    {
        "id": "Q166",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Statement Coverage",
        "type": "Single",
        "question": "Can 100% Statement Coverage detect that an 'else' branch is missing in an 'if' construct?",
        "options": [
            "A. Yes, statement coverage always detects missing branches.",
            "B. No, because if the condition evaluates to True, 100% statement coverage is achieved without ever exercising what happens when the condition is False.",
            "C. Yes, but only in Java.",
            "D. Statement coverage is not applicable to if statements."
        ],
        "answer": "B",
        "explanation": "100% Statement Coverage không thể phát hiện thiếu nhánh else vì khi chạy nhánh True, toàn bộ dòng lệnh đã được thực thi 100%, bỏ qua hoàn toàn hành vi khi điều kiện False."
    },
    {
        "id": "Q167",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Equivalence Partitioning",
        "type": "Single",
        "question": "A discount coupon gives 15% discount if the shopping cart total is between $100 and $500 (inclusive). What are the invalid partitions?",
        "options": [
            "A. Total < $100 and Total > $500",
            "B. Total = $100 and Total = $500",
            "C. Total between $200 and $300",
            "D. Total = $250"
        ],
        "answer": "A",
        "explanation": "Phân vùng hợp lệ là [$100, $500]. Hai phân vùng không hợp lệ là: Total < $100 (ví dụ $99.99) và Total > $500 (ví dụ $500.01)."
    },
    {
        "id": "Q168",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.3 White-box: Decision Coverage",
        "type": "Multiple",
        "question": "Which TWO of the following statements about White-box testing are TRUE? (Choose TWO options)",
        "options": [
            "A. 100% Decision Coverage guarantees 100% Statement Coverage.",
            "B. White-box testing requires no knowledge of the internal code structure.",
            "C. Cyclomatic complexity defines the minimum number of independent paths for decision coverage.",
            "D. 100% Statement coverage guarantees that the software has no bugs.",
            "E. White-box testing can only be done during User Acceptance Testing."
        ],
        "answer": "A, C",
        "explanation": "100% Decision Coverage luôn đảm bảo 100% Statement Coverage (A). Cyclomatic complexity xác định số đường đi độc lập tối thiểu để đạt độ bao phủ nhánh (C)."
    },
    {
        "id": "Q169",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.2 Black-box: Boundary Value Analysis",
        "type": "Single",
        "question": "Why does Boundary Value Analysis often discover more defects than Equivalence Partitioning alone?",
        "options": [
            "A. Because programmers frequently make off-by-one errors (e.g., using '>' instead of '>=') at the boundary edges of conditional statements.",
            "B. Because boundary values are chosen completely at random.",
            "C. Because boundary tests do not require expected results.",
            "D. Because boundary testing only runs on 64-bit operating systems."
        ],
        "answer": "A",
        "explanation": "Các lập trình viên thường xuyên mắc lỗi 'lệch 1 đơn vị' (off-by-one errors, nhầm lẫn giữa > và >=, hoặc < và <=) tại các điểm ranh giới của điều kiện. Vì vậy BVA bắt được rất nhiều lỗi biên mà việc chọn một giá trị ngẫu nhiên ở giữa phân vùng bỏ sót."
    },
    {
        "id": "Q170",
        "chapter": "Chapter 4: Test Analysis and Design",
        "topic": "4.4 Experience-based Techniques",
        "type": "Single",
        "question": "In which scenario would Exploratory Testing be the MOST effective supplement to formal scripted testing?",
        "options": [
            "A. Right after all scripted regression tests have passed, to investigate unexpected edge behaviors and complex interactions.",
            "B. Instead of writing any requirements documents at the start of a multi-million dollar defense contract.",
            "C. When testing must be executed by automated Jenkins pipelines without human intervention.",
            "D. When no software build has been compiled yet."
        ],
        "answer": "A",
        "explanation": "Exploratory testing là sự bổ trợ tuyệt vời sau khi bộ test scripted chính quy đã pass: tester tự do khám phá các góc khuất, các tổ hợp tương tác phức tạp và các hành vi bất ngờ của hệ thống mà kịch bản có sẵn chưa tính đến."
    }
]
