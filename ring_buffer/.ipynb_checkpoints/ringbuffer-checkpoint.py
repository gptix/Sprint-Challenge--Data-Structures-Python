"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        #Call: ListNode(value, prev=None, next=None)
        if not self.head:
#             print("no head exists")
            self.head = ListNode(value)
            print("Made a node.")
            print(f'head: {self.head}')
            self.tail = self.head
            print(f'tail: {self.tail}')
            print(f'head next: {self.head.next}')
        else:
#             print("head exists")
            old_head = self.head
            print(f'old_head: {old_head}')
            self.head = ListNode(value, next = old_head)
            self.head.next.prev = self.head
            print(f'head after change: {self.head}')
            self.head.next = old_head
            print(f'head.next after change: {self.head.next}')

            old_head.prev = self.head
            print(f'old first nodes new prev: {old_head.prev}')
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # print(f'length = {len(self)}')
        if len(self) == 0: # list is empty
            return None

        else:
            val = self.head.value

            if len(self) == 1: # make list empty
                self.head = None
                self.tail = None
            
            else:
                self.head = self.head.next
                self.head.next.prev = None
        
            self.length -= 1
            return val
    
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if not self.tail:
            self.tail = ListNode(value)
            self.head = self.tail
        else:
            old_tail = self.tail
            self.tail = ListNode(value, prev=old_tail)
            old_tail.next = self.tail
        self.length += 1
        return self.tail
            
    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # print(f'length = {len(self)}')
        if len(self) == 0: # list is empty
            return None

        else:
            val = self.tail.value

            if len(self) == 1: # make list empty
                self.head = None
                self.tail = None
            
            else:
                self.tail = self.tail.prev
                self.tail.prev.next = None
        
            self.length -= 1
            return val
        
    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if self.length <= 1:
            return "No action required"
        
        if node.prev:
            node.prev.next = node.next
        else: # it must be the head
            self.head = node.next
            
        if node.next:
            node.next.prev = node.prev
        else: # it must be the tail
            self.tail = node.prev

        self.length -=1  
        self.add_to_head(node.value)
        
    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if self.length <= 1:
            return "No action required"
        
        if node.next:
            node.next.prev = node.prev
        else: # it must be the tail
            self.tail = node.prev
            
        if node.prev:
            node.prev.next = node.next
        else: # it must be the head
            self.head = node.next

        self.length -= 1    
        self.add_to_tail(node.value)
        
        
    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.length == 0: # empty list
            return "No action required"
        
        elif self.head == self.tail: # one element
            self.head = None
            self.tail = None
        
        elif self.head == node: # multi-element
            self.head = self.head.next            
            self.head.prev = None
            
        elif self.tail == node: # multi-element
            self.tail = self.tail.prev       
            self.tail.next = None
            
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            
        self.length -= 1

            
      
    """Returns the highest value currently in the list"""
    def get_max(self):
        list_length = self.length
        
        if list_length == 0: # empty list
            return None
        
        else: 
            max_val = self.head.value
            if list_length == 1:
                return max_val
            
            else:
                current_node = self.head
                for i in range (1, list_length):
                    current_node = current_node.next
                    new_val = current_node.value
                    if new_val > max_val:
                        max_val = new_val
                return max_val


class RingBuffer(DoublyLinkedList):
    def __init__(self, capacity=2):
        super().__init__()
        self.capacity = capacity
        
    def append(self, value):
        print(f'\nself.head {self.head}')
        self.add_to_head(value)
        print(f'self.head {self.head}')
        if self.length > self.capacity:
            self.remove_from_tail()
            
    def get(self):
        if not self.head:
            return None
        else:
            current_node = self.head
            return_list = []
            while current_node:
                return_list.append(current_node)
                current_node = current_node.next
            return return_list