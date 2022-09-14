from queue import PriorityQueue

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f'{self.val} -> {None if not self.next else self.next.val}'

class Solution:
    def list_to_list_node(self, list):
        if len(list) == 0:
            return None
        if len(list) == 1:
            return ListNode(val = list[0])
        node = ListNode(val = list[0])
        node.next = self.list_to_list_node(list[1:])
        return node

    def mergeKLists(self, lists):
        res = []
        def fill_pq(PQ, heads):
            for i in range(len(heads)):
                PQ.put((heads[i].val, i))
                heads[i] = heads[i].next

        PQ = PriorityQueue(maxsize=len(lists))
        heads = [node for node in lists]
        fill_pq(PQ, heads)

        while not PQ.empty():
            val, index = PQ.get()
            res.append(val)
            if heads[index]:
                PQ.put((heads[index].val, index))
                heads[index] = heads[index].next
        
        return self.list_to_list_node(res)
    
    def print_linked_list(self, node):
        temp = node
        while temp:
            print(temp)
            temp = temp.next
    
def main():
    s = Solution()
    
    example_input = [s.list_to_list_node([1, 5, 9, 14]), 
                     s.list_to_list_node([2, 3, 4, 8]), 
                     s.list_to_list_node([5, 6, 7, 9, 15])]

    res = s.mergeKLists(example_input)
    
    s.print_linked_list(res)

main()