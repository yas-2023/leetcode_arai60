from typing import List
import re


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_addresses = set()
        for email in emails:
            regex_pattern = re.compile("(^[^\+@]+)\+*[^@]*@(.+)$")
            match = regex_pattern.match(email)
            if not match:
                continue
            local, domain = match.groups()
            local = local.replace(".", "")
            normalized_email = f"{local}@{domain}"
            unique_addresses.add(normalized_email)
        return len(unique_addresses)
