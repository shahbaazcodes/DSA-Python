class Solution:

    def is_palindrome(self, s, i=0):
        n = len(s)

        # Base Case: Reached or passed the middle point
        if i >= n // 2:
            return True

        # Non-matching pair found
        if s[i] != s[n - 1 - i]:
            return False

        # Recurse for next pair towards the middle
        return self.is_palindrome(s, i + 1)


# Testing the implementation
obj = Solution()
print(obj.is_palindrome("MADAM"))  # Output: True
print(obj.is_palindrome("RADAR"))  # Output: True
print(obj.is_palindrome("HELLO"))  # Output: False