# data_ch3.py - Chapter 3: Static Testing (35 Questions)

CH3_QUESTIONS = [
    {
        "id": "Q071",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.1 Static Testing Basics",
        "type": "Single",
        "question": "What is the FUNDAMENTAL difference between static testing and dynamic testing?",
        "options": [
            "A. Static testing is performed by computers, while dynamic testing is performed by humans.",
            "B. Static testing relies on manual examination or tool-driven analysis without executing the software, whereas dynamic testing requires software execution.",
            "C. Static testing cannot find code defects, whereas dynamic testing can find all document defects.",
            "D. Static testing only applies to user interface wireframes."
        ],
        "answer": "B",
        "explanation": "Điểm khác biệt cốt lõi: Static testing (kiểm thử tĩnh) kiểm tra tài liệu hoặc mã nguồn mà KHÔNG cần thực thi chương trình (không chạy code), giúp tìm trực tiếp defect; trong khi Dynamic testing (kiểm thử động) bắt buộc phải CHẠY chương trình với các giá trị đầu vào để quan sát hành vi và phát hiện failure."
    },
    {
        "id": "Q072",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.1 Static Testing Basics",
        "type": "Single",
        "question": "Which of the following defects is TYPICALLY MUCH EASIER to find using static testing (e.g., static analysis or code review) than dynamic testing?",
        "options": [
            "A. Unreachable (dead) code and undeclared variables.",
            "B. Memory leaks occurring only after 72 hours of heavy continuous load.",
            "C. Network latency fluctuations across international data centers.",
            "D. Third-party cloud service billing errors."
        ],
        "answer": "A",
        "explanation": "Static analysis và code review cực kỳ hiệu quả trong việc tìm: mã chết (dead/unreachable code), biến chưa được khởi tạo/khai báo, vi phạm coding standards, và cú pháp logic. Các lỗi về hiệu năng chịu tải lâu dài (B) hay độ trễ mạng (C) phải dùng dynamic testing."
    },
    {
        "id": "Q073",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.1 Static Testing Basics",
        "type": "Single",
        "question": "Which of the following work products CANNOT be evaluated by static testing techniques?",
        "options": [
            "A. System Requirements Specification (SRS)",
            "B. Test cases and test execution scripts",
            "C. Third-party compiled binary without source code running in live memory",
            "D. Database schema designs and SQL scripts"
        ],
        "answer": "C",
        "explanation": "Static testing có thể review hầu như mọi sản phẩm công việc dạng tài liệu hoặc mã nguồn (SRS, test cases, code, DB schema). Tuy nhiên, một file nhị phân compiled đang chạy trong RAM mà không có mã nguồn hay tài liệu thì chỉ có thể kiểm thử động (dynamic testing/black-box runtime)."
    },
    {
        "id": "Q074",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "In a formal review process, which of the following is the correct chronological sequence of phases?",
        "options": [
            "A. Planning -> Initiate review -> Individual review -> Issue communication and analysis -> Fixing and reporting",
            "B. Initiate review -> Planning -> Fixing -> Review meeting -> Individual review",
            "C. Individual review -> Planning -> Review meeting -> Fixing and reporting",
            "D. Planning -> Review meeting -> Individual review -> Fixing and reporting"
        ],
        "answer": "A",
        "explanation": "Thứ tự 5 giai đoạn của quy trình review chính quy chuẩn theo ISTQB: 1. Planning (Lập kế hoạch) -> 2. Initiate review (Khởi động) -> 3. Individual review/preparation (Từng cá nhân tự review) -> 4. Issue communication and analysis/Meeting (Họp trao đổi và ghi nhận lỗi) -> 5. Fixing and reporting (Sửa lỗi và báo cáo)."
    },
    {
        "id": "Q075",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "What is the primary activity carried out during the 'Individual Review' (Individual Preparation) phase?",
        "options": [
            "A. The author fixes all discovered defects in code.",
            "B. Each reviewer independently reviews the work product, identifying defects, questions, and anomalies.",
            "C. Management allocates budget and hardware resources.",
            "D. The moderator distributes the meeting agenda."
        ],
        "answer": "B",
        "explanation": "Trong pha Individual Review (chuẩn bị cá nhân), mỗi người tham gia tự mình đọc và phân tích tài liệu/code độc lập, ghi chép lại các defect, thắc mắc và điểm bất thường trước khi bước vào cuộc họp chung."
    },
    {
        "id": "Q076",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "Who is responsible for the overall success of a formal review meeting, acting as a neutral mediator to ensure everyone's input is heard?",
        "options": [
            "A. The Author",
            "B. The Facilitator (Moderator)",
            "C. The Customer",
            "D. The Junior Tester"
        ],
        "answer": "B",
        "explanation": "Facilitator (hay Moderator - người điều phối) là người đóng vai trò trung gian công tâm, điều hành cuộc họp review diễn ra đúng giờ, đảm bảo văn hóa thảo luận xây dựng và mọi thành viên đều được lắng nghe ý kiến."
    },
    {
        "id": "Q077",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "What is the role of the 'Scribe' (or Recorder) during a review meeting?",
        "options": [
            "A. To defend the code against all accusations of defects.",
            "B. To document all identified defects, open points, decisions, and recommendations made during the meeting.",
            "C. To determine whether the project budget should be cancelled.",
            "D. To execute automated regression test scripts."
        ],
        "answer": "B",
        "explanation": "Scribe (Recorder - thư ký) có nhiệm vụ ghi chép chính xác tất cả các defect, các vấn đề chưa thống nhất (open points), các quyết định và khuyến nghị được đưa ra trong buổi họp review."
    },
    {
        "id": "Q078",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "Which of the following review types is the MOST FORMAL, characterized by defined entry and exit criteria, formal checklists, measurement of metrics, and is LED BY A TRAINED FACILITATOR who is NOT the author?",
        "options": [
            "A. Informal Review",
            "B. Walkthrough",
            "C. Technical Review",
            "D. Inspection"
        ],
        "answer": "D",
        "explanation": "Inspection (Thanh tra) là hình thức review chính quy nhất (most formal), có tiêu chí đầu vào/đầu ra rõ ràng, dùng checklist, thu thập số liệu đo lường (metrics), và được điều hành bởi Facilitator được đào tạo (tuyệt đối không phải là tác giả của tài liệu)."
    },
    {
        "id": "Q079",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "Which type of review is TYPICALLY LED BY THE AUTHOR of the work product, with main goals of educating participants, explaining the document, and gathering feedback?",
        "options": [
            "A. Inspection",
            "B. Walkthrough",
            "C. Informal Review",
            "D. Static Code Analysis"
        ],
        "answer": "B",
        "explanation": "Walkthrough (Duyệt qua/đi dạo qua) là hình thức review do chính Tác giả (Author) chủ trì và dẫn dắt, với mục tiêu chính là giới thiệu, giải thích tài liệu cho các bên liên quan, lấy ý kiến đóng góp và đạt được sự đồng thuận."
    },
    {
        "id": "Q080",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "Two programmers sit side-by-side at one workstation, reviewing and discussing code as it is being written (pair programming). Which review type does this exemplify?",
        "options": [
            "A. Inspection",
            "B. Formal Technical Review",
            "C. Informal Review",
            "D. Management Audit"
        ],
        "answer": "C",
        "explanation": "Pair programming (lập trình theo cặp) hoặc nhờ đồng nghiệp ngồi xem hộ đoạn code (buddy check) là ví dụ điển hình của Informal Review (Review không chính quy) - không cần quy trình hay cuộc họp chính thức, tiết kiệm chi phí và diễn ra nhanh chóng."
    },
    {
        "id": "Q081",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "What is the PRIMARY focus of a 'Technical Review'?",
        "options": [
            "A. To socialize team members during lunch breaks.",
            "B. To achieve consensus on technical approaches, evaluate alternative designs, and ensure compliance with technical standards.",
            "C. To evaluate the salary increases of the engineering team.",
            "D. To negotiate the commercial software price with customers."
        ],
        "answer": "B",
        "explanation": "Technical Review tập trung vào khía cạnh kỹ thuật: đánh giá giải pháp thiết kế, so sánh các phương án kỹ thuật thay thế, đạt được sự đồng thuận giữa các kỹ sư và kiểm tra việc tuân thủ các tiêu chuẩn kỹ thuật."
    },
    {
        "id": "Q082",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "In which review technique does a reviewer evaluate the work product without any pre-defined guidelines, relying entirely on their own intuition and personal experience?",
        "options": [
            "A. Checklist-based Review",
            "B. Ad hoc Review",
            "C. Perspective-based Reading",
            "D. Role-based Review"
        ],
        "answer": "B",
        "explanation": "Ad hoc Review: Người review đọc tài liệu tự do, không có hướng dẫn hay checklist cố định nào, dựa hoàn toàn vào kinh nghiệm và trực giác của bản thân."
    },
    {
        "id": "Q083",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "Which review technique uses a set of questions (e.g., 'Are all inputs bounded?', 'Are error messages specified?') derived from past defect histories to guide the reviewer?",
        "options": [
            "A. Ad hoc Review",
            "B. Checklist-based Review",
            "C. Scenario Testing",
            "D. Fuzz Testing"
        ],
        "answer": "B",
        "explanation": "Checklist-based Review: Sử dụng danh sách các câu hỏi kiểm tra (checklists) được đúc kết từ kinh nghiệm và các defect phổ biến trong quá khứ để định hướng cho người review."
    },
    {
        "id": "Q084",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "During a requirements review, Reviewer 1 evaluates the document from the viewpoint of a Business Analyst, Reviewer 2 from the viewpoint of a Software Tester, and Reviewer 3 from the viewpoint of a Database Administrator. What review technique is being applied?",
        "options": [
            "A. Ad hoc Review",
            "B. Perspective-based Reading (PBR)",
            "C. Random Review",
            "D. Regression Review"
        ],
        "answer": "B",
        "explanation": "Perspective-based Reading (PBR - Đọc dựa trên góc nhìn): Kỹ thuật review sâu nhất, trong đó mỗi reviewer đóng vai trò một bên liên quan cụ thể (Tester, Developer, User, Security Specialist...) để phát hiện lỗi từ các lăng kính khác nhau."
    },
    {
        "id": "Q085",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "Which of the following is considered an ORGANIZATIONAL success factor for reviews?",
        "options": [
            "A. Forcing reviewers to review 200 pages of code in 30 minutes without advance notice.",
            "B. Management providing adequate time and resources for review preparation and execution.",
            "C. Evaluating developers' performance appraisals based directly on the number of bugs found in their code during reviews.",
            "D. Conducting review meetings without setting an objective."
        ],
        "answer": "B",
        "explanation": "Yếu tố thành công về mặt tổ chức của review: Ban quản lý (Management) phải bố trí đủ thời gian và nguồn lực trong kế hoạch dự án cho các hoạt động chuẩn bị và họp review. Tuyệt đối không dùng số lượng bug tìm được trong review để đánh giá trừ lương/thưởng vì sẽ phá hủy văn hóa cởi mở."
    },
    {
        "id": "Q086",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "What is the primary danger of using review defect metrics to punish or reward individual developers?",
        "options": [
            "A. Reviews will finish too quickly.",
            "B. It encourages defensiveness, concealment of defects, and destroys the collaborative culture essential for effective reviews.",
            "C. It makes compilers run slower.",
            "D. It prevents automated static analysis tools from running."
        ],
        "answer": "B",
        "explanation": "Nếu dùng số lượng defect tìm được trong review để phạt cá nhân, người viết tài liệu sẽ có xu hướng che giấu lỗi, trở nên thù địch, phòng thủ và phản ứng tiêu cực, làm mất đi tính minh bạch và tinh thần cộng tác trong nhóm."
    },
    {
        "id": "Q087",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.1 Static Testing Basics",
        "type": "Multiple",
        "question": "Which TWO of the following are benefits of static testing? (Choose TWO options)",
        "options": [
            "A. Detecting defects much earlier before dynamic test execution begins.",
            "B. Finding runtime hardware overheating issues.",
            "C. Reducing total defect fixing costs across the project lifecycle.",
            "D. Measuring real-time network transaction latency under peak load.",
            "E. Guaranteeing that the user will never request new features."
        ],
        "answer": "A, C",
        "explanation": "Lợi ích lớn nhất của Static testing: Phát hiện defect từ rất sớm khi chưa cần chạy code (A) và giảm chi phí sửa lỗi tổng thể trong toàn bộ vòng đời phát triển phần mềm (C)."
    },
    {
        "id": "Q088",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "In a review meeting, who decides whether a reported issue is an actual defect that needs fixing, an open question, or something to be rejected?",
        "options": [
            "A. The Scribe alone.",
            "B. The participants jointly through discussion, guided by the Facilitator.",
            "C. An external legal judge.",
            "D. Only the youngest team member."
        ],
        "answer": "B",
        "explanation": "Trong cuộc họp review, các thành viên tham gia thảo luận cùng nhau dưới sự điều phối của Facilitator để thống nhất xem vấn đề nêu ra có thực sự là defect cần sửa hay không."
    },
    {
        "id": "Q089",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "What type of review is typically recommended for safety-critical medical devices or avionics software standards compliance?",
        "options": [
            "A. Informal review over lunch.",
            "B. Formal Inspection with rigorous checklists and metrics tracking.",
            "C. Quick ad-hoc browsing without minutes.",
            "D. No reviews are needed for avionics software."
        ],
        "answer": "B",
        "explanation": "Đối với các hệ thống an toàn tính mạng (safety-critical) như thiết bị y tế hay hàng không, hình thức review bắt buộc là Inspection chính quy (Formal Inspection) với quy trình nghiêm ngặt, checklist chuẩn và lưu trữ biên bản kiểm toán."
    },
    {
        "id": "Q090",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.1 Static Testing Basics",
        "type": "Single",
        "question": "Which of the following can a static code analysis tool detect WITHOUT running the code?",
        "options": [
            "A. Syntax violations, unused variables, and potential null pointer dereferences.",
            "B. The exact transaction throughput under 10,000 concurrent active users.",
            "C. Server fan speed and battery degradation rate.",
            "D. The user's emotional satisfaction when viewing the landing page."
        ],
        "answer": "A",
        "explanation": "Công cụ Static Code Analysis (như SonarQube, Checkstyle, ESLint) phân tích mã nguồn và phát hiện: lỗi cú pháp, biến không dùng (dead code), nguy cơ null pointer, vi phạm chuẩn đặt tên và chuẩn bảo mật mà không cần chạy chương trình."
    },
    {
        "id": "Q091",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "In the Review Process, what does evaluating 'Exit Criteria' determine?",
        "options": [
            "A. Whether the reviewers can leave the room for lunch.",
            "B. Whether the review goals have been met and the work product can officially proceed to the next lifecycle phase.",
            "C. Which developer should be terminated.",
            "D. How many new PCs the company must buy."
        ],
        "answer": "B",
        "explanation": "Exit Criteria (Tiêu chí kết thúc review) xác định xem sản phẩm công việc đã đạt chuẩn chất lượng yêu cầu hay chưa (ví dụ: tất cả lỗi nghiêm trọng đã được sửa và xác minh) để cho phép chuyển sang giai đoạn phát triển tiếp theo."
    },
    {
        "id": "Q092",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "What is the primary role of 'Management' in supporting the review process?",
        "options": [
            "A. Acting as the Scribe during technical code inspections.",
            "B. Planning review schedules, allocating resources, and ensuring adequate time is assigned in project plans.",
            "C. Dictating exactly which lines of code must be deleted.",
            "D. Writing automated JUnit test cases."
        ],
        "answer": "B",
        "explanation": "Vai trò của Management trong review: Lập kế hoạch, phân bổ nguồn lực (nhân sự, thời gian), theo dõi tính hiệu quả về mặt chi phí và hỗ trợ văn hóa chất lượng trong tổ chức."
    },
    {
        "id": "Q093",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "Why is it recommended that the Facilitator (Moderator) in a formal Inspection should NOT be the author of the work product?",
        "options": [
            "A. Because the author does not have sufficient technical expertise.",
            "B. Because the author may have an emotional attachment to their own work and struggle to remain neutral when defects are identified.",
            "C. Because authors are prohibited from attending review meetings.",
            "D. Because facilitators must be external consultants only."
        ],
        "answer": "B",
        "explanation": "Tác giả thường có tâm lý gắn bó và bảo vệ tác phẩm của mình (emotional attachment). Việc để một người điều phối độc lập (Facilitator) chủ trì sẽ đảm bảo tính khách quan và duy trì không khí họp xây dựng."
    },
    {
        "id": "Q094",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "During which phase of the review process are documents checked against 'Entry Criteria' to avoid wasting reviewer time on immature or incomplete drafts?",
        "options": [
            "A. Fixing and reporting",
            "B. Initiate review (or Planning)",
            "C. Review meeting",
            "D. Retesting"
        ],
        "answer": "B",
        "explanation": "Trong giai đoạn Khởi động (Initiate review) hoặc Planning, tiêu chí đầu vào (Entry Criteria) được kiểm tra (ví dụ: tài liệu đã qua spell-check chưa, code đã build pass chưa) để tránh lãng phí thời gian của người review với các bản thảo quá sơ sài."
    },
    {
        "id": "Q095",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "Which review technique requires reviewers to construct user personas or assume realistic end-user roles (e.g., senior citizen, inexperienced teenager) to evaluate software usability requirements?",
        "options": [
            "A. Role-based Review",
            "B. Ad hoc Review",
            "C. Checklist-based Review",
            "D. Unit structural Review"
        ],
        "answer": "A",
        "explanation": "Role-based Review (Review dựa trên vai trò): Người đánh giá hóa thân vào các vai trò người dùng hoặc các bên liên quan cụ thể (ví dụ: người lớn tuổi, người chưa từng dùng máy tính) để đánh giá tài liệu yêu cầu."
    },
    {
        "id": "Q096",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.1 Static Testing Basics",
        "type": "Single",
        "question": "Why is static testing considered complementary to dynamic testing rather than a replacement for it?",
        "options": [
            "A. Because both find the exact same types of defects.",
            "B. Because static testing finds defects directly in documents/code, while dynamic testing exposes failures during execution; each finds defects that the other cannot easily detect.",
            "C. Because dynamic testing is completely obsolete.",
            "D. Because static testing can only be done after software deployment."
        ],
        "answer": "B",
        "explanation": "Static và Dynamic testing bổ trợ cho nhau: Static tìm trực tiếp các defect trong tài liệu và mã nguồn (như biến thừa, cú pháp sai, yêu cầu mâu thuẫn); Dynamic tìm các failure bộc lộ khi chạy thực tế (như race conditions, tràn bộ nhớ khi tải cao, lỗi kết nối mạng). Không phương pháp nào có thể thay thế hoàn toàn phương pháp kia."
    },
    {
        "id": "Q097",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "In a formal Inspection, what happens during the 'Fixing and Reporting' phase?",
        "options": [
            "A. The author fixes defects, the moderator or reviewer verifies the corrections, and metrics are finalized.",
            "B. The scribe reads all test cases out loud to the team.",
            "C. Management selects candidates for replacement.",
            "D. The customer signs the acceptance certificate."
        ],
        "answer": "A",
        "explanation": "Trong pha Fixing and Reporting, tác giả sửa chữa các defect đã được ghi nhận, người điều phối/người kiểm tra xác minh lại các bản sửa lỗi, và các số liệu đo lường chất lượng được tổng hợp."
    },
    {
        "id": "Q098",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Multiple",
        "question": "Which TWO of the following are primary objectives of an 'Inspection'? (Choose TWO options)",
        "options": [
            "A. Finding defects as efficiently and systematically as possible.",
            "B. Promoting social bonding among junior developers without taking notes.",
            "C. Collecting process and quality metrics for continuous improvement.",
            "D. Designing dynamic load test scripts.",
            "E. Demonstrating completed features to commercial end-users."
        ],
        "answer": "A, C",
        "explanation": "Hai mục tiêu cốt lõi của Inspection: Tìm kiếm defect một cách có hệ thống và hiệu quả nhất (A), đồng thời thu thập số liệu đo lường (metrics) về chất lượng và quy trình để cải tiến liên tục (C)."
    },
    {
        "id": "Q099",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.1 Static Testing Basics",
        "type": "Single",
        "question": "A tester reads through a user story specification and discovers that the business rule for calculating member discounts contradicts an earlier section on reward points. This is an example of finding a defect via:",
        "options": [
            "A. Dynamic white-box testing",
            "B. Static review of requirements",
            "C. Operational acceptance testing",
            "D. Confirmation testing"
        ],
        "answer": "B",
        "explanation": "Tester đọc tài liệu đặc tả User Story và phát hiện mâu thuẫn logic giữa các yêu cầu. Đây chính là Static Review (kiểm thử tĩnh tài liệu yêu cầu)."
    },
    {
        "id": "Q100",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "What is the recommended approach if reviewers discover that a work product distributed for inspection is riddled with basic formatting and compile errors before the review meeting?",
        "options": [
            "A. Continue the meeting anyway and spend the entire 3 hours fixing typos.",
            "B. Invoke the Entry Criteria to reject or postpone the review until the author brings the document to acceptable baseline quality.",
            "C. Cancel the software project completely.",
            "D. Blame the client."
        ],
        "answer": "B",
        "explanation": "Nếu tài liệu chưa đạt chất lượng tối thiểu ban đầu (vi phạm Entry Criteria), người điều phối cần hoãn hoặc từ chối buổi review để tác giả hoàn thiện lại, tránh làm lãng phí thời gian quý báu của toàn bộ hội đồng review."
    },
    {
        "id": "Q101",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "Which role in a review process is responsible for identifying anomalies and defects in the subject document?",
        "options": [
            "A. Reviewer",
            "B. Janitor",
            "C. Database Host",
            "D. Hardware vendor"
        ],
        "answer": "A",
        "explanation": "Reviewer (Người đánh giá) là người trực tiếp đọc, phân tích và phát hiện các điểm bất thường, sai sót và khuyết tật trong tài liệu được phân công."
    },
    {
        "id": "Q102",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "In 'Scenario-based' review technique, what guides the reviewers?",
        "options": [
            "A. A list of random words.",
            "B. Structured use case scenarios or operational workflows depicting how the work product will be used in realistic situations.",
            "C. Pure intuition without any context.",
            "D. Source code line numbers."
        ],
        "answer": "B",
        "explanation": "Scenario-based review: Người đánh giá sử dụng các kịch bản sử dụng cụ thể (use cases, quy trình nghiệp vụ thực tế) để lần theo từng bước xem tài liệu đặc tả có hỗ trợ đầy đủ kịch bản đó hay không."
    },
    {
        "id": "Q103",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.1 Static Testing Basics",
        "type": "Single",
        "question": "Which of the following is an example of a defect that dynamic testing CANNOT easily discover, but static testing can easily pinpoint?",
        "options": [
            "A. Variable defined but never used in any calculation (unused variable).",
            "B. Performance degradation under 5,000 requests/second.",
            "C. Application crash caused by packet loss over Wi-Fi.",
            "D. Screen flicker during rapid display refresh."
        ],
        "answer": "A",
        "explanation": "Một biến được khai báo nhưng không bao giờ dùng (unused variable) thường không làm sập chương trình khi chạy, nên kiểm thử động rất khó nhận ra; nhưng công cụ static analysis hoặc code review sẽ phát hiện ra ngay lập tức."
    },
    {
        "id": "Q104",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "What is a 'Defect Log' (or Review Issue Log) in the context of reviews?",
        "options": [
            "A. A list of employees who failed to attend the meeting.",
            "B. A documented record of all issues, defects, and improvement suggestions captured during the review process.",
            "C. The source code version control commit history.",
            "D. The user manual appendix."
        ],
        "answer": "B",
        "explanation": "Defect Log / Review Issue Log là biên bản ghi lại đầy đủ danh sách các vấn đề, defect và các đề xuất cải tiến được phát hiện trong quá trình review để theo dõi việc sửa lỗi."
    },
    {
        "id": "Q105",
        "chapter": "Chapter 3: Static Testing",
        "topic": "3.2 Review Process",
        "type": "Single",
        "question": "Which factor is CRITICAL to fostering a productive review meeting culture?",
        "options": [
            "A. Viewing the review as an opportunity to find bugs in the product, not to criticize the author personally.",
            "B. Threatening developers with pay cuts whenever a defect is found.",
            "C. Disallowing junior engineers from expressing opinions.",
            "D. Keeping review findings secret from the author."
        ],
        "answer": "A",
        "explanation": "Văn hóa then chốt để review hiệu quả: Coi review là cơ hội để tìm defect trong sản phẩm nhằm nâng cao chất lượng chung, tuyệt đối không biến thành buổi chỉ trích cá nhân người tạo ra sản phẩm."
    }
]
