def romanToInt(s: str) -> int:
    """
    Converts a Roman numeral string (s) to an integer.

    The method iterates through the string, comparing the value of the current
    symbol with the next symbol. If the current value is less than the next,
    it signifies a subtractive case (e.g., IV, XC), and the current value is
    subtracted from the total. Otherwise, the current value is added. The
    value of the final symbol is always added.
    """
    # 1. Define the mapping of Roman symbols to their integer values.
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    n = len(s)

    # 2. Iterate through the string up to the second-to-last character.
    for i in range(n - 1):
        current_symbol = s[i]
        next_symbol = s[i+1]
        
        current_value = roman_map[current_symbol]
        next_value = roman_map[next_symbol]

        # 3. Check for the subtractive rule:
        # If the current symbol's value is less than the next symbol's value,
        # it means this symbol is being subtracted (e.g., 'I' in 'IV').
        if current_value < next_value:
            total -= current_value
        # Otherwise, the value is additive (the usual case).
        else:
            total += current_value

    # 4. Add the value of the last symbol.
    # The last symbol in a valid Roman numeral is always additive.
    total += roman_map[s[n-1]]

    return total

# Example Test Cases:
s1 = "III"
s2 = "LVIII"
s3 = "MCMXCIV"

print(f"Roman '{s1}' -> Integer: {romanToInt(s1)}")
print(f"Roman '{s2}' -> Integer: {romanToInt(s2)}")
print(f"Roman '{s3}' -> Integer: {romanToInt(s3)}")
