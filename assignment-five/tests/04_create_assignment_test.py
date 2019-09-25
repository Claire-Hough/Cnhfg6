import pytest

from mycode.instructor import create_assignment


def test_successful_creation():
    """
    Instructors can create new assignments, each with unique names
    """
    assert create_assignment("Requirements Analysis", "Make a bunch of diagrams.")


def test_fail_creation():
    """
    A new assignment cannot be created if it is given the same name as an existing assignment
    """
    assert create_assignment("Resume", "Submit your resume.") == False
