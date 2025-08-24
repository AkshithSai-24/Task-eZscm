def parse_two_args(input_str):
    try:
        a, b = map(float, input_str.split(","))
        return a, b
    except Exception:
        raise ValueError("Input should be two numbers separated by a comma.")

def add_tool(input_str):
    a, b = parse_two_args(input_str)
    return a+b

def subtract_tool(input_str):
    a, b = parse_two_args(input_str)
    return a-b

def multiply_tool(input_str):
    a, b = parse_two_args(input_str)
    return a*b

def divide_tool(input_str):
    a, b = parse_two_args(input_str)
    return a/b

def power_tool(input_str):
    a, b = parse_two_args(input_str)
    return a**b

def sqrt_tool(input_str):
    try:
        a = float(input_str)
        return a ** 0.5
    except Exception:
        return "Input should be a single non-negative number."

def modulus_tool(input_str):
    a, b = parse_two_args(input_str)
    return a% b