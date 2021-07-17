import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []



    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.nums:
            self.nums.append(val)
            return True
        else:
            return False


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.nums:
            return False
        else:
            self.nums.remove(val)
            return True


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        x = random.randint(0, len(self.nums) - 1)
        return self.nums[x]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
