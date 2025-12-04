def is_valid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in s:
        # If opening bracket → push to stack
        if ch in "({[":
            stack.append(ch)
        else:
            # Closing bracket but stack empty
            if not stack:
                return False
            
            # If top of stack does not match
            if stack[-1] != pairs[ch]:
                return False
            
            # Pop matched bracket
            stack.pop()

    return len(stack) == 0


print(is_valid("({[]})"))
