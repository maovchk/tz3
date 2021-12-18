import pytest

from simple_math import minimum, maximum, addition, multiplication, process, sort


# Для получения оценки "2":
def test_minimum():
    assert minimum([1, 2, 3, 4]) == 1
    assert minimum([-3, 0, 4]) == -3
    assert minimum([-3.5, -2.76, 0, 2.4]) == -3.5
    assert minimum([2.34, -1.75, 0, 4, -10.11]) == -10.11


def test_maximum():
    assert maximum([1, 2, 3, 4]) == 4
    assert maximum([-3, 0, 4]) == 4
    assert maximum([-3.5, -2.76, 0, 2.4]) == 2.4
    assert maximum([2.34, -1.75, 0, 4, -10.11]) == 4


def test_addition():
    assert addition([1, 2, 3, 4]) == 10
    assert addition([-3, 0, 4]) == 1
    assert addition([-3.5, -2.76, 0, 2.4]) == -3.86
    assert addition([2.34, -1.75, 0, 4, -10.11]) == -5.52


def test_multiplication():
    assert multiplication([1, 2, 3, 4]) == 24
    assert multiplication([-3, 4]) == -12
    assert multiplication([-3.5, -2.76, 2.4]) == 23.184
    assert multiplication([2.4, -1.75, 4, -10.1]) == 169.68


# Для получения оценки "3":
def test_process():
    assert process([1, 2, 3]) == 0
    assert process([72587, -295829, 258928]) == 0
    assert process([75200670.7287528, -728278.5295829, 2859829.52892, -7386728.57287]) == 0


# Для получения оценки "4":
def test_sort():
    assert sort([3, 2, 0, 1]) == [0, 1, 2, 3]
    assert sort([-7, 6, 8, 0, -2]) == [-7, -2, 0, 6, 8]
    assert sort([-4.5, 6.12, 0.11, -7]) == [-7, -4.5, 0.11, 6.12]
