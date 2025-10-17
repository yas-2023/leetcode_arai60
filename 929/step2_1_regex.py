import re
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # 1. local（@/+前）と domain（@後）をグループ化してキャプチャ
        pattern = re.compile(r"^([^@\+]+)\+*[^@]*@(.+)$")
        unique_addresses = set()

        for email in emails:
            match = pattern.match(email)
            if not match:
                # 万一フォーマット不正ならスキップ
                continue

            local, domain = match.groups()
            # local部を加工
            local = re.sub(r"\.", "", local)

            normalized_email = f"{local}@{domain}"
            unique_addresses.add(normalized_email)

        return len(unique_addresses)
