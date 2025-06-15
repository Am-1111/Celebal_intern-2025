# Node class for a singly linked list
class Node:
    def __init__(self, val, next=None): #Constructor to initialize node with value and next   pointer
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Add node to the end of the list - O(n)
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # Display the linked list - O(n)
    def display(self):
        if not self.head:
            print("List is empty.")
            return
        curr = self.head
        elements = []
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(elements))

    # Delete the nth node (1-based index) - O(n)
    def delete_nth_node(self, n):
        if not self.head:
            raise Exception("Cannot delete from an empty list.")
        
        if n <= 0:
            raise IndexError("Index should be 1 or higher.")
        
        if n == 1:
            print(f"Deleting node at position {n} with value {self.head.val}")
            self.head = self.head.next
            return

        curr = self.head
        prev = None
        count = 1

        while curr and count < n:
            prev = curr
            curr = curr.next
            count += 1

        if not curr:
            raise IndexError("Index out of range.")

        print(f"Deleting node at position {n} with value {curr.val}")
        prev.next = curr.next

# Sample test
if __name__ == "__main__":
    ll = LinkedList()
    
    # Append nodes
    ll.append(1)
    ll.append(3)
    ll.append(4)
    ll.append(7)

    print("Initial linked list:")
    ll.display()

    # Delete the 3rd node (value = 4)
    try:
        ll.delete_nth_node(3)
    except Exception as e:
        print(e)

    print("After deleting 3rd node:")
    ll.display()

    # Edge case: Deleting from empty list
    try:
        empty_ll = LinkedList()
        empty_ll.delete_nth_node(1)
    except Exception as e:
        print("Error:", e)

    # Edge case: Deleting with index out of range
    try:
        ll.delete_nth_node(10)
    except Exception as e:
        print("Error:", e)
