# data_ch1.py - Chapter 1: Fundamentals of Testing (35 Questions)

CH1_QUESTIONS = [
    {
        "id": "Q001",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.1 What is Testing?",
        "type": "Single",
        "question": "Which of the following is a PRIMARY objective of testing?",
        "options": [
            "A. To prove that the software has no defects.",
            "B. To analyze the code and remove all identified faults.",
            "C. To evaluate work products, prevent defects, and find failures.",
            "D. To ensure that 100% of the software paths are executed."
        ],
        "answer": "C",
        "explanation": "Mục tiêu chính của testing bao gồm: đánh giá work products (requirements, design, code), ngăn ngừa defect (thông qua review sớm), tìm kiếm defects/failures, xây dựng độ tin cậy và cung cấp thông tin cho stakeholders. A sai vì kiểm thử chỉ chỉ ra sự hiện diện của lỗi, không chứng minh phần mềm không có lỗi (Nguyên lý 1). B là mục tiêu của Debugging, không phải Testing. D sai vì exhaustive testing là bất khả thi (Nguyên lý 2)."
    },
    {
        "id": "Q002",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.1 What is Testing?",
        "type": "Single",
        "question": "How does testing differ from debugging?",
        "options": [
            "A. Testing identifies the cause of failures, while debugging executes software to find defects.",
            "B. Dynamic testing shows failures caused by defects, while debugging locates the cause, fixes the code, and verifies the fix.",
            "C. Testing is performed exclusively by developers, while debugging is conducted exclusively by independent testers.",
            "D. Debugging only applies to static code reviews, while testing applies only to dynamic execution."
        ],
        "answer": "B",
        "explanation": "Testing (đặc biệt là dynamic testing) làm bộc lộ các failure do defect gây ra; trong khi Debugging là hoạt động (thường do developer thực hiện) nhằm xác định nguyên nhân gốc rễ (locate root cause), sửa mã nguồn (repair defect) và kiểm tra lại để đảm bảo đã sửa đúng."
    },
    {
        "id": "Q003",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.2 Why is Testing Necessary?",
        "type": "Single",
        "question": "A software developer makes a mistake while typing an algorithm, resulting in incorrect code logic. When the program runs with specific inputs, the calculation is wrong. According to the ISTQB glossary, what are these three phenomena termed, in order?",
        "options": [
            "A. Defect, Failure, Error",
            "B. Error (Mistake), Defect (Fault/Bug), Failure",
            "C. Failure, Defect, Error",
            "D. Bug, Mistake, Defect"
        ],
        "answer": "B",
        "explanation": "Thứ tự chuẩn theo ISTQB: Con người mắc lỗi/sai sót (Error/Mistake) -> tạo ra khuyết tật/lỗi trong mã nguồn hoặc tài liệu (Defect/Fault/Bug) -> khi chạy phần mềm trong điều kiện cụ thể, defect bộc lộ thành sự cố/hành vi sai lệch quan sát được (Failure)."
    },
    {
        "id": "Q004",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.2 Why is Testing Necessary?",
        "type": "Single",
        "question": "Which of the following statements correctly distinguishes Quality Assurance (QA) from Quality Control (QC)?",
        "options": [
            "A. QA is product-oriented and focuses on finding defects, while QC is process-oriented and focuses on preventing defects.",
            "B. QA is process-oriented and focuses on adherence to proper processes to prevent defects, while QC consists of product-oriented activities like testing to detect defects.",
            "C. QA and QC are identical terms and can be used interchangeably in all software projects.",
            "D. QC is strictly manual testing, while QA is automated testing."
        ],
        "answer": "B",
        "explanation": "Quality Assurance (QA) tập trung vào quy trình (process-oriented), đảm bảo quy trình được tuân thủ để ngăn ngừa khuyết tật ngay từ đầu. Quality Control (QC) tập trung vào sản phẩm (product-oriented), bao gồm các hoạt động như testing để phát hiện các khuyết tật trong sản phẩm trước khi phát hành."
    },
    {
        "id": "Q005",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.2 Why is Testing Necessary?",
        "type": "Single",
        "question": "An architect misunderstood the customer's concurrency requirement. As a result, the database schema lacked indexing on a high-traffic table, causing timeouts under peak loads. What was the ROOT CAUSE of the failure?",
        "options": [
            "A. The system timeout during peak hours.",
            "B. The missing indexes in the database schema.",
            "C. The architect's misunderstanding of the customer's concurrency requirement.",
            "D. The high volume of user traffic."
        ],
        "answer": "C",
        "explanation": "Root cause (nguyên nhân gốc rễ) là lý do cơ bản dẫn đến việc đưa ra defect. Ở đây, sự hiểu nhầm của kiến trúc sư về yêu cầu đồng thời (concurrency requirement) là nguyên nhân gốc rễ, dẫn đến defect (thiếu index), và gây ra failure (hệ thống bị timeout)."
    },
    {
        "id": "Q006",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.3 Seven Testing Principles",
        "type": "Single",
        "question": "A project manager states: 'Our testing team has executed thousands of tests and found zero defects this week, so the software is completely free of bugs.' Which testing principle directly contradicts this statement?",
        "options": [
            "A. Exhaustive testing is impossible.",
            "B. Testing shows the presence of defects, not their absence.",
            "C. Defects cluster together.",
            "D. Absence-of-errors is a fallacy."
        ],
        "answer": "B",
        "explanation": "Nguyên lý 1 (Testing shows the presence of defects, not their absence) khẳng định: Kiểm thử chỉ có thể chứng minh phần mềm có chứa lỗi, chứ không thể chứng minh phần mềm hoàn toàn không còn lỗi nào."
    },
    {
        "id": "Q007",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.3 Seven Testing Principles",
        "type": "Single",
        "question": "A team runs the exact same regression test suite for six months without adding new test cases. Over time, the suite discovers fewer and fewer defects, yet customers still report new bugs in production. Which testing principle explains this phenomenon?",
        "options": [
            "A. Pesticide paradox",
            "B. Defect clustering",
            "C. Early testing",
            "D. Context dependency"
        ],
        "answer": "A",
        "explanation": "Pesticide Paradox (Nghịch lý thuốc trừ sâu): Nếu các bài test giống hệt nhau được lặp đi lặp lại nhiều lần, cuối cùng chúng sẽ không tìm thêm được defect mới nào nữa. Để tìm được defect mới, cần thường xuyên cập nhật, sửa đổi test cases và viết thêm test cases mới."
    },
    {
        "id": "Q008",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.3 Seven Testing Principles",
        "type": "Single",
        "question": "Analysis of a large telecom billing system shows that approximately 80% of all reported production incidents originated from only 20% of its software modules. Which testing principle does this illustrate?",
        "options": [
            "A. Absence-of-errors is a fallacy",
            "B. Defects cluster together (Pareto Principle)",
            "C. Early testing saves time and money",
            "D. Exhaustive testing is impossible"
        ],
        "answer": "B",
        "explanation": "Defects cluster together (Lỗi thường tập trung): Theo quy luật Pareto (80/20), phần lớn các lỗi phát sinh thường tập trung ở một số lượng nhỏ các module phức tạp hoặc có nhiều tương tác."
    },
    {
        "id": "Q009",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.3 Seven Testing Principles",
        "type": "Single",
        "question": "A software product has been tested rigorously against all documented technical requirements, and zero defects remain open. However, when delivered to end-users, they find it difficult to use and unable to support their day-to-day business tasks. Which principle describes this situation?",
        "options": [
            "A. Exhaustive testing is impossible",
            "B. Absence-of-errors is a fallacy",
            "C. Pesticide paradox",
            "D. Testing is context dependent"
        ],
        "answer": "B",
        "explanation": "Absence-of-errors is a fallacy (Quan niệm sai lầm về việc không có lỗi): Việc sửa hết tất cả các lỗi và đáp ứng 100% tài liệu kỹ thuật không đảm bảo hệ thống sẽ thành công nếu hệ thống đó không hữu dụng hoặc không đáp ứng đúng nhu cầu thực tế của người dùng."
    },
    {
        "id": "Q010",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.3 Seven Testing Principles",
        "type": "Single",
        "question": "Why is testing an e-commerce web application conducted differently compared to testing the flight control software of a commercial airliner?",
        "options": [
            "A. Because exhaustive testing is possible for e-commerce, but not for avionics.",
            "B. Because of the principle: Testing is context dependent.",
            "C. Because avionics software does not have defects.",
            "D. Because pesticide paradox applies only to web applications."
        ],
        "answer": "B",
        "explanation": "Nguyên lý 'Testing is context dependent' (Kiểm thử phụ thuộc vào ngữ cảnh): Kiểm thử được thực hiện khác nhau tùy thuộc vào ngữ cảnh cụ thể (ví dụ ứng dụng y tế/hàng không cần tuân thủ tiêu chuẩn an toàn ngặt nghèo, trong khi trang web thương mại điện tử chú trọng trải nghiệm người dùng, tải cao và tính tương thích trình duyệt)."
    },
    {
        "id": "Q011",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.4 Test Process",
        "type": "Single",
        "question": "Which of the following lists the test process activities in the MOST LOGICAL chronological sequence?",
        "options": [
            "A. Test Planning -> Test Analysis -> Test Design -> Test Implementation -> Test Execution -> Test Completion",
            "B. Test Analysis -> Test Planning -> Test Execution -> Test Design -> Test Completion -> Test Monitoring",
            "C. Test Design -> Test Analysis -> Test Implementation -> Test Execution -> Test Planning",
            "D. Test Planning -> Test Execution -> Test Design -> Test Analysis -> Test Completion"
        ],
        "answer": "A",
        "explanation": "Quy trình kiểm thử chuẩn theo ISTQB: Test Planning (Lập kế hoạch) -> Test Analysis (Phân tích - What to test) -> Test Design (Thiết kế - How to test) -> Test Implementation (Triển khai - Chuẩn bị testware/data/env) -> Test Execution (Thực thi) -> Test Completion (Kết thúc)."
    },
    {
        "id": "Q012",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.4 Test Process",
        "type": "Single",
        "question": "During which activity of the test process are 'Test Conditions' identified and prioritized by evaluating the test basis?",
        "options": [
            "A. Test Planning",
            "B. Test Analysis",
            "C. Test Design",
            "D. Test Implementation"
        ],
        "answer": "B",
        "explanation": "Trong pha Test Analysis (Phân tích kiểm thử), tester nghiên cứu test basis (yêu cầu, kiến trúc...) để xác định 'What to test' dưới dạng các Test Conditions (điều kiện kiểm thử) và đánh giá khả năng kiểm thử (testability)."
    },
    {
        "id": "Q013",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.4 Test Process",
        "type": "Single",
        "question": "What is the primary difference between Test Design and Test Implementation?",
        "options": [
            "A. Test Design creates high-level test cases, while Test Implementation sequences them into test procedures and prepares test data/environment.",
            "B. Test Design executes tests, while Test Implementation logs defect reports.",
            "C. Test Design produces the Test Plan, while Test Implementation determines exit criteria.",
            "D. Test Design is performed by developers, while Test Implementation is done by business users."
        ],
        "answer": "A",
        "explanation": "Test Design trả lời câu hỏi 'How to test' (tạo test cases, test data requirements). Test Implementation trả lời câu hỏi 'Is everything in place to run the tests?' (sắp xếp test cases thành test procedures/test suites, tạo test data cụ thể, kiểm tra môi trường test)."
    },
    {
        "id": "Q014",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.4 Test Process",
        "type": "Single",
        "question": "Which test work product outlines the scope, objectives, schedule, resources, and risk management approach for a testing project?",
        "options": [
            "A. Test Charter",
            "B. Test Plan",
            "C. Test Summary Report",
            "D. Test Condition"
        ],
        "answer": "B",
        "explanation": "Test Plan (Kế hoạch kiểm thử) là tài liệu mô tả phạm vi (scope), mục tiêu (objectives), tài nguyên (resources), lịch trình (schedule) và các cách tiếp cận rủi ro cho hoạt động kiểm thử."
    },
    {
        "id": "Q015",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.4 Test Process",
        "type": "Single",
        "question": "Why is Bi-directional Traceability between the Test Basis and Test Work Products important?",
        "options": [
            "A. It guarantees that the code is completely bug-free.",
            "B. It enables impact analysis of changes, verifies test coverage, and facilitates test auditability.",
            "C. It allows developers to skip unit testing completely.",
            "D. It eliminates the need for test execution logging."
        ],
        "answer": "B",
        "explanation": "Bi-directional Traceability (Truy vết hai chiều) giữa yêu cầu (test basis) và test cases/test results giúp đánh giá phạm vi bao phủ (coverage), hỗ trợ phân tích tác động khi có thay đổi (impact analysis), và báo cáo tiến độ/kiểm toán rõ ràng."
    },
    {
        "id": "Q016",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.4 Test Process",
        "type": "Single",
        "question": "Which of the following tasks is performed as part of 'Test Completion'?",
        "options": [
            "A. Developing and prioritizing test procedures.",
            "B. Archiving testware, handing over test artifacts, and recording lessons learned.",
            "C. Comparing actual results against expected results.",
            "D. Defining test entry criteria for the next cycle."
        ],
        "answer": "B",
        "explanation": "Test Completion (Kết thúc kiểm thử) gồm các hoạt động: lưu trữ testware (archiving), bàn giao cho đội bảo trì, tổng kết bài học kinh nghiệm (lessons learned), và phát hành Test Summary Report."
    },
    {
        "id": "Q017",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.5 The Psychology of Testing",
        "type": "Single",
        "question": "Confirmation bias often impairs a developer's ability to test their own code effectively. What is confirmation bias?",
        "options": [
            "A. The tendency to search for, interpret, and recall information in a way that confirms one's preexisting beliefs.",
            "B. The conscious desire of a developer to deliver faulty code to the testing department.",
            "C. The inability of testers to write test automation scripts.",
            "D. The belief that exhaustive testing can easily be achieved with modern CI/CD tools."
        ],
        "answer": "A",
        "explanation": "Confirmation bias (Thiên kiến xác nhận) là xu hướng tâm lý tự nhiên của con người chỉ tìm kiếm và ghi nhận thông tin củng cố cho niềm tin có sẵn của mình (developer tin rằng code mình viết đúng, nên có xu hướng chỉ test các trường hợp làm cho code chạy thành công)."
    },
    {
        "id": "Q018",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.5 The Psychology of Testing",
        "type": "Single",
        "question": "Which of the following communication practices is recommended when a tester reports a defect to a developer?",
        "options": [
            "A. Blame the developer directly in the bug report title for carelessness.",
            "B. Communicate findings neutrally, objectively, and fact-focused, emphasizing the common goal of product quality.",
            "C. Wait until the end of the release before reporting any defects so developers are not disturbed.",
            "D. Only communicate defects verbally without writing steps to reproduce."
        ],
        "answer": "B",
        "explanation": "Giao tiếp trong kiểm thử cần trung lập, khách quan, dựa trên sự thật (fact-focused), không chỉ trích cá nhân, và hướng đến mục tiêu chung là nâng cao chất lượng sản phẩm."
    },
    {
        "id": "Q019",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.1 What is Testing?",
        "type": "Multiple",
        "question": "Which TWO of the following are typical objectives of testing? (Choose TWO options)",
        "options": [
            "A. Gaining confidence in the level of quality of the test object.",
            "B. Fixing all bugs found in the source code.",
            "C. Providing sufficient information to stakeholders to make informed decisions.",
            "D. Proving that the software cannot fail under any circumstance.",
            "E. Rewriting user stories to match development progress."
        ],
        "answer": "A, C",
        "explanation": "Mục tiêu điển hình của testing là xây dựng độ tin cậy vào chất lượng (A) và cung cấp thông tin để stakeholders đưa ra quyết định phát hành (C). B là việc của debugging; D vi phạm nguyên lý kiểm thử; E không phải là mục tiêu của kiểm thử."
    },
    {
        "id": "Q020",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.2 Why is Testing Necessary?",
        "type": "Single",
        "question": "A radiation therapy machine administered massive radiation overdoses to patients due to a race condition bug in the software. This real-world incident illustrates that:",
        "options": [
            "A. Software defects can cause severe financial loss, physical injury, or loss of life.",
            "B. All medical software should be tested exclusively with random testing.",
            "C. Debugging is sufficient to ensure complete system safety.",
            "D. Static analysis eliminates all runtime concurrency defects."
        ],
        "answer": "A",
        "explanation": "Ví dụ nổi tiếng về Therac-25 trong giáo trình kiểm thử minh họa rằng các lỗi phần mềm có thể gây thiệt hại nặng nề về tài chính, uy tín thương hiệu và thậm chí nguy hiểm đến tính mạng con người."
    },
    {
        "id": "Q021",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.3 Seven Testing Principles",
        "type": "Single",
        "question": "Why is 'Early Testing' (Shift Left) considered a best practice in software engineering?",
        "options": [
            "A. It allows testers to finish their jobs before development starts.",
            "B. The cost of finding and fixing a defect increases significantly in later phases of the SDLC.",
            "C. It prevents users from changing requirements during the project.",
            "D. It guarantees that no dynamic testing will be needed."
        ],
        "answer": "B",
        "explanation": "Nguyên lý 'Early testing saves time and money' (Shift Left): Chi phí phát hiện và sửa chữa khuyết tật ở giai đoạn yêu cầu hoặc thiết kế rẻ hơn rất nhiều (thường gấp hàng chục đến hàng trăm lần) so với khi phát hiện ở giai đoạn System test hoặc sau khi đã Release lên Production."
    },
    {
        "id": "Q022",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.4 Test Process",
        "type": "Single",
        "question": "What is the document containing preconditions, input values, expected results, and postconditions developed to verify compliance with a specific requirement called?",
        "options": [
            "A. Test Policy",
            "B. Test Condition",
            "C. Test Case",
            "D. Test Log"
        ],
        "answer": "C",
        "explanation": "Test Case (Trường hợp kiểm thử) là tập hợp các giá trị đầu vào (inputs), điều kiện tiên quyết (preconditions), kết quả mong đợi (expected results) và hậu điều kiện (postconditions) được phát triển cho một mục tiêu cụ thể."
    },
    {
        "id": "Q023",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.4 Test Process",
        "type": "Single",
        "question": "Which of the following is defined as 'an aspect of the test basis that can be verified by one or more test cases'?",
        "options": [
            "A. Test Condition",
            "B. Test Procedure",
            "C. Test Suite",
            "D. Test Strategy"
        ],
        "answer": "A",
        "explanation": "Test Condition (Điều kiện kiểm thử) là một khía cạnh hoặc thành phần của test basis có thể kiểm tra được bằng một hoặc nhiều test cases (ví dụ: 'chức năng đăng nhập thành công', 'xử lý khi nhập sai mật khẩu 3 lần')."
    },
    {
        "id": "Q024",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.4 Test Process",
        "type": "Single",
        "question": "What is a 'Test Procedure' (or Test Script)?",
        "options": [
            "A. A high-level description of business risks.",
            "B. A sequence of test cases in execution order, including any associated actions needed to set up initial preconditions and wrap up.",
            "C. A tool used solely for performance stress testing.",
            "D. A contract signed between the client and development manager."
        ],
        "answer": "B",
        "explanation": "Test Procedure (hoặc manual test script) là một chuỗi các test cases được sắp xếp theo trình tự thực thi cụ thể, bao gồm cả các bước thiết lập môi trường/dữ liệu ban đầu và các bước dọn dẹp sau khi chạy xong."
    },
    {
        "id": "Q025",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.4 Test Process",
        "type": "Single",
        "question": "What metric is evaluated during 'Test Monitoring and Control' to decide whether test execution can stop?",
        "options": [
            "A. Number of lines of code written per day.",
            "B. Exit criteria (Definition of Done for testing).",
            "C. Time spent in coffee breaks.",
            "D. Number of developer commits in the main branch."
        ],
        "answer": "B",
        "explanation": "Exit criteria (Tiêu chí dừng/hoàn thành kiểm thử) bao gồm các tiêu chí như: độ bao phủ đạt ngưỡng quy định, không còn lỗi blocker/critical nào mở, số lượng test case pass đạt yêu cầu, v.v."
    },
    {
        "id": "Q026",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.5 The Psychology of Testing",
        "type": "Single",
        "question": "Which of the following mindsets is MOST characteristic of an effective tester?",
        "options": [
            "A. Constructive optimism that assumes the code works properly until a user complains.",
            "B. Professional curiosity, critical thinking, attention to detail, and a mindset of healthy skepticism.",
            "C. Reluctance to point out flaws to avoid upsetting team members.",
            "D. Focusing solely on happy path scenarios to meet delivery deadlines."
        ],
        "answer": "B",
        "explanation": "Tư duy của một tester giỏi (Tester's mindset) bao gồm: tính tò mò (curiosity), hoài nghi tích cực (professional skepticism), tư duy phản biện (critical thinking) và chú ý đến chi tiết."
    },
    {
        "id": "Q027",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.1 What is Testing?",
        "type": "Single",
        "question": "Does testing only consist of running the software (dynamic execution)?",
        "options": [
            "A. Yes, static testing is part of development, not testing.",
            "B. No, testing also includes static activities such as reviewing requirements, design documents, and user stories.",
            "C. Yes, testing requires compiling and executing binary code.",
            "D. No, testing only includes automated unit testing."
        ],
        "answer": "B",
        "explanation": "Testing không chỉ gồm dynamic testing (thực thi phần mềm) mà còn bao gồm cả static testing (review tài liệu yêu cầu, kiến trúc, thiết kế, static code analysis)."
    },
    {
        "id": "Q028",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.2 Why is Testing Necessary?",
        "type": "Single",
        "question": "Which of the following CANNOT be considered a direct defect in software?",
        "options": [
            "A. An incorrect mathematical calculation formula in a billing algorithm.",
            "B. A missing validation check on a user input field.",
            "C. An earthquake that physically destroys the data center hosting the servers.",
            "D. An unhandled null pointer exception in a backend service."
        ],
        "answer": "C",
        "explanation": "Động đất làm sập trung tâm dữ liệu là một điều kiện/thảm họa môi trường bên ngoài (environmental condition), không phải là khuyết tật (defect) bên trong phần mềm."
    },
    {
        "id": "Q029",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.3 Seven Testing Principles",
        "type": "Single",
        "question": "If someone claims they will conduct 'exhaustive testing' for a module accepting three 32-bit integer inputs, why is their claim unfeasible?",
        "options": [
            "A. Because exhaustive testing requires automated tools which are too expensive.",
            "B. Because the number of input combinations is (2^32)^3 = 2^96, which would take millions of years to execute.",
            "C. Because integers cannot be tested with black-box techniques.",
            "D. Because ISTQB forbids testing more than two inputs at once."
        ],
        "answer": "B",
        "explanation": "Nguyên lý 'Exhaustive testing is impossible': Việc kiểm thử mọi tổ hợp đầu vào và tiền điều kiện là bất khả thi về mặt thời gian và chi phí do số lượng tổ hợp quá khổng lồ (2^96 tổ hợp)."
    },
    {
        "id": "Q030",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.4 Test Process",
        "type": "Single",
        "question": "What is the primary purpose of a 'Test Execution Log'?",
        "options": [
            "A. To document the chronological record of all details during test execution, such as test case IDs, tester name, timestamps, and pass/fail status.",
            "B. To describe the overall testing budget and project schedule.",
            "C. To list the names of employees to be laid off if testing fails.",
            "D. To assign Jira story points to developers."
        ],
        "answer": "A",
        "explanation": "Test Execution Log (Nhật ký thực thi kiểm thử) ghi lại tuần tự chi tiết quá trình chạy test: ai chạy, khi nào, test case nào, kết quả pass/fail, bằng chứng/screenshots, mã lỗi liên quan."
    },
    {
        "id": "Q031",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.4 Test Process",
        "type": "Multiple",
        "question": "Which THREE of the following are recognized test work products in the ISTQB test process? (Choose THREE options)",
        "options": [
            "A. Test Plan",
            "B. Defect Report",
            "C. Product Backlog Item",
            "D. Test Summary Report",
            "E. Source Code Repository"
        ],
        "answer": "A, B, D",
        "explanation": "Test Plan, Defect Report và Test Summary Report là các sản phẩm công việc kiểm thử (Test work products). Product Backlog Item là của Product Owner/Agile; Source Code Repository là của Developers."
    },
    {
        "id": "Q032",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.2 Why is Testing Necessary?",
        "type": "Single",
        "question": "When can a defect in software exist without causing a failure?",
        "options": [
            "A. It can never happen; every defect immediately causes a failure.",
            "B. When the specific code path containing the defect is never executed, or specific trigger conditions are not met.",
            "C. Only when the software is written in Python.",
            "D. Defects only exist after a failure is logged in Jira."
        ],
        "answer": "B",
        "explanation": "Một defect có thể nằm im trong mã nguồn (dormant) mà không bao giờ bộc lộ thành failure nếu nhánh mã đó không được chạy tới hoặc các điều kiện kích hoạt lỗi (inputs/môi trường cụ thể) không xảy ra."
    },
    {
        "id": "Q033",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.5 The Psychology of Testing",
        "type": "Single",
        "question": "Why can destructive criticism from a tester during defect reporting cause project friction?",
        "options": [
            "A. Because developers are legally prohibited from receiving feedback.",
            "B. Because finding faults in someone's work can be perceived as personal criticism; clear, polite, and fact-based communication prevents defensiveness.",
            "C. Because testers are not allowed to talk to developers under the V-model.",
            "D. Because defects should be kept secret from management."
        ],
        "answer": "B",
        "explanation": "Tâm lý học kiểm thử: Việc chỉ ra lỗi trong sản phẩm do người khác tạo ra dễ bị hiểu nhầm là chỉ trích cá nhân. Do đó, tester cần giữ thái độ khách quan, tập trung vào sự thật (fact-based) và tôn trọng đồng nghiệp."
    },
    {
        "id": "Q034",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.4 Test Process",
        "type": "Single",
        "question": "During which phase of the test process are automated test execution scripts written and verified?",
        "options": [
            "A. Test Analysis",
            "B. Test Design",
            "C. Test Implementation",
            "D. Test Completion"
        ],
        "answer": "C",
        "explanation": "Trong pha Test Implementation (Triển khai kiểm thử), các test cases được cụ thể hóa, các automated test scripts được lập trình và xác minh, bộ dữ liệu kiểm thử được nạp vào hệ thống."
    },
    {
        "id": "Q035",
        "chapter": "Chapter 1: Fundamentals of Testing",
        "topic": "1.1 What is Testing?",
        "type": "Single",
        "question": "Which of the following represents a VALIDATION activity rather than a Verification activity?",
        "options": [
            "A. Reviewing whether the software requirements specification matches system design documents.",
            "B. Conducting user acceptance testing with real end-users to confirm the system fulfills their operational needs.",
            "C. Running a linter on Java source code to ensure compliance with coding guidelines.",
            "D. Checking whether test cases cover 100% of the requirements matrix."
        ],
        "answer": "B",
        "explanation": "Verification là kiểm tra 'Are we building the product right?' (kiểm tra tính đúng đắn so với đặc tả). Validation là kiểm tra 'Are we building the right product?' (kiểm tra xem sản phẩm có đáp ứng đúng nhu cầu và mong đợi của người dùng thực tế hay không - UAT là ví dụ điển hình)."
    }
]
