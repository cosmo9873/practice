# https://www.jianshu.com/p/fdbcba5fe5bc

class Solution():
    def courseOverlap(self, input):
        map=dict()
        for _ in input:
            id,course=_[0],_[1]
            if id in map:
                map[id].append(course)
            else:
                map[id]=[course]

        # for course in map:
        #     l=len(map[course])
        #     for i in range(l):
        #         for j in range(i+1,l):
        #             print(map[course][i], map[course][j], course)

        # print(map)

        slist=list(map.keys())

        for i in range(len(slist)):
            for j in range(i+1, len(slist)):
                overlap=[]
                for course1 in map[slist[i]]:
                    for course2 in map[slist[j]]:
                        if course1 == course2:
                            overlap.append(course1)
                print(slist[i], slist[j],overlap)


student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]

# Sample Output (pseudocode, in any order):
# find_pairs(student_course_pairs_1) =>
# {
#   [58, 17]: ["Software Design", "Linear Algebra"]
#   [58, 94]: ["Economics"]
#   [58, 25]: ["Economics"]
#   [94, 25]: ["Economics"]
#   [17, 94]: []
#   [17, 25]: []
# }

student_course_pairs_2 = [
  ["42", "Software Design"],
  ["0", "Advanced Mechanics"],
  ["9", "Art History"],
]

# Sample output:
# find_pairs(student_course_pairs_2) =>
# {
#   [0, 42]: []
#   [0, 9]: []
#   [9, 42]: []
# }

a=Solution()
a.courseOverlap(student_course_pairs_2)