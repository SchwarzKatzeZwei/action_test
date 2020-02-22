# -*- coding: utf-8 -*-

import lib.calc as calc


def test_add():
    assert calc.add(9, 9) == 18


def test_multiply():
    assert calc.multiply(9, 9) == 81
