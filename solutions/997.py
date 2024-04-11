from collections import defaultdict


class Solution:
    """
    We can use a hashmap to keep track of the number of people trusts a person.
    A person who has n-1 number of people trusting hiim/her means that this
    person could potentially be the town judge. A set to keep track of people
    who trust another person can also be used because a judge wouldn't be in
    this set and doesn't trust anyone. Together, a judge is someone who has n-1
    people trusting them and does not exist in the set of people who trusts
    someone else in the town.

    Time: O(n)
    Space: O(n)
    """

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # edge case where only 1 person in this town doesn't trust anyone
        if not trust and n == 1:
            return 1

        # edge case where no one trusts anyone but there is more than 1 person
        if not trust and n > 1:
            return -1

        # number of people who trust this person
        incomingTrust = defaultdict(int)
        # a person who trusts someone else - the judge doesn't trust anyone
        trustsSomeone = set()

        for a, b in trust:
            incomingTrust[b] += 1
            trustsSomeone.add(a)

        for k, v in incomingTrust.items():
            # if everyone else in the town trusts this person (n-1) but this
            # person doesn't trust anyone else
            if v == n - 1 and k not in trustsSomeone:
                return k

        return -1
