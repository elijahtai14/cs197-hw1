class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f'ListNode {self.val} pointing to {None if not self.next else self.next.val}'

class Solution:
    def mergeKLists(self, lists):
        pass

def list_to_list_node(list):
    if len(list) == 0:
        return None
    if len(list) == 1:
        return ListNode(val = list[0])
    node = ListNode(val = list[0])
    node.next = list_to_list_node(list[1:])
    return node

def print_linked_list(node):
    temp = node
    while temp:
        print(temp)
        temp = temp.next
    
def main():
    s = Solution()

    example_input = [list_to_list_node([1, 5, 9, 14]), 
                     list_to_list_node([2, 3, 4, 8]), 
                     list_to_list_node([5, 6, 7, 9, 15])]

    print_linked_list(example_input[2])

    res = s.mergeKLists(example_input)
    print_linked_list(res)

main()