import re


class Stack:
    """A simple stack implemented using a Python list."""

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


OPERATORS = {
    "+": (1, "left"),
    "-": (1, "left"),
    "*": (2, "left"),
    "/": (2, "left"),
    "u+": (3, "right"),
    "u-": (3, "right"),
}


def tokenize(expression):
    """Split an expression into numbers, operators, and parentheses."""
    tokens = []
    i = 0
    while i < len(expression):
        char = expression[i]

        if char.isspace():
            i += 1
            continue

        if char.isdigit() or char == ".":
            match = re.match(r"(?:\d+(?:\.\d*)?|\.\d+)", expression[i:])
            if not match:
                raise ValueError(f"Invalid number near: {expression[i:]}")
            tokens.append(match.group())
            i += len(match.group())
            continue

        if char in "+-*/()":
            tokens.append(char)
            i += 1
            continue

        raise ValueError(f"Unsupported character: {char}")

    if not tokens:
        raise ValueError("Expression is empty.")
    return tokens


def to_postfix(expression):
    """Convert infix notation to postfix notation using an operator stack."""
    tokens = tokenize(expression)
    output = []
    operators = Stack()
    previous = None

    for token in tokens:
        if re.fullmatch(r"(?:\d+(?:\.\d*)?|\.\d+)", token):
            output.append(token)
            previous = "number"

        elif token in ("+", "-", "*", "/"):
            # A plus or minus is unary at the start or after an operator or '('.
            op = token
            if token in ("+", "-") and (
                previous is None or previous in ("operator", "left_paren")
            ):
                op = "u" + token

            while not operators.is_empty() and operators.peek() in OPERATORS:
                top = operators.peek()
                current_precedence, associativity = OPERATORS[op]
                top_precedence = OPERATORS[top][0]
                should_pop = (
                    top_precedence > current_precedence
                    or (
                        top_precedence == current_precedence
                        and associativity == "left"
                    )
                )
                if not should_pop:
                    break
                output.append(operators.pop())

            operators.push(op)
            previous = "operator"

        elif token == "(":
            operators.push(token)
            previous = "left_paren"

        elif token == ")":
            found_opening = False
            while not operators.is_empty():
                top = operators.pop()
                if top == "(":
                    found_opening = True
                    break
                output.append(top)
            if not found_opening:
                raise ValueError("Mismatched parentheses: missing '('.")
            previous = "right_paren"

    while not operators.is_empty():
        top = operators.pop()
        if top in ("(", ")"):
            raise ValueError("Mismatched parentheses: missing ')'.")
        output.append(top)

    return output


def evaluate_expression(expression):
    """Evaluate an arithmetic expression using a value stack."""
    postfix = to_postfix(expression)
    values = Stack()

    for token in postfix:
        if token in OPERATORS:
            if token in ("u+", "u-"):
                if values.size() < 1:
                    raise ValueError("Invalid expression.")
                value = float(values.pop())
                values.push(value if token == "u+" else -value)
                continue

            if values.size() < 2:
                raise ValueError("Invalid expression.")
            right = float(values.pop())
            left = float(values.pop())

            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            else:
                if right == 0:
                    raise ZeroDivisionError("Division by zero.")
                result = left / right

            values.push(result)
        else:
            values.push(float(token))

    if values.size() != 1:
        raise ValueError("Invalid expression.")
    return values.pop()


def format_result(value):
    """Avoid displaying an unnecessary .0 for whole-number results."""
    if value == int(value):
        return str(int(value))
    return f"{value:.10g}"


def process_file(input_filename="input.txt", output_filename="output.txt"):
    """Evaluate each expression and preserve separator lines."""
    with open(input_filename, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()

    output_lines = []
    for line_number, line in enumerate(lines, start=1):
        stripped = line.strip()

        if stripped and all(char in "-=_*" for char in stripped):
            output_lines.append(line.rstrip("\r\n"))
            continue

        if not stripped:
            output_lines.append("")
            continue

        try:
            result = evaluate_expression(stripped)
            output_lines.append(format_result(result))
        except (ValueError, ZeroDivisionError, IndexError) as error:
            output_lines.append(f"ERROR on line {line_number}: {error}")

    with open(output_filename, "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(output_lines))
        if output_lines:
            output_file.write("\n")


if __name__ == "__main__":
    try:
        process_file()
        print("Evaluation completed. Check output.txt.")
    except FileNotFoundError:
        print("input.txt was not found. Place it in the same folder as main.py.")
