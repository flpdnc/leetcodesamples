#include <iostream>
#include <unordered_map>
#include <string>
#include <cassert>

int romanToInt(std::string s) {
    std::unordered_map<char, int> SYMBOLS = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000},
    };

    int total = 0;

    for (int i = 0; i < s.length(); ++i) {
        if (i + 1 < s.length() && SYMBOLS[s[i]] < SYMBOLS[s[i + 1]]) {
            total -= SYMBOLS[s[i]];
        } else {
            total += SYMBOLS[s[i]];
        }
    }

    return total;
}

int main() {
    // Test 1
    assert(romanToInt("III") == 3);

    // Test 2
    assert(romanToInt("LVIII") == 58);

    // Test 3
    assert(romanToInt("MCMXCIV") == 1994);

    std::cout << "All tests passed successfully.\n";
    return 0;
}

