# Calculator Project Write-Up

1. Requirements Analysis & Design
	•	Objective: Build a calculator with a user interface capable of:
	•	Basic arithmetic: add, subtract, multiply, divide
	•	Advanced math: power, trigonometric functions, logarithm, exponent
	•	Stack: Python + Flask (for local web UI) and OpenAI API (for expression evaluation via prompt engineering).
	•	Design Approach:
	•	Browser-based UI served by Flask (http://127.0.0.1:5000)
	•	HTML form with buttons for digits and functions
	•	Input expression passed raw to backend → sent to OpenAI → numeric result returned
	•	Minimal CSS, function-first design
	•	Revamp: An earlier draft used Python’s math library (math.sin, math.log, etc.), but this wasn’t part of the assignment. I rebuilt the calculator so all evaluation is handled by AI.

⸻

2. Development
	•	Project created and completed in a single session, with a quick revamp after initial prototype.
	•	Steps implemented:
	1.	Flask app skeleton with routes
	2.	HTML template with 3-column keypad layout
	3.	OpenAI API integration with a tailored prompt
	4.	Buttons stripped down to insert exactly their label (e.g., sin, π, ^)—no math. prefixes
	5.	AI evaluator upgraded to handle the entire expression flexibly
	•	Development Time: ~2 hours for core build + ~20 minutes revamp (removing math dependency, refining AI prompt).
	•	Screenshots included:
	•	UI overview
	•	Arithmetic (add, subtract, multiply, divide)
	•	Exponentiation
	•	Logarithm
	•	Trigonometry (sin, cos, tan)
	•	π usage
	•	Error handling

⸻

3. Testing
	•	Functional Testing: Verified each operation (basic + advanced) produced correct numeric results.
	•	Error Handling:
	•	Division by zero → returns “Error,” no crash
	•	Random input like abc → handled gracefully by AI
	•	Defects Found:
	•	Layout limited to 3 columns (considered cosmetic, not fixed)
	•	In AI-only mode, parentheses don’t need to be perfectly balanced—GPT auto-corrects, which actually improves usability

⸻

4. Time & Effort Analysis
	•	Initial Estimate: ~10 hours (expected API integration + UI to take longer)
	•	Actual Time Spent: ~2 hours 20 minutes, completed on 9/24/2025
	•	Time Log:

Date	Hours	Category
09/24/2025	2.3	Requirements & Development & Testing

	•	Comparison:
	•	Estimated: 10 hrs
	•	Actual: 2 hrs 20 mins
	•	Difference due to smooth integration with Flask + OpenAI, and reduced need for manual error handling once AI took over.

⸻

5. Advantages of AI-Only Evaluation

Switching entirely to OpenAI evaluation gave the calculator far more mathematical flexibility than a standard scientific calculator:
	•	Trig functions assume degrees if no π symbol is detected, instead of forcing the user to toggle between radian/degree modes like a classic scientific calculator. This makes input more flexible and convenient.
	•	Parentheses autocorrect: even if a user forgets to close them, the AI still interprets the expression correctly.
	•	Flexible parsing: the calculator accepts natural-looking math syntax (2^8, sin(90), π*2) instead of rigid function names (math.sin, math.pi).

These autocorrections and flexibility could represent a unique strength of AI-driven calculators compared to traditional ones.

⸻

6. Conclusion

The calculator meets and exceeds assignment requirements:
	•	Handles arithmetic, power, trigonometry, log, and exponent functions.
	•	Provides a working user interface via browser.
	•	Uses AI exclusively for evaluation, demonstrating both prompt engineering and practical advantages over standard calculators.

The project was completed well under budgeted time, showing how generative AI can speed up prototyping while enhancing functionality.

⸻
