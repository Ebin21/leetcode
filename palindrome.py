class Solution(object):
    def isPalindrome(self, x):
        reversed_number = 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # Reverse the second half of the number
        
        while x > reversed_number:
            reversed_number = reversed_number * 10 + x % 10
            x //= 10

        # When the number has an odd number of digits, we can ignore the middle digit by reversed_number/10
        return x == reversed_number or x == reversed_number // 10
        