class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Get the lengths of the two strings
        n = len(haystack)
        m = len(needle)

        # Iterate through the haystack
        # We only need to check up to the point where a full 'needle' can still fit.
        # The loop runs from index 0 up to (n - m) loops.
        for i in range(n - m + 1):
            # Check if the substring of haystack starting at index i and
            # of length m (the length of needle) is equal to needle.
            # This simulates the "sliding window" comparison.
            if haystack[i:i + m] == needle:
                # If a match is found, return the starting index i
                return i

        # If the loop completes without finding a match, the needle is not in the haystack
        return -1