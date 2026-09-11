
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value})"

def main():
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)

    print("Root:", root.value)
    print("Left child:", root.left.value)
    print("Right child:", root.right.value)

if __name__ == "__main__":
    main()