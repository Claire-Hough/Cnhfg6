import pytest

from mycode.student import upload

def test_successful_upload():
    """
    Students can upload files of type '.zip' or '.py'
    """
    assert upload( 'assignment-five', '.zip')
    assert upload( 'test1', '.py' )
    
def test_failed_upload():
    """
    The upload will fail if a filetype other than '.zip' or '.py' are submitted
    """
    assert upload( 'project-2', '.html') == False
