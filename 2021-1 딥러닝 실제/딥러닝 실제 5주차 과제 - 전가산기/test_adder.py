#-*- coding:euc-kr -*-

import unittest
from adder import *
from test_adder_cases import *

class TestAdder(unittest.TestCase):
    def test_and_gate(self):
        for case in cases_and_gate:
            answer = and_gate(case['x'], case['y'])
            self.assertEqual(
                answer,
                case['output'],
                "AND 게이트의 잘못된 연산으로 ({})가 나왔습니다, {{'x': {}, 'y': {}}} => {}" \
                    .format(answer, case['x'], case['y'], case['output']))
    
    def test_or_gate(self):
        for case in cases_or_gate:
            answer = or_gate(case['x'], case['y'])
            self.assertEqual(
                answer,
                case['output'],
                "OR 게이트의 잘못된 연산으로 ({})가 나왔습니다, {{'x': {}, 'y': {}}} => {}" \
                    .format(answer, case['x'], case['y'], case['output']))
    
    def test_xor_gate(self):
        for case in cases_xor_gate:
            answer = xor_gate(case['x'], case['y'])
            self.assertEqual(
                answer,
                case['output'],
                "XOR 게이트의 잘못된 연산으로 ({})가 나왔습니다, {{'x': {}, 'y': {}}} => {}" \
                    .format(answer, case['x'], case['y'], case['output']))

    def test_half_adder(self):
        for case in cases_half_adder:
            self.assertEqual(
                half_adder(case['x'], case['y']),
                {'s': case['s'], 'c': case['c']},
                "반가산기 연산이 틀렸습니다, {{'x': {}, 'y': {}}} => {{'s': {}, 'c': {}}}" \
                    .format(case['x'], case['y'], case['s'], case['c']))
    
    def test_full_adder(self):
        for case in cases_full_adder:
            self.assertEqual(
                full_adder(case['x'], case['y'], case['z']),
                {'s': case['s'], 'c': case['c']},
                "전가산기 연산이 틀렸습니다, {{'x': {}, 'y': {}, 'z': {}}} => {{'s': {}, 'c': {}}}" \
                    .format(case['x'], case['y'], case['z'], case['s'], case['c']))

if __name__ == '__main__':
    unittest.main()
