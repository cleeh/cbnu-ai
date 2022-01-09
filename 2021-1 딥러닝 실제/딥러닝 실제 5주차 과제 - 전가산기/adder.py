def and_gate(x, y):
    return 1 if x > 0 and y > 0 else 0

def or_gate(x, y):
    return 1 if x > 0 or y > 0 else 0

def xor_gate(x, y):
    return 1 if (x > 0) != (y > 0) else 0

def half_adder(x, y):
    return {'s': xor_gate(x, y), 'c': and_gate(x, y)}

def full_adder(x, y, z):
    half = half_adder(x, y)
    return {
        's': xor_gate(half['s'], z),
        'c': or_gate(and_gate(half['s'], z), half['c'])}