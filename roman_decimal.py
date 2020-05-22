def romanToInteger(s):
    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s_copy = s[::-1]
    val = 0
    i = 0
    while i < len(s_copy):
        if i < len(s) - 1 and T[s_copy[i]] > T[s_copy[i + 1]]:
            val += T[s_copy[i]] - T[s_copy[i + 1]]
            i += 1
        else:
            val += T[s_copy[i]]
        i += 1
    return val


def main():
    roman_val = "XCVII"
    decimal_val = romanToInteger(roman_val)
    print("Roman Number: ", roman_val)
    print("Decimal Number: ", decimal_val)


if __name__ == '__main__':
    main()
