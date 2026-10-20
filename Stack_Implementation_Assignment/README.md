# Stack Implementation — DCOMP320

## Project files
- `main.py` — Python program containing the stack and expression evaluator.
- `input.txt` — sample mathematical expressions.
- `output.txt` — output produced by the program.
- `report.md` — written report draft for the assignment.

## Requirements
- Python 3.10 or newer (Python 3.13 is suitable).
- No third-party packages are required.

## How to run in VS Code
1. Extract this ZIP file.
2. Open the extracted folder in VS Code.
3. Make sure `main.py` and `input.txt` are in the same folder.
4. Open Terminal → New Terminal.
5. Run:
   ```bash
   python main.py
   ```
   On Windows, `py main.py` can also be used.
6. Open `output.txt` to see the results.

## Sample input
```text
3 + 5 * 2
-----
(8 / 4) + 7 * 2
-----
10 - (2 + 3) * 4
```

## Expected output
```text
13
-----
16
-----
-10
```

Note: The assignment scan appears to show `17` for the second expression, but according to standard arithmetic precedence `(8 / 4) + 7 * 2` evaluates to `2 + 14 = 16`. The program uses the mathematically correct result, 16.

## Supported operations and assumptions
- Addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
- Parentheses and decimal numbers.
- Unary plus and minus, such as `-5 + 2`.
- Standard operator precedence: parentheses first, multiplication/division before addition/subtraction.
- Division by zero and invalid expressions are reported as error lines.
- Separator lines containing characters such as hyphens, equals signs, or underscores are copied to the output.
