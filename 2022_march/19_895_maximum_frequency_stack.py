"""
895. Maximum Frequency Stack

Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.


Example 1:

Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Explanation
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
"""


class FreqStack:
    def __init__(self):
        # To trace how many occurred
        self.trace_stack = {}
        # To trace items that occurred per occurrence
        # Key = How often it occurred
        # Value = Items that are occurred at key time
        self.per_occurrence = {1: []}
        self.most_frequent = 1

    def push(self, val: int) -> None:
        # Never seen this element, hence initialize them
        if val not in self.trace_stack:
            self.trace_stack[val] = 1
            self.per_occurrence[1].append(val)
        else:
            # This val has been occurred previously, so increase the number of occurrences
            self.trace_stack[val] += 1
            # Check the current most_frequent and this val's frequency to check the most frequent
            self.most_frequent = max(self.most_frequent, self.trace_stack[val])
            # If the current val's frequency exists, we append this val to its frequency's array
            if self.per_occurrence.get(self.trace_stack[val]):
                self.per_occurrence[self.trace_stack[val]].append(val)
            else:
                # Else, this is the first element that occur that that frequency, so initialize an array with its value
                self.per_occurrence[self.trace_stack[val]] = [val]

    def pop(self) -> int:
        # We remove from the most frequency's last item, so from most frequency's array, pop it from there
        val = self.per_occurrence[self.most_frequent].pop()
        # and by removing this item, we know the number of val's occurrence will be reduced by one
        self.trace_stack[val] -= 1

        # If the most_frequent's no longer have any array, means there is nothing to check at this most_frequent
        # Hence, reduce the most frequent by one as well
        if len(self.per_occurrence[self.most_frequent]) == 0:
            self.most_frequent -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# freqStack = FreqStack()
# freqStack.push(4)
# freqStack.push(0)
# freqStack.push(9)
# freqStack.push(3)
# freqStack.push(4)
# freqStack.push(2)
# print(freqStack.pop())
# freqStack.push(6)
# print(freqStack.pop())
# freqStack.push(1)
# print(freqStack.pop())
# freqStack.push(1)
# print(freqStack.pop())
# freqStack.push(4)
# print(freqStack.pop())
# print(freqStack.pop())
# print(freqStack.pop())
# print(freqStack.pop())
# print(freqStack.pop())
# print(freqStack.pop())
# ["FreqStack","push","push","push","push","push","push","pop","push","pop","push","pop","push","pop","push","pop","pop","pop","pop","pop","pop"]
# [[],[4],[0],[9],[3],[4],[2],[],[6],[],[1],[],[1],[],[4],[],[],[],[],[],[]]

freqStack = FreqStack()
freqStack.push(5)
freqStack.push(1)
freqStack.push(2)
freqStack.push(5)
freqStack.push(5)
freqStack.push(5)
freqStack.push(1)
freqStack.push(6)
freqStack.push(1)
freqStack.push(5)
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
# ["FreqStack","push","push","push","push","push","push","push","push","push","push","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop"]
# [[],[5],[1],[2],[5],[5],[5],[1],[6],[1],[5],[],[],[],[],[],[],[],[],[],[]]
