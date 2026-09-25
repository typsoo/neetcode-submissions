class MinStack:

    def __init__(self):
        self.arr = []
        self.mini_arr = [float("inf")]
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.mini_arr.append( min(val, self.mini_arr[-1]))
        

    def pop(self) -> None:
        self.arr.pop()
        self.mini_arr.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.mini_arr[-1]
        
