class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = list(Counter(nums).items())
        print(count)
        count.sort(key=lambda pair: pair[1], reverse=True)

        ans=[]
        for i in range(k):
            ans.append(count[i][0])

        return ans