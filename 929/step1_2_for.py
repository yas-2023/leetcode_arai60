class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def get_base_email(email):
            local_name = []
            domain_name = []
            for char_ in email:

                if local_name and local_name[-1] == "@":
                    # for domain_name
                    domain_name.append(char_)
                elif local_name and local_name[-1] == "+":
                    # for local_name, skip +
                    if char_ == "@":
                        local_name.pop()  # +の削除
                        local_name.append(char_)
                else:
                    # for local_name
                    if char_ != ".":
                        local_name.append(char_)
                base_email = "".join(local_name) + "".join(domain_name)
            return str(base_email)

        unique_addresses = set()
        for email in emails:
            base_email = get_base_email(email)
            unique_addresses.add(base_email)
        return len(unique_addresses)
