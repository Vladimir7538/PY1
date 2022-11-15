from pprint import pprint


count = 16
list_ = [{'bin': bin(n), 'dec': n, 'hex': hex(n), 'oct': oct(n)} for n in range(count)]
pprint(list_)
