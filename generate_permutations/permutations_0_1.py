

def gen_binary(n, prefix=''):
    if n == 0:
        print(prefix)
    else:
        gen_binary(n - 1, prefix + '(')
        gen_binary(n - 1, prefix + ')')


gen_binary(4)