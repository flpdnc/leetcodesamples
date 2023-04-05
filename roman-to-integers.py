

def romanToInt(s):
    SYMBOLS = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        }
    s = list(s.upper())
    i = 0
    total = 0

    def check_add(sym, sym_plus):
        if sym == 'I' and sym_plus in ['V','X']:
            return (SYMBOLS[sym_plus] - SYMBOLS[sym]), True
        elif sym == 'X' and sym_plus in ['L','C']:
            return (SYMBOLS[sym_plus] - SYMBOLS[sym]), True
        elif sym == 'C' and sym_plus in ['D','M']:
            return (SYMBOLS[sym_plus] - SYMBOLS[sym]), True
        else:
            return SYMBOLS[sym], False
        
    while i < len(s):
        sym = s[i]
        if (i+1 < len(s)):
            sym_plus = s[i+1]
        else:
            sym_plus = ""
        sum_add, special = check_add(sym, sym_plus)
        total += sum_add

        if special:
            i += 2
        else:
            i += 1

    print(s, total)



romanToInt("III")
romanToInt("LVIII")
romanToInt("MCMXCIV")

