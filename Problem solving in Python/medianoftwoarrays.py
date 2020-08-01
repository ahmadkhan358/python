class Solution:
    def medianoftwoarrays(self, arr1, arr2):
        newArr = arr1 + arr2

        newArr.sort()

        length = len(newArr)

        if length % 2 == 0:
            return (newArr[int(length / 2 - 1)] + newArr[int(length / 2)])/2
        else:
            return newArr[int(length / 2)]

if __name__ == "__main__":
    sol = Solution()
    x = sol.medianoftwoarrays([1,2], [88])
    print(x)