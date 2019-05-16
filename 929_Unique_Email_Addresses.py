class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_num = set()
        for email in emails:
            local_name,domain_name = email.split('@')
            local_name = local_name.split('+')[0]
            local_name = local_name.replace('.','')
            email = local_name + '@' + domain_name
            email_num.add(email)
        return len(email_num)