

class Solution():
    def validBadge(self, r):

        holder=set()
        noExit=set()
        noEntry=set()

        for i, a in r:
            if a == 'exit':
                if i not in holder:
                    noEntry.add(i)
                else:
                    holder.remove(i)

            if a == 'enter':
                if i in holder:
                    noExit.add(i)
                else:
                    holder.add(i)

        return list(holder.union(noExit)),list(noEntry)

badge_records = [
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Paul",     "enter"],
  ["Curtis",   "enter"],
  ["Paul",     "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
]

a=Solution()
print(a.validBadge(badge_records))

