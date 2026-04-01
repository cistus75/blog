# 노드 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None # 리스트의 시작
        self.tail = None # 리스트의 끝 
        self.node_count = 0 # 노드의 개수

    def append(self, data):
        new_node = Node(data)
        # 리스트가 비어 있는 경우 첫 노드가 시작과 끝이 됨
        if self.node_count == 0:
            self.head = self.tail = new_node
        # 이미 노드가 존재할 경우 현재의 끝 노드의 next를 새 노드에 연결하고 이를 새로운 끝 지점으로 갱신함
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.node_count += 1
    
    # 순회를 통해 노드를 출력함
    def show(self): 
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next
        print("None")
