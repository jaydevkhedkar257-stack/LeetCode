class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        """Pushes element x to the back of queue."""
        self.in_stack.append(x)

    def pop(self) -> int:
        """Removes the element from the front of queue and returns it."""
        self._move_in_to_out()
        return self.out_stack.pop()

    def peek(self) -> int:
        """Get the front element."""
        self._move_in_to_out()
        return self.out_stack[-1]

    def empty(self) -> bool:
        """Returns whether the queue is empty."""
        return not self.in_stack and not self.out_stack

    def _move_in_to_out(self) -> None:
        """Helper to transfer elements from in_stack to out_stack if needed."""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())