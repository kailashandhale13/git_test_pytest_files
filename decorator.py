import time
def time_calculetor(func):
    def wrapper(*args,**kwargs):
        star = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f'time taken by function : {func.__name__} run in {end-star}.')
        return result
    return wrapper
@time_calculetor
def timer():
    time.sleep(2)
    print('timer funcation completed')

timer()

'''
# store function in the variable
def send_msg(msg):
    print(f'msg from function :{msg}')

func_as_variable=send_msg
func_as_variable('here we are as a function again')'''

'''
# function as argument

def upper_case(text):
    return text.upper()

def lower_case(text):
    return text.lower()

def greeting(func):
    greet = func(' hi there  i am from greeting')
    return greet

b = greeting(upper_case)
print(b)

print(greeting(lower_case))'''

'''
import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result=func(*args,**kwargs)
        end= time.time()
        print(f'the time taken by  {func.__name__}  in {end-start} in sec')
        return result
    return wrapper

@timer
def calculate_time():
    time.sleep(2)
    print('calculate_time funcation completed')

calculate_time()'''

def send_message(text):
    return f'Here is the message : {text}'

msg = send_message

print(msg('we are calling from msg'))


def upper_case(text):
    return text.upper()

def my_msg(func):
    msg = func('funcation as argument')
    return msg

print(my_msg(upper_case))


