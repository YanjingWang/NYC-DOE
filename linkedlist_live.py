class ListNode:
    def __init__(self, val=0, next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

  #operations
  # head, tail, add, remove, traverse, search, isEmpty, size
  # head = head.next --> pointer to the next node
  # basic two operations: 
  # head.next = new_node  --> pointer to the another node
  # when no pointer to the node, it will be garbage collected

  #add head, tail, middle   int: - + infinate

  #insert 5 to linkedlist 1->2->3->4->6
    # def insert(self,head, data):
    #     new_node = ListNode(data)
    #     if head is None:
    #         head = new_node
    #     else:
    #         cur = head
    #         while cur.next is not None:
    #             cur < data
    #             cur = cur.next
    #         cur.next = new_node
    #     return head
    def insertNode(self,head,val):
        #create a dummy node, dummy.next = head
        #dummy: dummy.next always points to the last node whose value is smaller than val
        #dummy: easy to handle the special case that the head = null
        #using dummy wwe don't need to use if else
        dummy = ListNode(float('-inf'))
        dummy.next = head
        cur_Node = dummy
        #jusify the linkedlist is done or not and find the last node whose value is smaller than val
        while cur_Node.next and cur_Node.next.val <= val:
            cur_Node = cur_Node.next
        #insert the new node between cur_Node and cur_Node.next
        new_Node = ListNode(val) #create a new node 5
        new_Node.next = cur_Node.next #5->6
        cur_Node.next = new_Node #4->5
        return dummy.next

    #how to traverse a linkedlist
    def traverse(self,head):
        cur = head
        while cur is not None:
            print(cur.val, end=' ')
            cur = cur.next
        print()
    def removeElements(self,head,val):
        dummy = ListNode(float('-inf'))
        dummy.next = head
        cur_Node = dummy
        while cur_Node.next:
            if cur_Node.next.val == val:
                cur_Node.next = cur_Node.next.next
            else:
                cur_Node = cur_Node.next
        return dummy.next
    def middleNode(self,head):
        if head is None:
            return None
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return print(slow.val)
    
    def getlength(self,head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def rorateRight(self,head,k): #hard
        if head is None:
            return None
        dummy = ListNode(float('-inf'))
        dummy.next = head

        length = self.getlength(head)
        k = k % length

        ahead = dummy #k steps ahead of behind, ahead is 3
        for i in range(k):
            ahead = ahead.next
        behind = dummy #behind is 1
        while ahead.next:
            ahead = ahead.next
            behind = behind.next
        #rotate
        ahead.next = dummy.next
        dummy.next = behind.next
        behind.next = None

        return dummy.next




#test case
node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(6)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

test = ListNode()
test.insertNode(node_1,5)
test.traverse(node_1)


#test case
node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(3)
node_5 = ListNode(6)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

test = ListNode()
test.removeElements(node_1,3)
test.traverse(node_1)


#test case
node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(6)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

test = ListNode()
test.middleNode(node_1)

#test case
node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(6)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

test = ListNode()
test.rorateRight(node_1,2)
test.traverse(node_1)





