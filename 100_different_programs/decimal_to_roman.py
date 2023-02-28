def decimal_to_roman(decimal):
    # Define a mapping of decimal values to Roman numerals
    roman_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    # Initialize an empty string to hold the Roman numeral representation
    roman_numeral = ''
    # Loop through the mapping in reverse order
    for value, numeral in sorted(roman_map.items(), reverse=True):
        # Divide the decimal number by the current value and get the integer quotient and remainder
        quotient, decimal = divmod(decimal, value)
        # Add the corresponding Roman numeral to the output string for each quotient
        roman_numeral += numeral * quotient
    return roman_numeral

def send_two_values(value1, value2):
    return (value1, value2)


print(decimal_to_roman(5))
print(decimal_to_roman(6))
print(decimal_to_roman(7))
print(decimal_to_roman(8))

x,y=send_two_values(12,17)
print(x,y)