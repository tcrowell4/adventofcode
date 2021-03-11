def get(x):
    #print(x,power)
    if type(x) == int or x.isdigit():
        power[x] = int(x)
    elif x not in power:
        print(">>>>>>",data[x])
        function, a, b, ins = data[x]
        power[x] = function(a, b)
        print(x,ins, power[x])
    return power[x]

def o(ins):
    if 'NOT'    in ins: return lambda a, b: ~ get(b)
    if 'AND'    in ins: return lambda a, b: get(a) & get(b)
    if 'OR'     in ins: return lambda a, b: get(a) | get(b)
    if 'RSHIFT' in ins: return lambda a, b: get(a) >> get(b)
    if 'LSHIFT' in ins: return lambda a, b: get(a) << get(b)
    else:               return lambda a, b: get(a)

with open('dict_comp_input.txt') as f:
    data = {x: (o(i), i[0], i[-1], i) for *i, _, x in map(str.split, f)}

power = {}
print(a := get('a'))
power = {'b': a}
print(get('a'))