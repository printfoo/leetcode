"""
Solution for Unique Email Addresses.

Idea:
"""

# solution
class Solution:
    def numUniqueEmails(self, emails: "List[str]") -> "int":
        return len({e.split("@")[0].split("+")[0].replace(".", "") + e.split("@")[1] for e in emails})

# Main.
if __name__ == "__main__":
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    print(Solution().numUniqueEmails(emails))
