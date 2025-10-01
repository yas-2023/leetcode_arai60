# LeetCodeのSolutionクラス形式
class Solution:
    def isValid(self, s: str) -> bool:
        """
        与えられた文字列が有効な括舗の組み合わせであるかを判定
        """
        parser = self.Parser(s)
        return parser.is_valid()

    class Parser:
        def __init__(self, s: str):
            self.s = s
            self.pos = 0
            self.open_brackets = {'(', '{', '['}
            self.corresponding_brackets = {'(': ')', '{': '}', '[': ']'}

        def is_valid(self) -> bool:
            """文字列全体が有効な構文かチェック"""

            # Groupの解析を開始
            if not self.parse_group():
                return False

            # 解析後、文字列が過不足なく消費されたかを確認
            return self.pos == len(self.s)

        def parse_group(self) -> bool:
            """
            文法（EBNF記法）:
            Group = { "(" {Group} ")" | "{" {Group} "}" | "[" {Group} "]" }
            """

            # --- { ... } の繰り返し部分 ---
            # 次の文字が開き括弧である限り、ループを続ける
            while self.pos < len(self.s) and self.s[self.pos] in self.open_brackets:

                # --- "(" {Group} ")" などの部分 ---
                open_bracket = self.s[self.pos]
                close_bracket = self.corresponding_brackets[open_bracket]
                self.pos += 1  # 開き括弧を消費

                # --- 内側の {Group} の解析 ---
                # 内側のグループを解析するために、再帰的にparse_group関数を呼び出す（部下に処理を投げるイメージ）
                # この呼び出しは、内側の0回以上の繰り返しを処理
                if not self.parse_group():
                    return False

                # 閉じ括弧を確認
                if self.pos >= len(self.s) or self.s[self.pos] != close_bracket:
                    return False
                self.pos += 1  # 閉じ括弧を消費

            # ループが正常に終了した場合（または一度も実行されなかった場合）、
            # この階層の解析は成功
            return True
