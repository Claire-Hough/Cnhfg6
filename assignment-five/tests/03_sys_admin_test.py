import pytest

from mycode.instructor import add_instructor


def test_successful_add_instructor():
    """
    A system admin can add someone as an instructor if their user type is 'instructor'
    """
    assert add_instructor('mary', 'jones', 'instructor')


def test_fail_add_instructor():
    """
    A system admin will not be able to add a user as an instructor if their type is not 'instructor'
    """
    assert add_instructor('sophia', 'smith', 'student') == False
