class Solution:
    def isValid(self, s: str) -> bool:
        bracket_types = ['()', '{}', '[]']
        while s:
            replace_flag = False
            for bracket in bracket_types:
                if bracket in s:
                    s = s.replace(bracket, "")
                    replace_flag = True
                    continue
            # sが空でなく置換されない場合はゴミが残っているのでinvalid
            if replace_flag is False:
                return False
        # whileを抜けられたらsが空になったということなのでvalid
        return True
