class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    
    def computeDifference(self):
        maximum_num = max(self.__elements)
        minimum_num = min(self.__elements)
        
        self.maximumDifference = maximum_num - minimum_num

# End of Difference class