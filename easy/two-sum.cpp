#include <unordered_map>
#include <vector>
#include <iostream>
#include <cassert>

std::vector<int> twoSum(std::vector<int>& nums, int target) {
    std::unordered_map<int, int> sum_check;
    for (int i = 0; i < nums.size(); ++i) {
        auto it = sum_check.find(nums[i]);
        if (it != sum_check.end()) {
            return {it->second, i};
        }
        sum_check[target - nums[i]] = i;
    }
    return {};
}

int main() {
    // Test 1
    {
        std::vector<int> nums = {3, 3};
        int target = 6;
        std::vector<int> result = twoSum(nums, target);
        std::vector<int> expected = {0, 1};
        assert(result == expected);
		std::cout << "Test 1 passes\n";
    }

    // Test 2
    {
        std::vector<int> nums = {3, 2, 4};
        int target = 6;
        std::vector<int> result = twoSum(nums, target);
        std::vector<int> expected = {1, 2};
        assert(result == expected);
		std::cout << "Test 2 passes\n";
    }

    // Test 3
    {
        std::vector<int> nums = {2, 7, 11, 15};
        int target = 9;
        std::vector<int> result = twoSum(nums, target);
        std::vector<int> expected = {0, 1};
        assert(result == expected);
		std::cout << "Test 3 passes\n";
    }

    return 0;
}


