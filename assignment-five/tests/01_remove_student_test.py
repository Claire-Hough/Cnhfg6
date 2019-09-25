import pytest

from mycode.student import remove_student


def test_successful_remove_student():
    """
    Instructors can remove students that are in their class by their student ID
    """
    assert remove_student(10843184)


def test_failed_remove_student():
    """
    Instructors will not be able to remove students that are not enrolled in their class
    """
    assert remove_student(12345678) == False
