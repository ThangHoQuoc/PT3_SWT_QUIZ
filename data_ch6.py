# data_ch6.py - Chapter 6: Tool Support for Testing (35 Questions)

CH6_QUESTIONS = [
    {
        "id": "Q216",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "Which of the following test tools is classified under 'Tools supporting static testing'?",
        "options": [
            "A. Static Code Analysis Tool (e.g., SonarQube)",
            "B. Load Testing Tool (e.g., Apache JMeter)",
            "C. Unit Test Runner (e.g., JUnit)",
            "D. Defect Tracking Tool (e.g., Jira)"
        ],
        "answer": "A",
        "explanation": "Static Code Analysis Tool (như SonarQube, Checkstyle) phân tích mã nguồn mà không cần thực thi chương trình, thuộc nhóm công cụ hỗ trợ kiểm thử tĩnh (Static testing). JMeter là công cụ hiệu năng, JUnit là công cụ thực thi/unit test, Jira là công cụ quản lý kiểm thử/defect."
    },
    {
        "id": "Q217",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "What is the PRIMARY purpose of a 'Dynamic Analysis Tool'?",
        "options": [
            "A. To format requirements into Word documents.",
            "B. To analyze code while it is running, detecting runtime issues such as memory leaks, unassigned pointers, and buffer overflows.",
            "C. To calculate developer salary deductions.",
            "D. To convert manual test cases into PDF format."
        ],
        "answer": "B",
        "explanation": "Dynamic Analysis Tool (Công cụ phân tích động - ví dụ Valgrind, Purify) phân tích ứng dụng trong lúc đang chạy để phát hiện các lỗi thời gian thực như rò rỉ bộ nhớ (memory leaks), con trỏ rác (dangling pointers), và tràn bộ đệm (buffer overflows)."
    },
    {
        "id": "Q218",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "Which category of testing tools includes features for logging defect tickets, assigning priorities, and tracking bugs through their lifecycle?",
        "options": [
            "A. Test Execution Tools",
            "B. Defect Management / Tracking Tools",
            "C. Performance Testing Tools",
            "D. Static Analysis Tools"
        ],
        "answer": "B",
        "explanation": "Defect Management / Incident Tracking Tools (như Jira, Bugzilla, Redmine) hỗ trợ ghi lại defect, phân loại mức độ nghiêm trọng/ưu tiên, và theo dõi vòng đời của lỗi từ khi mở đến khi đóng."
    },
    {
        "id": "Q219",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "What is a 'Test Harness'?",
        "options": [
            "A. A leather belt worn by testers in a server room.",
            "B. A test environment or collection of software and test data configured to test a program unit by running it under specific conditions and monitoring its behavior and outputs (often providing stubs and drivers).",
            "C. A tool used solely to format bug report screenshots.",
            "D. A contract between a test manager and a client."
        ],
        "answer": "B",
        "explanation": "Test Harness (Khung kiểm thử): Tập hợp các phần mềm giả lập, stubs, drivers và dữ liệu kiểm thử được cấu hình để thực thi một module hoặc chương trình trong điều kiện xác định và theo dõi kết quả đầu ra của nó."
    },
    {
        "id": "Q220",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "Which of the following is a POTENTIAL BENEFIT of test automation?",
        "options": [
            "A. Eliminating the need to ever train testers again.",
            "B. Greater consistency and repeatability of test execution, reducing repetitive human effort.",
            "C. Guaranteeing that zero defects will ever escape to production.",
            "D. Replacing all manual exploratory testing completely."
        ],
        "answer": "B",
        "explanation": "Lợi ích lớn của kiểm thử tự động: Đảm bảo tính nhất quán (consistency) và khả năng lặp lại chính xác (repeatability) của các bài test, giảm thiểu sự nhàm chán và công sức thủ công lặp đi lặp lại của con người."
    },
    {
        "id": "Q221",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "Which of the following is a COMMON RISK or pitfall when introducing a test automation tool?",
        "options": [
            "A. Underestimating the time, effort, and cost required to maintain automated test scripts over time.",
            "B. Automated tests execute too fast.",
            "C. Automated test reports are too easy to read.",
            "D. Developers refuse to use computers."
        ],
        "answer": "A",
        "explanation": "Rủi ro phổ biến nhất khi triển khai công cụ tự động hóa: Đánh giá quá thấp thời gian, công sức và chi phí bảo trì kịch bản kiểm thử (test script maintenance) khi giao diện hoặc logic phần mềm thay đổi liên tục."
    },
    {
        "id": "Q222",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "Why is the naive 'Capture/Replay' (Record and Playback) approach generally DISCOURAGED for large-scale enterprise test automation suites?",
        "options": [
            "A. Because captured scripts are brittle and break easily whenever minor UI changes occur, requiring excessive maintenance.",
            "B. Because capture/replay tools are prohibited by ISO standards.",
            "C. Because computers cannot record mouse clicks.",
            "D. Because captured scripts cannot be executed on weekends."
        ],
        "answer": "A",
        "explanation": "Phương pháp Record/Playback tạo ra các kịch bản rất giòn (brittle): chỉ cần một thay đổi nhỏ về giao diện (như đổi ID button, đổi vị trí ô nhập) là toàn bộ script bị gãy (fail), dẫn đến chi phí bảo trì khổng lồ."
    },
    {
        "id": "Q223",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "In test automation, what is the 'Data-Driven' testing approach?",
        "options": [
            "A. Storing test inputs and expected outcomes in external data files (e.g., CSV, Excel, DB) so that a single test script can execute multiple test cases with different data.",
            "B. Manually typing inputs directly into hardcoded code statements.",
            "C. Relying entirely on random data generated by the computer.",
            "D. Storing test results on USB thumb drives."
        ],
        "answer": "A",
        "explanation": "Data-Driven Testing (Kiểm thử theo dữ liệu): Tách biệt logic của kịch bản kiểm thử ra khỏi dữ liệu. Dữ liệu kiểm thử (inputs và expected outputs) được lưu trong file ngoài (Excel, CSV, database), cho phép 1 script duy nhất có thể chạy hàng trăm bộ dữ liệu khác nhau."
    },
    {
        "id": "Q224",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "What is the 'Keyword-Driven' (Action-Driven) test automation approach?",
        "options": [
            "A. Writing test cases using action words (e.g., 'Click', 'EnterText', 'VerifyText') stored in tables, which are executed by calling generic script modules.",
            "B. Searching Google for software testing keywords.",
            "C. Testing whether keyboard keys are sticky.",
            "D. Only testing software on Windows 95."
        ],
        "answer": "A",
        "explanation": "Keyword-Driven Testing (Kiểm thử theo từ khóa): Sử dụng các từ khóa hành động cụ thể (như 'Login', 'Click', 'CheckBalance') kèm các tham số. Tester nghiệp vụ có thể viết test case bằng từ khóa mà không cần biết lập trình, kịch bản khung sẽ tự động gọi code tương ứng."
    },
    {
        "id": "Q225",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.2 Effective Use of Tools",
        "type": "Single",
        "question": "What is the PRIMARY purpose of conducting a 'Pilot Project' before rolling out a new testing tool across an entire organization?",
        "options": [
            "A. To learn the tool in depth, evaluate how it fits with existing processes, decide on standard usage guidelines, and assess realistic benefits and costs.",
            "B. To immediately replace all senior testers with the tool.",
            "C. To spend all remaining annual IT budget before December 31st.",
            "D. To write the software user manual."
        ],
        "answer": "A",
        "explanation": "Mục tiêu cốt lõi của Dự án thử nghiệm (Pilot Project): Giúp tìm hiểu sâu về công cụ trong điều kiện thực tế, đánh giá sự tương thích với quy trình sẵn có, thiết lập các quy chuẩn sử dụng (naming convention, lưu trữ), và đánh giá chính xác lợi ích so với chi phí trước khi triển khai diện rộng."
    },
    {
        "id": "Q226",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.2 Effective Use of Tools",
        "type": "Single",
        "question": "Which of the following is considered a CRITICAL success factor when deploying a new testing tool across multiple project teams?",
        "options": [
            "A. Providing ongoing training, coaching, and mentoring to the staff who will use the tool.",
            "B. Forcing all teams to adopt the tool on day one without any documentation or training.",
            "C. Banning testers from discussing issues encountered with the tool.",
            "D. Disabling version control for automated test scripts."
        ],
        "answer": "A",
        "explanation": "Yếu tố thành công then chốt khi triển khai công cụ mới: Cung cấp đầy đủ đào tạo (training), kèm cặp (coaching/mentoring), tài liệu hướng dẫn và hỗ trợ kỹ thuật liên tục cho những người sử dụng công cụ."
    },
    {
        "id": "Q227",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "Which type of tool measures the percentage of executable code structures (such as statements or decisions) exercised by a test suite?",
        "options": [
            "A. Coverage Measurement Tool (Coverage Analyzer)",
            "B. Defect Management Tool",
            "C. Configuration Management Tool",
            "D. Requirements Traceability Matrix Tool"
        ],
        "answer": "A",
        "explanation": "Coverage Measurement Tool (như JaCoCo, Istanbul, Cobertura) đo lường tỷ lệ phần trăm các thành phần mã nguồn (statements, branches, lines) đã được thực thi bởi bộ kiểm thử."
    },
    {
        "id": "Q228",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "What is an UNREALISTIC EXPECTATION often held by management regarding test automation tools?",
        "options": [
            "A. Expecting that purchasing an automated tool will immediately reduce test effort to zero without requiring time for scripting and maintenance.",
            "B. Expecting that automated tests can be run overnight.",
            "C. Expecting that automated tests provide repeatable execution.",
            "D. Expecting that automation scripts can be stored in Git."
        ],
        "answer": "A",
        "explanation": "Kỳ vọng phi thực tế phổ biến của ban quản lý: Nghĩ rằng chỉ cần bỏ tiền mua một công cụ tự động hóa đắt tiền là công sức kiểm thử sẽ lập tức về số 0, mà không lường trước công sức khổng lồ để học, lập trình kịch bản và bảo trì."
    },
    {
        "id": "Q229",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "Which tool type helps create synthetic or anonymized test datasets needed to execute test cases without violating privacy laws?",
        "options": [
            "A. Test Data Preparation Tool",
            "B. Static Linter",
            "C. Unit Test Runner",
            "D. Code Profiler"
        ],
        "answer": "A",
        "explanation": "Test Data Preparation Tool (Công cụ chuẩn bị dữ liệu kiểm thử) giúp tạo ra các tập dữ liệu giả lập có cấu trúc hợp lệ hoặc làm mờ/ẩn danh hóa (anonymize) dữ liệu sản xuất thực tế để tuân thủ luật bảo mật thông tin cá nhân (như GDPR)."
    },
    {
        "id": "Q230",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "Which testing tool category evaluates whether a system conforms to accessibility standards (e.g., WCAG) for users with visual or physical impairments?",
        "options": [
            "A. Accessibility Testing Tool (e.g., Axe, Wave)",
            "B. Load Testing Tool",
            "C. Stress Testing Tool",
            "D. Code Coverage Tool"
        ],
        "answer": "A",
        "explanation": "Accessibility Testing Tool (Công cụ kiểm thử khả năng tiếp cận - như Axe, WAVE) kiểm tra việc tuân thủ các chuẩn hỗ trợ người khuyết tật (WCAG) như độ tương phản màu sắc, thẻ alt cho hình ảnh, điều hướng bàn phím."
    },
    {
        "id": "Q231",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "What risk arises if a test team treats test automation scripts as informal throwaway code without placing them under Version Control?",
        "options": [
            "A. Loss of traceability, loss of script history, inability to synchronize scripts with software builds, and accidental overwrites.",
            "B. Scripts run too quickly.",
            "C. Automated test reports become encrypted.",
            "D. The compiler refuses to execute binary files."
        ],
        "answer": "A",
        "explanation": "Nếu kịch bản tự động hóa không được quản lý bằng Hệ thống kiểm soát phiên bản (Version Control như Git): Sẽ mất khả năng truy vết giữa script và bản build phần mềm, dễ bị ghi đè mất mã nguồn, và không thể rollback khi script bị lỗi."
    },
    {
        "id": "Q232",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "Which testing tool generates massive concurrent virtual user traffic to measure web server response times and transaction throughput under peak stress?",
        "options": [
            "A. Performance and Load Testing Tool (e.g., JMeter, Gatling)",
            "B. Static Review Tool",
            "C. Requirements Management Tool",
            "D. Spell Checker"
        ],
        "answer": "A",
        "explanation": "Performance / Load Testing Tool (như JMeter, Gatling, LoadRunner) giả lập hàng ngàn người dùng ảo truy cập đồng thời để đo lường thông lượng, thời gian phản hồi và độ ổn định của hệ thống dưới tải trọng cao."
    },
    {
        "id": "Q233",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.2 Effective Use of Tools",
        "type": "Single",
        "question": "When selecting a testing tool, which of the following criteria is essential regarding the technology stack?",
        "options": [
            "A. Verifying that the tool is compatible with the programming languages, operating systems, and frameworks used by the software under test.",
            "B. Ensuring the tool logo is the test manager's favorite color.",
            "C. Ensuring the tool was released in the last 24 hours.",
            "D. Verifying the tool does not require an electrical connection."
        ],
        "answer": "A",
        "explanation": "Tiêu chí cốt lõi khi chọn công cụ: Đảm bảo công cụ tương thích và hỗ trợ tốt cho các nền tảng công nghệ, ngôn ngữ lập trình, hệ điều hành và framework mà hệ thống đang sử dụng (ví dụ: công cụ web test có hỗ trợ React/Angular không)."
    },
    {
        "id": "Q234",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Multiple",
        "question": "Which TWO of the following are recognized risks of introducing test automation? (Choose TWO options)",
        "options": [
            "A. Over-reliance on the tool, leading testers to stop conducting critical manual exploratory tests.",
            "B. Automated tests find defects too consistently.",
            "C. Underestimating the continuous maintenance effort required when the system under test evolves.",
            "D. Automated tests reduce repetitive work.",
            "E. Automated test runs can be scheduled during the night."
        ],
        "answer": "A, C",
        "explanation": "Hai rủi ro lớn của tự động hóa: Quá ỷ lại vào công cụ dẫn đến bỏ qua việc khám phá thủ công (A), và đánh giá thấp công sức bảo trì kịch bản lâu dài (C). B, D, E là lợi ích hoặc đặc điểm tích cực."
    },
    {
        "id": "Q235",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "What is an 'Open Source' testing tool?",
        "options": [
            "A. A tool whose source code is publicly accessible and can typically be used, modified, and distributed without licensing fees (e.g., Selenium, JUnit).",
            "B. A tool that only works with the computer cover open.",
            "C. A tool that requires payment of $50,000 per user.",
            "D. A proprietary tool owned by Microsoft."
        ],
        "answer": "A",
        "explanation": "Open Source tool (Công cụ nguồn mở - như Selenium, JUnit, JMeter) là công cụ mà mã nguồn được công khai miễn phí, cộng đồng có thể tự do sử dụng, chỉnh sửa và đóng góp phát triển mà không phải trả phí bản quyền thương mại đắt đỏ."
    },
    {
        "id": "Q236",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.2 Effective Use of Tools",
        "type": "Single",
        "question": "Why should a 'Proof of Concept' (PoC) be performed before purchasing an expensive commercial test execution tool?",
        "options": [
            "A. To prove whether the tool can actually identify UI controls and execute test actions effectively on the organization's unique software architecture.",
            "B. To delay the project until next quarter.",
            "C. To avoid writing any test cases.",
            "D. To train all 5,000 employees in the company."
        ],
        "answer": "A",
        "explanation": "Proof of Concept (PoC - Kiểm chứng tính khả thi): Giúp xác minh thực tế xem công cụ có nhận diện được các component/control UI đặc thù của dự án và chạy ổn định trên kiến trúc phần mềm của công ty hay không trước khi ký hợp đồng mua bản quyền đắt tiền."
    },
    {
        "id": "Q237",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "In continuous integration (CI) pipelines, what role do automated test execution tools play?",
        "options": [
            "A. They automatically execute regression and smoke test suites on every code commit to provide immediate feedback on build health.",
            "B. They replace all software architects.",
            "C. They generate PowerPoint presentations for marketing.",
            "D. They turn off server cooling systems."
        ],
        "answer": "A",
        "explanation": "Trong pipeline CI/CD, các công cụ kiểm thử tự động chạy ngay các bộ smoke test và regression test mỗi khi có bản commit mới, giúp phát hiện lỗi tức thì và ngăn chặn code lỗi lọt vào nhánh chính."
    },
    {
        "id": "Q238",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "What is the primary danger if a test tool vendor goes out of business or discontinues support for a proprietary tool?",
        "options": [
            "A. The organization may be left with unmaintained legacy test suites that cannot be upgraded, run on modern OS versions, or integrated with modern CI systems.",
            "B. All computers in the office will explode.",
            "C. Internet bandwidth will increase.",
            "D. Source code will automatically delete itself."
        ],
        "answer": "A",
        "explanation": "Rủi ro phụ thuộc nhà cung cấp (Vendor lock-in): Nếu nhà cung cấp công cụ độc quyền ngừng phát triển hoặc phá sản, tổ chức sẽ bị kẹt lại với bộ test script cũ không thể nâng cấp, không tương thích với HĐH mới và tốn chi phí rất lớn để làm lại từ đầu."
    },
    {
        "id": "Q239",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.2 Effective Use of Tools",
        "type": "Single",
        "question": "How should an organization plan the rollout of a new testing tool following a successful pilot project?",
        "options": [
            "A. Incrementally roll out the tool across teams, providing coaching and adapting guidelines based on early team feedback.",
            "B. Enforce immediate overnight adoption across all 100 teams simultaneously.",
            "C. Fire anyone who asks questions about the tool.",
            "D. Discard the guidelines defined during the pilot project."
        ],
        "answer": "A",
        "explanation": "Triển khai từng bước (Incremental rollout): Sau dự án thí điểm thành công, công cụ nên được nhân rộng dần dần qua từng nhóm, vừa triển khai vừa kèm cặp, đào tạo và liên tục hoàn thiện quy trình chuẩn dựa trên bài học thực tế."
    },
    {
        "id": "Q240",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "Which tool type helps testers link requirement items to test conditions, test cases, and defect reports to maintain bi-directional traceability?",
        "options": [
            "A. Requirements Management / ALM Tool (Application Lifecycle Management)",
            "B. Performance Stress Tool",
            "C. Memory Leak Profiler",
            "D. Compiling Linker"
        ],
        "answer": "A",
        "explanation": "Công cụ Quản lý Yêu cầu / ALM (như Jira + Xray, Azure DevOps, HP ALM) cho phép thiết lập và duy trì liên kết truy vết hai chiều (Bi-directional Traceability) từ User Story -> Test Case -> Test Execution -> Defect."
    },
    {
        "id": "Q241",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "What is 'Model-Based Testing' (MBT) tool support?",
        "options": [
            "A. Tools that use graphical models of system behavior (such as state machines or activity diagrams) to automatically generate test cases and test inputs.",
            "B. Tools that hire fashion models to test phones.",
            "C. Tools that take 3D photos of server hardware.",
            "D. Tools that design marketing brochures."
        ],
        "answer": "A",
        "explanation": "Model-Based Testing (MBT): Các công cụ sử dụng mô hình hành vi hệ thống (như State Machine, Flowchart) để tự động sinh ra các kịch bản kiểm thử (test cases) và dữ liệu đầu vào."
    },
    {
        "id": "Q242",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "Which of the following describes 'Static Application Security Testing' (SAST) tools?",
        "options": [
            "A. Tools that analyze source code or byte code without executing it to detect security vulnerabilities (e.g., SQL injection, XSS).",
            "B. Tools that launch live DDoS attacks against a running server.",
            "C. Tools that test firewall power cables.",
            "D. Physical locks on office doors."
        ],
        "answer": "A",
        "explanation": "SAST (Static Application Security Testing - ví dụ Checkmarx, Fortify) phân tích mã nguồn ở trạng thái tĩnh (không chạy code) để phát hiện các lỗ hổng bảo mật phổ biến như SQL Injection, Cross-Site Scripting (XSS), tràn bộ đệm."
    },
    {
        "id": "Q243",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "What is the key difference between SAST and DAST (Dynamic Application Security Testing) tools?",
        "options": [
            "A. SAST inspects source code statically; DAST tests the running application externally by simulating attacks (penetration testing).",
            "B. SAST is for games; DAST is for banking.",
            "C. DAST only works on Android devices.",
            "D. SAST requires live server internet connection; DAST does not."
        ],
        "answer": "A",
        "explanation": "SAST kiểm tra mã nguồn tĩnh bên trong (white-box security); trong khi DAST (Dynamic Application Security Testing - như OWASP ZAP, Burp Suite) kiểm tra ứng dụng đang chạy thực tế từ bên ngoài (black-box security) bằng cách bắn các payload tấn công mô phỏng hacker."
    },
    {
        "id": "Q244",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.2 Effective Use of Tools",
        "type": "Single",
        "question": "Which factor must be evaluated regarding the organization's maturity before introducing complex test automation frameworks?",
        "options": [
            "A. Whether the organization already has disciplined test processes, well-defined test cases, and technical programming competencies to maintain scripts.",
            "B. Whether the company has more than 10,000 employees.",
            "C. Whether all desks are painted blue.",
            "D. Whether the company is publicly traded."
        ],
        "answer": "A",
        "explanation": "Đánh giá mức độ trưởng thành của tổ chức: Nếu tổ chức chưa có quy trình kiểm thử bài bản, test case thủ công còn chưa rõ ràng và nhóm thiếu kỹ năng lập trình thì việc đưa công cụ tự động hóa phức tạp vào chắc chắn sẽ thất bại."
    },
    {
        "id": "Q245",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "Can test execution tools completely eliminate the need for human judgment and exploratory testing?",
        "options": [
            "A. Yes, modern tools have full human intelligence.",
            "B. No, automated execution tools only repeat scripted instructions blindly; human critical thinking and exploration are indispensable for finding unexpected edge-case bugs.",
            "C. Yes, if scripts are written in Python.",
            "D. No, because automation tools cannot connect to the internet."
        ],
        "answer": "B",
        "explanation": "Công cụ kiểm thử tự động chỉ thực thi mù quáng các bước đã được lập trình sẵn. Chúng không có trực giác, sự tò mò hay tư duy phản biện của con người để phát hiện các lỗi bất thường ngoài kịch bản."
    },
    {
        "id": "Q246",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "Why is 'Ease of Script Maintenance' a top criterion when designing a test automation framework?",
        "options": [
            "A. Because application UIs and requirements evolve constantly, and high maintenance overhead will eventually cause teams to abandon the automated test suite.",
            "B. Because compilers refuse to run large scripts.",
            "C. Because testers prefer manual typing.",
            "D. Because test scripts are limited to 50 lines of code."
        ],
        "answer": "A",
        "explanation": "Giao diện và nghiệp vụ của phần mềm luôn biến đổi liên tục. Nếu framework khó bảo trì, mỗi lần có thay đổi nhỏ tester phải sửa hàng trăm chỗ thì chi phí duy trì sẽ vượt quá lợi ích mang lại, dẫn đến bộ automation suite bị bỏ xó."
    },
    {
        "id": "Q247",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.2 Effective Use of Tools",
        "type": "Single",
        "question": "During a tool pilot project, which activity helps define how test scripts will be structured across the team?",
        "options": [
            "A. Establishing coding standards, naming conventions, and modular directory structures for test assets.",
            "B. Ordering new office furniture.",
            "C. Deleting old requirement documents.",
            "D. Cancelling weekly team standup meetings."
        ],
        "answer": "A",
        "explanation": "Trong dự án thí điểm, nhóm cần thiết lập các quy chuẩn lập trình (coding standards), quy tắc đặt tên (naming conventions) và cấu trúc thư mục lưu trữ thống nhất cho tất cả các kịch bản kiểm thử."
    },
    {
        "id": "Q248",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "What is an advantage of Open Source testing tools compared to commercial proprietary tools?",
        "options": [
            "A. Absence of software license purchasing fees and active community-driven plugins.",
            "B. Guaranteed 24/7 dedicated telephone support with legal liability guarantees.",
            "C. They never have any bugs.",
            "D. They do not require any programming knowledge."
        ],
        "answer": "A",
        "explanation": "Ưu điểm của công cụ Open Source: Không tốn chi phí mua license định kỳ, cộng đồng người dùng đông đảo phát triển nhiều thư viện/plugin mở rộng phong phú và dễ tích hợp."
    },
    {
        "id": "Q249",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.1 Test Tool Considerations",
        "type": "Single",
        "question": "Which of the following is a key characteristic of 'Page Object Model' (POM) design pattern in GUI test automation?",
        "options": [
            "A. It encapsulates web page elements and interactions inside dedicated class files, separating the test logic from UI locators to dramatically improve maintainability.",
            "B. It prints every web page onto physical paper.",
            "C. It restricts web pages to 1 single image.",
            "D. It eliminates the need for test assertions."
        ],
        "answer": "A",
        "explanation": "Design pattern Page Object Model (POM): Gom toàn bộ các định danh phần tử (locators) và hành vi trên từng trang web vào một class riêng biệt. Khi giao diện web thay đổi, tester chỉ cần sửa locator ở đúng một class đại diện cho trang đó thay vì sửa ở hàng trăm test case."
    },
    {
        "id": "Q250",
        "chapter": "Chapter 6: Tool Support for Testing",
        "topic": "6.2 Effective Use of Tools",
        "type": "Single",
        "question": "What is the ULTIMATE measure of whether the introduction of a testing tool was successful?",
        "options": [
            "A. Whether the tool delivers a positive Return on Investment (ROI) by enhancing testing efficiency, improving defect detection, and maintaining team productivity over time.",
            "B. Whether the tool CD-ROM is kept in a safe.",
            "C. Whether the test manager was featured on television.",
            "D. Whether 100% of human testers were laid off."
        ],
        "answer": "A",
        "explanation": "Thước đo tối hậu cho sự thành công của việc áp dụng công cụ: Tỷ suất hoàn vốn đầu tư (ROI) dương - công cụ giúp nâng cao năng suất và chất lượng kiểm thử, phát hiện lỗi nhanh hơn và giảm chi phí kiểm thử dài hạn một cách bền vững."
    }
]
