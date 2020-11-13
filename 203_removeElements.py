class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements_203(head, val):

    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    while head.val == val:
        head = head.next

    node = pre = head
    while node.next!=None:

        if node.val == val:
            pre.next = node.next
            node = pre.next
            node.next = None

        else:
            pre = node
            node = node.next

    if node.val == val:
        pre.next = None

    return head
