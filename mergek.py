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
        
        head = ListNode(val = list[0])
        cur = head

        for i in range(1, len(list)):
            cur.next = ListNode(val = list[i])
            cur = cur.next
        
        return head
   
    def mergeKLists(self, lists):
        res = []
        def fill_pq(PQ, heads):
            for i in range(len(heads)):
                if not heads[i] is None:
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
        a = self.list_to_list_node(res)
        return a
    
    def print_linked_list(self, node):
        temp = node
        while not temp is None:
            print(temp.val)
            temp = temp.next

class Solution2:
    def list_to_list_node(self, list):
        
        if len(list) == 0:
            return None
        
        head = ListNode(val = list[0])
        cur = head

        for i in range(1, len(list)):
            cur.next = ListNode(val = list[i])
            cur = cur.next
        
        return head

    def mergeKLists_helper(self, PQ, lists, res):
        if PQ.empty():
            return
        
        val, index = PQ.get()
        if not lists[index] is None:
            PQ.put((lists[index].val, index))
            lists[index] = lists[index].next
        
        res.append(val)

        self.mergeKLists_helper(PQ, lists, res)
    
    def mergeKLists(self, lists):
        PQ = PriorityQueue()

        def fill_pq(PQ, lists):
            for i in range(len(lists)):
                if not lists[i] is None:
                    PQ.put((lists[i].val, i))
                    lists[i] = lists[i].next
        fill_pq(PQ, lists)

        res = []
        self.mergeKLists_helper(PQ, lists, res)
        return self.list_to_list_node(res)    

    def print_linked_list(self, node):
        temp = node
        while not temp is None:
            print(temp.val)
            temp = temp.next    
    
def main():
    s = Solution2()
    
    example_input = [s.list_to_list_node([0, 2, 5])]

    r = s.mergeKLists(example_input)
    
    s.print_linked_list(r)

main()