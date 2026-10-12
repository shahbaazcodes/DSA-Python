class Solution:

    def reverse_array(self, arr, left, right):
        if left >= right:
            return

        # Swap elements at left and right
        arr[left], arr[right] = arr[right], arr[left]

        # RECURSIVE STEP: Move left forward (+1) and right backward (-1)
        self.reverse_array(arr, left + 1, right - 1)


arr = [1, 2, 3, 4, 5]
obj = Solution()
obj.reverse_array(arr, 0, len(arr) - 1)
print(arr)  # Output: [5, 4, 3, 2, 1]