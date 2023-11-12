class FactoIterator:
    def __init__(self, n):
        self.n = n
        self.result = 1
        self.order = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.order > self.n:
            raise StopIteration
        
        self.result *= self.order
        self.order += 1
        return self.result

facto_iter = FactoIterator(5)

a = next(facto_iter)
print(a)

#for factorial in facto_iter:
#    print(factorial)