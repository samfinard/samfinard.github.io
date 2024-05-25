# Stack

## 1. What is a stack?

A stack is a Last In First Out data (LIFO) data structure, meaning the first elements to get removed are the most recently added elements. Imagine a stack of paper which you are continuously adding more paper to. You can only add more paper to the top of the stack, and you can only read the top sheet which is the most recently added sheet. If you want to remove 1 piece of paper it's easiest to remove the top sheet. This is exactly how a stack in Computer Science works.

### 1A. Stack Operations

| Operation | Runtime |
| --------- | ------- |
| **Access top** *(peek)*| $O(1)$ |
| Search | $O(n)$ |
| Deletion | $O(n)$ |
| **Delete top** *(pop)*| $O(1)$ |
| Insertion | $O(n)$ |
| **Insert top** *(push)*| $O(1)$ |

A stack always contains a pointer to its top element. This is why doing operations at the top of a stack take constant time - accessing the top requires $0$ pointer updates while deleting/inserting at the top require $2$ pointer updates. However, operations in arbitrary positions of the stack take $O(n)$ time because stack elements must maintain their linear ordering. By inserting/deleting somewhere in the stack you will have to update the pointers of up to $n$ elements. Searching is no better - you might have to traverse the entire stack to determine if there exists some target element.

### 2. Common real-world applications of stacks

- Undo mechanisms in software
- History of pages visited in web browsers
- Compiler syntax checking of nested parenthesis [[leetcode]](https://leetcode.com/problems/valid-parentheses/description/)
- Expression evaluation and conversion [[leetcode]](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)
- Managing function calls

### 3. Implementation of a stack in C

This implementation of a stack is done with an [array](array.md). Another common implementation is with a linked list.

```c
#define MAX_SIZE 100

typedef struct {
    int arr[MAX_SIZE];
    int top;
} Stack;

void initialize(Stack* stack) {
    stack->top = -1;
}

void push(Stack* stack, int data) {
    if (stack->top == MAX_SIZE - 1;) {
        printf("Stack Overflow");
        return;
    }
    stack->arr[++stack->top] = data;
}

int pop(Stack* stack) {
    if (stack->top == -1;) {
        printf("Stack Underflow");
        return -1;
    }
    return stack->arr[stack->top--];
}

int peek(Stack* stack) {
    if (stack->top == -1;) {
        printf("Stack is empty");
        return -1;
    }
    return stack->arr[stack->top];
}


```

### 4. Advanced applications

- Backtracking and state management
- Monotonic stack
- DFS
