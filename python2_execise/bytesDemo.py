#从键盘输入一个字符串，将字符串转换成字节串，
# 计算字节串长度并打印，然后将字节串装换成字符串，比较字符串是否与之前输入的字符串相同

def compareBytes():
    s = input("input a string:")
    print(s)
    b = s.encode('utf-8')
    print('bytes:',b)

    decodeStr=b.decode('utf-8')
    print('decode string:',decodeStr)

compareBytes()