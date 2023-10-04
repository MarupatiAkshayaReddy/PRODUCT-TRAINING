def order_of_parenthesis(input_str):
    stack = []
    count = 0

    for char in input_str:
        if char == '(':
            stack.append(char)
        elif char == ')' and stack:
            stack.pop()
            count += 1

    return count

input_str = input("")
output = order_of_parenthesis(input_str)
print(output)
