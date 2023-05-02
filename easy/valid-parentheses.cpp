#include <iostream>
#include <stack>
#include <string>
#include <cassert>

bool isValid(std::string s) {
    std::stack<char> open_order;

    for (char& i : s) {
        if (i == '(' || i == '{' || i == '[') {
            open_order.push(i);
        } else if (i == ')' || i == '}' || i == ']') {
            if (open_order.empty()) {
                return false;
            }
            char match = open_order.top();
            open_order.pop();
            if ((i == ')' && match != '(') ||
                (i == '}' && match != '{') ||
                (i == ']' && match != '[')) {
                return false;
            }
        }
    }

    return open_order.empty();
}

int main() {
    // Test 1
    assert(isValid("()") == true);

    // Test 2
    assert(isValid("()[]{}") == true);

    // Test 3
    assert(isValid("(]") == false);

    std::cout << "All tests passed successfully.\n";
    return 0;
}

