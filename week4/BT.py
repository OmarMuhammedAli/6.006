class Binary_Node:
    def __init__(A, data):
        A.data = data
        A.left = None
        A.right = None
        A.parent = None

    # Traversal methods
    def subtree_itr(A, order='inorder'):
        if order == "preorder":
            yield from A.preorder_itr()
        elif order == "inorder":
            yield from A.inorder_itr()
        elif order == "postorder":
            yield from A.postorder_itr()
        return None
    
    def preorder_itr(A):
        yield A
        if A.left:
            yield from A.left.preorder_itr()
        if A.right:
            yield from A.right.preorder_itr()
    
    def inorder_itr(A):
        if A.left:
            yield from A.left.inorder_itr()
        yield A
        if A.right:
            yield from A.right.inorder_itr()

    def postorder_itr(A):
        if A.left:
            yield from A.left.postorder_itr()
        if A.right:
            yield from A.right.postorder_itr()
        yield A

    #Tree Navigation
    # All methods are based on the inorder traversal
    def subtree_min(A):
        return A.left.subtree_min() if A.left else A
    
    def subtree_max(A):
        return A.right.subtree_max() if A.right else A

    def successor(A):
        if A.right:
            return A.right.subtree_min()
        parent = A.parent
        while parent and A == parent.right:
            A = parent
            parent = A.parent
        return parent
    
    def predecessor(A):
        if A.left:
            return A.left.subtree_max()
        parent = A.parent
        while parent and A == parent.left:
            A = parent
            parent = A.parent
        return parent

    def insert_before(A, B):
        if A.left:
            A.left.subtree_max().right, B.parent = B, A.left.subtree_max()
        else:
            A.left, B.parent = B, A
    
    def insert_after(A, B):
        if A.right:
            A.right.subtree_min().left, B.parent = B, A.right.subtree_min()
        else:
            A.right, B.parent = B, A
    
    def subtree_delete(A):
        print(f'parent: {A.parent.data}' if A.parent else 'parent: None')
        if A.left or A.right:
            B = A.predecessor() if A.left else A.successor()
            A.data, B.data = B.data, A.data
            return B.subtree_delete()
        
        if A.parent:
            print(f'A.data = {A.data}')
            if A.parent.left == A:
                A.parent.left = None
            else:
                A.parent.right = None
        return A
    
    def print_subtree(A, order='inorder'):
        for i in A.subtree_itr(order):
            print(i.data, end=' ')
        print()

class Binary_Tree:
    def __init__(T, Node_Type=Binary_Node):
        T.root = None
        T.Node_Type = Node_Type
        T.size = 0
    
    def __len__(T):
        return T.size
    
    def __iter__(T):
        if T.root:
            yield from T.root.subtree_itr()
    
    def build(self, data):
        A = [item for item in data]
        def build_subtree(A, i, j):
            c = (i+j)//2
            root = self.Node_Type(A[c])
            if i < c:
                root.left = build_subtree(A, i, c-1)
                root.left.parent = root
            if c < j:
                root.right = build_subtree(A, c+1, j)
                root.right.parent = root
            return root
        self.root = build_subtree(A, 0, len(A)-1)
        self.size = len(A)
    
def main():
    # root = Binary_Node(10)
    # root.left = Binary_Node(6, parent=root)
    # root.right = Binary_Node(14, parent=root)
    # root.left.left = Binary_Node(4, parent=root.left)
    # root.left.right = Binary_Node(8, parent=root.left)
    # root.right.left = Binary_Node(12, parent=root.right)
    # root.right.right = Binary_Node(16, parent=root.right)
    # root.print_subtree()
    # print(root.right.left.subtree_delete().data)
    # print('\nafter deletion: ')
    # root.print_subtree()
    
    # print(f'\nmin: {root.subtree_min().data}')
    # print(f'max: {root.subtree_max().data}')
    # print(f'successor: {root.successor().data}')
    # print(f'predecessor: {root.predecessor().data}')
    tree = Binary_Tree()
    tree.build([1,2,3,4,5,6,7,8,9,10])
    for i in tree:
        print(i.data, end=' ')
if __name__ == '__main__':
    main()