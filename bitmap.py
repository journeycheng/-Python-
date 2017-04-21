class Bitmap(object):
    def __init__(self, max):
        self.size = int((max + 31 - 1) /31)
        self.array = [0 for i in range(self.size)]
        
    def calcElemIndex(self, num):
        return num / 31
    
    def calcBitIndex(self, num):
        return num % 31
    
    def set(self, num):
        elemIndex = self.calcElemIndex(num)
        bitIndex = self.calcBitIndex(num)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem | (1 << bitIndex)
        
    def clean(self, num):
        elemIndex = self.calcElemIndex(num)
        bitIndex = self.calcBitIndex(num)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem & (~(1 << bitIndex))
        
    def test(self, num):
        elemIndex = self.calcElemIndex(num)
        bitIndex = self.calcBitIndex(num)
        if self.array[elemIndex] & (1 << bitIndex):
            return True
        return False
