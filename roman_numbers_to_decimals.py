"""
How To Convert Roman Numbers to Decimals?

Remember that the base numbers are not the numbers that are used by the Romans as they have count values such as I: 1, V: 5, X: 10, C: 100, D: 500, M: 1000, etc.

1. Work your way through the string of Roman numerals from left to right, examining two adjacent characters at a time.
If you want then you can also specify that the direction of loops, but it does not matter as long as the comparisons are implemented accordingly.

2. If the value on the left is higher than the value on the right, then subtract the count at that position from the final value. Otherwise, just add it.

3. Once the process is complete, the final value is the decimal value equivalent of the roman number.
"""


tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    # Sprcify more numbers if you wish
}

def RomanNumeralToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral) - 1):
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]
    sum += tallies[romanNumeral[-1]]
    return sum

roman_numeral = input("Enter the Roman Number: ")
print(RomanNumeralToDecimal(romanNumeral=roman_numeral))