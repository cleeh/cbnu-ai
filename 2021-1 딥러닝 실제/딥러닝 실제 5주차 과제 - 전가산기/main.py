#-*- coding:euc-kr -*-

from adder import full_adder
from test_adder_cases import cases_full_adder

if __name__ == '__main__':
    for case in cases_full_adder:
        result = full_adder(case['x'], case['y'], case['z'])
        print("(X, Y, Z) = ({}, {}, {}) => (S, C) = ({}, {})" \
            .format(case['x'], case['y'], case['z'], result['s'], result['c']))
