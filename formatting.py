def formatting(expr):
    expr = expr.replace(' ', '')
    if expr.find(')*('):
        number_input = cnf(expr)
    else:
        number_input = dnf(expr)
    return number_input


def make_list(expr):
    curr_expr = expr
    new_expr = list()
    if curr_expr.find(')+(') != -1:
        curr_expr = curr_expr.replace('(', '')
        curr_expr = curr_expr.replace(')', '')
        curr_expr = curr_expr.split('+')
        for i in range(len(curr_expr)):
            new_expr.append(curr_expr[i].split('*'))
    else:
        curr_expr = curr_expr.replace('(', '')
        curr_expr = curr_expr.replace(')', '')
        curr_expr = curr_expr.split('*')
        for i in range(len(curr_expr)):
            new_expr.append(curr_expr[i].split('+'))

    return new_expr


def cnf(expr):
    curr_expr = make_list(expr)
    dec = list()
    dec_str = ''
    number: str
    for i in curr_expr:
        number = ''
        for j in i:
            if j[0] == '!':
                number += '1'
            else:
                number += '0'
        dec.append(convert_num(number))
    dec = exclude(expr, dec)
    for i in dec:
        dec_str += str(i) + ' '
    return dec_str


def exclude(expr, dec):
    level = 0

    for i in reversed(range(6)):
        if expr.find(str(i)) != -1:
            level = i
            break
    if level % 2 == 0:
        number_list = [i for i in range(level ** 2)]
    else:
        number_list = [i for i in range(level ** 2 - 1)]
    for i in dec:
        try:
            number_list.remove(i)
        except ValueError:
            break
    return number_list


def convert_num(bin_number):
    dec_number = 0
    for i in range(len(bin_number)):
        dec_number += 2 ** i * int(bin_number[len(bin_number) - 1 - i])
    return dec_number


def dnf(expr):
    curr_expr = make_list(expr)
    dec = list()
    dec_str = ''
    number: str
    for i in curr_expr:
        number = ''
        for j in i:
            if j[0] == '!':
                number += '1'
            else:
                number += '0'
        dec.append(convert_num(number))

    return dec_str
