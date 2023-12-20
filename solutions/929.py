class Solution:
    '''
    Create a set of the unique emails that were created. Perform string parsing as needed.

    Time: O(n*k)
    Space: O(n*k)
    where n is the number of emails and k is the longest email length
    '''
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq = set()
        for email in emails:
            local, domain = email.split("@")
            newLocal = ""
            for letter in local:
                if letter == "+":
                    break
                elif letter != ".":
                    newLocal += letter

            add = newLocal + "@" + domain
            uniq.add(add)
        return len(uniq)