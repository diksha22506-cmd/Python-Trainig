#Define a class to perform operations on rectangle.
class Rectangle :
    #member variable.
    length = 0
    breadth = 0
    #method to intialize the data.
    def intialize (self,l,b):
        self.length = l
        self.breadth = b
        #method to display data.
        def display_data(self):
            print("Length:", self.length)
            print("Breadth:", self.breadth)