def longestCommonPrefix(strs: list[str]) -> str:
    """
    Finds the longest common prefix string amongst an array of strings.

    The method uses a vertical scanning approach. It iterates through the 
    characters of the first string, and for each character, it checks if 
    the same character exists at the same position in all other strings.
    The moment a mismatch or the end of a string is encountered, the 
    prefix found so far is returned.
    """
    # Edge case: If the list is empty, there is no common prefix.
    if not strs:
        return ""

    # Choose the first string as the reference for potential prefix length.
    first_string = strs[0]

    # Iterate through the characters of the first string (vertical scan)
    for j in range(len(first_string)):
        char = first_string[j]

        # Iterate through the rest of the strings in the array (horizontal check)
        for i in range(1, len(strs)):
            current_string = strs[i]
            
            # Check two conditions for prefix termination:
            # 1. We have reached the end of the current string (`j == len(current_string)`).
            # 2. The character at the current position does not match (`current_string[j] != char`).
            if j == len(current_string) or current_string[j] != char:
                # The common prefix ends right before the current index `j`.
                return first_string[:j]

    # If the loop completes, the entire first string is the common prefix.
    return first_string

# Example Test Cases:
strs1 = ["flower", "flow", "flight"]
strs2 = ["dog", "racecar", "car"]
strs3 = ["apple", "apricot", "apply"]
strs4 = ["a"]
strs5 = ["", "b"]

print(f"Input: {strs1} -> Output: '{longestCommonPrefix(strs1)}'")
print(f"Input: {strs2} -> Output: '{longestCommonPrefix(strs2)}'")
print(f"Input: {strs3} -> Output: '{longestCommonPrefix(strs3)}'")
print(f"Input: {strs4} -> Output: '{longestCommonPrefix(strs4)}'")
print(f"Input: {strs5} -> Output: '{longestCommonPrefix(strs5)}'")
