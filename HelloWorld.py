def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    roman_map = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    roman_numeral = ''
    print(roman_map.items())
    print("roman_map", roman_map)
    
    for value, numeral in sorted(roman_map.items(), reverse=False):
        # cleprint("value", value, "numeral", numeral)
        while num >= value:
            roman_numeral += numeral
            num -= value
    return roman_numeral

intToRoman(150)