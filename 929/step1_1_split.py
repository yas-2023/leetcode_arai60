class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_addresses = set()
        for email in emails:
            local_name = email.split("@")[0]
            local_name = local_name.split("+")[0]
            local_name = local_name.replace(".", "")
            domain_name = email.split("@")[1]
            unique_addresses.add(local_name + "@" + domain_name)
            print(unique_addresses)
        return len(unique_addresses)
