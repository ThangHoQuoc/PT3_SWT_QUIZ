# data_ch2.py - Chapter 2: Testing Throughout the SDLC (35 Questions)

CH2_QUESTIONS = [
    {
        "id": "Q036",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.1 SDLC Models",
        "type": "Single",
        "question": "In the standard V-model, which test level directly corresponds to the 'Component / Detailed Design' phase?",
        "options": [
            "A. Acceptance Testing",
            "B. System Testing",
            "C. Component (Unit) Testing",
            "D. Operational Acceptance Testing"
        ],
        "answer": "C",
        "explanation": "Trong mô hình chữ V chuẩn (V-model): Business Requirements ứng với Acceptance Testing; System Requirements/Architecture ứng với System Testing; High-level/Architectural Design ứng với Integration Testing; và Detailed Component Design ứng với Component (Unit) Testing."
    },
    {
        "id": "Q037",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.1 SDLC Models",
        "type": "Single",
        "question": "Which of the following is an essential characteristic of good testing applicable to ANY software development lifecycle model?",
        "options": [
            "A. Testing must only start after 100% of the code has been written and compiled.",
            "B. For every development activity, there is a corresponding test activity.",
            "C. All test levels must share the exact same test objectives and test environments.",
            "D. Testers must not be involved in requirement reviews to preserve objectivity."
        ],
        "answer": "B",
        "explanation": "Đặc trưng của testing tốt trong mọi mô hình SDLC: Với mỗi hoạt động phát triển (development activity), luôn có một hoạt động kiểm thử tương ứng (corresponding test activity); mỗi cấp độ kiểm thử có mục tiêu cụ thể riêng."
    },
    {
        "id": "Q038",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.1 SDLC Models",
        "type": "Single",
        "question": "In Agile development methodologies such as Scrum, when does testing take place?",
        "options": [
            "A. In a dedicated testing sprint at the end of the project year.",
            "B. Continuously throughout each iteration/sprint alongside development.",
            "C. Only during the weekend before each production release.",
            "D. Exclusively by the Product Owner after sprint review."
        ],
        "answer": "B",
        "explanation": "Trong các mô hình Agile (như Scrum), kiểm thử là một hoạt động liên tục (continuous) diễn ra song song với phát triển trong suốt từng Sprint/Iteration để tạo ra sản phẩm hoàn thiện sẵn sàng bàn giao (Potentially Shippable Increment)."
    },
    {
        "id": "Q039",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.2 Test Levels",
        "type": "Single",
        "question": "When testing a single module in isolation before it is integrated, a tester replaces a yet-to-be-developed caller module with a simulated program. What is this simulated component called?",
        "options": [
            "A. Stub",
            "B. Driver",
            "C. Mock Object",
            "D. Test Harness"
        ],
        "answer": "B",
        "explanation": "Driver là chương trình giả lập dùng để gọi module đang được kiểm thử (thay thế cho module gọi cấp trên chưa hoàn thành). Stub là chương trình giả lập thay thế cho module cấp dưới được gọi bởi module đang test."
    },
    {
        "id": "Q040",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.2 Test Levels",
        "type": "Single",
        "question": "What is the primary role of a 'Stub' in unit and integration testing?",
        "options": [
            "A. To invoke the module under test and pass parameters to it.",
            "B. To simulate the behavior of a missing called component that the module under test depends upon.",
            "C. To automatically format defect reports in Jira.",
            "D. To measure test case execution time."
        ],
        "answer": "B",
        "explanation": "Stub (thành phần cuống) thay thế cho một module cấp dưới chưa được viết xong, nhận lời gọi từ module đang test và trả về kết quả giả lập để module đang test có thể chạy được."
    },
    {
        "id": "Q041",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.2 Test Levels",
        "type": "Single",
        "question": "Which test level focuses PRIMARILY on the interactions and interfaces between integrated units or packages?",
        "options": [
            "A. Component Testing",
            "B. Component Integration Testing",
            "C. System Testing",
            "D. User Acceptance Testing"
        ],
        "answer": "B",
        "explanation": "Component Integration Testing tập trung vào sự tương tác và giao diện (interfaces) giữa các thành phần hoặc gói module đã được kết hợp với nhau."
    },
    {
        "id": "Q042",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.2 Test Levels",
        "type": "Single",
        "question": "What is the MAIN disadvantage of the 'Big Bang' integration testing approach?",
        "options": [
            "A. It requires too many stubs and drivers to be developed.",
            "B. When failures occur, defect localization is extremely difficult because all components were combined at once.",
            "C. It cannot be used with object-oriented languages.",
            "D. It requires end-users to sign off on technical code."
        ],
        "answer": "B",
        "explanation": "Chiến lược Big Bang gom tất cả các module lại và test cùng một lúc. Nhược điểm lớn nhất là khi xảy ra lỗi (failure), cực kỳ khó khăn để xác định lỗi xuất phát từ module nào hoặc interface nào (defect localization is very difficult)."
    },
    {
        "id": "Q043",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.2 Test Levels",
        "type": "Single",
        "question": "Which integration strategy starts testing from the topmost control module down through the hierarchy, requiring the extensive use of Stubs?",
        "options": [
            "A. Bottom-up Integration",
            "B. Top-down Integration",
            "C. Big Bang Integration",
            "D. Operational Integration"
        ],
        "answer": "B",
        "explanation": "Top-down Integration đi từ module điều khiển trên cùng xuống các module thấp hơn, do các module thấp chưa xong nên phải sử dụng rất nhiều Stub."
    },
    {
        "id": "Q044",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.2 Test Levels",
        "type": "Single",
        "question": "Which of the following BEST describes the environment requirements for System Testing?",
        "options": [
            "A. It should be the developer's personal laptop with debugging tools active.",
            "B. It should correspond as closely as possible to the eventual production environment.",
            "C. Any random virtual machine without database access is sufficient.",
            "D. It must be hosted exclusively on a mobile device."
        ],
        "answer": "B",
        "explanation": "Môi trường System Testing cần tương đồng tối đa với môi trường Production thực tế (về cấu hình server, mạng, hệ quản trị CSDL, tài nguyên) để giảm thiểu rủi ro môi trường gây ra sai lệch kết quả."
    },
    {
        "id": "Q045",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.2 Test Levels",
        "type": "Single",
        "question": "A hospital IT team performs tests to verify system backup and restore procedures, disaster recovery failover, and periodic data archiving. Which type of Acceptance Testing is this?",
        "options": [
            "A. User Acceptance Testing (UAT)",
            "B. Operational Acceptance Testing (OAT)",
            "C. Contractual Acceptance Testing",
            "D. Alpha Testing"
        ],
        "answer": "B",
        "explanation": "Operational Acceptance Testing (OAT - Kiểm thử chấp nhận vận hành) do đội ngũ quản trị hệ thống thực hiện nhằm kiểm tra: backup & restore, disaster recovery, bảo trì hệ thống, quản lý tài khoản người dùng và bảo mật hệ thống vận hành."
    },
    {
        "id": "Q046",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.2 Test Levels",
        "type": "Single",
        "question": "What is the difference between Alpha Testing and Beta Testing?",
        "options": [
            "A. Alpha testing is performed at the developing organization's site by internal staff/potential customers; Beta testing is performed at external users' own locations.",
            "B. Alpha testing is non-functional testing; Beta testing is purely functional testing.",
            "C. Alpha testing is automated; Beta testing is strictly manual.",
            "D. Alpha testing is done after Beta testing has completed."
        ],
        "answer": "A",
        "explanation": "Alpha testing được thực hiện tại địa điểm của tổ chức phát triển phần mềm (developer's site) bởi người dùng nội bộ hoặc khách hàng tiềm năng. Beta testing (field testing) được thực hiện độc lập tại chính môi trường và địa điểm của người dùng cuối (users' own site)."
    },
    {
        "id": "Q047",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.3 Test Types",
        "type": "Single",
        "question": "Testing software to assess its response time under high user concurrent load, memory consumption, and throughput is classified as:",
        "options": [
            "A. Functional Testing",
            "B. Non-functional Testing",
            "C. Structural Testing",
            "D. Confirmation Testing"
        ],
        "answer": "B",
        "explanation": "Kiểm thử hiệu năng (thời gian đáp ứng, thông lượng, sử dụng bộ nhớ) kiểm tra 'how well' (hệ thống hoạt động tốt như thế nào) chứ không phải 'what it does' (chức năng là gì), nên đây là Non-functional Testing."
    },
    {
        "id": "Q048",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.3 Test Types",
        "type": "Single",
        "question": "A tester executes a test case that previously failed. The test now passes, proving that the reported defect was corrected. What type of testing did the tester just execute?",
        "options": [
            "A. Regression Testing",
            "B. Confirmation Testing (Re-testing)",
            "C. Stress Testing",
            "D. Component Integration Testing"
        ],
        "answer": "B",
        "explanation": "Confirmation testing (còn gọi là Re-testing) là việc chạy lại đúng test case từng bị fail trước đó để xác nhận rằng defect đã được developer sửa thành công."
    },
    {
        "id": "Q049",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.3 Test Types",
        "type": "Single",
        "question": "After a developer fixes a defect in the payment gateway module, the QA team executes a test suite covering the shopping cart and user login modules to ensure they were not accidentally broken. What type of testing is this?",
        "options": [
            "A. Confirmation Testing",
            "B. Regression Testing",
            "C. Usability Testing",
            "D. Unit Testing"
        ],
        "answer": "B",
        "explanation": "Regression testing (Kiểm thử hồi quy) là việc kiểm tra các phần không bị sửa đổi của phần mềm để đảm bảo rằng việc sửa bug hoặc thay đổi code mới không vô tình làm hỏng các tính năng cũ đang hoạt động tốt."
    },
    {
        "id": "Q050",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.3 Test Types",
        "type": "Single",
        "question": "Why are regression test suites prime candidates for Test Automation?",
        "options": [
            "A. Because regression tests are run only once in a project lifecycle.",
            "B. Because regression tests are executed repeatedly after every code change, build, or release.",
            "C. Because regression tests cannot be designed using black-box techniques.",
            "D. Because automated tools can detect requirements misunderstandings better than humans."
        ],
        "answer": "B",
        "explanation": "Bộ kiểm thử hồi quy được chạy lặp đi lặp lại rất nhiều lần sau mỗi lần build/thay đổi code, do đó tự động hóa regression testing mang lại tỷ suất hoàn vốn đầu tư (ROI) rất cao và tiết kiệm nhiều công sức manual."
    },
    {
        "id": "Q051",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.4 Maintenance Testing",
        "type": "Single",
        "question": "Which of the following is a recognized TRIGGER for Maintenance Testing?",
        "options": [
            "A. Upgrading an application's database engine to a new major version (Migration).",
            "B. Writing the initial test policy for a brand-new project.",
            "C. An employee joining the QA team for the first time.",
            "D. Creating the user story cards during sprint planning."
        ],
        "answer": "A",
        "explanation": "Các yếu tố kích hoạt kiểm thử bảo trì (triggers for maintenance testing) gồm có: Sửa đổi (Modifications - enhancements, bug fixes), Chuyển đổi nền tảng (Migration - đổi HĐH, nâng cấp database), và Ngừng hoạt động (Retirement - lưu trữ dữ liệu)."
    },
    {
        "id": "Q052",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.4 Maintenance Testing",
        "type": "Single",
        "question": "What is the primary role of 'Impact Analysis' in maintenance testing?",
        "options": [
            "A. To calculate the salary bonus for developers.",
            "B. To evaluate the consequences of a change to determine how much regression testing is needed and which areas are affected.",
            "C. To automatically write test scripts without human intervention.",
            "D. To determine the exact date of project cancellation."
        ],
        "answer": "B",
        "explanation": "Impact Analysis (Phân tích tác động) giúp đánh giá hệ quả của một thay đổi (change) đối với toàn bộ hệ thống, từ đó xác định phạm vi cần kiểm thử hồi quy (regression test scope) và các khu vực bị ảnh hưởng."
    },
    {
        "id": "Q053",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.2 Test Levels",
        "type": "Single",
        "question": "Who TYPICALLY executes Component (Unit) Testing in modern software engineering?",
        "options": [
            "A. End users during Beta trials.",
            "B. The software developers who wrote the code.",
            "C. Independent third-party audit firms.",
            "D. Technical writers."
        ],
        "answer": "B",
        "explanation": "Component (Unit) testing thường do chính lập trình viên (software developers) thực hiện trong môi trường phát triển của họ (sử dụng các xUnit framework như JUnit, NUnit)."
    },
    {
        "id": "Q054",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.3 Test Types",
        "type": "Single",
        "question": "Which of the following is categorized as a Functional Test Type?",
        "options": [
            "A. Testing security vulnerability to SQL injection.",
            "B. Testing whether the calculateTax() method returns 10% tax for standard goods.",
            "C. Testing recovery time after a sudden database failure.",
            "D. Testing how easily a colorblind user can navigate the user interface."
        ],
        "answer": "B",
        "explanation": "Tính toán thuế đúng 10% cho mặt hàng chuẩn là kiểm tra chức năng hệ thống thực hiện cái gì ('what the system does' - Functional Testing). SQL injection là Security, Recovery là Reliability, Colorblind navigation là Usability (đều là Non-functional)."
    },
    {
        "id": "Q055",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.3 Test Types",
        "type": "Single",
        "question": "Can structural (white-box) testing techniques be applied at any test level?",
        "options": [
            "A. No, white-box testing is exclusively restricted to unit testing.",
            "B. Yes, white-box testing can be applied at all test levels (e.g., component testing, integration testing, system testing).",
            "C. No, white-box testing can only be applied during acceptance testing.",
            "D. Yes, but only if the software is written in C++."
        ],
        "answer": "B",
        "explanation": "Kỹ thuật White-box (dựa trên cấu trúc) có thể áp dụng ở mọi cấp độ kiểm thử: ở Component level (độ bao phủ dòng lệnh, nhánh), ở Integration level (độ bao phủ giao diện, cấu trúc gọi hàm), và ở System level (độ bao phủ luồng nghiệp vụ menu, kiến trúc)."
    },
    {
        "id": "Q056",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.2 Test Levels",
        "type": "Multiple",
        "question": "Which TWO of the following are examples of Non-functional testing? (Choose TWO options)",
        "options": [
            "A. Usability Testing",
            "B. Boundary Value Analysis of user input fields",
            "C. Performance Stress Testing",
            "D. Checking if order total equals subtotal plus shipping fee",
            "E. Use Case functional path verification"
        ],
        "answer": "A, C",
        "explanation": "Usability testing (tính khả dụng) và Performance Stress testing (kiểm thử chịu tải hiệu năng) là kiểm thử phi chức năng (Non-functional). B, D, E là kiểm thử chức năng."
    },
    {
        "id": "Q057",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.2 Test Levels",
        "type": "Single",
        "question": "What is the primary test basis for System Testing?",
        "options": [
            "A. Component code and data structures.",
            "B. System and Software Requirement Specifications (SRS), Use Cases, and Business Processes.",
            "C. Detailed class diagrams and method signatures.",
            "D. Compiler assembly output."
        ],
        "answer": "B",
        "explanation": "Test basis cho System Testing là: Tài liệu đặc tả yêu cầu phần mềm và hệ thống (SRS), Use Cases, sơ đồ quy trình nghiệp vụ (Business Processes) và tài liệu phân tích rủi ro hệ thống."
    },
    {
        "id": "Q058",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.4 Maintenance Testing",
        "type": "Single",
        "question": "When a legacy banking application is being retired and replaced by a cloud ERP, what kind of maintenance testing is CRITICAL?",
        "options": [
            "A. Testing data migration and the procedures for long-term archiving and retrieval of financial records.",
            "B. Testing the compiler optimizations of the decommissioned source code.",
            "C. Unit testing of obsolete modules.",
            "D. Code review of the discarded programming language."
        ],
        "answer": "A",
        "explanation": "Khi hệ thống bị ngừng hoạt động (Retirement), kiểm thử duy trì tập trung vào việc di chuyển dữ liệu (data migration), lưu trữ an toàn lâu dài (archiving) và khả năng trích xuất/kiểm toán dữ liệu khi cần."
    },
    {
        "id": "Q059",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.2 Test Levels",
        "type": "Single",
        "question": "Which integration strategy requires writing 'Drivers' for low-level modules while high-level modules are not yet available?",
        "options": [
            "A. Top-down Integration",
            "B. Bottom-up Integration",
            "C. Big Bang Integration",
            "D. Ad-hoc Integration"
        ],
        "answer": "B",
        "explanation": "Bottom-up Integration đi từ các module thấp nhất lên, do đó cần viết các Driver để gọi và truyền dữ liệu cho các module cấp thấp đang được test."
    },
    {
        "id": "Q060",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.1 SDLC Models",
        "type": "Single",
        "question": "What is the key advantage of an Incremental and Iterative development model (e.g., Agile) regarding testing?",
        "options": [
            "A. Testing can be completely automated with no human testers needed.",
            "B. Working software increments are produced frequently, allowing early testing and rapid stakeholder feedback.",
            "C. No documentation or test cases need to be written.",
            "D. Defect reporting is completely eliminated."
        ],
        "answer": "B",
        "explanation": "Ưu điểm lớn nhất của mô hình lặp và tăng trưởng (Agile): Các phần mềm có thể chạy được ra đời liên tục qua mỗi sprint, cho phép kiểm thử sớm và nhận phản hồi nhanh chóng từ stakeholders."
    },
    {
        "id": "Q061",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.2 Test Levels",
        "type": "Single",
        "question": "A test team verifies that an enterprise software application adheres strictly to the European Union GDPR privacy regulation. What test level / type is this?",
        "options": [
            "A. Component Testing",
            "B. Contractual and Regulatory Acceptance Testing",
            "C. Component Integration Testing",
            "D. Unit Structural Testing"
        ],
        "answer": "B",
        "explanation": "Kiểm tra sự tuân thủ các quy định pháp luật (như GDPR, HIPAA, chuẩn bảo mật ngành) là Contractual and Regulatory Acceptance Testing (Kiểm thử chấp nhận theo hợp đồng và quy chuẩn)."
    },
    {
        "id": "Q062",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.3 Test Types",
        "type": "Single",
        "question": "Which ISO standard defines quality characteristics for software product quality (such as functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability, portability)?",
        "options": [
            "A. ISO/IEC 25010",
            "B. ISO 9001",
            "C. IEEE 829",
            "D. ISO 14000"
        ],
        "answer": "A",
        "explanation": "ISO/IEC 25010 (trước đây là ISO/IEC 9126) là tiêu chuẩn quốc tế định nghĩa mô hình chất lượng sản phẩm phần mềm (Software Product Quality Model)."
    },
    {
        "id": "Q063",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.3 Test Types",
        "type": "Single",
        "question": "What is 'Portability Testing'?",
        "options": [
            "A. Testing how quickly a tester can move from one desk to another.",
            "B. Testing whether the software can be effectively transferred from one hardware, software, or operational environment to another.",
            "C. Testing the weight of the server racks.",
            "D. Testing internet bandwidth consumption."
        ],
        "answer": "B",
        "explanation": "Portability Testing (Kiểm thử tính khả chuyển) đánh giá khả năng chuyển đổi hoặc vận hành của phần mềm trên các môi trường phần cứng, hệ điều hành hoặc trình duyệt khác nhau (bao gồm adaptability, installability, replaceability)."
    },
    {
        "id": "Q064",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.2 Test Levels",
        "type": "Single",
        "question": "In System Integration Testing (SIT), what is being tested?",
        "options": [
            "A. Individual methods within a Java class.",
            "B. Interactions between the system under test and other external systems, microservices, or third-party web services.",
            "C. Font sizes in CSS files.",
            "D. Developer commit messages."
        ],
        "answer": "B",
        "explanation": "System Integration Testing (SIT) kiểm tra sự tương tác và tích hợp giữa hệ thống đang phát triển với các hệ thống bên ngoài khác (ví dụ: cổng thanh toán ngân hàng, hệ thống ERP của đối tác, các web services của bên thứ ba)."
    },
    {
        "id": "Q065",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.1 SDLC Models",
        "type": "Single",
        "question": "Which of the following is true about testing in a Waterfall lifecycle?",
        "options": [
            "A. Formal dynamic testing occurs primarily in late phases after coding has been fully completed.",
            "B. Testing starts and finishes before design begins.",
            "C. No test planning is ever documented.",
            "D. Waterfall projects do not require unit testing."
        ],
        "answer": "A",
        "explanation": "Trong mô hình Thác nước (Waterfall), việc kiểm thử động chính quy diễn ra ở các giai đoạn muộn sau khi toàn bộ mã nguồn đã được hoàn thiện, dẫn đến rủi ro phát hiện lỗi muộn và chi phí sửa lỗi cao."
    },
    {
        "id": "Q066",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.3 Test Types",
        "type": "Single",
        "question": "Which test type evaluates the ease with which users can learn, operate, and navigate an application?",
        "options": [
            "A. Maintainability Testing",
            "B. Usability Testing",
            "C. Reliability Testing",
            "D. Scalability Testing"
        ],
        "answer": "B",
        "explanation": "Usability Testing (Kiểm thử tính khả dụng) đánh giá mức độ dễ học (learnability), dễ thao tác (operability) và sự hài lòng của người dùng khi sử dụng hệ thống."
    },
    {
        "id": "Q067",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.4 Maintenance Testing",
        "type": "Single",
        "question": "Why can impact analysis be difficult in legacy software systems?",
        "options": [
            "A. Because legacy systems have too much automated documentation.",
            "B. Because specifications may be missing/outdated, and complex dependencies within old code may not be fully understood.",
            "C. Because legacy systems are written exclusively in Python.",
            "D. Because impact analysis can only be done on microservices."
        ],
        "answer": "B",
        "explanation": "Phân tích tác động đối với hệ thống cũ thường rất khó khăn do tài liệu đặc tả có thể đã bị thất lạc hoặc lạc hậu qua nhiều năm, cùng với các phụ thuộc phức tạp đan xen trong code cũ mà không ai nắm rõ toàn bộ."
    },
    {
        "id": "Q068",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.2 Test Levels",
        "type": "Multiple",
        "question": "Which TWO of the following statements about Acceptance Testing are TRUE? (Choose TWO options)",
        "options": [
            "A. Acceptance testing is solely aimed at finding crashes and memory leaks.",
            "B. Acceptance testing helps establish confidence in the system before release.",
            "C. Acceptance testing is always performed exclusively by independent penetration testers.",
            "D. Business users and customers are typical participants in User Acceptance Testing.",
            "E. Acceptance testing is only performed in sequential Waterfall models."
        ],
        "answer": "B, D",
        "explanation": "Mục tiêu chính của Acceptance Testing là xây dựng niềm tin (confidence) trước khi bàn giao (B) và đối tượng tham gia chính trong UAT là khách hàng / người dùng nghiệp vụ (D)."
    },
    {
        "id": "Q069",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.3 Test Types",
        "type": "Single",
        "question": "What is 'Maintainability Testing'?",
        "options": [
            "A. Testing how easily a system can be modified, corrected, or adapted to environmental changes.",
            "B. Testing how often the database requires battery replacements.",
            "C. Testing whether the application crashes when internet disconnects.",
            "D. Testing how fast the user can press keyboard keys."
        ],
        "answer": "A",
        "explanation": "Maintainability Testing (Kiểm thử khả năng bảo trì) đánh giá mức độ dễ dàng để sửa đổi, khắc phục sự cố, hoặc nâng cấp hệ thống (gồm tính module hóa, khả năng phân tích, khả năng tái sử dụng, khả năng kiểm thử được)."
    },
    {
        "id": "Q070",
        "chapter": "Chapter 2: Testing Throughout the SDLC",
        "topic": "2.2 Test Levels",
        "type": "Single",
        "question": "At which test level are Mock objects, Stubs, and Drivers MOST frequently utilized?",
        "options": [
            "A. Acceptance Testing",
            "B. Component (Unit) and Component Integration Testing",
            "C. User Acceptance Testing",
            "D. Operational Acceptance Testing"
        ],
        "answer": "B",
        "explanation": "Mock objects, Stubs và Drivers được sử dụng phổ biến và rộng rãi nhất ở cấp độ Component (Unit) Testing và Component Integration Testing để cô lập đối tượng cần kiểm tra."
    }
]
