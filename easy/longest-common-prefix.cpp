#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>

bool is_common_prefix(const std::vector<std::string>& strs, int length) {
    std::string prefix = strs[0].substr(0, length);
    for (const auto& s : strs) {
        if (s.substr(0, length) != prefix) {
            return false;
        }
    }
    return true;
}

std::string longestCommonPrefix(const std::vector<std::string>& strs) {
    if (strs.empty()) {
        return "";
    }

    int min_length = std::min_element(strs.begin(), strs.end(),
                                      [](const std::string& a, const std::string& b) {
                                          return a.size() < b.size();
                                      })->size();

    int low = 1, high = min_length;
    if (is_common_prefix(strs, min_length)) {
        return strs[0].substr(0, min_length);
    }
    while (low <= high) {
        int mid = (low + high) / 2;
        if (is_common_prefix(strs, mid)) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    return strs[0].substr(0, (low + high) / 2);
}

int main() {
    // Test 1
    assert(longestCommonPrefix({"ab", "a"}) == "a");

    // Test 2
    assert(longestCommonPrefix({"dog", "racecar", "car"}) == "");

    // Test 3
    assert(longestCommonPrefix({"flower", "flow", "flight"}) == "fl");

    std::cout << "All tests passed successfully.\n";
    return 0;
}

