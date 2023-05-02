#include <iostream>
#include <stack>
#include <vector>
#include <cassert>

class TreeNode {
public:
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int val = 0, TreeNode* left = nullptr, TreeNode* right = nullptr)
        : val(val), left(left), right(right) {}
};

bool isSymmetric(TreeNode* root) {
    if (!root->left && !root->right) {
        return true;
    }
    if ((root->left && !root->right) || (root->right && !root->left)) {
        return false;
    }

    std::vector<std::pair<int, int>> left_res;
    TreeNode* left_curr = root->left;
    std::stack<TreeNode*> left_stack;

    while (left_curr != nullptr || !left_stack.empty()) {
        while (left_curr != nullptr) {
            left_stack.push(left_curr);
            left_curr = left_curr->left;
        }
        left_curr = left_stack.top();
        left_stack.pop();
        left_res.push_back({left_curr->val, left_stack.size()});
        left_curr = left_curr->right;
    }

    std::vector<std::pair<int, int>> right_res;
    TreeNode* right_curr = root->right;
    std::stack<TreeNode*> right_stack;

    while (right_curr != nullptr || !right_stack.empty()) {
        while (right_curr != nullptr) {
            right_stack.push(right_curr);
            right_curr = right_curr->right;
        }
        right_curr = right_stack.top();
        right_stack.pop();
        right_res.push_back({right_curr->val, right_stack.size()});
        right_curr = right_curr->left;
    }

    return right_res == left_res;
}

int main() {
    // Test 1
    {
        TreeNode* root = new TreeNode(
            1,
            new TreeNode(2, new TreeNode(3), new TreeNode(4)),
            new TreeNode(2, new TreeNode(4), new TreeNode(3))
        );
        assert(isSymmetric(root) == true);
        delete root;
    }

    // Test 2
    {
        TreeNode* root = new TreeNode(1);
        assert(isSymmetric(root) == true);
        delete root;
    }

    // Test 3
    {
        TreeNode* root = new TreeNode(
            1,
            new TreeNode(2, new TreeNode(2)),
            new TreeNode(2, new TreeNode(2))
        );
        assert(isSymmetric(root) == false);
        delete root;
    }

    std::cout << "All tests passed successfully.\n";
    return 0;
}

