class Solution:
    def lengthOfLongestSubstring(self, s):
       n = len(s)
       ans = 0
       j = 0
       m = dict()

       for i in range(n):
           if s[i] in m.keys():
               j = max(m[s[i]], j)
               print("j {}".format(j))
           ans = max(ans, i - j + 1)
           print("ans {}".format(ans))
           m[s[i]] = i + 1

           print(m)

       return ans


if __name__ == "__main__":
    sol = Solution()
    x = sol.lengthOfLongestSubstring("abcabcdeagbb")
    print(x)