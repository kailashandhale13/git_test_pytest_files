'''Encapsulation is the concept of binding the data member and function
    togather so that work on the data in the simgel unit'''
#Class in the exmaple of Encapsulation
#Due to this we can hide the internal state object from outside. this is also call as information hidding.
#Encapsulation restrict on direct access of object. and also prevent the accidental modification of data


class employee:
    def __init__(self,name,age,salary):
        self.name=name # public
        self._age=age  # protected
        self.__salary=salary # privite

    def display(self):
        print('name',self.name)
        print('age',self._age)
        print('salary',self.__salary)
    def __get_pravite(self):
        print('salary- __get_pravite',self.__salary)

    def _get_protected(self):
        print('age _get_protected ',self._age)

e1 = employee('kailash',30,70000)
e1.display()
e1._get_protected()
e1._employee__get_pravite()

