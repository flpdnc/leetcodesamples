class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def list_form(self):
        res = [self.val]
        curr = self.next
        while curr is not None:
            res.append(curr.val)
            curr = curr.next
        return res


def addTwoNumbers(l1, l2):
    l1_curr = l1
    l2_curr = l2
    carry_holder = 0
    new_val = 0
    res = ListNode()
    pointer = res
    while l1_curr is not None or l2_curr is not None:
        if l1_curr is None:
            l1_val = 0
            l1_next = None
        if l2_curr is None:
            l2_val = 0
            l2_next = None
        if l1_curr is not None:
            l1_val = l1_curr.val
            l1_curr = l1_curr.next
        if l2_curr is not None:
            l2_val = l2_curr.val
            l2_curr = l2_curr.next
        new_val = (l1_val + l2_val + carry_holder) % 10
        carry_holder = (l1_val + l2_val + carry_holder) // 10 
        pointer.next = ListNode(val=new_val)
        pointer = pointer.next
    if carry_holder:
        pointer.next = ListNode(val=1)

    return res.next.list_form()




import unittest

class TestAddTwoNumbers(unittest.TestCase):

    def test_first_sample(self):
        l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None))) 
        l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))
        expected = ListNode(val=7, next=ListNode(val=0, next=ListNode(val=8, next=None)))
        self.assertEqual(addTwoNumbers(l1, l2), expected.list_form())

    def test_second_sample(self):
        l1 = ListNode(val=0, next=None) 
        l2 = ListNode(val=0, next=None)
        expected = ListNode(val=0, next=None)
        self.assertEqual(addTwoNumbers(l1, l2), expected.list_form())

    def test_third_sample(self):
        l1 = ListNode(
                val=9,
                next=ListNode(
                    val=9,
                    next=ListNode(
                        val=9,
                        next=ListNode(
                            val=9,
                            next=ListNode(
                                val=9,
                                next=ListNode(
                                    val=9,
                                    next=ListNode(
                                        val=9, 
                                        next=None
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
        l2 = ListNode(
                val=9,
                next=ListNode(
                    val=9,
                    next=ListNode(
                        val=9,
                        next=ListNode(
                            val=9,
                            next=None
                            )
                        )
                    )
                )
        expected = ListNode(
                val=8,
                next=ListNode(
                    val=9,
                    next=ListNode(
                        val=9,
                        next=ListNode(
                            val=9,
                            next=ListNode(
                                val=0,
                                next=ListNode(
                                    val=0,
                                    next=ListNode(
                                        val=0, 
                                        next=ListNode(
                                            val=1,
                                            next=None
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
        self.assertEqual(addTwoNumbers(l1, l2), expected.list_form())

if __name__ == '__main__':
    unittest.main()
