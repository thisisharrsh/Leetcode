class RandomizedCollection:

    def __init__(self):
        self.items,self.idx = [],defaultdict(set)

    def insert(self, val: int) -> bool:
        self.items.append(val)
        self.idx[val].add(len(self.items)-1)
        return len(self.idx[val]) == 1 

    def remove(self, val: int) -> bool:
        if not self.idx[val]:
            return False
        outindex , inindex = self.idx[val].pop(),self.items[-1]
        self.items[outindex] = inindex
        self.idx[inindex].add(outindex)
        self.idx[inindex].discard(len(self.items)-1)
        self.items.pop()
        return True
        
    def getRandom(self) -> int:
        return choice(self.items)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()