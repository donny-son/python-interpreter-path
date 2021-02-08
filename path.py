import sys

sp = sys.path
max_len = max([len(p) for p in sp])

if __name__=='__main__':
    print('Current PATHs for Python Interpreter..')
    print('-' * max_len)
    for p in sp:
        print(p)
    print('-' * max_len)
