class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse= True)
        ans = happiness[0]
        count = 1
        k -= 1
        for i in range(1,len(happiness)):
            if k <= 0:
                break
            else:
                if happiness[i] - count > 0:
                    ans += happiness[i] - count
                    count += 1
                    k -= 1
                else: 
                    break
        return ans
        
