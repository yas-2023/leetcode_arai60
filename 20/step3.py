class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {")": "(", "}": "{", "]": "["}
        close_brackets = close_open.keys()
        open_brackets = close_open.values()
        open_stack = []

        for bracket in s:
            if bracket in open_brackets:
                open_stack.append(bracket)
            elif bracket in close_brackets:
                if not open_stack:
                    return False
                elif open_stack.pop() != close_open[bracket]:
                    return False
            else:
                return False
        return not open_stack
