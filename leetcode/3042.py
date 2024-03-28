class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        ans = 0
        for i in range(len(words) - 1):
            for j in range(i+1,len(words)):
                if len(words[i]) > len(words[j]):
                    continue
                else:
                    if words[j][0:len(words[i])] == words[i] and words[j][len(words[j])-len(words[i]):] == words[i]:
                        ans += 1
        return ans
a = Solution()
print(a.countPrefixSuffixPairs(["a","aba","ababa","aa"]))

