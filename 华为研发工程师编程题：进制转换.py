'''
[编程题] 进制转换
时间限制：1秒
空间限制：32768K
写出一个程序，接受一个十六进制的数值字符串，输出该数值的十进制字符串。（多组同时输入 ）

输入描述:
输入一个十六进制的数值字符串。


输出描述:
输出该数值的十进制字符串。

输入例子1:
0xA

输出例子1:
10
'''

'''
解题思路：简单
   仔细小心考虑到每一种情况就能做出来
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

while True:
    try:
        x_num = input()[2:]
        d_num = 0
        length = len(x_num)
        for i in range(length):
            if x_num[i] == 'A':
                d_num += 10 * 16 ** (length - 1 - i)
            elif x_num[i] == 'B':
                d_num += 11 * 16 ** (length - 1 - i)
            elif x_num[i] == 'C':
                d_num += 12 * 16 ** (length - 1 - i)
            elif x_num[i] == 'D':
                d_num += 13 * 16 ** (length - 1 - i)
            elif x_num[i] == 'E':
                d_num += 14 * 16 ** (length - 1 - i)
            elif x_num[i] == 'F':
                d_num += 15 * 16 ** (length - 1 - i)
            else:
                d_num += int(x_num[i]) * 16 ** (length - 1 - i)
        print(d_num)
    except:
        break
