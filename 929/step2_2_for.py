from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def normalize_email(address: str) -> str:
            local_chars = []
            domain_chars = []
            in_domain = False
            plus_seen = False

            for char_ in address:
                if in_domain:
                    domain_chars.append(char_)
                    continue

                if char_ == '@':
                    in_domain = True
                    domain_chars.append('@')
                elif plus_seen:
                    # ローカル部で+以降はスキップ
                    continue
                elif char_ == '+':
                    plus_seen = True
                elif char_ == '.':
                    # ローカル部の.は無視
                    continue
                else:
                    local_chars.append(char_)

            return "".join(local_chars) + "".join(domain_chars)

        unique_addresses = {normalize_email(email) for email in emails}
        return len(unique_addresses)
