# def my_iterator(data):
#     def __init__(self,data):
#         self.data = data
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self,data):
#         if self.index < len(self.data):
#             result = self.data[self.index]
#             self.index +=1
#             return result
#         else:
#             StopIteration

# mylist=[1,2,3,4,5]

# obj = my_iterator(mylist)

# for item in obj:
#     print(item)









class myiterator:
    def __init__(self,data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

thelist =[1,2,3,4,56,7]

mylist = myiterator(thelist)
for i in mylist:
    print(i)
