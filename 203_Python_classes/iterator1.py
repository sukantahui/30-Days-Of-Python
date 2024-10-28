class Primes:
    def __iter__(self):
        self.a=2
        return self
    def __next__(self):
        x=self.a
        self.a=self.a+1
        return x
    

myPrime = Primes()
myIter = iter(myPrime)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
    