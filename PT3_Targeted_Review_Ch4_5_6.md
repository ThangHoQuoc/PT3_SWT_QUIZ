# TRỌNG TÂM ÔN THI PROGRESS TEST 3 (PT3) - MÔN SWT301
## PHẠM VI TRỌNG TÂM: CHAPTER 4 (TECHNIQUES) + CHAPTER 5 (MANAGEMENT) + CHAPTER 6 (TOOLS)
### TỔNG SỐ: 180 CÂU HỎI CHUYÊN SÂU (BÀI TẬP TÍNH TOÁN, ĐỘ PHỦ, RỦI RO, TOOL AUTOMATION)

> **Lưu ý đặc biệt cho PT3:** Đề thi Progress Test 3 thường có tỷ trọng câu hỏi bài tập tính toán và áp dụng rất cao, đặc biệt là các dạng:
> 1. **Equivalence Partitioning & Boundary Value Analysis (2-value vs 3-value):** Xác định số phân vùng, các giá trị biên (số nguyên, số thực, ngày tháng), và số test case tối thiểu không bị error masking.
> 2. **Decision Table Testing:** Đếm số quy tắc 2^N, rút gọn bảng (collapsing rules với '-') và suy ra số test case tối thiểu.
> 3. **State Transition Testing:** Tính độ bao phủ 0-switch (1-transition coverage), 1-switch coverage, nhận biết invalid transitions.
> 4. **White-box Statement & Decision Coverage:** Tính số test case tối thiểu để đạt 100% Statement / Decision coverage cho các đoạn code if-else, while, switch; tính Cyclomatic Complexity V(G) = E - N + 2P = P + 1.
> 5. **Risk Analysis:** Tính mức độ rủi ro Risk Level = Likelihood * Impact và thứ tự ưu tiên kiểm thử.
> 6. **Defect Management & Review / Tools:** Phân biệt Severity vs Priority, trạng thái bug lifecycle, mục tiêu của Pilot Project và các rủi ro của Test Automation.

---

## BẢNG CÔNG THỨC VÀ QUY TẮC VÀNG CHO BÀI TẬP TÍNH TOÁN (CHEAT SHEET)

| Kỹ thuật / Chỉ số | Công thức / Quy tắc tính nhanh | Ví dụ kinh điển trong đề thi |
| :--- | :--- | :--- |
| **2-value BVA (cho đoạn [min, max])** | Mỗi biên có 2 điểm: {min-1, min} và {max, max+1} | Miền [1, 50] -> Điểm biên là: 0, 1, 50, 51 |
| **3-value BVA (cho đoạn [min, max])** | Mỗi biên có 3 điểm: {min-1, min, min+1} và {max-1, max, max+1} | Miền [1, 50] -> Điểm biên là: 0, 1, 2, 49, 50, 51 |
| **Số cột Decision Table đầy đủ** | $2^N$ với $N$ là số điều kiện nhị phân độc lập (True/False) | 3 điều kiện nhị phân -> $2^3 = 8$ rules (cột) |
| **0-switch Transition Coverage** | $(\text{Số transition đã test} / \text{Tổng số valid transition}) \times 100\%$ | Có 6 transition, đã chạy 5 transition -> Coverage = 83.33% |
| **Statement Coverage** | $(\text{Số statement đã chạy} / \text{Tổng số executable statement}) \times 100\%$ | `if (x>10) print('Hi')`: x=15 bao phủ 100% statement (1 test case) |
| **Decision / Branch Coverage** | $(\text{Số decision outcomes đã chạy} / \text{Tổng số outcomes}) \times 100\%$ | Cần chạy cả nhánh True và False (tối thiểu 2 test cases cho 1 if) |
| **Mối quan hệ Statement & Decision** | 100% Decision Coverage $\implies$ 100% Statement Coverage. Chiều ngược lại **KHÔNG ĐÚNG** | 100% Statement có thể chỉ đạt 50% Decision coverage nếu chỉ có nhánh True |
| **Cyclomatic Complexity $V(G)$** | 1. $V(G) = E - N + 2P$<br>2. $V(G) = P + 1$ ($P$ là số decision nodes)<br>3. $V(G) = \text{Miền kín} + 1$ | 3 câu lệnh if độc lập -> $P=3 \implies V(G) = 3 + 1 = 4$ |
| **Risk Level (Mức độ rủi ro)** | $\text{Risk Level} = \text{Likelihood} \times \text{Impact}$ | Likelihood = 4, Impact = 5 -> Risk = 20 (ưu tiên test trước) |
| **Defect Density** | $\text{Defect Density} = \text{Số lỗi} / \text{Quy mô (KLOC / FPs)}$ | 50 lỗi trong 10.000 dòng code -> 5 lỗi / KLOC |

---

## NGÂN HÀNG 180 CÂU HỎI LUYỆN TẬP CHUYÊN SÂU CHO PT3 (Từ Q106 đến Q300)

### Q106. [Chapter 4: Test Analysis and Design - 4.1 Categories of Test Techniques] (Chọn 1 đáp án đúng)

Which of the following BEST characterizes Black-box (specification-based) test techniques?

- **A.** Test cases are derived from the internal source code and control flow logic.
- **B.** Test cases are derived from analysis of the specified behavior and requirements of the software without reference to its internal structure.
- **C.** Test cases are created solely based on the personal intuition and gut feelings of the developer.
- **D.** Test cases are generated automatically by compilers.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q106)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Black-box test techniques (kỹ thuật hộp đen / dựa trên đặc tả): Test cases được thiết kế dựa trên yêu cầu, đặc tả chức năng và hành vi của hệ thống mà không cần biết hay can thiệp vào cấu trúc mã nguồn bên trong.
</details>

---

### Q107. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Equivalence Partitioning] (Chọn 1 đáp án đúng)

An input field accepts an integer age for purchasing a child ticket: valid age is between 3 and 12 (inclusive). Which of the following correctly identifies all the equivalence partitions for this input?

- **A.** One valid partition: [3, 12]; Two invalid partitions: age < 3 and age > 12.
- **B.** One valid partition: [3, 12]; One invalid partition: age != 7.
- **C.** Two valid partitions: [3, 7] and [8, 12]; No invalid partitions.
- **D.** Infinite valid partitions.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q107)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Với miền giá trị tuổi hợp lệ từ 3 đến 12 (bao gồm cả 3 và 12): Có 1 phân vùng tương đương hợp lệ là [3, 12] và 2 phân vùng tương đương không hợp lệ là age < 3 (ví dụ 2) và age > 12 (ví dụ 13).
</details>

---

### Q108. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Equivalence Partitioning] (Chọn 1 đáp án đúng)

Why should invalid equivalence partitions be tested SEPARATELY rather than combined into a single test case?

- **A.** To save execution time.
- **B.** To avoid error masking, where one invalid input hides the failure or prevents the evaluation of another invalid input.
- **C.** Because test automation tools cannot accept more than one input value.
- **D.** It is an optional guideline with no technical justification.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q108)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Hiện tượng che giấu lỗi (Error Masking): Nếu kết hợp nhiều giá trị không hợp lệ trong cùng 1 test case, hệ thống có thể từ chối ngay ở trường đầu tiên và không kiểm tra trường thứ hai, làm che giấu lỗi tiềm ẩn ở trường thứ hai. Do đó mỗi giá trị invalid cần được test riêng lẻ.
</details>

---

### Q109. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Boundary Value Analysis] (Chọn 1 đáp án đúng)

A system accepts an order quantity between 1 and 50 units (inclusive). Using 2-value Boundary Value Analysis (BVA), which set of test input values is required?

- **A.** 0, 1, 50, 51
- **B.** 1, 25, 50
- **C.** 0, 1, 2, 49, 50, 51
- **D.** -1, 0, 50, 100

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q109)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Trong kỹ thuật 2-value BVA (phân tích giá trị biên 2 điểm): Với miền hợp lệ [1, 50], các giá trị biên là cận dưới và giá trị ngay ngoài cận dưới (1 và 0), cùng với cận trên và giá trị ngay ngoài cận trên (50 và 51). Tập giá trị là {0, 1, 50, 51}.
</details>

---

### Q110. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Boundary Value Analysis] (Chọn 1 đáp án đúng)

Using 3-value Boundary Value Analysis (BVA) for the integer range [10, 100], which values should be selected for the lower boundary (around 10)?

- **A.** 9, 10, 11
- **B.** 10, 100
- **C.** 8, 9, 10
- **D.** 9, 10

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q110)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** 3-value BVA chọn 3 giá trị tại mỗi biên: giá trị tại biên, giá trị ngay dưới biên và giá trị ngay trên biên. Tại biên dưới 10, ba giá trị là: 9 (just below), 10 (boundary), 11 (just above).
</details>

---

### Q111. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Equivalence Partitioning] (Chọn 1 đáp án đúng)

A student grading module gives:
- Grade A for score 85 to 100
- Grade B for score 70 to 84
- Grade C for score 50 to 69
- Grade F for score 0 to 49
Scores below 0 or above 100 are rejected as invalid.
What is the MINIMUM number of test cases required to achieve 100% Equivalence Partitioning coverage?

- **A.** 4 test cases
- **B.** 5 test cases
- **C.** 6 test cases
- **D.** 8 test cases

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q111)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `C`
- **GIẢI THÍCH:** Có 4 phân vùng hợp lệ: [85, 100], [70, 84], [50, 69], [0, 49] và 2 phân vùng không hợp lệ: score < 0 và score > 100. Tổng cộng có 6 phân vùng tương đương. Để đạt 100% EP coverage, cần tối thiểu 6 test cases (mỗi test case đại diện cho 1 phân vùng).
</details>

---

### Q112. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Decision Table Testing] (Chọn 1 đáp án đúng)

A decision table has 3 independent binary (True/False) conditions. How many total columns (combinations/rules) does the fully expanded truth table contain?

- **A.** 3
- **B.** 6
- **C.** 8
- **D.** 9

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q112)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `C`
- **GIẢI THÍCH:** Với N điều kiện nhị phân độc lập, số lượng cột (rules/tổ hợp) tối đa là 2^N. Với N = 3 điều kiện: 2^3 = 8 cột.
</details>

---

### Q113. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Decision Table Testing] (Chọn 1 đáp án đúng)

In a Decision Table, what does a dash ('-') or 'N/A' (Don't Care) in a condition row indicate?

- **A.** The condition is impossible to test.
- **B.** The value of this condition does not affect the outcome/action for that rule.
- **C.** The test case failed during execution.
- **D.** The developer forgot to implement the feature.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q113)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Dấu gạch ngang ('-') hoặc Don't Care trong bảng quyết định thể hiện rằng giá trị của điều kiện đó (dù là True hay False) đều không làm thay đổi hành động (action) sinh ra của quy tắc đó. Nó cho phép gộp 2 cột thành 1.
</details>

---

### Q114. [Chapter 4: Test Analysis and Design - 4.2 Black-box: State Transition Testing] (Chọn 1 đáp án đúng)

In State Transition Testing, what is '0-switch coverage' (also known as branch transition coverage)?

- **A.** Testing every state only once without triggering transitions.
- **B.** Testing all valid individual transitions between states at least once.
- **C.** Testing all sequences of two consecutive transitions.
- **D.** Executing zero tests on the state machine.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q114)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** 0-switch coverage (hay 1-transition coverage) yêu cầu mọi bước chuyển trạng thái hợp lệ đơn lẻ (single valid transition) phải được thực thi ít nhất một lần. 1-switch coverage là kiểm tra chuỗi 2 bước chuyển liên tiếp.
</details>

---

### Q115. [Chapter 4: Test Analysis and Design - 4.2 Black-box: State Transition Testing] (Chọn 1 đáp án đúng)

An online shopping order has the following states: [Cart] -> [Checkout] -> [Paid] -> [Shipped] -> [Delivered]. A customer in [Cart] state attempts to click 'Delivered'. What does this scenario represent in State Transition Testing?

- **A.** A valid 0-switch transition
- **B.** An invalid (disallowed) transition test case
- **C.** A circular loop transition
- **D.** A white-box branch coverage metric

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q115)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Việc cố gắng chuyển từ trạng thái [Cart] thẳng sang [Delivered] là một bước chuyển không hợp lệ (Invalid / Disallowed Transition). Kiểm tra các bước chuyển không hợp lệ là một phần quan trọng của State Transition Testing nhằm xác minh hệ thống có bắt lỗi và ngăn chặn hành vi sai trái hay không.
</details>

---

### Q116. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Use Case Testing] (Chọn 1 đáp án đúng)

When designing test cases from a Use Case specification, which path is TYPICALLY tested first?

- **A.** The exception flow when server loses power.
- **B.** The basic (main success/happy) flow representing normal, error-free execution.
- **C.** The database rollback scenario.
- **D.** The boundary timeout flow.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q116)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Khi thiết kế test case từ Use Case, luồng cơ bản (Basic flow / Happy path / Main success scenario) mô tả quá trình thực hiện thông suốt, thành công và không gặp lỗi luôn được ưu tiên kiểm tra đầu tiên.
</details>

---

### Q117. [Chapter 4: Test Analysis and Design - 4.3 White-box: Statement Coverage] (Chọn 1 đáp án đúng)

Consider the following pseudocode snippet:
```
1: Read(x);
2: if (x > 10) {
3:     print("Large");
4: }
5: print("Done");
```
What is the MINIMUM number of test cases required to achieve 100% Statement Coverage?

- **A.** 1 test case (e.g., x = 15)
- **B.** 2 test cases (e.g., x = 15 and x = 5)
- **C.** 3 test cases
- **D.** 0 test cases

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q117)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Để đạt 100% Statement Coverage (bao phủ tất cả dòng lệnh): Chỉ cần chạy 1 test case với x = 15 (x > 10 là True). Khi đó dòng 1, 2, 3, 4, 5 đều được thực thi. Do đó số test case tối thiểu là 1.
</details>

---

### Q118. [Chapter 4: Test Analysis and Design - 4.3 White-box: Decision Coverage] (Chọn 1 đáp án đúng)

Consider the exact same pseudocode snippet:
```
1: Read(x);
2: if (x > 10) {
3:     print("Large");
4: }
5: print("Done");
```
What is the MINIMUM number of test cases required to achieve 100% Decision (Branch) Coverage?

- **A.** 1 test case
- **B.** 2 test cases (e.g., x = 15 [True] and x = 5 [False])
- **C.** 3 test cases
- **D.** 4 test cases

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q118)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Cấu trúc 'if (x > 10)' có 2 kết quả quyết định (decision outcomes): True và False. Để đạt 100% Decision Coverage, phải thực thi cả 2 nhánh True và False. Cần tối thiểu 2 test cases: 1 test case cho True (ví dụ x = 15) và 1 test case cho False (ví dụ x = 5).
</details>

---

### Q119. [Chapter 4: Test Analysis and Design - 4.3 White-box: Coverage Relationships] (Chọn 1 đáp án đúng)

Which of the following statements correctly expresses the relationship between Statement Coverage and Decision Coverage?

- **A.** 100% Statement Coverage guarantees 100% Decision Coverage.
- **B.** 100% Decision Coverage guarantees 100% Statement Coverage, but 100% Statement Coverage does NOT guarantee 100% Decision Coverage.
- **C.** There is no relationship between Statement Coverage and Decision Coverage.
- **D.** Decision Coverage can never exceed 50%.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q119)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Định lý cốt lõi trong White-box testing: Đạt 100% Decision Coverage luôn luôn đảm bảo đạt 100% Statement Coverage. Tuy nhiên, chiều ngược lại KHÔNG đúng: 100% Statement Coverage KHÔNG đảm bảo 100% Decision Coverage (như ví dụ với câu lệnh if đơn không có else).
</details>

---

### Q120. [Chapter 4: Test Analysis and Design - 4.3 White-box: Cyclomatic Complexity] (Chọn 1 đáp án đúng)

A control flow graph of a method has 9 edges (E), 7 nodes (N), and 1 connected component (P = 1). What is the McCabe Cyclomatic Complexity V(G)?

- **A.** 2
- **B.** 4
- **C.** 9
- **D.** 16

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q120)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Công thức tính Cyclomatic Complexity của McCabe: V(G) = E - N + 2P. Ở đây E = 9, N = 7, P = 1. Ta có: V(G) = 9 - 7 + 2(1) = 2 + 2 = 4.
</details>

---

### Q121. [Chapter 4: Test Analysis and Design - 4.3 White-box: Cyclomatic Complexity] (Chọn 1 đáp án đúng)

A Java method contains 3 independent simple 'if' statements and no loops or switch blocks. Using the predicate formula V(G) = P + 1 (where P is the number of decision points), what is the Cyclomatic Complexity?

- **A.** 3
- **B.** 4
- **C.** 7
- **D.** 8

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q121)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Với mỗi điểm quyết định nhị phân (decision point/predicate node), P = 3. Độ phức tạp Cyclomatic V(G) = P + 1 = 3 + 1 = 4. Đây cũng là số đường đi độc lập tuyến tính (basis paths) tối đa trong hàm.
</details>

---

### Q122. [Chapter 4: Test Analysis and Design - 4.4 Experience-based Techniques] (Chọn 1 đáp án đúng)

A veteran tester anticipates that users will likely enter blank spaces, special characters ($#@!), or paste 10,000 characters into the username box because similar bugs occurred in three past projects. Which testing technique is being applied?

- **A.** Decision Table Testing
- **B.** Error Guessing
- **C.** Finite State Testing
- **D.** Statement Testing

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q122)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Error Guessing (Đoán lỗi): Kỹ thuật dựa trên kinh nghiệm, kiến thức về các lỗi phổ biến trong quá khứ và trực giác của tester để dự đoán những lỗi mà developer dễ mắc phải.
</details>

---

### Q123. [Chapter 4: Test Analysis and Design - 4.4 Experience-based Techniques] (Chọn 1 đáp án đúng)

What is the key characteristic of Exploratory Testing?

- **A.** Test cases are fully documented and frozen six months prior to execution.
- **B.** Test design, test execution, test logging, and learning are performed concurrently during time-boxed sessions.
- **C.** Testing is executed completely at random by an automated bot without human oversight.
- **D.** It requires 100% white-box branch coverage.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q123)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Exploratory Testing (Kiểm thử thăm dò): Quá trình học hỏi (learning), thiết kế kiểm thử (test design), thực thi (execution) và ghi chép (logging) diễn ra đồng thời (concurrently) trong các phiên có giới hạn thời gian (time-boxed sessions) dựa trên test charter.
</details>

---

### Q124. [Chapter 4: Test Analysis and Design - 4.4 Experience-based Techniques] (Chọn 1 đáp án đúng)

In Session-Based Test Management (SBTM) for exploratory testing, what document guides the tester by specifying the mission and scope of the test session?

- **A.** Test Policy
- **B.** Test Charter
- **C.** Test Script
- **D.** Defect Density Matrix

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q124)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Test Charter (Hiến chương kiểm thử) xác định mục tiêu (mission), phạm vi (scope) và các rủi ro trọng tâm cần khám phá trong một phiên kiểm thử thăm dò (time-box thường kéo dài từ 60 đến 120 phút).
</details>

---

### Q125. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Boundary Value Analysis] (Chọn 1 đáp án đúng)

A system calculates shipping rates based on weight W in kilograms:
- 0 < W <= 5: $10
- 5 < W <= 20: $25
- 20 < W <= 50: $50
Weights <= 0 or > 50 are invalid.
Using 2-value Boundary Value Analysis, which values should test the boundary between the first and second valid partitions around W = 5?

- **A.** 5 and 6 (or 5.0 and 5.1 for decimals)
- **B.** 0 and 50
- **C.** 1 and 20
- **D.** 4 and 6

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q125)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Tại ranh giới giữa 2 khoảng (0, 5] và (5, 20]: Biên là 5 (thuộc phân vùng 1) và giá trị ngay sát trên 5 (ví dụ 6 nếu là số nguyên, hoặc 5.1 nếu là số thập phân) thuộc phân vùng 2.
</details>

---

### Q126. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Decision Table Testing] (Chọn 1 đáp án đúng)

Consider a decision table for a banking loan with 4 binary conditions:
1. Employed (Y/N)
2. Credit Score > 700 (Y/N)
3. Existing Debt < $10,000 (Y/N)
4. Collateral Available (Y/N)
If no rules can be collapsed, how many test cases are required for full decision table coverage?

- **A.** 4
- **B.** 8
- **C.** 16
- **D.** 32

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q126)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `C`
- **GIẢI THÍCH:** Số quy tắc (cột) đầy đủ khi có 4 điều kiện nhị phân độc lập là 2^4 = 16 quy tắc tương ứng 16 test cases.
</details>

---

### Q127. [Chapter 4: Test Analysis and Design - 4.3 White-box: Decision Coverage] (Chọn 1 đáp án đúng)

Consider the following code snippet:
```
if (A && B) {
    executeAction1();
} else {
    executeAction2();
}
```
To achieve 100% Decision (Branch) Coverage, which of the following pairs of test inputs (A, B) is SUFFICIENT?

- **A.** Test 1: (A=True, B=True) -> True branch; Test 2: (A=False, B=True) -> False branch
- **B.** Test 1: (A=True, B=False); Test 2: (A=False, B=True)
- **C.** Test 1: (A=True, B=True); Test 2: (A=True, B=True)
- **D.** Only 4 test cases can achieve Decision Coverage.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q127)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Decision Coverage chỉ quan tâm đến toàn bộ biểu thức điều kiện (A && B) trả về True hay False: Cần 1 test case làm (A && B) = True (chính là A=True, B=True) và 1 test case làm (A && B) = False (ví dụ A=False, B=True). Như vậy chỉ cần 2 test cases là đủ 100% Decision Coverage.
</details>

---

### Q128. [Chapter 4: Test Analysis and Design - 4.3 White-box: Statement Coverage] (Chọn 1 đáp án đúng)

Consider this code:
```
int discount = 0;
if (isMember) {
    discount = 10;
}
if (couponCodeValid) {
    discount += 5;
}
return discount;
```
What is the MINIMUM number of test cases required to achieve 100% Statement Coverage?

- **A.** 1 test case: (isMember = True, couponCodeValid = True)
- **B.** 2 test cases
- **C.** 4 test cases
- **D.** 3 test cases

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q128)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Chỉ cần 1 test case với cả hai điều kiện đều True: isMember = True và couponCodeValid = True. Khi đó cả hai khối lệnh bên trong if đều được thực thi, đảm bảo 100% các dòng lệnh trong hàm đều được chạy qua.
</details>

---

### Q129. [Chapter 4: Test Analysis and Design - 4.3 White-box: Decision Coverage] (Chọn 1 đáp án đúng)

For the same code:
```
int discount = 0;
if (isMember) {
    discount = 10;
}
if (couponCodeValid) {
    discount += 5;
}
return discount;
```
What is the MINIMUM number of test cases required to achieve 100% Decision Coverage?

- **A.** 1 test case
- **B.** 2 test cases: Test 1 (True, True) and Test 2 (False, False)
- **C.** 4 test cases
- **D.** 3 test cases

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q129)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Có 2 câu lệnh if độc lập, mỗi if có 2 nhánh True và False (tổng cộng 4 nhánh: If1-True, If1-False, If2-True, If2-False). Cần tối thiểu 2 test cases: Test 1 (isMember=True, couponCodeValid=True) bao phủ If1-True và If2-True; Test 2 (isMember=False, couponCodeValid=False) bao phủ If1-False và If2-False. Tổng cộng 2 test cases đạt 100% Decision Coverage.
</details>

---

### Q130. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Equivalence Partitioning] (Chọn 1 đáp án đúng)

A PIN code for a debit card must consist of EXACTLY 4 numeric digits. Which of the following represents an INVALID equivalence partition?

- **A.** '1234'
- **B.** '9081'
- **C.** '123' (3 digits) or '12345' (5 digits)
- **D.** '0000'

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q130)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `C`
- **GIẢI THÍCH:** PIN hợp lệ gồm đúng 4 chữ số. Phân vùng không hợp lệ (Invalid Partition) bao gồm: ít hơn 4 chữ số (ví dụ '123'), nhiều hơn 4 chữ số (ví dụ '12345'), hoặc chứa ký tự không phải số (ví dụ '12A4').
</details>

---

### Q131. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Use Case Testing] (Chọn 1 đáp án đúng)

In Use Case Testing, what is an 'Extension' or 'Alternative Flow'?

- **A.** The path where everything works perfectly without variation.
- **B.** A path describing alternative ways of achieving the goal or optional user behaviors.
- **C.** A compiler plug-in used to build Java code.
- **D.** The physical internet cable connected to the computer.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q131)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Alternative Flow (Luồng thay thế / mở rộng) mô tả các nhánh rẽ khác để hoàn thành mục tiêu hoặc các hành vi tùy chọn của người dùng (ví dụ: thanh toán bằng thẻ tín dụng thay vì thanh toán bằng ví điện tử).
</details>

---

### Q132. [Chapter 4: Test Analysis and Design - 4.2 Black-box: State Transition Testing] (Chọn 1 đáp án đúng)

In a state transition diagram with 4 states and 6 transitions, a test suite exercises 5 of the 6 transitions. What is the 0-switch transition coverage?

- **A.** 50%
- **B.** 83.33%
- **C.** 100%
- **D.** 75%

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q132)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Độ bao phủ chuyển trạng thái 0-switch = (Số transition được thực thi / Tổng số transition) * 100% = (5 / 6) * 100% = 83.33%.
</details>

---

### Q133. [Chapter 4: Test Analysis and Design - 4.3 White-box: Statement vs Decision Coverage] (Chọn 1 đáp án đúng)

A test suite achieves 100% Statement Coverage on a module containing 4 'if-then' statements (without 'else'). What is the MINIMUM possible Decision Coverage that this test suite could have achieved?

- **A.** 100%
- **B.** 50%
- **C.** 0%
- **D.** 25%

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q133)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Nếu test case làm cho cả 4 câu lệnh if đều rơi vào nhánh True, tất cả dòng lệnh đều được thực thi (đạt 100% Statement Coverage). Tuy nhiên, cả 4 nhánh False đều chưa được thực thi lần nào. Vì có 8 nhánh quyết định (4 True + 4 False) mà mới chạy 4 nhánh True, nên Decision Coverage tối thiểu có thể chỉ là 4/8 = 50%.
</details>

---

### Q134. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Decision Table Testing] (Chọn 1 đáp án đúng)

Two rules in a decision table have identical actions. Rule 1 requires Condition A = True, Condition B = True. Rule 2 requires Condition A = True, Condition B = False. How can these two rules be simplified (collapsed)?

- **A.** By deleting Condition A.
- **B.** By merging them into a single rule with Condition A = True and Condition B = '-' (Don't Care).
- **C.** They cannot be simplified.
- **D.** By setting Action = False.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q134)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Vì khi Condition A = True thì dù Condition B là True hay False thì kết quả Action đều giống hệt nhau, ta có thể gộp (collapse) 2 rule này thành 1 rule duy nhất: Condition A = True, Condition B = '-' (Don't Care).
</details>

---

### Q135. [Chapter 4: Test Analysis and Design - 4.4 Experience-based Techniques] (Chọn 1 đáp án đúng)

When is Exploratory Testing MOST USEFUL and effective?

- **A.** When specifications are scarce or poorly documented, and when rapid feedback is required under tight schedules.
- **B.** When automated testing is legally mandated to be 100% repeatable.
- **C.** When testers have zero domain knowledge and zero software experience.
- **D.** When no software has been written yet.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q135)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Exploratory testing phát huy hiệu quả cao nhất khi tài liệu đặc tả thiếu thốn hoặc sơ sài, thời gian gấp rút cần phản hồi nhanh, hoặc dùng để bổ trợ sau khi đã chạy xong các test case formal nhằm tìm thêm các lỗi bất ngờ.
</details>

---

### Q136. [Chapter 4: Test Analysis and Design - 4.1 Categories of Test Techniques] (Chọn nhiều đáp án)

Which TWO of the following are classified as White-box test techniques? (Choose TWO options)

- **A.** Statement Testing
- **B.** Equivalence Partitioning
- **C.** Decision (Branch) Testing
- **D.** State Transition Testing
- **E.** Use Case Testing

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q136)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A, C`
- **GIẢI THÍCH:** Statement Testing và Decision Testing là các kỹ thuật White-box (dựa trên cấu trúc mã nguồn). B, D, E là các kỹ thuật Black-box (dựa trên đặc tả).
</details>

---

### Q137. [Chapter 4: Test Analysis and Design - 4.1 Categories of Test Techniques] (Chọn nhiều đáp án)

Which TWO of the following are Experience-based test techniques? (Choose TWO options)

- **A.** Error Guessing
- **B.** Boundary Value Analysis
- **C.** Exploratory Testing
- **D.** Decision Table Testing
- **E.** Cyclomatic Complexity Analysis

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q137)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A, C`
- **GIẢI THÍCH:** Error Guessing và Exploratory Testing là các kỹ thuật kiểm thử dựa trên kinh nghiệm (Experience-based techniques).
</details>

---

### Q138. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Equivalence Partitioning] (Chọn 1 đáp án đúng)

A bonus salary calculation specifies:
- Employees with tenure 0 to < 2 years: 0% bonus
- Employees with tenure 2 to < 5 years: 10% bonus
- Employees with tenure 5 to 10 years: 20% bonus
Negative tenure is invalid. How many valid equivalence partitions exist?

- **A.** 1
- **B.** 2
- **C.** 3
- **D.** 4

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q138)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `C`
- **GIẢI THÍCH:** Có 3 phân vùng hợp lệ: [0, 2), [2, 5), và [5, 10]. Phân vùng < 0 hoặc > 10 là không hợp lệ.
</details>

---

### Q139. [Chapter 4: Test Analysis and Design - 4.3 White-box: Statement Coverage] (Chọn 1 đáp án đúng)

A program contains 20 executable statements. A single test case executes 15 of these statements. What is the Statement Coverage percentage?

- **A.** 50%
- **B.** 75%
- **C.** 80%
- **D.** 100%

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q139)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Statement Coverage = (Số câu lệnh đã thực thi / Tổng số câu lệnh) * 100% = (15 / 20) * 100% = 75%.
</details>

---

### Q140. [Chapter 4: Test Analysis and Design - 4.3 White-box: Decision Coverage] (Chọn 1 đáp án đúng)

A program contains 6 decision points (each having 2 outcomes: True and False). A test suite executes 9 of the 12 possible decision outcomes. What is the Decision Coverage?

- **A.** 50%
- **B.** 75%
- **C.** 90%
- **D.** 66.7%

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q140)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Tổng số decision outcomes = 6 * 2 = 12. Số outcomes đã thực thi = 9. Decision Coverage = (9 / 12) * 100% = 75%.
</details>

---

### Q141. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Boundary Value Analysis] (Chọn 1 đáp án đúng)

A field accepts a string whose length must be between 5 and 20 characters. What string lengths represent the 2-value boundary values?

- **A.** 4, 5, 20, 21
- **B.** 5, 20
- **C.** 0, 5, 20, 100
- **D.** 4, 5, 6, 19, 20, 21

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q141)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Độ dài chuỗi hợp lệ L trong khoảng [5, 20]. Áp dụng 2-value BVA: Giá trị biên dưới là 5 và giá trị kế cận ngoài là 4. Giá trị biên trên là 20 và giá trị kế cận ngoài là 21. Tập giá trị biên cần test độ dài là {4, 5, 20, 21}.
</details>

---

### Q142. [Chapter 4: Test Analysis and Design - 4.2 Black-box: State Transition Testing] (Chọn 1 đáp án đúng)

An authentication system allows up to 3 failed login attempts before locking an account. The states are: [Unlocked], [Locked]. The events are: 'Valid password' and 'Invalid password'. Which test case will transition the state from [Unlocked] to [Locked]?

- **A.** Enter 1 invalid password then 1 valid password.
- **B.** Enter 3 consecutive invalid passwords.
- **C.** Enter 1 valid password.
- **D.** Leave the password field blank once.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q142)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Theo đặc tả máy trạng thái, điều kiện bảo vệ (guard condition) để chuyển từ Unlocked sang Locked là số lần nhập sai liên tiếp đạt ngưỡng 3 lần (3 consecutive invalid passwords).
</details>

---

### Q143. [Chapter 4: Test Analysis and Design - 4.3 White-box: Cyclomatic Complexity] (Chọn 1 đáp án đúng)

What does Cyclomatic Complexity represent in terms of white-box testing?

- **A.** The total number of bugs found in the code.
- **B.** The upper bound for the number of linearly independent paths needed to achieve 100% branch/decision coverage.
- **C.** The execution time of the program in milliseconds.
- **D.** The number of developers needed to maintain the software.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q143)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Độ phức tạp Cyclomatic (McCabe) cung cấp giới hạn trên cho số lượng đường đi độc lập tuyến tính (basis paths) cần thiết trong đồ thị luồng điều khiển để đạt được độ bao phủ nhánh hoàn chỉnh.
</details>

---

### Q144. [Chapter 4: Test Analysis and Design - 4.4 Experience-based Techniques] (Chọn 1 đáp án đúng)

What is 'Checklist-based Testing'?

- **A.** An experience-based technique where testers design, implement, and execute tests to cover test conditions found in a checklist.
- **B.** Writing random code in a text file.
- **C.** Only checking if the computer monitor is plugged in.
- **D.** An automated technique that executes all database tables.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q144)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Checklist-based testing: Kỹ thuật kiểm thử dựa trên kinh nghiệm, trong đó tester dựa vào một danh sách các mục cần kiểm tra (checklist - đúc kết từ kinh nghiệm, chuẩn chất lượng, hoặc lỗi hay gặp) để thiết kế và thực thi test.
</details>

---

### Q145. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Decision Table Testing] (Chọn 1 đáp án đúng)

In a Decision Table, conditions represent ______ and actions represent ______.

- **A.** Outputs; Inputs
- **B.** Inputs or system states; Outputs or system responses
- **C.** Developers; Testers
- **D.** Bugs; Fixes

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q145)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Trong Bảng quyết định (Decision Table): Các hàng Conditions (Điều kiện) đại diện cho các đầu vào (inputs) hoặc trạng thái hệ thống; các hàng Actions (Hành động) đại diện cho các đầu ra (outputs) hoặc phản hồi của hệ thống.
</details>

---

### Q146. [Chapter 4: Test Analysis and Design - 4.3 White-box: Statement Coverage] (Chọn 1 đáp án đúng)

Given the code:
```
if (temperature > 37.5) {
    alertPatient();
    logRecord();
}
```
If a tester runs one test with temperature = 36.0, what is the statement coverage achieved?

- **A.** 100%
- **B.** 33.3%
- **C.** 0%
- **D.** 50%

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q146)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Khi temperature = 36.0, điều kiện 'if (temperature > 37.5)' là False. Khối lệnh bên trong gồm alertPatient() và logRecord() bị bỏ qua. Chỉ có dòng lệnh kiểm tra điều kiện if được thực thi. Trong 3 câu lệnh có thể thực thi, chỉ 1 được chạy -> độ bao phủ dòng lệnh đạt xấp xỉ 33.3%.
</details>

---

### Q147. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Use Case Testing] (Chọn 1 đáp án đúng)

Which of the following is an example of an 'Exception Flow' in a Use Case for withdrawing cash from an ATM?

- **A.** User inserts card, enters correct PIN, and receives cash.
- **B.** User requests an amount greater than the ATM's available cash balance, and the transaction is cancelled with an error message.
- **C.** User chooses to print a receipt after cash withdrawal.
- **D.** User selects English instead of Vietnamese.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q147)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Exception Flow (Luồng ngoại lệ) mô tả tình huống lỗi ngăn cản Actor đạt được mục tiêu chính (ví dụ: máy ATM hết tiền, tài khoản không đủ số dư, thẻ bị khóa).
</details>

---

### Q148. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Equivalence Partitioning] (Chọn 1 đáp án đúng)

An online store accepts coupon codes with the following rule: code must be either 'SAVE10', 'SAVE20', or 'FREESHIP'. Any other string is invalid. How many equivalence partitions are there?

- **A.** 1 valid partition, 1 invalid partition
- **B.** 3 valid partitions ('SAVE10', 'SAVE20', 'FREESHIP') and 1 invalid partition (any other string)
- **C.** Infinite valid partitions
- **D.** 2 valid partitions and 0 invalid partitions

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q148)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Vì mỗi mã giảm giá hợp lệ mang lại một mức giảm giá khác nhau ('SAVE10' giảm 10%, 'SAVE20' giảm 20%, 'FREESHIP' miễn phí vận chuyển), mỗi mã hợp lệ là một phân vùng riêng biệt (3 valid partitions). Bất kỳ chuỗi nào khác là phân vùng không hợp lệ (1 invalid partition). Tổng cộng 4 phân vùng.
</details>

---

### Q149. [Chapter 4: Test Analysis and Design - 4.3 White-box: Control Flow Graphs] (Chọn 1 đáp án đúng)

In a Control Flow Graph (CFG), what do NODES and EDGES represent?

- **A.** Nodes represent test cases, edges represent bug reports.
- **B.** Nodes represent one or more sequential statements; edges represent transfers of control (branches) between nodes.
- **C.** Nodes represent programmers, edges represent network cables.
- **D.** Nodes represent database tables, edges represent foreign keys.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q149)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Trong Đồ thị luồng điều khiển (Control Flow Graph): Nodes (Đỉnh) đại diện cho một khối các câu lệnh thực thi tuần tự; Edges (Cạnh nối) đại diện cho luồng chuyển giao điều khiển giữa các đỉnh (các nhánh rẽ True/False).
</details>

---

### Q150. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Boundary Value Analysis] (Chọn 1 đáp án đúng)

A speed camera issues a ticket if car speed is strictly greater than 60 km/h (speed > 60). Drivers traveling at or below 60 km/h are not ticketed. What are the 2-value boundary test values for integer speeds around the boundary?

- **A.** 59 and 60
- **B.** 60 and 61
- **C.** 60 and 100
- **D.** 0 and 60

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q150)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Ranh giới là 60: Với speed = 60 km/h (không bị phạt - Valid/No ticket); với speed = 61 km/h (bị phạt - Valid/Ticket). Hai giá trị biên liền kề là 60 và 61.
</details>

---

### Q151. [Chapter 4: Test Analysis and Design - 4.3 White-box: Decision Coverage] (Chọn 1 đáp án đúng)

Why is 100% Decision Coverage considered STRONGER than 100% Statement Coverage?

- **A.** Because Decision Coverage requires fewer test cases.
- **B.** Because Decision Coverage exercises both the True and False outcomes of all decisions, thereby guaranteeing that every statement is also executed.
- **C.** Because Decision Coverage does not require access to code.
- **D.** Because compilers automatically enforce Decision Coverage.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q151)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Decision Coverage mạnh hơn Statement Coverage vì nó buộc phải kiểm tra tất cả các kết quả rẽ nhánh (cả True và False). Khi tất cả các nhánh rẽ đều được đi qua thì mọi câu lệnh nằm trong các nhánh đó chắc chắn đều được thực thi.
</details>

---

### Q152. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Decision Table Testing] (Chọn 1 đáp án đúng)

A movie theater offers a discount if: (Age < 18 OR Student = Yes) AND LoyaltyMember = Yes. How many total combinations of these three conditions exist in a full truth table?

- **A.** 3
- **B.** 6
- **C.** 8
- **D.** 12

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q152)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `C`
- **GIẢI THÍCH:** Có 3 điều kiện nhị phân (Age < 18, Student, LoyaltyMember). Tổng số tổ hợp trong bảng chân trị đầy đủ là 2^3 = 8 cột.
</details>

---

### Q153. [Chapter 4: Test Analysis and Design - 4.3 White-box: Cyclomatic Complexity] (Chọn 1 đáp án đúng)

If a control flow graph divides the plane into 5 enclosed regions (R) plus 1 external infinite region, what is its Cyclomatic Complexity?

- **A.** 5
- **B.** 6
- **C.** 7
- **D.** 12

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q153)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Theo định lý đồ thị phẳng của McCabe, Cyclomatic Complexity V(G) = Số miền kín (enclosed regions) + 1 miền vô hạn bên ngoài = 5 + 1 = 6.
</details>

---

### Q154. [Chapter 4: Test Analysis and Design - 4.2 Black-box: State Transition Testing] (Chọn 1 đáp án đúng)

What is a 'State Table' in State Transition Testing?

- **A.** A table listing employee salaries by US state.
- **B.** A matrix showing the current states on one axis, events on the other axis, and the resulting next states (and actions) in the cells.
- **C.** A database table storing system crashes.
- **D.** A Gantt chart for scheduling testing sprints.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q154)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** State Table (Bảng trạng thái): Một bảng ma trận biểu diễn trạng thái hiện tại (hàng), các sự kiện kích hoạt (cột), và ô giao nhau chứa trạng thái tiếp theo cùng hành động tương ứng. Các ô trống trong bảng chỉ ra các bước chuyển không hợp lệ (invalid transitions).
</details>

---

### Q155. [Chapter 4: Test Analysis and Design - 4.4 Experience-based Techniques] (Chọn 1 đáp án đúng)

A tester with 10 years of experience in testing e-commerce checkouts focuses their manual tests on race conditions when two users purchase the last available stock item simultaneously. What technique is this?

- **A.** Error Guessing based on domain expertise
- **B.** 100% Statement Coverage
- **C.** Cyclomatic Boundary Reduction
- **D.** Static Linting

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q155)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Tester dựa trên kinh nghiệm chuyên sâu về domain thương mại điện tử để nhắm vào lỗi tranh chấp tài nguyên (race condition) - đây là kỹ thuật Error Guessing (Đoán lỗi dựa trên kinh nghiệm).
</details>

---

### Q156. [Chapter 4: Test Analysis and Design - 4.1 Categories of Test Techniques] (Chọn 1 đáp án đúng)

Which category of test technique derives test cases from an analysis of the software's internal architecture, code structure, or data flow?

- **A.** Black-box techniques
- **B.** White-box (Structure-based) techniques
- **C.** Specification-based techniques
- **D.** Random monkey testing

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q156)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** White-box techniques (Kỹ thuật hộp trắng / dựa trên cấu trúc) thiết kế test cases dựa trên phân tích cấu trúc bên trong phần mềm, mã nguồn, luồng điều khiển và luồng dữ liệu.
</details>

---

### Q157. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Boundary Value Analysis] (Chọn 1 đáp án đúng)

When is Boundary Value Analysis (BVA) APPLICABLE?

- **A.** Only on un-ordered qualitative descriptions like favorite color.
- **B.** On ordered numeric or sequential data where boundaries between partitions exist.
- **C.** Exclusively on hardware wiring diagrams.
- **D.** Only when testing non-functional usability.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q157)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** BVA chỉ có thể áp dụng trên các dữ liệu có thứ tự (ordered data - như số nguyên, số thực, ngày tháng, độ dài chuỗi) nơi mà các ranh giới giữa các phân vùng có thể xác định rõ ràng.
</details>

---

### Q158. [Chapter 4: Test Analysis and Design - 4.3 White-box: Loop Testing] (Chọn 1 đáp án đúng)

When testing a simple loop of maximum N iterations, which boundary values should typically be tested?

- **A.** Skip loop entirely (0 iterations), 1 iteration, 2 iterations, typical iterations, N-1 iterations, N iterations, and attempt N+1 iterations.
- **B.** Only test 100,000 iterations.
- **C.** Loops should never be tested dynamically.
- **D.** Test 1 iteration only.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q158)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Kỹ thuật kiểm thử vòng lặp (Loop testing) tiêu chuẩn kiểm tra các biên: không chạy vòng lặp (0 lần), 1 lần, 2 lần, số lần điển hình ở giữa, N-1 lần, N lần (cận trên), và N+1 lần (nếu có thể).
</details>

---

### Q159. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Equivalence Partitioning] (Chọn 1 đáp án đúng)

A web form accepts credit card types: Visa, MasterCard, and American Express. Any other credit card type is rejected. How many valid and invalid equivalence partitions are there?

- **A.** 1 valid partition, 1 invalid partition
- **B.** 3 valid partitions (Visa, MasterCard, Amex) and 1 invalid partition (any other card)
- **C.** 3 valid partitions and 3 invalid partitions
- **D.** Infinite valid partitions

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q159)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Có 3 giá trị hợp lệ riêng biệt được chấp nhận (3 valid partitions) và tất cả các loại thẻ khác gộp lại thành 1 phân vùng không hợp lệ (1 invalid partition).
</details>

---

### Q160. [Chapter 4: Test Analysis and Design - 4.3 White-box: Path Testing] (Chọn 1 đáp án đúng)

What is an 'Independent Path' in a control flow graph?

- **A.** A path that has no edges.
- **B.** Any path through the code that introduces at least one new edge that is not part of any previously defined path.
- **C.** A path that never executes any statements.
- **D.** A test case written by an external vendor.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q160)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Đường đi độc lập (Independent Path / Basis Path) là một đường đi xuyên qua đồ thị luồng điều khiển từ điểm bắt đầu đến điểm kết thúc mà chứa ít nhất một cạnh nối (edge) chưa từng xuất hiện trong các đường đi đã xác định trước đó.
</details>

---

### Q161. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Use Case Testing] (Chọn 1 đáp án đúng)

Who is an 'Actor' in the context of Use Case Testing?

- **A.** A Hollywood movie celebrity.
- **B.** A person, external system, or hardware device that interacts with the system to achieve a specific goal.
- **C.** The developer who wrote the unit test.
- **D.** The relational database schema.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q161)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Trong Use Case, Actor (Tác nhân) là người dùng, hệ thống bên ngoài hoặc thiết bị phần cứng tương tác với hệ thống đang kiểm thử để thực hiện một mục tiêu cụ thể.
</details>

---

### Q162. [Chapter 4: Test Analysis and Design - 4.3 White-box: Branch Coverage Calculation] (Chọn 1 đáp án đúng)

Consider a C function with a 'switch(x)' statement containing 4 'case' blocks and 1 'default' block. How many branch outcomes must be executed to achieve 100% Decision (Branch) Coverage for this switch?

- **A.** 1
- **B.** 4
- **C.** 5
- **D.** 10

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q162)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `C`
- **GIẢI THÍCH:** Cấu trúc switch có 4 nhánh case và 1 nhánh default -> tổng cộng có 5 nhánh rẽ độc lập. Để đạt 100% Branch Coverage, cần kiểm thử cả 5 nhánh (5 test cases).
</details>

---

### Q163. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Decision Table Testing] (Chọn 1 đáp án đúng)

Why is Decision Table Testing particularly valuable for testing complex business logic?

- **A.** Because it generates source code automatically.
- **B.** Because it systematically reveals combinations of conditions that might otherwise be overlooked or missing in specifications.
- **C.** Because it proves that the software has 0 bugs.
- **D.** Because it replaces the need for performance testing.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q163)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Bảng quyết định cực kỳ hữu ích với logic nghiệp vụ phức tạp vì nó liệt kê có hệ thống mọi tổ hợp điều kiện, giúp phát hiện ngay các kịch bản bị bỏ sót hoặc mâu thuẫn trong tài liệu đặc tả.
</details>

---

### Q164. [Chapter 4: Test Analysis and Design - 4.4 Experience-based Techniques] (Chọn 1 đáp án đúng)

What is the primary drawback of relying EXCLUSIVELY on experience-based test techniques?

- **A.** They are too formal and require too much paperwork.
- **B.** Test coverage is subjective, unpredictable, difficult to quantify, and heavily dependent on individual tester skill.
- **C.** They can only be executed by automated test robots.
- **D.** They guarantee 100% statement coverage.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q164)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Nhược điểm lớn nhất của kỹ thuật dựa trên kinh nghiệm: Độ bao phủ kiểm thử mang tính chủ quan, khó đo lường chính xác bằng số liệu, và phụ thuộc quá nhiều vào năng lực cá nhân của người test.
</details>

---

### Q165. [Chapter 4: Test Analysis and Design - 4.2 Black-box: State Transition Testing] (Chọn 1 đáp án đúng)

In a state diagram, what triggers a 'Transition' from one state to another?

- **A.** An Event (optionally accompanied by a guard condition and an action)
- **B.** A compiler warning
- **C.** A Jira sprint retro meeting
- **D.** An increase in server temperature

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q165)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Một bước chuyển trạng thái (Transition) được kích hoạt bởi một Sự kiện (Event/Input), có thể đi kèm Điều kiện bảo vệ (Guard condition) và sinh ra một Hành động (Action).
</details>

---

### Q166. [Chapter 4: Test Analysis and Design - 4.3 White-box: Statement Coverage] (Chọn 1 đáp án đúng)

Can 100% Statement Coverage detect that an 'else' branch is missing in an 'if' construct?

- **A.** Yes, statement coverage always detects missing branches.
- **B.** No, because if the condition evaluates to True, 100% statement coverage is achieved without ever exercising what happens when the condition is False.
- **C.** Yes, but only in Java.
- **D.** Statement coverage is not applicable to if statements.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q166)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** 100% Statement Coverage không thể phát hiện thiếu nhánh else vì khi chạy nhánh True, toàn bộ dòng lệnh đã được thực thi 100%, bỏ qua hoàn toàn hành vi khi điều kiện False.
</details>

---

### Q167. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Equivalence Partitioning] (Chọn 1 đáp án đúng)

A discount coupon gives 15% discount if the shopping cart total is between $100 and $500 (inclusive). What are the invalid partitions?

- **A.** Total < $100 and Total > $500
- **B.** Total = $100 and Total = $500
- **C.** Total between $200 and $300
- **D.** Total = $250

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q167)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Phân vùng hợp lệ là [$100, $500]. Hai phân vùng không hợp lệ là: Total < $100 (ví dụ $99.99) và Total > $500 (ví dụ $500.01).
</details>

---

### Q168. [Chapter 4: Test Analysis and Design - 4.3 White-box: Decision Coverage] (Chọn nhiều đáp án)

Which TWO of the following statements about White-box testing are TRUE? (Choose TWO options)

- **A.** 100% Decision Coverage guarantees 100% Statement Coverage.
- **B.** White-box testing requires no knowledge of the internal code structure.
- **C.** Cyclomatic complexity defines the minimum number of independent paths for decision coverage.
- **D.** 100% Statement coverage guarantees that the software has no bugs.
- **E.** White-box testing can only be done during User Acceptance Testing.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q168)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A, C`
- **GIẢI THÍCH:** 100% Decision Coverage luôn đảm bảo 100% Statement Coverage (A). Cyclomatic complexity xác định số đường đi độc lập tối thiểu để đạt độ bao phủ nhánh (C).
</details>

---

### Q169. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Boundary Value Analysis] (Chọn 1 đáp án đúng)

Why does Boundary Value Analysis often discover more defects than Equivalence Partitioning alone?

- **A.** Because programmers frequently make off-by-one errors (e.g., using '>' instead of '>=') at the boundary edges of conditional statements.
- **B.** Because boundary values are chosen completely at random.
- **C.** Because boundary tests do not require expected results.
- **D.** Because boundary testing only runs on 64-bit operating systems.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q169)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Các lập trình viên thường xuyên mắc lỗi 'lệch 1 đơn vị' (off-by-one errors, nhầm lẫn giữa > và >=, hoặc < và <=) tại các điểm ranh giới của điều kiện. Vì vậy BVA bắt được rất nhiều lỗi biên mà việc chọn một giá trị ngẫu nhiên ở giữa phân vùng bỏ sót.
</details>

---

### Q170. [Chapter 4: Test Analysis and Design - 4.4 Experience-based Techniques] (Chọn 1 đáp án đúng)

In which scenario would Exploratory Testing be the MOST effective supplement to formal scripted testing?

- **A.** Right after all scripted regression tests have passed, to investigate unexpected edge behaviors and complex interactions.
- **B.** Instead of writing any requirements documents at the start of a multi-million dollar defense contract.
- **C.** When testing must be executed by automated Jenkins pipelines without human intervention.
- **D.** When no software build has been compiled yet.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q170)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Exploratory testing là sự bổ trợ tuyệt vời sau khi bộ test scripted chính quy đã pass: tester tự do khám phá các góc khuất, các tổ hợp tương tác phức tạp và các hành vi bất ngờ của hệ thống mà kịch bản có sẵn chưa tính đến.
</details>

---

### Q171. [Chapter 5: Test Management - 5.1 Test Organization] (Chọn 1 đáp án đúng)

Which of the following represents the HIGHEST level of test independence according to ISTQB?

- **A.** Developers testing their own code.
- **B.** Independent developers or peers from the same development team testing each other's code.
- **C.** Independent test team within the organization reporting to project management.
- **D.** Independent external test specialists (e.g., third-party certification or security specialists) outside the organization.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q171)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `D`
- **GIẢI THÍCH:** Thang đo tính độc lập của kiểm thử (từ thấp đến cao): 1. Lập trình viên tự test code của mình -> 2. Đồng nghiệp trong nhóm phát triển test chéo -> 3. Đội kiểm thử độc lập nội bộ trong tổ chức -> 4. Người dùng/khách hàng độc lập -> 5. Chuyên gia kiểm thử độc lập bên ngoài tổ chức (highest independence).
</details>

---

### Q172. [Chapter 5: Test Management - 5.1 Test Organization] (Chọn 1 đáp án đúng)

What is a potential DISADVANTAGE of having completely independent testers working in total isolation from developers?

- **A.** Independent testers find too many defects.
- **B.** Communication isolation, lack of shared ownership of quality, and developers may lose a sense of responsibility for defect prevention.
- **C.** Independent testing is strictly forbidden by ISTQB.
- **D.** Independent testers cannot use automated testing tools.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q172)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Nhược điểm tiềm ẩn khi đội tester quá độc lập và tách biệt: Thiếu giao tiếp cởi mở, developer có thể ỷ lại ('đã có tester lo rồi nên không cần cẩn thận'), làm giảm tinh thần trách nhiệm chung về chất lượng sản phẩm.
</details>

---

### Q173. [Chapter 5: Test Management - 5.1 Test Organization] (Chọn 1 đáp án đúng)

Which of the following tasks is TYPICALLY performed by the Test Manager (Test Leader) rather than a Tester?

- **A.** Analyzing requirements and designing detailed test cases.
- **B.** Setting up the test execution environment and preparing test data.
- **C.** Developing and updating the Test Plan, allocating resources, and selecting test metrics.
- **D.** Executing manual test procedures and logging bug tickets in Jira.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q173)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `C`
- **GIẢI THÍCH:** Nhiệm vụ của Test Manager (Test Leader): Lập và cập nhật Kế hoạch kiểm thử (Test Plan), phân bổ nguồn lực, lựa chọn các chỉ số đo lường (metrics), quản lý cấu hình và viết báo cáo tổng kết (Test Summary Report). A, B, D là nhiệm vụ của Tester.
</details>

---

### Q174. [Chapter 5: Test Management - 5.1 Test Organization] (Chọn 1 đáp án đúng)

Which of the following tasks is TYPICALLY performed by a Tester rather than the Test Manager?

- **A.** Writing the company-wide Test Policy.
- **B.** Deciding which testing metrics to report to upper executive management.
- **C.** Designing, implementing, and executing test cases and test suites.
- **D.** Negotiating testing budget with external clients.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q174)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `C`
- **GIẢI THÍCH:** Tester là người trực tiếp thiết kế (design), chuẩn bị (implement) và thực thi (execute) các test cases và test suites. Các việc mang tính chiến lược, chính sách và ngân sách thuộc về Test Manager.
</details>

---

### Q175. [Chapter 5: Test Management - 5.2 Test Planning and Estimation] (Chọn 1 đáp án đúng)

Which international standard defined the traditional industry benchmark format for Software Test Documentation, including the Test Plan template?

- **A.** IEEE 829 (now ISO/IEC/IEEE 29119-3)
- **B.** ISO 9001
- **C.** IEEE 754
- **D.** RFC 2616

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q175)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** IEEE 829 (tiêu chuẩn về tài liệu kiểm thử phần mềm, hiện nay được cập nhật trong bộ chuẩn ISO/IEC/IEEE 29119-3) định nghĩa cấu trúc chuẩn cho Test Plan, Test Case, Test Log, Test Incident Report, và Test Summary Report.
</details>

---

### Q176. [Chapter 5: Test Management - 5.2 Test Planning and Estimation] (Chọn 1 đáp án đúng)

A test team prioritizes and designs tests based primarily on the probability and consequence of potential software failures. Which test strategy is this?

- **A.** Model-based strategy
- **B.** Analytical strategy (Risk-based testing)
- **C.** Reactive strategy
- **D.** Methodical strategy

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q176)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Chiến lược phân tích (Analytical Strategy), điển hình là Risk-based testing (Kiểm thử dựa trên rủi ro), phân tích xác suất và mức độ tác động của các lỗi tiềm ẩn để định hướng và ưu tiên các bài kiểm thử.
</details>

---

### Q177. [Chapter 5: Test Management - 5.2 Test Planning and Estimation] (Chọn 1 đáp án đúng)

Which test strategy relies heavily on testing against formal checklists of common defects, ISO standard quality attributes, or organizational guidelines?

- **A.** Methodical strategy
- **B.** Reactive strategy
- **C.** Consultative strategy
- **D.** Model-based strategy

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q177)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Chiến lược bài bản (Methodical Strategy): Sử dụng có hệ thống các tập hợp kiểm tra định sẵn, chẳng hạn như checklists về các lỗi phổ biến, các danh mục thuộc tính chất lượng theo chuẩn ISO 25010, hoặc hướng dẫn giao diện người dùng.
</details>

---

### Q178. [Chapter 5: Test Management - 5.2 Test Planning and Estimation] (Chọn 1 đáp án đúng)

A team decides to spend the majority of testing effort building automated regression test suites and continuous integration pipelines to minimize the danger of regression bugs. What test strategy is this?

- **A.** Regression-averse strategy
- **B.** Directed strategy
- **C.** Reactive strategy
- **D.** Consultative strategy

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q178)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Chiến lược chống hồi quy (Regression-averse Strategy): Tập trung tối đa vào việc phòng ngừa và phát hiện lỗi hồi quy bằng cách xây dựng bộ kịch bản tự động hóa mạnh mẽ và chạy liên tục trong CI/CD pipeline.
</details>

---

### Q179. [Chapter 5: Test Management - 5.2 Test Planning and Estimation] (Chọn 1 đáp án đúng)

Which test strategy delays test design until the software is actually delivered, letting testing adapt reactively based on findings during exploratory execution?

- **A.** Reactive strategy
- **B.** Analytical strategy
- **C.** Standard-compliant strategy
- **D.** Model-based strategy

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q179)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Chiến lược phản ứng (Reactive Strategy): Hoạt động kiểm thử được kích hoạt và điều chỉnh dựa trên sự tương tác thực tế với phần mềm (như Exploratory Testing), thay vì lập kế hoạch chi tiết từ trước.
</details>

---

### Q180. [Chapter 5: Test Management - 5.2 Test Planning and Estimation] (Chọn 1 đáp án đúng)

What is the purpose of 'Entry Criteria' (Definition of Ready) in a Test Plan?

- **A.** To determine when testing has completed and software can be released.
- **B.** To define the prerequisite conditions that must be satisfied before a specific test level or test activity can officially start.
- **C.** To list the names of employees entering the office.
- **D.** To calculate developer severance packages.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q180)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Entry Criteria (Tiêu chí đầu vào) xác định các điều kiện tiên quyết cần được thỏa mãn trước khi một giai đoạn kiểm thử có thể chính thức bắt đầu (ví dụ: môi trường test đã sẵn sàng, smoke test pass 100%, tài liệu yêu cầu đã được review).
</details>

---

### Q181. [Chapter 5: Test Management - 5.2 Test Planning and Estimation] (Chọn 1 đáp án đúng)

Which of the following is a typical 'Exit Criteria' (Definition of Done) for System Testing?

- **A.** 100% of planned test cases executed, 95% pass rate, and zero open Blocker or Critical defects.
- **B.** The test environment has been turned on.
- **C.** All testers have arrived at the testing lab.
- **D.** A new sprint backlog is opened.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q181)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Exit Criteria (Tiêu chí dừng/hoàn thành) xác định khi nào mục tiêu kiểm thử đã đạt được (ví dụ: đạt độ bao phủ quy định, tỷ lệ pass cao, không còn lỗi nghiêm trọng nào tồn đọng).
</details>

---

### Q182. [Chapter 5: Test Management - 5.2 Test Planning and Estimation] (Chọn 1 đáp án đúng)

In test estimation, what is the 'Wideband Delphi' technique?

- **A.** A technique where an automated AI calculates the testing budget.
- **B.** An expert-based consensus estimation method where a panel of experts independently estimate effort, discuss differences in an anonymous iterative meeting, and converge on an estimate.
- **C.** An algorithm measuring database latency.
- **D.** An outsourced vendor pricing model.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q182)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Wideband Delphi là kỹ thuật ước lượng dựa trên chuyên gia (expert-based) theo cơ chế đồng thuận: một nhóm các chuyên gia ước lượng độc lập, sau đó thảo luận ẩn danh qua nhiều vòng lặp để thu hẹp khoảng cách và hội tụ về một con số ước lượng thống nhất.
</details>

---

### Q183. [Chapter 5: Test Management - 5.2 Test Planning and Estimation] (Chọn 1 đáp án đúng)

What is the primary difference between 'Metrics-based' and 'Expert-based' test estimation approaches?

- **A.** Metrics-based uses historical data and mathematical formulas from past projects; Expert-based relies on the intuition and experience of technical experts.
- **B.** Metrics-based only works on Windows; Expert-based works on Linux.
- **C.** Metrics-based is free; Expert-based costs $1,000 per hour.
- **D.** Metrics-based cannot estimate unit testing.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q183)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Metrics-based (dựa trên số liệu) sử dụng dữ liệu đo đạc thực tế từ các dự án tương tự trong quá khứ hoặc các công thức toán học; trong khi Expert-based (dựa trên chuyên gia) dựa trên trực giác, hiểu biết và kinh nghiệm thực tiễn của những người có chuyên môn.
</details>

---

### Q184. [Chapter 5: Test Management - 5.5 Risks and Testing] (Chọn 1 đáp án đúng)

How is the 'Level of Risk' mathematically determined in Risk-Based Testing?

- **A.** Risk Level = Likelihood of failure * Impact of failure
- **B.** Risk Level = Number of lines of code / Number of developers
- **C.** Risk Level = Total project cost + Server hardware cost
- **D.** Risk Level = Number of test cases * 100%

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q184)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Mức độ rủi ro (Risk Level / Risk Priority Number) = Xác suất xảy ra rủi ro (Likelihood/Probability) nhân với Mức độ tác hại/hậu quả nếu rủi ro xảy ra (Impact/Consequence).
</details>

---

### Q185. [Chapter 5: Test Management - 5.5 Risks and Testing] (Chọn 1 đáp án đúng)

Which of the following is classified as a PRODUCT RISK (Quality Risk) rather than a Project Risk?

- **A.** The software calculation algorithm computes an inaccurate interest rate for loan customers.
- **B.** A key senior test automation engineer resigns in the middle of the project.
- **C.** The third-party hardware vendor delays delivery of the testing server by 4 weeks.
- **D.** Management reduces the testing budget by 30%.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q185)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Product Risk (Rủi ro sản phẩm) là rủi ro liên quan trực tiếp đến chất lượng và tính năng của phần mềm (ví dụ: tính sai lãi suất, hổng bảo mật, lỗi crash). Các phương án B, C, D liên quan đến tiến độ, nhân sự, nhà cung cấp và ngân sách -> đó là Project Risk (Rủi ro dự án).
</details>

---

### Q186. [Chapter 5: Test Management - 5.5 Risks and Testing] (Chọn 1 đáp án đúng)

Which of the following is classified as a PROJECT RISK (Management Risk)?

- **A.** An online transaction module fails to encrypt credit card numbers.
- **B.** Contractual dispute with an outsourced software vendor leading to schedule delays.
- **C.** The mobile app crashes when switching between portrait and landscape modes.
- **D.** The search engine returns zero results for valid keyword queries.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q186)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Tranh chấp hợp đồng với nhà thầu phụ gây chậm tiến độ dự án là Project Risk (rủi ro quản lý/dự án). Các phương án A, C, D là Product Risk.
</details>

---

### Q187. [Chapter 5: Test Management - 5.5 Risks and Testing] (Chọn 1 đáp án đúng)

In Risk-Based Testing, which items should be tested FIRST and with the HIGHEST DEPTH of test coverage?

- **A.** Items with High Likelihood and High Impact (Highest Risk Level).
- **B.** Items that are easiest to automate.
- **C.** Items with Low Likelihood and Low Impact.
- **D.** Items chosen alphabetically by feature name.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q187)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Trong kiểm thử dựa trên rủi ro (RBT), những tính năng có rủi ro cao nhất (xác suất xảy ra lỗi cao và mức độ thiệt hại nghiêm trọng nếu gặp lỗi - High Likelihood & High Impact) luôn được ưu tiên kiểm thử đầu tiên và bao phủ sâu nhất.
</details>

---

### Q188. [Chapter 5: Test Management - 5.6 Defect Management] (Chọn 1 đáp án đúng)

What is the difference between DEFECT SEVERITY and DEFECT PRIORITY?

- **A.** Severity reflects the technical impact/degree of damage caused by the defect; Priority reflects the urgency/business importance of fixing the defect.
- **B.** Severity is assigned by marketing; Priority is assigned by the compiler.
- **C.** Severity and Priority are identical terms with no distinction.
- **D.** Priority is measured in kilograms; Severity is measured in seconds.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q188)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Severity (Mức độ nghiêm trọng) thể hiện tác động kỹ thuật của lỗi đối với hệ thống (ví dụ: làm sập toàn bộ hệ thống là Critical/Blocker). Priority (Mức độ ưu tiên) thể hiện mức độ cấp bách cần sửa lỗi xét theo góc độ kinh doanh/thời hạn phát hành.
</details>

---

### Q189. [Chapter 5: Test Management - 5.6 Defect Management] (Chọn 1 đáp án đúng)

A spelling mistake appears in the company's legal name on the public home page of a major bank. How should this defect be classified regarding Severity and Priority?

- **A.** High Severity, Low Priority
- **B.** Low Severity (system function is unimpaired), High Priority (causes severe public reputation damage, must be fixed immediately)
- **C.** High Severity, High Priority
- **D.** Low Severity, Low Priority

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q189)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Ví dụ kinh điển: Sai chính tả tên thương hiệu của ngân hàng ngay trên trang chủ không làm sập hệ thống (Low Severity), nhưng ảnh hưởng nghiêm trọng đến uy tín thương hiệu nên phải sửa ngay lập tức trước khi ra mắt (High Priority).
</details>

---

### Q190. [Chapter 5: Test Management - 5.6 Defect Management] (Chọn 1 đáp án đúng)

An obscure edge-case crash occurs only when a user runs the software on Windows XP with Japanese language encoding, a configuration used by 0.001% of customers. How would this defect typically be classified?

- **A.** High Severity (crash), Low Priority (very rare, unlikely to impact business)
- **B.** Low Severity, High Priority
- **C.** High Severity, High Priority
- **D.** Low Severity, Low Priority

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q190)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Hệ thống bị crash là lỗi nghiêm trọng về mặt kỹ thuật (High Severity), nhưng xác suất xảy ra cực kỳ hiếm trên môi trường hầu như không ai dùng (0.001%) nên độ ưu tiên sửa lỗi trong sprint này là thấp (Low Priority).
</details>

---

### Q191. [Chapter 5: Test Management - 5.6 Defect Management] (Chọn 1 đáp án đúng)

Which of the following elements is ESSENTIAL in an effective Defect Report to enable developers to reproduce the issue?

- **A.** An aggressive complaint about the developer's coding skills.
- **B.** Clear, numbered, step-by-step instructions to reproduce the failure, along with expected vs actual results.
- **C.** A request for immediate compensation.
- **D.** The tester's horoscope.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q191)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Một Defect Report hiệu quả bắt buộc phải có: các bước tái hiện lỗi chi tiết theo thứ tự (step-by-step steps to reproduce), kết quả mong đợi (expected result), kết quả thực tế (actual result), cùng thông tin môi trường và bằng chứng đính kèm (screenshots/logs).
</details>

---

### Q192. [Chapter 5: Test Management - 5.6 Defect Management] (Chọn 1 đáp án đúng)

In a standard defect lifecycle, what state transition occurs when a tester re-tests a fixed bug and discovers that the failure STILL OCCURS?

- **A.** Fixed -> Closed
- **B.** Resolved -> Reopened
- **C.** New -> Deferred
- **D.** Closed -> Rejected

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q192)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Khi developer đánh dấu lỗi là Fixed/Resolved, tester tiến hành kiểm tra lại (Retest). Nếu lỗi vẫn còn xuất hiện, tester chuyển trạng thái bug từ Resolved sang Reopened (Mở lại).
</details>

---

### Q193. [Chapter 5: Test Management - 5.6 Defect Management] (Chọn 1 đáp án đúng)

When a defect is reported, but product management decides that fixing it in the current release is too risky or not cost-effective, which status is assigned?

- **A.** Deferred (Postponed)
- **B.** Closed
- **C.** Verified
- **D.** Duplicate

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q193)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Trạng thái Deferred (Hoãn lại): Ban quản lý chấp nhận sự tồn tại của defect trong bản phát hành hiện tại và dời việc sửa chữa sang một bản phát hành tiếp theo trong tương lai.
</details>

---

### Q194. [Chapter 5: Test Management - 5.3 Test Monitoring and Control] (Chọn 1 đáp án đúng)

What is 'Defect Density'?

- **A.** The physical weight of the bug report binder.
- **B.** The number of defects identified in a work product divided by the size of the work product (e.g., defects per KLOC or defects per Function Point).
- **C.** The speed at which testers write test cases.
- **D.** The number of developers working in one room.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q194)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Defect Density (Mật độ lỗi) = Số lượng defect tìm thấy / Quy mô của sản phẩm (ví dụ: số lỗi trên 1.000 dòng lệnh KLOC, hoặc số lỗi trên 1 Function Point/User Story).
</details>

---

### Q195. [Chapter 5: Test Management - 5.3 Test Monitoring and Control] (Chọn 1 đáp án đúng)

What is the PRIMARY purpose of issuing regular Test Progress Reports during test execution?

- **A.** To publicly embarrass poor performers.
- **B.** To provide feedback and visibility to project stakeholders regarding progress against the test plan, risks, defect trends, and test coverage.
- **C.** To invoice the customer on a daily basis.
- **D.** To announce the date of the team holiday party.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q195)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Mục tiêu của Báo cáo tiến độ kiểm thử (Test Progress Report): Cung cấp thông tin minh bạch, kịp thời cho stakeholders về tiến độ so với kế hoạch, tình hình thực thi test case, xu hướng phát sinh defect và mức độ bao phủ.
</details>

---

### Q196. [Chapter 5: Test Management - 5.3 Test Monitoring and Control] (Chọn 1 đáp án đúng)

What is the difference between a Test Progress Report and a Test Summary Report?

- **A.** A Test Progress Report is issued periodically during testing; a Test Summary Report is issued at completion/milestone to evaluate overall test results against exit criteria.
- **B.** Test Progress Reports are written in French; Test Summary Reports are in English.
- **C.** Test Summary Reports are only written by marketing managers.
- **D.** A Test Progress Report is written only after software retirement.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q196)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Test Progress Report được phát hành định kỳ (hàng ngày/tuần) trong quá trình đang thực thi test. Test Summary Report được phát hành khi kết thúc một giai đoạn kiểm thử hoặc khi dự án hoàn thành để đánh giá tổng thể kết quả so với tiêu chí kết thúc (exit criteria).
</details>

---

### Q197. [Chapter 5: Test Management - 5.4 Configuration Management] (Chọn 1 đáp án đúng)

Why is Configuration Management (CM) ESSENTIAL to software testing?

- **A.** It ensures that all testware (test cases, scripts, data) and software test items are uniquely identified, version-controlled, tracked, and reproducible.
- **B.** It prevents testers from finding too many bugs.
- **C.** It allows developers to deploy code directly to production without testing.
- **D.** It eliminates the need for test execution logs.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q197)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Quản lý cấu hình (Configuration Management) đảm bảo rằng tất cả các tài sản kiểm thử (testware, scripts, dữ liệu kiểm thử) và phiên bản phần mềm (builds) đều được định danh duy nhất, kiểm soát phiên bản chặt chẽ, truy vết được và có thể tái hiện chính xác môi trường khi cần.
</details>

---

### Q198. [Chapter 5: Test Management - 5.2 Test Planning and Estimation] (Chọn 1 đáp án đúng)

Which of the following factors would TYPICALLY INCREASE the required testing effort?

- **A.** The system has high complexity, strict safety-critical regulatory requirements, and high defect rates.
- **B.** The requirements are extremely simple and stable.
- **C.** The test team already has excellent test automation scripts for all modules.
- **D.** The developers have 100% unit test coverage.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q198)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Các yếu tố làm tăng công sức kiểm thử: Hệ thống phức tạp, có yêu cầu tuân thủ an toàn nghiêm ngặt (safety-critical), chất lượng bản build ban đầu kém nhiều lỗi, yêu cầu nghiệp vụ thường xuyên thay đổi.
</details>

---

### Q199. [Chapter 5: Test Management - 5.5 Risks and Testing] (Chọn nhiều đáp án)

Which TWO of the following are examples of Product Risks? (Choose TWO options)

- **A.** Software crashes when processing more than 100 concurrent checkout orders.
- **B.** The project sponsor terminates the project funding due to budget cuts.
- **C.** User data is transmitted across the internet without SSL encryption.
- **D.** The testing team cannot hire qualified automation testers in time.
- **E.** An earthquake disables the corporate power grid.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q199)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A, C`
- **GIẢI THÍCH:** Crash khi chịu tải 100 giao dịch (A) và truyền dữ liệu người dùng không mã hóa SSL (C) là các khiếm khuyết trực tiếp của sản phẩm phần mềm (Product Risks). B và D là rủi ro dự án (Project Risks); E là thảm họa thiên tai.
</details>

---

### Q200. [Chapter 5: Test Management - 5.2 Test Planning and Estimation] (Chọn 1 đáp án đúng)

In Agile teams, which estimation technique uses playing cards with Fibonacci numbers (1, 2, 3, 5, 8...) where team members simultaneously reveal estimates to reach consensus on user story points?

- **A.** Planning Poker
- **B.** Function Point Analysis
- **C.** Cyclomatic Estimation
- **D.** Waterfall Delphi

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q200)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Planning Poker là kỹ thuật ước lượng đồng thuận phổ biến trong Agile/Scrum: các thành viên dùng bộ bài có dãy số Fibonacci để đưa ra điểm số ước lượng cùng một lúc, thảo luận về những khác biệt lớn và chốt con số thống nhất.
</details>

---

### Q201. [Chapter 5: Test Management - 5.6 Defect Management] (Chọn 1 đáp án đúng)

What is the primary objective of a 'Defect Triage Meeting'?

- **A.** To analyze, prioritize, and assign newly reported defects, deciding which will be fixed in the current release and which deferred.
- **B.** To fire the developers responsible for the defects.
- **C.** To rewrite the company mission statement.
- **D.** To order pizza for the engineering team.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q201)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Cuộc họp phân loại lỗi (Defect Triage Meeting) gồm đại diện Tester, Developer và Product Owner nhằm xem xét các bug mới phát sinh, đánh giá mức độ nghiêm trọng/ưu tiên, và quyết định bug nào sửa ngay, bug nào hoãn lại (defer) hoặc từ chối (reject).
</details>

---

### Q202. [Chapter 5: Test Management - 5.3 Test Monitoring and Control] (Chọn 1 đáp án đúng)

During test execution, what is an action of 'Test Control' when monitoring reveals testing is running 3 days behind schedule?

- **A.** Reallocating additional testers to high-risk areas, de-scoping low-priority test cases, or re-negotiating the deadline.
- **B.** Ignoring the issue and hoping for the best.
- **C.** Immediately releasing the un-tested software to production.
- **D.** Deleting all test cases to show 100% completion.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q202)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Test Control (Kiểm soát kiểm thử) là việc đưa ra các hành động khắc phục khi việc giám sát (Monitoring) phát hiện có sai lệch so với kế hoạch: điều chuyển nhân lực sang vùng rủi ro cao, cắt giảm các test case ưu tiên thấp, hoặc đàm phán lại thời hạn bàn giao.
</details>

---

### Q203. [Chapter 5: Test Management - 5.1 Test Organization] (Chọn 1 đáp án đúng)

What is a key benefit of having an independent test team within an organization?

- **A.** They bring an objective, unbiased viewpoint and can spot defects that developers take for granted.
- **B.** They cost zero dollars to maintain.
- **C.** They eliminate the need for requirement specifications.
- **D.** They can prevent developers from writing code.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q203)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Lợi ích lớn nhất của đội kiểm thử độc lập: Mang lại góc nhìn khách quan, không bị thiên kiến xác nhận chi phối, từ đó phát hiện ra các sai sót và giả định sai lầm mà lập trình viên thường bỏ qua.
</details>

---

### Q204. [Chapter 5: Test Management - 5.5 Risks and Testing] (Chọn 1 đáp án đúng)

What is 'Risk Mitigation' in Risk-based Testing?

- **A.** The process of taking actions (such as designing and executing targeted test cases) to reduce the likelihood or impact of potential product failures.
- **B.** Pretending the risk does not exist.
- **C.** Deleting the risky code module.
- **D.** Increasing the retail price of the software.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q204)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Giảm thiểu rủi ro (Risk Mitigation): Thực hiện các biện pháp chủ động (như thiết kế các test case có trọng tâm, thực thi kiểm thử sớm, bổ sung code review) nhằm giảm xác suất xảy ra lỗi hoặc giảm nhẹ hậu quả của rủi ro.
</details>

---

### Q205. [Chapter 5: Test Management - 5.2 Test Planning and Estimation] (Chọn 1 đáp án đúng)

What section of a standard IEEE 829 Test Plan lists features that will EXPLICITLY NOT be tested during the test cycle?

- **A.** Features Not to be Tested (Out of Scope)
- **B.** Pass/Fail Criteria
- **C.** Test Deliverables
- **D.** Environmental Needs

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q205)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Mục 'Features Not to be Tested' (hoặc Out of Scope) trong tài liệu Test Plan ghi rõ các tính năng nằm ngoài phạm vi kiểm thử của đợt này nhằm quản lý kỳ vọng rõ ràng với các bên liên quan.
</details>

---

### Q206. [Chapter 5: Test Management - 5.6 Defect Management] (Chọn 1 đáp án đúng)

If a tester files a defect report claiming the shopping cart total is incorrect, but investigation reveals the tester used an outdated tax table that was updated last week, what should the defect status be updated to?

- **A.** Rejected (or Invalid / Not a Bug)
- **B.** Fixed
- **C.** Reopened
- **D.** Blocker

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q206)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Nếu tester báo lỗi do hiểu sai yêu cầu hoặc dùng dữ liệu cũ không còn hiệu lực, defect report sẽ được cập nhật trạng thái thành Rejected (Từ chối) hoặc Not a Bug (Không phải lỗi).
</details>

---

### Q207. [Chapter 5: Test Management - 5.3 Test Monitoring and Control] (Chọn 1 đáp án đúng)

Which testing metric illustrates the number of new defects reported each day versus the number of defects resolved and closed over time?

- **A.** Defect Arrival and Resolution Trend (Defect Burn-down / Cumulative defect curve)
- **B.** Server CPU temperature chart
- **C.** Cyclomatic Complexity gauge
- **D.** Equivalence boundary ratio

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q207)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Biểu đồ xu hướng phát hiện và giải quyết lỗi (Defect Trend / Defect Arrival vs Resolution Curve) cho thấy số lượng lỗi mới tìm thấy mỗi ngày so với số lượng lỗi đã fix và đóng, giúp dự đoán thời điểm hệ thống đạt độ ổn định để release.
</details>

---

### Q208. [Chapter 5: Test Management - 5.2 Test Planning and Estimation] (Chọn 1 đáp án đúng)

In a Test Plan, what is 'Test Strategy'?

- **A.** The high-level description of test levels to be performed and the testing approach within those levels.
- **B.** The password to access the test server.
- **C.** The names of all test case authors.
- **D.** The source code repository commit history.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q208)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Chiến lược kiểm thử (Test Strategy) là mô tả cấp cao định hướng cách tiếp cận kiểm thử, xác định các cấp độ kiểm thử được thực hiện, các phương pháp kỹ thuật áp dụng và cách quản lý rủi ro.
</details>

---

### Q209. [Chapter 5: Test Management - 5.5 Risks and Testing] (Chọn 1 đáp án đúng)

In a risk matrix, Risk A has Likelihood = 4, Impact = 5 (Risk = 20). Risk B has Likelihood = 2, Impact = 3 (Risk = 6). Risk C has Likelihood = 5, Impact = 2 (Risk = 10). What is the correct priority order for testing?

- **A.** Risk A -> Risk C -> Risk B
- **B.** Risk B -> Risk C -> Risk A
- **C.** Risk C -> Risk A -> Risk B
- **D.** All risks should be tested at the same time.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q209)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Điểm mức độ rủi ro: Risk A = 20, Risk C = 10, Risk B = 6. Theo nguyên tắc Risk-based testing, rủi ro cao nhất được ưu tiên kiểm thử trước: Thứ tự là Risk A -> Risk C -> Risk B.
</details>

---

### Q210. [Chapter 5: Test Management - 5.6 Defect Management] (Chọn 1 đáp án đúng)

Why is an 'Isolating' step recommended before reporting a defect?

- **A.** To find the minimal set of steps that reliably reproduces the failure and confirm it is not caused by tester error or transient environmental glitch.
- **B.** To delete the evidence before anyone notices.
- **C.** To prevent other testers from filing bug reports.
- **D.** To encrypt the bug report.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q210)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Cô lập lỗi (Defect Isolation): Tester cần thử nghiệm để tìm ra chuỗi bước tối thiểu và chính xác nhất để tái hiện lỗi một cách ổn định, loại trừ các yếu tố nhiễu do thao tác nhầm hoặc mạng chập chờn trước khi gửi ticket.
</details>

---

### Q211. [Chapter 5: Test Management - 5.1 Test Organization] (Chọn nhiều đáp án)

Which TWO of the following tasks are typical responsibilities of a Test Manager? (Choose TWO options)

- **A.** Writing and finalizing the Test Plan.
- **B.** Coding unit tests inside the Java service class.
- **C.** Gathering and analyzing testing metrics to author the Test Summary Report.
- **D.** Performing exploratory testing on UI widgets.
- **E.** Recompiling the application binary after bug fixes.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q211)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A, C`
- **GIẢI THÍCH:** Test Manager chịu trách nhiệm lập Test Plan (A) và thu thập số liệu đo lường để viết Test Summary Report (C). B là việc của developer, D là việc của tester, E là của build engineer/developer.
</details>

---

### Q212. [Chapter 5: Test Management - 5.4 Configuration Management] (Chọn 1 đáp án đúng)

What problem occurs during testing if Configuration Management is POOR or absent?

- **A.** Testers might test the wrong build version, verify bugs against obsolete code, or fail to reproduce issues because the environment configuration was not tracked.
- **B.** Compilers refuse to generate bytecode.
- **C.** The internet shuts down.
- **D.** Automated test scripts run 1000 times faster.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q212)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Nếu quản lý cấu hình kém: Tester có thể chạy test trên sai bản build, retest bug trên code cũ chưa được cập nhật, hoặc không thể tái hiện lại lỗi vì không biết chính xác cấu hình môi trường lúc lỗi xảy ra.
</details>

---

### Q213. [Chapter 5: Test Management - 5.2 Test Planning and Estimation] (Chọn 1 đáp án đúng)

In a Test Plan, what is an 'Environmental Need'?

- **A.** The specification of hardware, network infrastructure, software licenses, operating systems, and database configurations required to execute tests.
- **B.** The number of plants in the office lobby.
- **C.** The recycling bins available in the kitchen.
- **D.** The air conditioning temperature in the breakroom.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q213)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Environmental Needs (Nhu cầu môi trường): Mục trong Test Plan liệt kê đầy đủ các yêu cầu về phần cứng, mạng, hệ điều hành, bản quyền phần mềm, máy chủ cơ sở dữ liệu cần có để thiết lập môi trường test.
</details>

---

### Q214. [Chapter 5: Test Management - 5.6 Defect Management] (Chọn 1 đáp án đúng)

When two testers independently discover the exact same underlying defect under slightly different UI steps and both submit tickets, what action should the defect triage team take?

- **A.** Keep one ticket as Primary and mark the other as Duplicate.
- **B.** Delete both tickets immediately.
- **C.** Reprimand both testers.
- **D.** Build two separate software fixes.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q214)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Khi phát hiện 2 ticket trùng nhau, quy trình chuẩn là giữ lại một ticket chính (Primary) và đánh dấu ticket còn lại là Trùng lặp (Duplicate) kèm liên kết tham chiếu đến ticket chính.
</details>

---

### Q215. [Chapter 5: Test Management - 5.2 Test Planning and Estimation] (Chọn 1 đáp án đúng)

Which testing document serves as the formal handover record at the conclusion of testing, summarizing total tests executed, remaining open defects, and recommendation on whether release criteria have been met?

- **A.** Test Summary Report
- **B.** Test Charter
- **C.** Test Procedure
- **D.** Defect Log

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q215)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Test Summary Report (Báo cáo tổng kết kiểm thử) là tài liệu bàn giao chính thức khi kết thúc kiểm thử, tổng hợp số lượng test case đã chạy, các defect còn mở và đưa ra đánh giá khuyến nghị xem sản phẩm đã đủ điều kiện release hay chưa.
</details>

---

### Q216. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

Which of the following test tools is classified under 'Tools supporting static testing'?

- **A.** Static Code Analysis Tool (e.g., SonarQube)
- **B.** Load Testing Tool (e.g., Apache JMeter)
- **C.** Unit Test Runner (e.g., JUnit)
- **D.** Defect Tracking Tool (e.g., Jira)

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q216)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Static Code Analysis Tool (như SonarQube, Checkstyle) phân tích mã nguồn mà không cần thực thi chương trình, thuộc nhóm công cụ hỗ trợ kiểm thử tĩnh (Static testing). JMeter là công cụ hiệu năng, JUnit là công cụ thực thi/unit test, Jira là công cụ quản lý kiểm thử/defect.
</details>

---

### Q217. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

What is the PRIMARY purpose of a 'Dynamic Analysis Tool'?

- **A.** To format requirements into Word documents.
- **B.** To analyze code while it is running, detecting runtime issues such as memory leaks, unassigned pointers, and buffer overflows.
- **C.** To calculate developer salary deductions.
- **D.** To convert manual test cases into PDF format.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q217)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Dynamic Analysis Tool (Công cụ phân tích động - ví dụ Valgrind, Purify) phân tích ứng dụng trong lúc đang chạy để phát hiện các lỗi thời gian thực như rò rỉ bộ nhớ (memory leaks), con trỏ rác (dangling pointers), và tràn bộ đệm (buffer overflows).
</details>

---

### Q218. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

Which category of testing tools includes features for logging defect tickets, assigning priorities, and tracking bugs through their lifecycle?

- **A.** Test Execution Tools
- **B.** Defect Management / Tracking Tools
- **C.** Performance Testing Tools
- **D.** Static Analysis Tools

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q218)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Defect Management / Incident Tracking Tools (như Jira, Bugzilla, Redmine) hỗ trợ ghi lại defect, phân loại mức độ nghiêm trọng/ưu tiên, và theo dõi vòng đời của lỗi từ khi mở đến khi đóng.
</details>

---

### Q219. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

What is a 'Test Harness'?

- **A.** A leather belt worn by testers in a server room.
- **B.** A test environment or collection of software and test data configured to test a program unit by running it under specific conditions and monitoring its behavior and outputs (often providing stubs and drivers).
- **C.** A tool used solely to format bug report screenshots.
- **D.** A contract between a test manager and a client.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q219)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Test Harness (Khung kiểm thử): Tập hợp các phần mềm giả lập, stubs, drivers và dữ liệu kiểm thử được cấu hình để thực thi một module hoặc chương trình trong điều kiện xác định và theo dõi kết quả đầu ra của nó.
</details>

---

### Q220. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

Which of the following is a POTENTIAL BENEFIT of test automation?

- **A.** Eliminating the need to ever train testers again.
- **B.** Greater consistency and repeatability of test execution, reducing repetitive human effort.
- **C.** Guaranteeing that zero defects will ever escape to production.
- **D.** Replacing all manual exploratory testing completely.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q220)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Lợi ích lớn của kiểm thử tự động: Đảm bảo tính nhất quán (consistency) và khả năng lặp lại chính xác (repeatability) của các bài test, giảm thiểu sự nhàm chán và công sức thủ công lặp đi lặp lại của con người.
</details>

---

### Q221. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

Which of the following is a COMMON RISK or pitfall when introducing a test automation tool?

- **A.** Underestimating the time, effort, and cost required to maintain automated test scripts over time.
- **B.** Automated tests execute too fast.
- **C.** Automated test reports are too easy to read.
- **D.** Developers refuse to use computers.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q221)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Rủi ro phổ biến nhất khi triển khai công cụ tự động hóa: Đánh giá quá thấp thời gian, công sức và chi phí bảo trì kịch bản kiểm thử (test script maintenance) khi giao diện hoặc logic phần mềm thay đổi liên tục.
</details>

---

### Q222. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

Why is the naive 'Capture/Replay' (Record and Playback) approach generally DISCOURAGED for large-scale enterprise test automation suites?

- **A.** Because captured scripts are brittle and break easily whenever minor UI changes occur, requiring excessive maintenance.
- **B.** Because capture/replay tools are prohibited by ISO standards.
- **C.** Because computers cannot record mouse clicks.
- **D.** Because captured scripts cannot be executed on weekends.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q222)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Phương pháp Record/Playback tạo ra các kịch bản rất giòn (brittle): chỉ cần một thay đổi nhỏ về giao diện (như đổi ID button, đổi vị trí ô nhập) là toàn bộ script bị gãy (fail), dẫn đến chi phí bảo trì khổng lồ.
</details>

---

### Q223. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

In test automation, what is the 'Data-Driven' testing approach?

- **A.** Storing test inputs and expected outcomes in external data files (e.g., CSV, Excel, DB) so that a single test script can execute multiple test cases with different data.
- **B.** Manually typing inputs directly into hardcoded code statements.
- **C.** Relying entirely on random data generated by the computer.
- **D.** Storing test results on USB thumb drives.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q223)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Data-Driven Testing (Kiểm thử theo dữ liệu): Tách biệt logic của kịch bản kiểm thử ra khỏi dữ liệu. Dữ liệu kiểm thử (inputs và expected outputs) được lưu trong file ngoài (Excel, CSV, database), cho phép 1 script duy nhất có thể chạy hàng trăm bộ dữ liệu khác nhau.
</details>

---

### Q224. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

What is the 'Keyword-Driven' (Action-Driven) test automation approach?

- **A.** Writing test cases using action words (e.g., 'Click', 'EnterText', 'VerifyText') stored in tables, which are executed by calling generic script modules.
- **B.** Searching Google for software testing keywords.
- **C.** Testing whether keyboard keys are sticky.
- **D.** Only testing software on Windows 95.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q224)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Keyword-Driven Testing (Kiểm thử theo từ khóa): Sử dụng các từ khóa hành động cụ thể (như 'Login', 'Click', 'CheckBalance') kèm các tham số. Tester nghiệp vụ có thể viết test case bằng từ khóa mà không cần biết lập trình, kịch bản khung sẽ tự động gọi code tương ứng.
</details>

---

### Q225. [Chapter 6: Tool Support for Testing - 6.2 Effective Use of Tools] (Chọn 1 đáp án đúng)

What is the PRIMARY purpose of conducting a 'Pilot Project' before rolling out a new testing tool across an entire organization?

- **A.** To learn the tool in depth, evaluate how it fits with existing processes, decide on standard usage guidelines, and assess realistic benefits and costs.
- **B.** To immediately replace all senior testers with the tool.
- **C.** To spend all remaining annual IT budget before December 31st.
- **D.** To write the software user manual.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q225)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Mục tiêu cốt lõi của Dự án thử nghiệm (Pilot Project): Giúp tìm hiểu sâu về công cụ trong điều kiện thực tế, đánh giá sự tương thích với quy trình sẵn có, thiết lập các quy chuẩn sử dụng (naming convention, lưu trữ), và đánh giá chính xác lợi ích so với chi phí trước khi triển khai diện rộng.
</details>

---

### Q226. [Chapter 6: Tool Support for Testing - 6.2 Effective Use of Tools] (Chọn 1 đáp án đúng)

Which of the following is considered a CRITICAL success factor when deploying a new testing tool across multiple project teams?

- **A.** Providing ongoing training, coaching, and mentoring to the staff who will use the tool.
- **B.** Forcing all teams to adopt the tool on day one without any documentation or training.
- **C.** Banning testers from discussing issues encountered with the tool.
- **D.** Disabling version control for automated test scripts.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q226)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Yếu tố thành công then chốt khi triển khai công cụ mới: Cung cấp đầy đủ đào tạo (training), kèm cặp (coaching/mentoring), tài liệu hướng dẫn và hỗ trợ kỹ thuật liên tục cho những người sử dụng công cụ.
</details>

---

### Q227. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

Which type of tool measures the percentage of executable code structures (such as statements or decisions) exercised by a test suite?

- **A.** Coverage Measurement Tool (Coverage Analyzer)
- **B.** Defect Management Tool
- **C.** Configuration Management Tool
- **D.** Requirements Traceability Matrix Tool

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q227)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Coverage Measurement Tool (như JaCoCo, Istanbul, Cobertura) đo lường tỷ lệ phần trăm các thành phần mã nguồn (statements, branches, lines) đã được thực thi bởi bộ kiểm thử.
</details>

---

### Q228. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

What is an UNREALISTIC EXPECTATION often held by management regarding test automation tools?

- **A.** Expecting that purchasing an automated tool will immediately reduce test effort to zero without requiring time for scripting and maintenance.
- **B.** Expecting that automated tests can be run overnight.
- **C.** Expecting that automated tests provide repeatable execution.
- **D.** Expecting that automation scripts can be stored in Git.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q228)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Kỳ vọng phi thực tế phổ biến của ban quản lý: Nghĩ rằng chỉ cần bỏ tiền mua một công cụ tự động hóa đắt tiền là công sức kiểm thử sẽ lập tức về số 0, mà không lường trước công sức khổng lồ để học, lập trình kịch bản và bảo trì.
</details>

---

### Q229. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

Which tool type helps create synthetic or anonymized test datasets needed to execute test cases without violating privacy laws?

- **A.** Test Data Preparation Tool
- **B.** Static Linter
- **C.** Unit Test Runner
- **D.** Code Profiler

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q229)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Test Data Preparation Tool (Công cụ chuẩn bị dữ liệu kiểm thử) giúp tạo ra các tập dữ liệu giả lập có cấu trúc hợp lệ hoặc làm mờ/ẩn danh hóa (anonymize) dữ liệu sản xuất thực tế để tuân thủ luật bảo mật thông tin cá nhân (như GDPR).
</details>

---

### Q230. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

Which testing tool category evaluates whether a system conforms to accessibility standards (e.g., WCAG) for users with visual or physical impairments?

- **A.** Accessibility Testing Tool (e.g., Axe, Wave)
- **B.** Load Testing Tool
- **C.** Stress Testing Tool
- **D.** Code Coverage Tool

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q230)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Accessibility Testing Tool (Công cụ kiểm thử khả năng tiếp cận - như Axe, WAVE) kiểm tra việc tuân thủ các chuẩn hỗ trợ người khuyết tật (WCAG) như độ tương phản màu sắc, thẻ alt cho hình ảnh, điều hướng bàn phím.
</details>

---

### Q231. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

What risk arises if a test team treats test automation scripts as informal throwaway code without placing them under Version Control?

- **A.** Loss of traceability, loss of script history, inability to synchronize scripts with software builds, and accidental overwrites.
- **B.** Scripts run too quickly.
- **C.** Automated test reports become encrypted.
- **D.** The compiler refuses to execute binary files.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q231)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Nếu kịch bản tự động hóa không được quản lý bằng Hệ thống kiểm soát phiên bản (Version Control như Git): Sẽ mất khả năng truy vết giữa script và bản build phần mềm, dễ bị ghi đè mất mã nguồn, và không thể rollback khi script bị lỗi.
</details>

---

### Q232. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

Which testing tool generates massive concurrent virtual user traffic to measure web server response times and transaction throughput under peak stress?

- **A.** Performance and Load Testing Tool (e.g., JMeter, Gatling)
- **B.** Static Review Tool
- **C.** Requirements Management Tool
- **D.** Spell Checker

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q232)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Performance / Load Testing Tool (như JMeter, Gatling, LoadRunner) giả lập hàng ngàn người dùng ảo truy cập đồng thời để đo lường thông lượng, thời gian phản hồi và độ ổn định của hệ thống dưới tải trọng cao.
</details>

---

### Q233. [Chapter 6: Tool Support for Testing - 6.2 Effective Use of Tools] (Chọn 1 đáp án đúng)

When selecting a testing tool, which of the following criteria is essential regarding the technology stack?

- **A.** Verifying that the tool is compatible with the programming languages, operating systems, and frameworks used by the software under test.
- **B.** Ensuring the tool logo is the test manager's favorite color.
- **C.** Ensuring the tool was released in the last 24 hours.
- **D.** Verifying the tool does not require an electrical connection.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q233)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Tiêu chí cốt lõi khi chọn công cụ: Đảm bảo công cụ tương thích và hỗ trợ tốt cho các nền tảng công nghệ, ngôn ngữ lập trình, hệ điều hành và framework mà hệ thống đang sử dụng (ví dụ: công cụ web test có hỗ trợ React/Angular không).
</details>

---

### Q234. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn nhiều đáp án)

Which TWO of the following are recognized risks of introducing test automation? (Choose TWO options)

- **A.** Over-reliance on the tool, leading testers to stop conducting critical manual exploratory tests.
- **B.** Automated tests find defects too consistently.
- **C.** Underestimating the continuous maintenance effort required when the system under test evolves.
- **D.** Automated tests reduce repetitive work.
- **E.** Automated test runs can be scheduled during the night.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q234)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A, C`
- **GIẢI THÍCH:** Hai rủi ro lớn của tự động hóa: Quá ỷ lại vào công cụ dẫn đến bỏ qua việc khám phá thủ công (A), và đánh giá thấp công sức bảo trì kịch bản lâu dài (C). B, D, E là lợi ích hoặc đặc điểm tích cực.
</details>

---

### Q235. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

What is an 'Open Source' testing tool?

- **A.** A tool whose source code is publicly accessible and can typically be used, modified, and distributed without licensing fees (e.g., Selenium, JUnit).
- **B.** A tool that only works with the computer cover open.
- **C.** A tool that requires payment of $50,000 per user.
- **D.** A proprietary tool owned by Microsoft.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q235)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Open Source tool (Công cụ nguồn mở - như Selenium, JUnit, JMeter) là công cụ mà mã nguồn được công khai miễn phí, cộng đồng có thể tự do sử dụng, chỉnh sửa và đóng góp phát triển mà không phải trả phí bản quyền thương mại đắt đỏ.
</details>

---

### Q236. [Chapter 6: Tool Support for Testing - 6.2 Effective Use of Tools] (Chọn 1 đáp án đúng)

Why should a 'Proof of Concept' (PoC) be performed before purchasing an expensive commercial test execution tool?

- **A.** To prove whether the tool can actually identify UI controls and execute test actions effectively on the organization's unique software architecture.
- **B.** To delay the project until next quarter.
- **C.** To avoid writing any test cases.
- **D.** To train all 5,000 employees in the company.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q236)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Proof of Concept (PoC - Kiểm chứng tính khả thi): Giúp xác minh thực tế xem công cụ có nhận diện được các component/control UI đặc thù của dự án và chạy ổn định trên kiến trúc phần mềm của công ty hay không trước khi ký hợp đồng mua bản quyền đắt tiền.
</details>

---

### Q237. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

In continuous integration (CI) pipelines, what role do automated test execution tools play?

- **A.** They automatically execute regression and smoke test suites on every code commit to provide immediate feedback on build health.
- **B.** They replace all software architects.
- **C.** They generate PowerPoint presentations for marketing.
- **D.** They turn off server cooling systems.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q237)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Trong pipeline CI/CD, các công cụ kiểm thử tự động chạy ngay các bộ smoke test và regression test mỗi khi có bản commit mới, giúp phát hiện lỗi tức thì và ngăn chặn code lỗi lọt vào nhánh chính.
</details>

---

### Q238. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

What is the primary danger if a test tool vendor goes out of business or discontinues support for a proprietary tool?

- **A.** The organization may be left with unmaintained legacy test suites that cannot be upgraded, run on modern OS versions, or integrated with modern CI systems.
- **B.** All computers in the office will explode.
- **C.** Internet bandwidth will increase.
- **D.** Source code will automatically delete itself.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q238)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Rủi ro phụ thuộc nhà cung cấp (Vendor lock-in): Nếu nhà cung cấp công cụ độc quyền ngừng phát triển hoặc phá sản, tổ chức sẽ bị kẹt lại với bộ test script cũ không thể nâng cấp, không tương thích với HĐH mới và tốn chi phí rất lớn để làm lại từ đầu.
</details>

---

### Q239. [Chapter 6: Tool Support for Testing - 6.2 Effective Use of Tools] (Chọn 1 đáp án đúng)

How should an organization plan the rollout of a new testing tool following a successful pilot project?

- **A.** Incrementally roll out the tool across teams, providing coaching and adapting guidelines based on early team feedback.
- **B.** Enforce immediate overnight adoption across all 100 teams simultaneously.
- **C.** Fire anyone who asks questions about the tool.
- **D.** Discard the guidelines defined during the pilot project.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q239)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Triển khai từng bước (Incremental rollout): Sau dự án thí điểm thành công, công cụ nên được nhân rộng dần dần qua từng nhóm, vừa triển khai vừa kèm cặp, đào tạo và liên tục hoàn thiện quy trình chuẩn dựa trên bài học thực tế.
</details>

---

### Q240. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

Which tool type helps testers link requirement items to test conditions, test cases, and defect reports to maintain bi-directional traceability?

- **A.** Requirements Management / ALM Tool (Application Lifecycle Management)
- **B.** Performance Stress Tool
- **C.** Memory Leak Profiler
- **D.** Compiling Linker

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q240)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Công cụ Quản lý Yêu cầu / ALM (như Jira + Xray, Azure DevOps, HP ALM) cho phép thiết lập và duy trì liên kết truy vết hai chiều (Bi-directional Traceability) từ User Story -> Test Case -> Test Execution -> Defect.
</details>

---

### Q241. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

What is 'Model-Based Testing' (MBT) tool support?

- **A.** Tools that use graphical models of system behavior (such as state machines or activity diagrams) to automatically generate test cases and test inputs.
- **B.** Tools that hire fashion models to test phones.
- **C.** Tools that take 3D photos of server hardware.
- **D.** Tools that design marketing brochures.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q241)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Model-Based Testing (MBT): Các công cụ sử dụng mô hình hành vi hệ thống (như State Machine, Flowchart) để tự động sinh ra các kịch bản kiểm thử (test cases) và dữ liệu đầu vào.
</details>

---

### Q242. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

Which of the following describes 'Static Application Security Testing' (SAST) tools?

- **A.** Tools that analyze source code or byte code without executing it to detect security vulnerabilities (e.g., SQL injection, XSS).
- **B.** Tools that launch live DDoS attacks against a running server.
- **C.** Tools that test firewall power cables.
- **D.** Physical locks on office doors.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q242)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** SAST (Static Application Security Testing - ví dụ Checkmarx, Fortify) phân tích mã nguồn ở trạng thái tĩnh (không chạy code) để phát hiện các lỗ hổng bảo mật phổ biến như SQL Injection, Cross-Site Scripting (XSS), tràn bộ đệm.
</details>

---

### Q243. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

What is the key difference between SAST and DAST (Dynamic Application Security Testing) tools?

- **A.** SAST inspects source code statically; DAST tests the running application externally by simulating attacks (penetration testing).
- **B.** SAST is for games; DAST is for banking.
- **C.** DAST only works on Android devices.
- **D.** SAST requires live server internet connection; DAST does not.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q243)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** SAST kiểm tra mã nguồn tĩnh bên trong (white-box security); trong khi DAST (Dynamic Application Security Testing - như OWASP ZAP, Burp Suite) kiểm tra ứng dụng đang chạy thực tế từ bên ngoài (black-box security) bằng cách bắn các payload tấn công mô phỏng hacker.
</details>

---

### Q244. [Chapter 6: Tool Support for Testing - 6.2 Effective Use of Tools] (Chọn 1 đáp án đúng)

Which factor must be evaluated regarding the organization's maturity before introducing complex test automation frameworks?

- **A.** Whether the organization already has disciplined test processes, well-defined test cases, and technical programming competencies to maintain scripts.
- **B.** Whether the company has more than 10,000 employees.
- **C.** Whether all desks are painted blue.
- **D.** Whether the company is publicly traded.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q244)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Đánh giá mức độ trưởng thành của tổ chức: Nếu tổ chức chưa có quy trình kiểm thử bài bản, test case thủ công còn chưa rõ ràng và nhóm thiếu kỹ năng lập trình thì việc đưa công cụ tự động hóa phức tạp vào chắc chắn sẽ thất bại.
</details>

---

### Q245. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

Can test execution tools completely eliminate the need for human judgment and exploratory testing?

- **A.** Yes, modern tools have full human intelligence.
- **B.** No, automated execution tools only repeat scripted instructions blindly; human critical thinking and exploration are indispensable for finding unexpected edge-case bugs.
- **C.** Yes, if scripts are written in Python.
- **D.** No, because automation tools cannot connect to the internet.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q245)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Công cụ kiểm thử tự động chỉ thực thi mù quáng các bước đã được lập trình sẵn. Chúng không có trực giác, sự tò mò hay tư duy phản biện của con người để phát hiện các lỗi bất thường ngoài kịch bản.
</details>

---

### Q246. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

Why is 'Ease of Script Maintenance' a top criterion when designing a test automation framework?

- **A.** Because application UIs and requirements evolve constantly, and high maintenance overhead will eventually cause teams to abandon the automated test suite.
- **B.** Because compilers refuse to run large scripts.
- **C.** Because testers prefer manual typing.
- **D.** Because test scripts are limited to 50 lines of code.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q246)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Giao diện và nghiệp vụ của phần mềm luôn biến đổi liên tục. Nếu framework khó bảo trì, mỗi lần có thay đổi nhỏ tester phải sửa hàng trăm chỗ thì chi phí duy trì sẽ vượt quá lợi ích mang lại, dẫn đến bộ automation suite bị bỏ xó.
</details>

---

### Q247. [Chapter 6: Tool Support for Testing - 6.2 Effective Use of Tools] (Chọn 1 đáp án đúng)

During a tool pilot project, which activity helps define how test scripts will be structured across the team?

- **A.** Establishing coding standards, naming conventions, and modular directory structures for test assets.
- **B.** Ordering new office furniture.
- **C.** Deleting old requirement documents.
- **D.** Cancelling weekly team standup meetings.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q247)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Trong dự án thí điểm, nhóm cần thiết lập các quy chuẩn lập trình (coding standards), quy tắc đặt tên (naming conventions) và cấu trúc thư mục lưu trữ thống nhất cho tất cả các kịch bản kiểm thử.
</details>

---

### Q248. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

What is an advantage of Open Source testing tools compared to commercial proprietary tools?

- **A.** Absence of software license purchasing fees and active community-driven plugins.
- **B.** Guaranteed 24/7 dedicated telephone support with legal liability guarantees.
- **C.** They never have any bugs.
- **D.** They do not require any programming knowledge.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q248)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Ưu điểm của công cụ Open Source: Không tốn chi phí mua license định kỳ, cộng đồng người dùng đông đảo phát triển nhiều thư viện/plugin mở rộng phong phú và dễ tích hợp.
</details>

---

### Q249. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

Which of the following is a key characteristic of 'Page Object Model' (POM) design pattern in GUI test automation?

- **A.** It encapsulates web page elements and interactions inside dedicated class files, separating the test logic from UI locators to dramatically improve maintainability.
- **B.** It prints every web page onto physical paper.
- **C.** It restricts web pages to 1 single image.
- **D.** It eliminates the need for test assertions.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q249)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Design pattern Page Object Model (POM): Gom toàn bộ các định danh phần tử (locators) và hành vi trên từng trang web vào một class riêng biệt. Khi giao diện web thay đổi, tester chỉ cần sửa locator ở đúng một class đại diện cho trang đó thay vì sửa ở hàng trăm test case.
</details>

---

### Q250. [Chapter 6: Tool Support for Testing - 6.2 Effective Use of Tools] (Chọn 1 đáp án đúng)

What is the ULTIMATE measure of whether the introduction of a testing tool was successful?

- **A.** Whether the tool delivers a positive Return on Investment (ROI) by enhancing testing efficiency, improving defect detection, and maintaining team productivity over time.
- **B.** Whether the tool CD-ROM is kept in a safe.
- **C.** Whether the test manager was featured on television.
- **D.** Whether 100% of human testers were laid off.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q250)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Thước đo tối hậu cho sự thành công của việc áp dụng công cụ: Tỷ suất hoàn vốn đầu tư (ROI) dương - công cụ giúp nâng cao năng suất và chất lượng kiểm thử, phát hiện lỗi nhanh hơn và giảm chi phí kiểm thử dài hạn một cách bền vững.
</details>

---

### Q266. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Boundary Value Analysis] (Chọn 1 đáp án đúng)

A discount system accepts purchase amounts from $1.00 to $99.99 (inclusive, 2 decimal places). Using 2-value Boundary Value Analysis, which values should be tested around the upper boundary ($99.99)?

- **A.** $99.99 and $100.00
- **B.** $99.98, $99.99, $100.00
- **C.** $90.00 and $100.00
- **D.** $99.00 and $100.00

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q266)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Vì dữ liệu có độ chính xác 2 chữ số thập phân, bước nhảy nhỏ nhất là 0.01. Tại cận trên $99.99: Giá trị biên hợp lệ là $99.99 và giá trị kế cận ngay ngoài biên là $100.00 ($99.99 + 0.01). Hai giá trị cần test là $99.99 và $100.00.
</details>

---

### Q267. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Boundary Value Analysis] (Chọn 1 đáp án đúng)

For the same range [$1.00, $99.99] with 2 decimal precision, what are the 3-value boundary test values around the lower boundary ($1.00)?

- **A.** $0.99, $1.00, $1.01
- **B.** $0.00, $1.00, $2.00
- **C.** $0.90, $1.00, $1.10
- **D.** $1.00, $50.00, $99.99

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q267)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Kỹ thuật 3-value BVA chọn 3 giá trị tại mỗi biên: ngay dưới biên, tại biên, và ngay trên biên. Tại biên dưới $1.00 với độ chính xác 0.01: $0.99 (just below), $1.00 (boundary), $1.01 (just above).
</details>

---

### Q268. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Equivalence Partitioning] (Chọn 1 đáp án đúng)

An insurance premium calculates risk based on two input variables:
- Age: [18 to 65] (valid), <18 (invalid), >65 (invalid)
- Smoker: Yes (valid), No (valid)
What is the MINIMUM number of test cases to cover all valid equivalence partitions?

- **A.** 2 test cases
- **B.** 4 test cases
- **C.** 6 test cases
- **D.** 1 test case

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q268)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Có 1 phân vùng hợp lệ cho Age: [18, 65]. Có 2 phân vùng hợp lệ cho Smoker: Yes và No. Để bao phủ tất cả các phân vùng hợp lệ của cả 2 biến, chỉ cần tối thiểu 2 test cases kết hợp: TC1 (Age=30, Smoker=Yes) và TC2 (Age=40, Smoker=No).
</details>

---

### Q269. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Equivalence Partitioning] (Chọn 1 đáp án đúng)

For the same insurance system (Age: 1 valid, 2 invalid; Smoker: 2 valid, 1 invalid [other inputs]), what is the MINIMUM number of test cases to test all INVALID equivalence partitions without error masking?

- **A.** 1 test case
- **B.** 3 test cases
- **C.** 6 test cases
- **D.** 8 test cases

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q269)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Có 2 phân vùng invalid cho Age (Age < 18 và Age > 65) và 1 phân vùng invalid cho Smoker (giá trị khác Yes/No). Theo nguyên tắc chống error masking, mỗi giá trị invalid phải được test riêng biệt với giá trị hợp lệ của biến kia. Do đó cần đúng 3 test cases: TC1 (Age=15, Smoker=Yes), TC2 (Age=70, Smoker=Yes), TC3 (Age=30, Smoker=Invalid).
</details>

---

### Q270. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Decision Table Testing] (Chọn 1 đáp án đúng)

A hotel discount rule states:
- Condition 1: Weekend stay (True/False)
- Condition 2: Member of loyalty club (True/False)
If Weekend stay is False, NO DISCOUNT is granted regardless of loyalty club membership.
How many rules can be collapsed for the case Weekend = False?

- **A.** 2 rules can be collapsed into 1 rule (Weekend = False, Member = '-', Action = No discount)
- **B.** 4 rules
- **C.** Rules cannot be collapsed in hotel systems
- **D.** 0 rules

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q270)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Khi Weekend = False, dù Member là True hay False thì kết quả Action đều là 'No discount'. Do đó 2 cột (False, True) và (False, False) được gộp lại thành 1 cột duy nhất: Weekend = False, Member = '-' (Don't Care), Action = No discount.
</details>

---

### Q271. [Chapter 4: Test Analysis and Design - 4.2 Black-box: State Transition Testing] (Chọn 1 đáp án đúng)

A turnstile gate has two states: [Locked] and [Unlocked].
- In [Locked], inserting a coin transitions to [Unlocked].
- In [Locked], pushing the turnstile stays in [Locked].
- In [Unlocked], pushing the turnstile transitions to [Locked].
- In [Unlocked], inserting a coin stays in [Unlocked].
How many total transitions (including transitions to the same state) exist in this state machine?

- **A.** 2 transitions
- **B.** 4 transitions
- **C.** 8 transitions
- **D.** 1 transition

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q271)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Có 2 trạng thái và mỗi trạng thái có 2 sự kiện (Push và Coin), tổng cộng có 2 * 2 = 4 transitions: 1. Locked -> Coin -> Unlocked; 2. Locked -> Push -> Locked; 3. Unlocked -> Push -> Locked; 4. Unlocked -> Coin -> Unlocked.
</details>

---

### Q272. [Chapter 4: Test Analysis and Design - 4.2 Black-box: State Transition Testing] (Chọn 1 đáp án đúng)

What is '1-switch coverage' in State Transition Testing?

- **A.** Executing all valid sequences of two consecutive transitions (pairs of transitions).
- **B.** Executing only one test case.
- **C.** Turning off the computer switch once.
- **D.** Testing every state exactly once.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q272)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** 1-switch coverage (kiểm thử chuỗi 2 bước chuyển liên tiếp): Yêu cầu tất cả các cặp bước chuyển hợp lệ liên tiếp (sequences of two consecutive transitions) phải được thực thi ít nhất một lần. Mức độ bao phủ này sâu hơn 0-switch (chỉ test từng bước chuyển đơn lẻ).
</details>

---

### Q273. [Chapter 4: Test Analysis and Design - 4.3 White-box: Statement Coverage] (Chọn 1 đáp án đúng)

Consider the code snippet:
```java
int compute(int x, int y) {
    int res = 0;
    if (x > 0 && y > 0) {
        res = x + y;
    }
    return res;
}
```
What input values of (x, y) will achieve 100% Statement Coverage with a SINGLE test case?

- **A.** x = 5, y = 10
- **B.** x = -5, y = 10
- **C.** x = 0, y = 0
- **D.** x = 5, y = -1

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q273)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Khi x = 5 và y = 10, biểu thức (x > 0 && y > 0) là True, dòng lệnh 'res = x + y;' bên trong if được thực thi. Như vậy 100% các dòng lệnh trong hàm đều được chạy qua chỉ với 1 test case duy nhất.
</details>

---

### Q274. [Chapter 4: Test Analysis and Design - 4.3 White-box: Decision Coverage] (Chọn 1 đáp án đúng)

For the same function:
```java
int compute(int x, int y) {
    int res = 0;
    if (x > 0 && y > 0) {
        res = x + y;
    }
    return res;
}
```
What is the MINIMUM number of test cases to achieve 100% Decision (Branch) Coverage?

- **A.** 1 test case
- **B.** 2 test cases (one where (x>0 && y>0) is True, one where it is False)
- **C.** 4 test cases
- **D.** 3 test cases

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q274)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Cấu trúc if có 2 kết quả nhánh: True và False. Cần tối thiểu 2 test cases: 1 test case làm cho điều kiện True (ví dụ x=1, y=1) và 1 test case làm cho điều kiện False (ví dụ x=-1, y=1).
</details>

---

### Q275. [Chapter 4: Test Analysis and Design - 4.3 White-box: Modified Condition / Decision Coverage] (Chọn 1 đáp án đúng)

What is Modified Condition / Decision Coverage (MC/DC), commonly used in safety-critical avionics software (DO-178C)?

- **A.** A technique requiring that each individual condition within a decision is shown to independently affect the decision outcome.
- **B.** A technique where testers modify source code during testing.
- **C.** A tool used solely for database indexing.
- **D.** A black-box exploratory charter.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q275)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** MC/DC (Modified Condition/Decision Coverage): Kỹ thuật White-box cao cấp bắt buộc trong phần mềm hàng không (chuẩn DO-178C Level A), yêu cầu chứng minh rằng mỗi điều kiện con đơn lẻ có thể độc lập làm thay đổi kết quả của toàn bộ biểu thức điều kiện quyết định.
</details>

---

### Q276. [Chapter 4: Test Analysis and Design - 4.3 White-box: Cyclomatic Complexity] (Chọn 1 đáp án đúng)

A method has 1 `while` loop, 2 independent `if` statements, and 1 `switch` statement with 3 `case` labels (and a default). What is the Cyclomatic Complexity V(G)?

- **A.** 7
- **B.** 6
- **C.** 4
- **D.** 9

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q276)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Công thức V(G) = Số điểm quyết định nhị phân + 1: 1 while loop = 1; 2 independent ifs = 2; switch với 3 case = 3 nhánh quyết định. Tổng số điểm quyết định P = 1 + 2 + 3 = 6. Do đó V(G) = P + 1 = 6 + 1 = 7.
</details>

---

### Q277. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Use Case Testing] (Chọn 1 đáp án đúng)

A tester designs test cases for an online banking transfer. Test Case 1 covers the 'Happy Path' (sufficient balance, valid OTP). Test Case 2 covers 'Invalid OTP entered twice'. Test Case 3 covers 'Transfer amount exceeds daily limit'. What technique is being applied?

- **A.** Use Case Testing (covering basic flow, alternate flow, and exception flows)
- **B.** Structural Statement Coverage
- **C.** Static Inspection
- **D.** Code Profiling

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q277)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Đây là kỹ thuật Use Case Testing: Thiết kế các test case bao phủ luồng chính (Main/Basic flow), luồng thay thế (Alternate flow) và luồng xử lý ngoại lệ (Exception flow) của ca sử dụng.
</details>

---

### Q278. [Chapter 4: Test Analysis and Design - 4.3 White-box: Path Testing] (Chọn 1 đáp án đúng)

In a program with 2 sequential, independent `if` statements (each having an `else` branch), how many total execution paths exist through the code?

- **A.** 2 paths
- **B.** 4 paths
- **C.** 8 paths
- **D.** 1 path

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q278)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Với 2 câu lệnh if-else tuần tự độc lập: If thứ nhất có 2 nhánh, If thứ hai có 2 nhánh. Tổng số đường đi khả dĩ xuyên qua chương trình là 2 * 2 = 4 đường đi: (True, True), (True, False), (False, True), (False, False).
</details>

---

### Q279. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Decision Table Testing] (Chọn 1 đáp án đúng)

A login function has 2 conditions:
1. Username correct? (Y/N)
2. Password correct? (Y/N)
Action: Grant access if both Y; otherwise Display error.
How many test cases are derived from the minimized decision table?

- **A.** 3 test cases: Rule 1 (Y, Y -> Access), Rule 2 (Y, N -> Error), Rule 3 (N, - -> Error)
- **B.** 10 test cases
- **C.** 1 test case
- **D.** 8 test cases

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q279)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Bảng đầy đủ có 4 cột: (Y,Y), (Y,N), (N,Y), (N,N). Khi Username = N, dù Password đúng hay sai đều báo lỗi Error, nên (N,Y) và (N,N) gộp thành (N, '-'). Vậy bảng rút gọn còn 3 test cases tối thiểu.
</details>

---

### Q280. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Boundary Value Analysis] (Chọn 1 đáp án đúng)

An input accepts calendar day of the month for February in a standard non-leap year (valid: 1 to 28). What are the 2-value boundary test values for day?

- **A.** 0, 1, 28, 29
- **B.** 1, 28
- **C.** -1, 0, 28, 31
- **D.** 0, 1, 2, 27, 28, 29

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q280)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Miền hợp lệ là [1, 28]. Áp dụng 2-value BVA: Biên dưới là 1 và kế cận ngoài là 0. Biên trên là 28 và kế cận ngoài là 29. Tập giá trị biên là {0, 1, 28, 29}.
</details>

---

### Q281. [Chapter 4: Test Analysis and Design - 4.4 Experience-based Techniques] (Chọn 1 đáp án đúng)

A software tester tests a search engine by entering SQL injection strings (`' OR '1'='1`) and extremely long strings (100,000 characters) without looking at requirements. What experience-based technique is this?

- **A.** Error Guessing based on common attack patterns
- **B.** Formal Verification
- **C.** 100% Branch Coverage
- **D.** Static Architecture Review

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q281)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Tester sử dụng các mẫu tấn công và lỗi phổ biến trong quá khứ để đoán lỗi (Error Guessing), nhằm xem hệ thống có xử lý an toàn với các đầu vào độc hại hay không.
</details>

---

### Q282. [Chapter 4: Test Analysis and Design - 4.3 White-box: Statement vs Decision Coverage] (Chọn 1 đáp án đúng)

Why is Path Coverage rarely achievable in programs containing loops?

- **A.** Because loops can execute an arbitrarily large or infinite number of times, causing combinatorial explosion of possible execution paths.
- **B.** Because compilers do not allow loops to be tested.
- **C.** Because path testing is only applicable to HTML.
- **D.** Because path coverage does not require test cases.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q282)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Hiện tượng bùng nổ tổ hợp đường đi (combinatorial explosion): Một vòng lặp chạy từ 0 đến N lần sẽ nhân số lượng đường đi lên gấp hàng triệu lần, khiến việc đạt 100% Path Coverage trong thực tế là bất khả thi.
</details>

---

### Q283. [Chapter 4: Test Analysis and Design - 4.2 Black-box: Equivalence Partitioning] (Chọn 1 đáp án đúng)

An employee leave booking system accepts leave duration from 0.5 days to 30.0 days in increments of 0.5 days (e.g., 0.5, 1.0, 1.5 ... 30.0). Which of the following is an INVALID equivalence partition?

- **A.** 1.3 days (invalid increment)
- **B.** 15.5 days
- **C.** 0.5 days
- **D.** 30.0 days

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q283)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Giá trị 1.3 ngày vi phạm quy tắc bước nhảy 0.5 ngày (invalid increment), thuộc phân vùng không hợp lệ.
</details>

---

### Q284. [Chapter 4: Test Analysis and Design - 4.3 White-box: Cyclomatic Complexity] (Chọn 1 đáp án đúng)

If Cyclomatic Complexity of a Java method is calculated as 15, what does this indicate according to software engineering best practices?

- **A.** The method is simple and easy to maintain.
- **B.** The method has high complexity, is difficult to test thoroughly, and should be refactored into smaller modular methods.
- **C.** The method has zero bugs.
- **D.** The method cannot be executed by the JVM.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q284)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `B`
- **GIẢI THÍCH:** Theo chuẩn McCabe, hàm có V(G) > 10 là hàm có độ phức tạp cao, tiềm ẩn nhiều lỗi và rất khó bảo trì; nên xem xét tái cấu trúc (refactor) chia nhỏ thành các hàm con.
</details>

---

### Q285. [Chapter 4: Test Analysis and Design - 4.1 Categories of Test Techniques] (Chọn nhiều đáp án)

Which TWO of the following are specification-based (Black-box) test techniques? (Choose TWO options)

- **A.** Boundary Value Analysis
- **B.** Decision Coverage
- **C.** State Transition Testing
- **D.** Statement Testing
- **E.** Cyclomatic Complexity Calculation

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q285)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A, C`
- **GIẢI THÍCH:** Boundary Value Analysis (BVA) và State Transition Testing là các kỹ thuật Black-box (dựa trên đặc tả). B, D, E là các kỹ thuật/chỉ số White-box.
</details>

---

### Q286. [Chapter 5: Test Management - 5.5 Risks and Testing] (Chọn 1 đáp án đúng)

In a medical heart-monitoring device, the probability of a data sync glitch is Low (2 out of 5), but if it occurs, the impact on patient health is Catastrophic (5 out of 5). What is the calculated Risk Priority Level?

- **A.** 10 (High Risk due to critical impact)
- **B.** 7
- **C.** 2.5
- **D.** 0

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q286)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Risk Level = Likelihood * Impact = 2 * 5 = 10. Dù xác suất thấp nhưng tác hại liên quan đến tính mạng bệnh nhân là thảm khốc, nên đây vẫn là rủi ro mức độ cao cần ưu tiên kiểm thử nghiêm ngặt.
</details>

---

### Q287. [Chapter 5: Test Management - 5.3 Test Monitoring and Control] (Chọn 1 đáp án đúng)

In software testing, what does an 'S-Curve' (Cumulative Test Execution Curve) visually represent over project duration?

- **A.** Slow progress initially, accelerating rapidly during main execution, and flattening out as exit criteria and test completion are reached.
- **B.** The salary curve of testers.
- **C.** Hardware memory usage.
- **D.** Internet bandwidth consumption.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q287)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Đường cong chữ S (S-Curve): Biểu đồ tích lũy tiến độ kiểm thử chuẩn - ban đầu tiến độ tăng chậm khi mới thiết lập môi trường, sau đó tăng tốc rất nhanh ở giai đoạn chạy test cao điểm, và thoải dần khi gần hoàn thành và hệ thống ổn định.
</details>

---

### Q288. [Chapter 5: Test Management - 5.6 Defect Management] (Chọn 1 đáp án đúng)

A tester logs a defect stating: 'The button does not work.' The developer rejects it as 'Not Reproducible'. What critical information was MISSING from the report?

- **A.** Detailed preconditions, exact step-by-step reproduction instructions, test data used, and actual vs expected results.
- **B.** The tester's phone number.
- **C.** A picture of the computer mouse.
- **D.** The brand of the developer's keyboard.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q288)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Báo cáo lỗi quá sơ sài không thể tái hiện được nếu thiếu: điều kiện tiên quyết (preconditions), các bước thực hiện tuần tự, dữ liệu đầu vào đã dùng và so sánh kết quả thực tế với kết quả mong đợi.
</details>

---

### Q289. [Chapter 5: Test Management - 5.2 Test Planning and Estimation] (Chọn 1 đáp án đúng)

What is the primary role of 'Definition of Ready' (DoR) in Agile Scrum testing?

- **A.** Ensuring that a User Story has clear acceptance criteria, sufficient detail, and testable requirements before the team agrees to pull it into a Sprint.
- **B.** Declaring that all developers are ready for lunch.
- **C.** Stating that the sprint backlog is completely deleted.
- **D.** Terminating the test manager.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q289)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Definition of Ready (DoR - Tiêu chí sẵn sàng): Đảm bảo rằng một User Story đã có đầy đủ tiêu chí chấp nhận (Acceptance Criteria), thông tin rõ ràng và có thể kiểm thử được trước khi nhóm nhận vào Sprint để phát triển.
</details>

---

### Q290. [Chapter 5: Test Management - 5.2 Test Planning and Estimation] (Chọn 1 đáp án đúng)

What is the primary difference between a Test Strategy and a Test Plan?

- **A.** A Test Strategy is organizational/project-independent describing general test approaches; a Test Plan is specific to a particular project detailing scope, schedule, and resources.
- **B.** A Test Plan is only for developers; a Test Strategy is only for clients.
- **C.** They are identical documents.
- **D.** Test Strategy is written only after testing finishes.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q290)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Test Strategy là định hướng chiến lược cấp cao (thường dùng chung cho nhiều dự án trong tổ chức); trong khi Test Plan là kế hoạch chi tiết cho một dự án/giai đoạn cụ thể (gồm nhân sự, lịch trình, phạm vi, ngân sách).
</details>

---

### Q291. [Chapter 5: Test Management - 5.1 Test Organization] (Chọn 1 đáp án đúng)

What is a major risk if a software project employs ZERO independent testers and relies solely on developers testing their own code?

- **A.** Confirmation bias will lead developers to overlook defects caused by blind spots in their own assumptions.
- **B.** Testing will cost too much money.
- **C.** Code execution speed will drop by 50%.
- **D.** The compiler will refuse to build the project.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q291)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Nếu lập trình viên chỉ tự test code của mình: Thiên kiến xác nhận (Confirmation bias) khiến họ chỉ kiểm tra các trường hợp chạy đúng (happy path) và bỏ qua các giả định sai lầm của chính mình.
</details>

---

### Q292. [Chapter 5: Test Management - 5.6 Defect Management] (Chọn 1 đáp án đúng)

What happens when a defect report is marked as 'Deferred' by the change control board?

- **A.** The defect is acknowledged as a valid bug, but will not be fixed in the current release due to schedule, cost, or risk constraints.
- **B.** The defect is permanently erased from Jira history.
- **C.** The tester is penalized.
- **D.** The application is completely rewritten.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q292)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Trạng thái Deferred: Hội đồng quản lý thay đổi (CCB) thừa nhận lỗi là có thật, nhưng quyết định hoãn sửa sang các phiên bản sau vì thời gian gấp rút hoặc rủi ro sửa lỗi quá lớn.
</details>

---

### Q293. [Chapter 5: Test Management - 5.5 Risks and Testing] (Chọn 1 đáp án đúng)

Which of the following is an example of a Project Risk related to CONTRACTS?

- **A.** A third-party software library vendor breaches SLA agreements and fails to deliver the payment API on schedule.
- **B.** The mobile application crashes when internet is disconnected.
- **C.** The user enters an invalid credit card number.
- **D.** A division by zero error occurs in financial reporting.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q293)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Nhà cung cấp bên thứ ba vi phạm thỏa thuận hợp đồng SLA dẫn đến chậm tiến độ là rủi ro dự án liên quan đến hợp đồng/nhà thầu (Project Risk).
</details>

---

### Q294. [Chapter 5: Test Management - 5.3 Test Monitoring and Control] (Chọn 1 đáp án đúng)

What does a high 'Defect Reopen Rate' typically indicate?

- **A.** Developers may be writing poor-quality bug fixes, or the root cause was not properly addressed, or regression occurred.
- **B.** Testers do not know how to run tests.
- **C.** The software has 100% test coverage.
- **D.** The compiler is malfunctioning.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q294)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Tỷ lệ Reopen bug cao (Defect Reopen Rate cao): Cho thấy chất lượng sửa lỗi của developer chưa tốt, chỉ sửa phần ngọn mà chưa giải quyết nguyên nhân gốc rễ, hoặc việc sửa lỗi gây ra lỗi mới.
</details>

---

### Q295. [Chapter 5: Test Management - 5.2 Test Planning and Estimation] (Chọn 1 đáp án đúng)

In test effort estimation, what does 'Estimation by Analogy' mean?

- **A.** Estimating effort for a new project based on actual effort spent on similar projects completed in the past.
- **B.** Guessing a random number between 1 and 100.
- **C.** Calculating the square root of code lines.
- **D.** Letting an AI write all code.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q295)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Ước lượng tương tự (Estimation by Analogy): Phương pháp ước lượng công sức cho dự án mới dựa trên việc so sánh và đối chiếu với dữ liệu thực tế từ các dự án tương đồng đã hoàn thành trong quá khứ.
</details>

---

### Q296. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

What is the primary formula used to calculate Return on Investment (ROI) for a test automation initiative?

- **A.** ROI = (Net Benefits from Automation - Cost of Automation) / Cost of Automation * 100%
- **B.** ROI = Number of test cases * 100
- **C.** ROI = Server CPU usage * RAM size
- **D.** ROI = Number of bug tickets logged in Jira

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q296)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** ROI của tự động hóa = (Lợi ích ròng thu được - Chi phí đầu tư cho tự động hóa) / Chi phí đầu tư cho tự động hóa * 100%. Lợi ích bao gồm số giờ manual tiết kiệm được, phát hiện lỗi sớm và rút ngắn chu kỳ release.
</details>

---

### Q297. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

Why is hardcoding test input data and expected results directly inside UI test scripts considered a POOR automation practice?

- **A.** Because whenever data changes, tester must manually modify code across multiple scripts, drastically increasing maintenance overhead.
- **B.** Because compilers refuse to run hardcoded strings.
- **C.** Because computers run out of disk space.
- **D.** Because ISO standards mandate SQL databases.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q297)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Hardcode dữ liệu vào script làm tăng chi phí bảo trì. Thay vào đó nên áp dụng Data-Driven Testing để tách dữ liệu ra các file bên ngoài (CSV, Excel, JSON).
</details>

---

### Q298. [Chapter 6: Tool Support for Testing - 6.2 Effective Use of Tools] (Chọn 1 đáp án đúng)

What should be done with test automation assets during the 'Test Completion' phase?

- **A.** Archive test scripts, test data, and execution results into version control and hand them over to maintenance teams with clear documentation.
- **B.** Delete all scripts to make room on the hard drive.
- **C.** Encrypt scripts and hide passwords.
- **D.** Print all scripts on paper and shred them.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q298)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Trong pha Kết thúc kiểm thử (Test Completion), các tài sản tự động hóa (scripts, test data, cấu hình) cần được lưu trữ cẩn thận vào hệ thống quản lý phiên bản (Git) và bàn giao đầy đủ cho đội ngũ vận hành/bảo trì.
</details>

---

### Q299. [Chapter 6: Tool Support for Testing - 6.1 Test Tool Considerations] (Chọn 1 đáp án đúng)

Which testing tool provides detailed memory leak analysis by tracking heap memory allocation and identifying un-freed pointers during execution?

- **A.** Dynamic Memory Analysis Tool (e.g., Valgrind, LeakCanary)
- **B.** Static Spell Checker
- **C.** Requirement Traceability Matrix Tool
- **D.** Bug Tracking Database

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q299)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Công cụ phân tích động bộ nhớ (như Valgrind, LeakCanary) theo dõi việc cấp phát bộ nhớ heap khi chương trình đang chạy để phát hiện các lỗi rò rỉ bộ nhớ (memory leaks) và con trỏ chưa được giải phóng.
</details>

---

### Q300. [Chapter 6: Tool Support for Testing - 6.2 Effective Use of Tools] (Chọn 1 đáp án đúng)

What is the ultimate benefit of combining continuous automated testing with a robust Defect Tracking tool?

- **A.** Provides continuous quality visibility, rapid defect turnaround, and objective data for release go/no-go decisions.
- **B.** Completely eliminates the need to write software code.
- **C.** Guarantees that users will never file complaints.
- **D.** Replaces the need for database storage.

<details>
<summary>👉 <b>Xem đáp án & giải thích (Q300)</b></summary>

- **ĐÁP ÁN ĐÚNG:** `A`
- **GIẢI THÍCH:** Sự kết hợp giữa kiểm thử tự động liên tục và công cụ theo dõi lỗi mang lại cái nhìn minh bạch liên tục về chất lượng phần mềm, giúp rút ngắn chu kỳ sửa lỗi và cung cấp số liệu khách quan giúp ban quản lý tự tin ra quyết định phát hành (release).
</details>

---
