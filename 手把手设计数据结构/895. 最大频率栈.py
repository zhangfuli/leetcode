class FreqStack:
    def __init__(self):
        self.freqStack = []
        self.hashmap = {}

    def push(self, val):
        if val in self.hashmap:
            self.hashmap[val] += 1
            if len(self.freqStack) < self.hashmap[val]:
                self.freqStack.append([val])
            else:
                self.freqStack[self.hashmap[val] - 1].append(val)
        else:
            self.hashmap[val] = 1
            self.freqStack[self.hashmap[val] - 1].append(val)
        return None

    def pop(self):
        res = self.freqStack[-1].pop(-1)
        if len(self.freqStack[-1]) == 0:
            self.freqStack.pop(-1)
        self.hashmap[res] -= 1
        if self.hashmap[res] == 0:
            self.hashmap.pop(res)
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
