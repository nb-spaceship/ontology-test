# import base58

# encodes = base58.b58encode('02802683d48aa9b34f9a0e91f5e27fedc8ac6486b1')

# print(encodes)

# print(base58.b58decode(encodes))
# #base58.b58encode_check(b'hello world')

# #base58.b58decode_check(b'3vQB7B6MrGQZaxCuFg4oh')
# #base58.b58decode_check(b'4vQB7B6MrGQZaxCuFg4oh')
import time

def deco01(func):
    def wrapper(*args, **kwargs):
        print("this is deco01")
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
        print("deco01 end here")
    return wrapper

def deco02(func):
    def wrapper(*args, **kwargs):
        print("this is deco02")
        func(*args, **kwargs)

        print("deco02 end here")
    return wrapper

@deco01
@deco02
def func(a,b):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b))



if __name__ == '__main__':
    #f = func
    #f(3,4)
    #func(3,4)
    b = bytearray(1)
    b[0] = 0xff
    print(int(b[0]))
