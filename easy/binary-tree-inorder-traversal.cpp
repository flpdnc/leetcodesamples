#include <memory>
#include <vector>
#include <stack>
#include <cassert>
#include <iostream>

class TreeNode {
public:
    int val;
    std::unique_ptr<TreeNode> left;
    std::unique_ptr<TreeNode> right;

    TreeNode(int val = 0, TreeNode* left = nullptr, TreeNode* right = nullptr)
        : val(val), left(left), right(right) {}
};

std::vector<int> inorderTraversal(TreeNode* root) {
    std::vector<int> res;
    std::stack<TreeNode*> stack;
    TreeNode* curr = root;

    while (curr != nullptr || !stack.empty()) {
        while (curr != nullptr) {
            stack.push(curr);
            curr = curr->left.get();
        }
        curr = stack.top();
        stack.pop();
        res.push_back(curr->val);
        curr = curr->right.get();
    }

    return res;
}

int main() {
    // Test 1
    {
        auto root = std::make_unique<TreeNode>(1, nullptr, new TreeNode(2, new TreeNode(3), nullptr));
        auto result = inorderTraversal(root.get());
        std::vector<int> expected = {1, 3, 2};
        assert(result == expected);
		std::cout << "Test 1 passes\n";
    }

    // Test 2
    {
        TreeNode* root = nullptr;
        auto result = inorderTraversal(root);
        std::vector<int> expected = {};
        assert(result == expected);
		std::cout << "Test 2 passes\n";
    }

    // Test 3
    {
        auto root = std::make_unique<TreeNode>(1);
        auto result = inorderTraversal(root.get());
        std::vector<int> expected = {1};
        assert(result == expected);
		std::cout << "Test 3 passes\n";
    }

    // Test 4
    {
        auto root = std::make_unique<TreeNode>(1, new TreeNode(2), nullptr);
        auto result = inorderTraversal(root.get());
        std::vector<int> expected = {2, 1};
        assert(result == expected);
		std::cout << "Test 4 passes\n";
    }

    // Test 5
    {
        auto root = std::make_unique<TreeNode>(2, new TreeNode(3, new TreeNode(1), nullptr), nullptr);
        auto result = inorderTraversal(root.get());
        std::vector<int> expected = {1, 3, 2};
        assert(result == expected);
		std::cout << "Test 5 passes\n";
    }

    return 0;
}
