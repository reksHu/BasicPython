import  sys
def myprint():
    sys.stdout.write('hello\n')
    print('你好吗')
    sys.stderr.write("error print")

myprint()

#python stdoutDemo.py>stdout.txt