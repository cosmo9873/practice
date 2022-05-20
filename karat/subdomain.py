# https://leetcode.com/problems/subdomain-visit-count/solution/

import collections
from collections import Counter

class Solution:
    def subdomainVisits(self, cpdomain):
        ans=collections.Counter()
        for domain in cpdomain:
            count, domain=domain.split()
            frags=domain.split('.')
            for i in range(len(frags)):
                ans[".".join(frags[i:])]+= int(count)

        return ["{} {}".format(ct, domain) for domain, ct in ans.items()]


cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
a=Solution()
print(a.subdomainVisits(cpdomains))
