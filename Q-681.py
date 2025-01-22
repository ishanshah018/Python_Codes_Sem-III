class Data:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value
       

    def __gt__(self, other):
        return self.value > other.value

# Example usage
data1 = Data(10)
data2 = Data(20)
print(data1 < data2)
print(data1 > data2)
