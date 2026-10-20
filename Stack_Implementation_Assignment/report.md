# Stack Implementation for Mathematical Expression Evaluation

## Title Page
**Assignment:** Stack Implementation  
**Course:** DCOMP320 — Data Structures and Algorithm  
**Student Name:** __________________________  
**Student ID:** _____________________________  
**Lecturer:** Amandus Benjamin Coker  
**Submission Date:** ________________________

## 1. Introduction
This project implements a Python program that reads mathematical expressions from a text file, evaluates each expression using a stack-based approach, and writes the results to another text file. The program supports arithmetic operators and parentheses. It also preserves separator lines so that the output follows the same layout as the input.

## 2. Data Structures Used
A stack is a linear data structure that follows the Last In, First Out (LIFO) rule. The last item added is the first item removed. The stack in this program is implemented using a Python list.

The stack provides three main operations:
- **Push:** adds an item to the top of the stack.
- **Pop:** removes and returns the top item.
- **Peek:** returns the top item without removing it.

Stacks are useful in computing for expression evaluation, function calls, undo operations, and checking balanced parentheses.

## 3. Program Design
The program is divided into functions:
- `tokenize()` separates an expression into numbers, operators, and parentheses.
- `to_postfix()` converts the expression into postfix notation using an operator stack and operator precedence.
- `evaluate_expression()` evaluates postfix notation using a value stack.
- `format_result()` displays whole-number results without an unnecessary decimal part.
- `process_file()` reads the input file, evaluates each expression, and writes results to the output file.

The conversion to postfix notation makes it possible to apply operator precedence and parentheses consistently without using Python's `eval()` function.

## 4. Program Operation
The program reads `input.txt` one line at a time. Expression lines are evaluated, while separator lines are copied unchanged. The results are written in the same order to `output.txt`.

For example:
- `3 + 5 * 2` gives `13`, because multiplication is performed before addition.
- `(8 / 4) + 7 * 2` gives `16`, because the parentheses are evaluated first and then multiplication.
- `10 - (2 + 3) * 4` gives `-10`, because the expression inside parentheses is evaluated first, then multiplied by four.

## 5. Testing and Results
The sample expressions were tested against standard arithmetic rules.

| Test | Expression | Expected result |
|---|---|---:|
| 1 | `3 + 5 * 2` | 13 |
| 2 | `(8 / 4) + 7 * 2` | 16 |
| 3 | `10 - (2 + 3) * 4` | -10 |
| 4 | `-5 + 2` | -3 |
| 5 | `8 / 0` | Error message |

The program should be run from the folder containing `main.py` and `input.txt`. After execution, the results can be checked in `output.txt`.

**Important note about the assignment example:** The scanned assignment appears to list `17` for `(8 / 4) + 7 * 2`. Using standard arithmetic, the result is `16`: `8 / 4 = 2`, `7 * 2 = 14`, and `2 + 14 = 16`. This discrepancy should be confirmed with the lecturer.

## 6. Conclusion
This project demonstrates how a stack can be used to evaluate mathematical expressions in Python. It supports operator precedence, parentheses, and basic error handling. The file-based design separates the input data from the program and stores the calculated results in an output file.

## 7. References
Python Software Foundation (n.d.) *Python 3 Documentation*. Available at: https://docs.python.org/3/ (Accessed: 18 October 2026).

Runestone Academy (n.d.) *Problem Solving with Algorithms and Data Structures*. Available at: https://runestone.academy/ (Accessed: 18 October 2026).
