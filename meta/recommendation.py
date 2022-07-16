'''
table
ts, item_id, country_id

90 countries 

US: [(phone, 10), (tv, 9), (headset, 5), (book, 1)] (max 100)
MX: [(firework, 13), (book, 10), (tv, 3), (phone, 1)]
.....

M countries
N unique items

'''

#100K qps

from collections import defaultdict
import heapq
from typing import List

class Recommdation: 
    def __init__(self, data):
        self.data = data

    def recommend_v1(self, country_id:str, K: int)->List[str]:
        return [item_id for item_id, count in self.data[country_id][:K]]

    def quickselect(lst, k):
        pass

    def recommend_v2(self, country_ids:list, K:int)->List[str]:
        result_map=defaultdict(int)
        for country in country_ids:
            for item, count in self.data[country]:
                result_map[item] += count
        
        return [item_id for item_id, count in sorted(result_map.items(), key=lambda x:-x[1])[:K]]

        # heap = []
        # for item_id, count in result_map.items():
        #     heapq.heappush(heap, (count, item_id))
        #     if len(heap) > K:
        #         heapq.heappop(heap)
        
        # return [item_id for count, item_id in heap]


#time complexity: O(NlogK) vs O(NlogN)
#space complexity: O(N)

hourly_metadata = {
    "US": [('phone', 10), ('tv', 6), ('headset', 5), ('book', 4)],
    "MX": [('firework', 10), ('ticket', 5), ('tv', 4), ('book', 4)],
    "CN": [('engine', 8), ('ticket', 5), ('player', 3), ('book', 4), ('tv', 1)]
}

r = Recommdation(hourly_metadata)

print(r.recommend_v2(["US", "MX", "CN"], 2))