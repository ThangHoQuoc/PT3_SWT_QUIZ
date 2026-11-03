# data_ch5.py - Chapter 5: Test Management (45 Questions)

CH5_QUESTIONS = [
    {
        "id": "Q171",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.1 Test Organization",
        "type": "Single",
        "question": "Which of the following represents the HIGHEST level of test independence according to ISTQB?",
        "options": [
            "A. Developers testing their own code.",
            "B. Independent developers or peers from the same development team testing each other's code.",
            "C. Independent test team within the organization reporting to project management.",
            "D. Independent external test specialists (e.g., third-party certification or security specialists) outside the organization."
        ],
        "answer": "D",
        "explanation": "Thang đo tính độc lập của kiểm thử (từ thấp đến cao): 1. Lập trình viên tự test code của mình -> 2. Đồng nghiệp trong nhóm phát triển test chéo -> 3. Đội kiểm thử độc lập nội bộ trong tổ chức -> 4. Người dùng/khách hàng độc lập -> 5. Chuyên gia kiểm thử độc lập bên ngoài tổ chức (highest independence)."
    },
    {
        "id": "Q172",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.1 Test Organization",
        "type": "Single",
        "question": "What is a potential DISADVANTAGE of having completely independent testers working in total isolation from developers?",
        "options": [
            "A. Independent testers find too many defects.",
            "B. Communication isolation, lack of shared ownership of quality, and developers may lose a sense of responsibility for defect prevention.",
            "C. Independent testing is strictly forbidden by ISTQB.",
            "D. Independent testers cannot use automated testing tools."
        ],
        "answer": "B",
        "explanation": "Nhược điểm tiềm ẩn khi đội tester quá độc lập và tách biệt: Thiếu giao tiếp cởi mở, developer có thể ỷ lại ('đã có tester lo rồi nên không cần cẩn thận'), làm giảm tinh thần trách nhiệm chung về chất lượng sản phẩm."
    },
    {
        "id": "Q173",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.1 Test Organization",
        "type": "Single",
        "question": "Which of the following tasks is TYPICALLY performed by the Test Manager (Test Leader) rather than a Tester?",
        "options": [
            "A. Analyzing requirements and designing detailed test cases.",
            "B. Setting up the test execution environment and preparing test data.",
            "C. Developing and updating the Test Plan, allocating resources, and selecting test metrics.",
            "D. Executing manual test procedures and logging bug tickets in Jira."
        ],
        "answer": "C",
        "explanation": "Nhiệm vụ của Test Manager (Test Leader): Lập và cập nhật Kế hoạch kiểm thử (Test Plan), phân bổ nguồn lực, lựa chọn các chỉ số đo lường (metrics), quản lý cấu hình và viết báo cáo tổng kết (Test Summary Report). A, B, D là nhiệm vụ của Tester."
    },
    {
        "id": "Q174",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.1 Test Organization",
        "type": "Single",
        "question": "Which of the following tasks is TYPICALLY performed by a Tester rather than the Test Manager?",
        "options": [
            "A. Writing the company-wide Test Policy.",
            "B. Deciding which testing metrics to report to upper executive management.",
            "C. Designing, implementing, and executing test cases and test suites.",
            "D. Negotiating testing budget with external clients."
        ],
        "answer": "C",
        "explanation": "Tester là người trực tiếp thiết kế (design), chuẩn bị (implement) và thực thi (execute) các test cases và test suites. Các việc mang tính chiến lược, chính sách và ngân sách thuộc về Test Manager."
    },
    {
        "id": "Q175",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.2 Test Planning and Estimation",
        "type": "Single",
        "question": "Which international standard defined the traditional industry benchmark format for Software Test Documentation, including the Test Plan template?",
        "options": [
            "A. IEEE 829 (now ISO/IEC/IEEE 29119-3)",
            "B. ISO 9001",
            "C. IEEE 754",
            "D. RFC 2616"
        ],
        "answer": "A",
        "explanation": "IEEE 829 (tiêu chuẩn về tài liệu kiểm thử phần mềm, hiện nay được cập nhật trong bộ chuẩn ISO/IEC/IEEE 29119-3) định nghĩa cấu trúc chuẩn cho Test Plan, Test Case, Test Log, Test Incident Report, và Test Summary Report."
    },
    {
        "id": "Q176",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.2 Test Planning and Estimation",
        "type": "Single",
        "question": "A test team prioritizes and designs tests based primarily on the probability and consequence of potential software failures. Which test strategy is this?",
        "options": [
            "A. Model-based strategy",
            "B. Analytical strategy (Risk-based testing)",
            "C. Reactive strategy",
            "D. Methodical strategy"
        ],
        "answer": "B",
        "explanation": "Chiến lược phân tích (Analytical Strategy), điển hình là Risk-based testing (Kiểm thử dựa trên rủi ro), phân tích xác suất và mức độ tác động của các lỗi tiềm ẩn để định hướng và ưu tiên các bài kiểm thử."
    },
    {
        "id": "Q177",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.2 Test Planning and Estimation",
        "type": "Single",
        "question": "Which test strategy relies heavily on testing against formal checklists of common defects, ISO standard quality attributes, or organizational guidelines?",
        "options": [
            "A. Methodical strategy",
            "B. Reactive strategy",
            "C. Consultative strategy",
            "D. Model-based strategy"
        ],
        "answer": "A",
        "explanation": "Chiến lược bài bản (Methodical Strategy): Sử dụng có hệ thống các tập hợp kiểm tra định sẵn, chẳng hạn như checklists về các lỗi phổ biến, các danh mục thuộc tính chất lượng theo chuẩn ISO 25010, hoặc hướng dẫn giao diện người dùng."
    },
    {
        "id": "Q178",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.2 Test Planning and Estimation",
        "type": "Single",
        "question": "A team decides to spend the majority of testing effort building automated regression test suites and continuous integration pipelines to minimize the danger of regression bugs. What test strategy is this?",
        "options": [
            "A. Regression-averse strategy",
            "B. Directed strategy",
            "C. Reactive strategy",
            "D. Consultative strategy"
        ],
        "answer": "A",
        "explanation": "Chiến lược chống hồi quy (Regression-averse Strategy): Tập trung tối đa vào việc phòng ngừa và phát hiện lỗi hồi quy bằng cách xây dựng bộ kịch bản tự động hóa mạnh mẽ và chạy liên tục trong CI/CD pipeline."
    },
    {
        "id": "Q179",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.2 Test Planning and Estimation",
        "type": "Single",
        "question": "Which test strategy delays test design until the software is actually delivered, letting testing adapt reactively based on findings during exploratory execution?",
        "options": [
            "A. Reactive strategy",
            "B. Analytical strategy",
            "C. Standard-compliant strategy",
            "D. Model-based strategy"
        ],
        "answer": "A",
        "explanation": "Chiến lược phản ứng (Reactive Strategy): Hoạt động kiểm thử được kích hoạt và điều chỉnh dựa trên sự tương tác thực tế với phần mềm (như Exploratory Testing), thay vì lập kế hoạch chi tiết từ trước."
    },
    {
        "id": "Q180",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.2 Test Planning and Estimation",
        "type": "Single",
        "question": "What is the purpose of 'Entry Criteria' (Definition of Ready) in a Test Plan?",
        "options": [
            "A. To determine when testing has completed and software can be released.",
            "B. To define the prerequisite conditions that must be satisfied before a specific test level or test activity can officially start.",
            "C. To list the names of employees entering the office.",
            "D. To calculate developer severance packages."
        ],
        "answer": "B",
        "explanation": "Entry Criteria (Tiêu chí đầu vào) xác định các điều kiện tiên quyết cần được thỏa mãn trước khi một giai đoạn kiểm thử có thể chính thức bắt đầu (ví dụ: môi trường test đã sẵn sàng, smoke test pass 100%, tài liệu yêu cầu đã được review)."
    },
    {
        "id": "Q181",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.2 Test Planning and Estimation",
        "type": "Single",
        "question": "Which of the following is a typical 'Exit Criteria' (Definition of Done) for System Testing?",
        "options": [
            "A. 100% of planned test cases executed, 95% pass rate, and zero open Blocker or Critical defects.",
            "B. The test environment has been turned on.",
            "C. All testers have arrived at the testing lab.",
            "D. A new sprint backlog is opened."
        ],
        "answer": "A",
        "explanation": "Exit Criteria (Tiêu chí dừng/hoàn thành) xác định khi nào mục tiêu kiểm thử đã đạt được (ví dụ: đạt độ bao phủ quy định, tỷ lệ pass cao, không còn lỗi nghiêm trọng nào tồn đọng)."
    },
    {
        "id": "Q182",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.2 Test Planning and Estimation",
        "type": "Single",
        "question": "In test estimation, what is the 'Wideband Delphi' technique?",
        "options": [
            "A. A technique where an automated AI calculates the testing budget.",
            "B. An expert-based consensus estimation method where a panel of experts independently estimate effort, discuss differences in an anonymous iterative meeting, and converge on an estimate.",
            "C. An algorithm measuring database latency.",
            "D. An outsourced vendor pricing model."
        ],
        "answer": "B",
        "explanation": "Wideband Delphi là kỹ thuật ước lượng dựa trên chuyên gia (expert-based) theo cơ chế đồng thuận: một nhóm các chuyên gia ước lượng độc lập, sau đó thảo luận ẩn danh qua nhiều vòng lặp để thu hẹp khoảng cách và hội tụ về một con số ước lượng thống nhất."
    },
    {
        "id": "Q183",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.2 Test Planning and Estimation",
        "type": "Single",
        "question": "What is the primary difference between 'Metrics-based' and 'Expert-based' test estimation approaches?",
        "options": [
            "A. Metrics-based uses historical data and mathematical formulas from past projects; Expert-based relies on the intuition and experience of technical experts.",
            "B. Metrics-based only works on Windows; Expert-based works on Linux.",
            "C. Metrics-based is free; Expert-based costs $1,000 per hour.",
            "D. Metrics-based cannot estimate unit testing."
        ],
        "answer": "A",
        "explanation": "Metrics-based (dựa trên số liệu) sử dụng dữ liệu đo đạc thực tế từ các dự án tương tự trong quá khứ hoặc các công thức toán học; trong khi Expert-based (dựa trên chuyên gia) dựa trên trực giác, hiểu biết và kinh nghiệm thực tiễn của những người có chuyên môn."
    },
    {
        "id": "Q184",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.5 Risks and Testing",
        "type": "Single",
        "question": "How is the 'Level of Risk' mathematically determined in Risk-Based Testing?",
        "options": [
            "A. Risk Level = Likelihood of failure * Impact of failure",
            "B. Risk Level = Number of lines of code / Number of developers",
            "C. Risk Level = Total project cost + Server hardware cost",
            "D. Risk Level = Number of test cases * 100%"
        ],
        "answer": "A",
        "explanation": "Mức độ rủi ro (Risk Level / Risk Priority Number) = Xác suất xảy ra rủi ro (Likelihood/Probability) nhân với Mức độ tác hại/hậu quả nếu rủi ro xảy ra (Impact/Consequence)."
    },
    {
        "id": "Q185",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.5 Risks and Testing",
        "type": "Single",
        "question": "Which of the following is classified as a PRODUCT RISK (Quality Risk) rather than a Project Risk?",
        "options": [
            "A. The software calculation algorithm computes an inaccurate interest rate for loan customers.",
            "B. A key senior test automation engineer resigns in the middle of the project.",
            "C. The third-party hardware vendor delays delivery of the testing server by 4 weeks.",
            "D. Management reduces the testing budget by 30%."
        ],
        "answer": "A",
        "explanation": "Product Risk (Rủi ro sản phẩm) là rủi ro liên quan trực tiếp đến chất lượng và tính năng của phần mềm (ví dụ: tính sai lãi suất, hổng bảo mật, lỗi crash). Các phương án B, C, D liên quan đến tiến độ, nhân sự, nhà cung cấp và ngân sách -> đó là Project Risk (Rủi ro dự án)."
    },
    {
        "id": "Q186",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.5 Risks and Testing",
        "type": "Single",
        "question": "Which of the following is classified as a PROJECT RISK (Management Risk)?",
        "options": [
            "A. An online transaction module fails to encrypt credit card numbers.",
            "B. Contractual dispute with an outsourced software vendor leading to schedule delays.",
            "C. The mobile app crashes when switching between portrait and landscape modes.",
            "D. The search engine returns zero results for valid keyword queries."
        ],
        "answer": "B",
        "explanation": "Tranh chấp hợp đồng với nhà thầu phụ gây chậm tiến độ dự án là Project Risk (rủi ro quản lý/dự án). Các phương án A, C, D là Product Risk."
    },
    {
        "id": "Q187",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.5 Risks and Testing",
        "type": "Single",
        "question": "In Risk-Based Testing, which items should be tested FIRST and with the HIGHEST DEPTH of test coverage?",
        "options": [
            "A. Items with High Likelihood and High Impact (Highest Risk Level).",
            "B. Items that are easiest to automate.",
            "C. Items with Low Likelihood and Low Impact.",
            "D. Items chosen alphabetically by feature name."
        ],
        "answer": "A",
        "explanation": "Trong kiểm thử dựa trên rủi ro (RBT), những tính năng có rủi ro cao nhất (xác suất xảy ra lỗi cao và mức độ thiệt hại nghiêm trọng nếu gặp lỗi - High Likelihood & High Impact) luôn được ưu tiên kiểm thử đầu tiên và bao phủ sâu nhất."
    },
    {
        "id": "Q188",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.6 Defect Management",
        "type": "Single",
        "question": "What is the difference between DEFECT SEVERITY and DEFECT PRIORITY?",
        "options": [
            "A. Severity reflects the technical impact/degree of damage caused by the defect; Priority reflects the urgency/business importance of fixing the defect.",
            "B. Severity is assigned by marketing; Priority is assigned by the compiler.",
            "C. Severity and Priority are identical terms with no distinction.",
            "D. Priority is measured in kilograms; Severity is measured in seconds."
        ],
        "answer": "A",
        "explanation": "Severity (Mức độ nghiêm trọng) thể hiện tác động kỹ thuật của lỗi đối với hệ thống (ví dụ: làm sập toàn bộ hệ thống là Critical/Blocker). Priority (Mức độ ưu tiên) thể hiện mức độ cấp bách cần sửa lỗi xét theo góc độ kinh doanh/thời hạn phát hành."
    },
    {
        "id": "Q189",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.6 Defect Management",
        "type": "Single",
        "question": "A spelling mistake appears in the company's legal name on the public home page of a major bank. How should this defect be classified regarding Severity and Priority?",
        "options": [
            "A. High Severity, Low Priority",
            "B. Low Severity (system function is unimpaired), High Priority (causes severe public reputation damage, must be fixed immediately)",
            "C. High Severity, High Priority",
            "D. Low Severity, Low Priority"
        ],
        "answer": "B",
        "explanation": "Ví dụ kinh điển: Sai chính tả tên thương hiệu của ngân hàng ngay trên trang chủ không làm sập hệ thống (Low Severity), nhưng ảnh hưởng nghiêm trọng đến uy tín thương hiệu nên phải sửa ngay lập tức trước khi ra mắt (High Priority)."
    },
    {
        "id": "Q190",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.6 Defect Management",
        "type": "Single",
        "question": "An obscure edge-case crash occurs only when a user runs the software on Windows XP with Japanese language encoding, a configuration used by 0.001% of customers. How would this defect typically be classified?",
        "options": [
            "A. High Severity (crash), Low Priority (very rare, unlikely to impact business)",
            "B. Low Severity, High Priority",
            "C. High Severity, High Priority",
            "D. Low Severity, Low Priority"
        ],
        "answer": "A",
        "explanation": "Hệ thống bị crash là lỗi nghiêm trọng về mặt kỹ thuật (High Severity), nhưng xác suất xảy ra cực kỳ hiếm trên môi trường hầu như không ai dùng (0.001%) nên độ ưu tiên sửa lỗi trong sprint này là thấp (Low Priority)."
    },
    {
        "id": "Q191",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.6 Defect Management",
        "type": "Single",
        "question": "Which of the following elements is ESSENTIAL in an effective Defect Report to enable developers to reproduce the issue?",
        "options": [
            "A. An aggressive complaint about the developer's coding skills.",
            "B. Clear, numbered, step-by-step instructions to reproduce the failure, along with expected vs actual results.",
            "C. A request for immediate compensation.",
            "D. The tester's horoscope."
        ],
        "answer": "B",
        "explanation": "Một Defect Report hiệu quả bắt buộc phải có: các bước tái hiện lỗi chi tiết theo thứ tự (step-by-step steps to reproduce), kết quả mong đợi (expected result), kết quả thực tế (actual result), cùng thông tin môi trường và bằng chứng đính kèm (screenshots/logs)."
    },
    {
        "id": "Q192",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.6 Defect Management",
        "type": "Single",
        "question": "In a standard defect lifecycle, what state transition occurs when a tester re-tests a fixed bug and discovers that the failure STILL OCCURS?",
        "options": [
            "A. Fixed -> Closed",
            "B. Resolved -> Reopened",
            "C. New -> Deferred",
            "D. Closed -> Rejected"
        ],
        "answer": "B",
        "explanation": "Khi developer đánh dấu lỗi là Fixed/Resolved, tester tiến hành kiểm tra lại (Retest). Nếu lỗi vẫn còn xuất hiện, tester chuyển trạng thái bug từ Resolved sang Reopened (Mở lại)."
    },
    {
        "id": "Q193",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.6 Defect Management",
        "type": "Single",
        "question": "When a defect is reported, but product management decides that fixing it in the current release is too risky or not cost-effective, which status is assigned?",
        "options": [
            "A. Deferred (Postponed)",
            "B. Closed",
            "C. Verified",
            "D. Duplicate"
        ],
        "answer": "A",
        "explanation": "Trạng thái Deferred (Hoãn lại): Ban quản lý chấp nhận sự tồn tại của defect trong bản phát hành hiện tại và dời việc sửa chữa sang một bản phát hành tiếp theo trong tương lai."
    },
    {
        "id": "Q194",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.3 Test Monitoring and Control",
        "type": "Single",
        "question": "What is 'Defect Density'?",
        "options": [
            "A. The physical weight of the bug report binder.",
            "B. The number of defects identified in a work product divided by the size of the work product (e.g., defects per KLOC or defects per Function Point).",
            "C. The speed at which testers write test cases.",
            "D. The number of developers working in one room."
        ],
        "answer": "B",
        "explanation": "Defect Density (Mật độ lỗi) = Số lượng defect tìm thấy / Quy mô của sản phẩm (ví dụ: số lỗi trên 1.000 dòng lệnh KLOC, hoặc số lỗi trên 1 Function Point/User Story)."
    },
    {
        "id": "Q195",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.3 Test Monitoring and Control",
        "type": "Single",
        "question": "What is the PRIMARY purpose of issuing regular Test Progress Reports during test execution?",
        "options": [
            "A. To publicly embarrass poor performers.",
            "B. To provide feedback and visibility to project stakeholders regarding progress against the test plan, risks, defect trends, and test coverage.",
            "C. To invoice the customer on a daily basis.",
            "D. To announce the date of the team holiday party."
        ],
        "answer": "B",
        "explanation": "Mục tiêu của Báo cáo tiến độ kiểm thử (Test Progress Report): Cung cấp thông tin minh bạch, kịp thời cho stakeholders về tiến độ so với kế hoạch, tình hình thực thi test case, xu hướng phát sinh defect và mức độ bao phủ."
    },
    {
        "id": "Q196",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.3 Test Monitoring and Control",
        "type": "Single",
        "question": "What is the difference between a Test Progress Report and a Test Summary Report?",
        "options": [
            "A. A Test Progress Report is issued periodically during testing; a Test Summary Report is issued at completion/milestone to evaluate overall test results against exit criteria.",
            "B. Test Progress Reports are written in French; Test Summary Reports are in English.",
            "C. Test Summary Reports are only written by marketing managers.",
            "D. A Test Progress Report is written only after software retirement."
        ],
        "answer": "A",
        "explanation": "Test Progress Report được phát hành định kỳ (hàng ngày/tuần) trong quá trình đang thực thi test. Test Summary Report được phát hành khi kết thúc một giai đoạn kiểm thử hoặc khi dự án hoàn thành để đánh giá tổng thể kết quả so với tiêu chí kết thúc (exit criteria)."
    },
    {
        "id": "Q197",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.4 Configuration Management",
        "type": "Single",
        "question": "Why is Configuration Management (CM) ESSENTIAL to software testing?",
        "options": [
            "A. It ensures that all testware (test cases, scripts, data) and software test items are uniquely identified, version-controlled, tracked, and reproducible.",
            "B. It prevents testers from finding too many bugs.",
            "C. It allows developers to deploy code directly to production without testing.",
            "D. It eliminates the need for test execution logs."
        ],
        "answer": "A",
        "explanation": "Quản lý cấu hình (Configuration Management) đảm bảo rằng tất cả các tài sản kiểm thử (testware, scripts, dữ liệu kiểm thử) và phiên bản phần mềm (builds) đều được định danh duy nhất, kiểm soát phiên bản chặt chẽ, truy vết được và có thể tái hiện chính xác môi trường khi cần."
    },
    {
        "id": "Q198",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.2 Test Planning and Estimation",
        "type": "Single",
        "question": "Which of the following factors would TYPICALLY INCREASE the required testing effort?",
        "options": [
            "A. The system has high complexity, strict safety-critical regulatory requirements, and high defect rates.",
            "B. The requirements are extremely simple and stable.",
            "C. The test team already has excellent test automation scripts for all modules.",
            "D. The developers have 100% unit test coverage."
        ],
        "answer": "A",
        "explanation": "Các yếu tố làm tăng công sức kiểm thử: Hệ thống phức tạp, có yêu cầu tuân thủ an toàn nghiêm ngặt (safety-critical), chất lượng bản build ban đầu kém nhiều lỗi, yêu cầu nghiệp vụ thường xuyên thay đổi."
    },
    {
        "id": "Q199",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.5 Risks and Testing",
        "type": "Multiple",
        "question": "Which TWO of the following are examples of Product Risks? (Choose TWO options)",
        "options": [
            "A. Software crashes when processing more than 100 concurrent checkout orders.",
            "B. The project sponsor terminates the project funding due to budget cuts.",
            "C. User data is transmitted across the internet without SSL encryption.",
            "D. The testing team cannot hire qualified automation testers in time.",
            "E. An earthquake disables the corporate power grid."
        ],
        "answer": "A, C",
        "explanation": "Crash khi chịu tải 100 giao dịch (A) và truyền dữ liệu người dùng không mã hóa SSL (C) là các khiếm khuyết trực tiếp của sản phẩm phần mềm (Product Risks). B và D là rủi ro dự án (Project Risks); E là thảm họa thiên tai."
    },
    {
        "id": "Q200",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.2 Test Planning and Estimation",
        "type": "Single",
        "question": "In Agile teams, which estimation technique uses playing cards with Fibonacci numbers (1, 2, 3, 5, 8...) where team members simultaneously reveal estimates to reach consensus on user story points?",
        "options": [
            "A. Planning Poker",
            "B. Function Point Analysis",
            "C. Cyclomatic Estimation",
            "D. Waterfall Delphi"
        ],
        "answer": "A",
        "explanation": "Planning Poker là kỹ thuật ước lượng đồng thuận phổ biến trong Agile/Scrum: các thành viên dùng bộ bài có dãy số Fibonacci để đưa ra điểm số ước lượng cùng một lúc, thảo luận về những khác biệt lớn và chốt con số thống nhất."
    },
    {
        "id": "Q201",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.6 Defect Management",
        "type": "Single",
        "question": "What is the primary objective of a 'Defect Triage Meeting'?",
        "options": [
            "A. To analyze, prioritize, and assign newly reported defects, deciding which will be fixed in the current release and which deferred.",
            "B. To fire the developers responsible for the defects.",
            "C. To rewrite the company mission statement.",
            "D. To order pizza for the engineering team."
        ],
        "answer": "A",
        "explanation": "Cuộc họp phân loại lỗi (Defect Triage Meeting) gồm đại diện Tester, Developer và Product Owner nhằm xem xét các bug mới phát sinh, đánh giá mức độ nghiêm trọng/ưu tiên, và quyết định bug nào sửa ngay, bug nào hoãn lại (defer) hoặc từ chối (reject)."
    },
    {
        "id": "Q202",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.3 Test Monitoring and Control",
        "type": "Single",
        "question": "During test execution, what is an action of 'Test Control' when monitoring reveals testing is running 3 days behind schedule?",
        "options": [
            "A. Reallocating additional testers to high-risk areas, de-scoping low-priority test cases, or re-negotiating the deadline.",
            "B. Ignoring the issue and hoping for the best.",
            "C. Immediately releasing the un-tested software to production.",
            "D. Deleting all test cases to show 100% completion."
        ],
        "answer": "A",
        "explanation": "Test Control (Kiểm soát kiểm thử) là việc đưa ra các hành động khắc phục khi việc giám sát (Monitoring) phát hiện có sai lệch so với kế hoạch: điều chuyển nhân lực sang vùng rủi ro cao, cắt giảm các test case ưu tiên thấp, hoặc đàm phán lại thời hạn bàn giao."
    },
    {
        "id": "Q203",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.1 Test Organization",
        "type": "Single",
        "question": "What is a key benefit of having an independent test team within an organization?",
        "options": [
            "A. They bring an objective, unbiased viewpoint and can spot defects that developers take for granted.",
            "B. They cost zero dollars to maintain.",
            "C. They eliminate the need for requirement specifications.",
            "D. They can prevent developers from writing code."
        ],
        "answer": "A",
        "explanation": "Lợi ích lớn nhất của đội kiểm thử độc lập: Mang lại góc nhìn khách quan, không bị thiên kiến xác nhận chi phối, từ đó phát hiện ra các sai sót và giả định sai lầm mà lập trình viên thường bỏ qua."
    },
    {
        "id": "Q204",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.5 Risks and Testing",
        "type": "Single",
        "question": "What is 'Risk Mitigation' in Risk-based Testing?",
        "options": [
            "A. The process of taking actions (such as designing and executing targeted test cases) to reduce the likelihood or impact of potential product failures.",
            "B. Pretending the risk does not exist.",
            "C. Deleting the risky code module.",
            "D. Increasing the retail price of the software."
        ],
        "answer": "A",
        "explanation": "Giảm thiểu rủi ro (Risk Mitigation): Thực hiện các biện pháp chủ động (như thiết kế các test case có trọng tâm, thực thi kiểm thử sớm, bổ sung code review) nhằm giảm xác suất xảy ra lỗi hoặc giảm nhẹ hậu quả của rủi ro."
    },
    {
        "id": "Q205",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.2 Test Planning and Estimation",
        "type": "Single",
        "question": "What section of a standard IEEE 829 Test Plan lists features that will EXPLICITLY NOT be tested during the test cycle?",
        "options": [
            "A. Features Not to be Tested (Out of Scope)",
            "B. Pass/Fail Criteria",
            "C. Test Deliverables",
            "D. Environmental Needs"
        ],
        "answer": "A",
        "explanation": "Mục 'Features Not to be Tested' (hoặc Out of Scope) trong tài liệu Test Plan ghi rõ các tính năng nằm ngoài phạm vi kiểm thử của đợt này nhằm quản lý kỳ vọng rõ ràng với các bên liên quan."
    },
    {
        "id": "Q206",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.6 Defect Management",
        "type": "Single",
        "question": "If a tester files a defect report claiming the shopping cart total is incorrect, but investigation reveals the tester used an outdated tax table that was updated last week, what should the defect status be updated to?",
        "options": [
            "A. Rejected (or Invalid / Not a Bug)",
            "B. Fixed",
            "C. Reopened",
            "D. Blocker"
        ],
        "answer": "A",
        "explanation": "Nếu tester báo lỗi do hiểu sai yêu cầu hoặc dùng dữ liệu cũ không còn hiệu lực, defect report sẽ được cập nhật trạng thái thành Rejected (Từ chối) hoặc Not a Bug (Không phải lỗi)."
    },
    {
        "id": "Q207",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.3 Test Monitoring and Control",
        "type": "Single",
        "question": "Which testing metric illustrates the number of new defects reported each day versus the number of defects resolved and closed over time?",
        "options": [
            "A. Defect Arrival and Resolution Trend (Defect Burn-down / Cumulative defect curve)",
            "B. Server CPU temperature chart",
            "C. Cyclomatic Complexity gauge",
            "D. Equivalence boundary ratio"
        ],
        "answer": "A",
        "explanation": "Biểu đồ xu hướng phát hiện và giải quyết lỗi (Defect Trend / Defect Arrival vs Resolution Curve) cho thấy số lượng lỗi mới tìm thấy mỗi ngày so với số lượng lỗi đã fix và đóng, giúp dự đoán thời điểm hệ thống đạt độ ổn định để release."
    },
    {
        "id": "Q208",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.2 Test Planning and Estimation",
        "type": "Single",
        "question": "In a Test Plan, what is 'Test Strategy'?",
        "options": [
            "A. The high-level description of test levels to be performed and the testing approach within those levels.",
            "B. The password to access the test server.",
            "C. The names of all test case authors.",
            "D. The source code repository commit history."
        ],
        "answer": "A",
        "explanation": "Chiến lược kiểm thử (Test Strategy) là mô tả cấp cao định hướng cách tiếp cận kiểm thử, xác định các cấp độ kiểm thử được thực hiện, các phương pháp kỹ thuật áp dụng và cách quản lý rủi ro."
    },
    {
        "id": "Q209",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.5 Risks and Testing",
        "type": "Single",
        "question": "In a risk matrix, Risk A has Likelihood = 4, Impact = 5 (Risk = 20). Risk B has Likelihood = 2, Impact = 3 (Risk = 6). Risk C has Likelihood = 5, Impact = 2 (Risk = 10). What is the correct priority order for testing?",
        "options": [
            "A. Risk A -> Risk C -> Risk B",
            "B. Risk B -> Risk C -> Risk A",
            "C. Risk C -> Risk A -> Risk B",
            "D. All risks should be tested at the same time."
        ],
        "answer": "A",
        "explanation": "Điểm mức độ rủi ro: Risk A = 20, Risk C = 10, Risk B = 6. Theo nguyên tắc Risk-based testing, rủi ro cao nhất được ưu tiên kiểm thử trước: Thứ tự là Risk A -> Risk C -> Risk B."
    },
    {
        "id": "Q210",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.6 Defect Management",
        "type": "Single",
        "question": "Why is an 'Isolating' step recommended before reporting a defect?",
        "options": [
            "A. To find the minimal set of steps that reliably reproduces the failure and confirm it is not caused by tester error or transient environmental glitch.",
            "B. To delete the evidence before anyone notices.",
            "C. To prevent other testers from filing bug reports.",
            "D. To encrypt the bug report."
        ],
        "answer": "A",
        "explanation": "Cô lập lỗi (Defect Isolation): Tester cần thử nghiệm để tìm ra chuỗi bước tối thiểu và chính xác nhất để tái hiện lỗi một cách ổn định, loại trừ các yếu tố nhiễu do thao tác nhầm hoặc mạng chập chờn trước khi gửi ticket."
    },
    {
        "id": "Q211",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.1 Test Organization",
        "type": "Multiple",
        "question": "Which TWO of the following tasks are typical responsibilities of a Test Manager? (Choose TWO options)",
        "options": [
            "A. Writing and finalizing the Test Plan.",
            "B. Coding unit tests inside the Java service class.",
            "C. Gathering and analyzing testing metrics to author the Test Summary Report.",
            "D. Performing exploratory testing on UI widgets.",
            "E. Recompiling the application binary after bug fixes."
        ],
        "answer": "A, C",
        "explanation": "Test Manager chịu trách nhiệm lập Test Plan (A) và thu thập số liệu đo lường để viết Test Summary Report (C). B là việc của developer, D là việc của tester, E là của build engineer/developer."
    },
    {
        "id": "Q212",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.4 Configuration Management",
        "type": "Single",
        "question": "What problem occurs during testing if Configuration Management is POOR or absent?",
        "options": [
            "A. Testers might test the wrong build version, verify bugs against obsolete code, or fail to reproduce issues because the environment configuration was not tracked.",
            "B. Compilers refuse to generate bytecode.",
            "C. The internet shuts down.",
            "D. Automated test scripts run 1000 times faster."
        ],
        "answer": "A",
        "explanation": "Nếu quản lý cấu hình kém: Tester có thể chạy test trên sai bản build, retest bug trên code cũ chưa được cập nhật, hoặc không thể tái hiện lại lỗi vì không biết chính xác cấu hình môi trường lúc lỗi xảy ra."
    },
    {
        "id": "Q213",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.2 Test Planning and Estimation",
        "type": "Single",
        "question": "In a Test Plan, what is an 'Environmental Need'?",
        "options": [
            "A. The specification of hardware, network infrastructure, software licenses, operating systems, and database configurations required to execute tests.",
            "B. The number of plants in the office lobby.",
            "C. The recycling bins available in the kitchen.",
            "D. The air conditioning temperature in the breakroom."
        ],
        "answer": "A",
        "explanation": "Environmental Needs (Nhu cầu môi trường): Mục trong Test Plan liệt kê đầy đủ các yêu cầu về phần cứng, mạng, hệ điều hành, bản quyền phần mềm, máy chủ cơ sở dữ liệu cần có để thiết lập môi trường test."
    },
    {
        "id": "Q214",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.6 Defect Management",
        "type": "Single",
        "question": "When two testers independently discover the exact same underlying defect under slightly different UI steps and both submit tickets, what action should the defect triage team take?",
        "options": [
            "A. Keep one ticket as Primary and mark the other as Duplicate.",
            "B. Delete both tickets immediately.",
            "C. Reprimand both testers.",
            "D. Build two separate software fixes."
        ],
        "answer": "A",
        "explanation": "Khi phát hiện 2 ticket trùng nhau, quy trình chuẩn là giữ lại một ticket chính (Primary) và đánh dấu ticket còn lại là Trùng lặp (Duplicate) kèm liên kết tham chiếu đến ticket chính."
    },
    {
        "id": "Q215",
        "chapter": "Chapter 5: Test Management",
        "topic": "5.2 Test Planning and Estimation",
        "type": "Single",
        "question": "Which testing document serves as the formal handover record at the conclusion of testing, summarizing total tests executed, remaining open defects, and recommendation on whether release criteria have been met?",
        "options": [
            "A. Test Summary Report",
            "B. Test Charter",
            "C. Test Procedure",
            "D. Defect Log"
        ],
        "answer": "A",
        "explanation": "Test Summary Report (Báo cáo tổng kết kiểm thử) là tài liệu bàn giao chính thức khi kết thúc kiểm thử, tổng hợp số lượng test case đã chạy, các defect còn mở và đưa ra đánh giá khuyến nghị xem sản phẩm đã đủ điều kiện release hay chưa."
    }
]
