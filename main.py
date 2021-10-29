# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def summer(lis):
    """
    这里是函数的说明文档，doc的位置
    :param lis: 参数列表的说明
    :return: 返回值的说明
    """
    total = 0
    for i in lis:
        total += i
    return total

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    s = set([1, 1, 2, 3, 3, 4])
    print(s)
    a=9
    b=3
    print(a+b)
    我=1
    print(我)

    lis=[1 , 2 , 3 , 4 , 5 , 6]
    s=summer(lis)
    print (s+1)




    def func(*args):
        for arg in args:
            print(arg)


    li = [1, 2, 3]
    func(*li)

    list1 = [1, 2, 3, 4, 5]
    a = 1
    print(id(a))

    flag = False

    for i in list1:
        if i == a:
            flag = True
            break

    if flag:
        print("a是list1的元素之一")
    else:
        print("a不是list1的元素")

    b=6
    if b not in list1:
        print("b not in list")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


a = 10
def test():
    global a
    a += 1
    print(a)
test()

name = 'jack'

def outer():
    name='tom'

    def inner():
        name ='mary'
        print(name)

    inner()

outer()