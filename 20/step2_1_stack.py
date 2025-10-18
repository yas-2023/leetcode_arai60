from collections import deque


def isValid(s: str) -> bool:
    unclosed_opening_stack = deque()
    closing_to_opening = {')': '(', ']': '[', '}': '{'}

    for bracket in s:
        if bracket in closing_to_opening.values():
            unclosed_opening_stack.append(bracket)
        elif bracket in closing_to_opening.keys():
            if not unclosed_opening_stack:
                return False
            elif unclosed_opening_stack.pop() != closing_to_opening[bracket]:
                return False
        else:
            return False
    return not unclosed_opening_stack
