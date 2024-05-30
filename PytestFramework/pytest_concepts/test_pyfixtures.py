import pytest


# Fixtures:
# In pytest, fixtures are reusable components for setting up and tearing down resources or test data.
# setup - set of code which will perform before the execution of the test function.
# teardown - set of code which will perform after the execution of the test function.

@pytest.fixture()
def precondition_and_postcondition():
    print('launch the browser')
    print('navigate to the url')
    yield
    print('logout')
    print('quit the session')


@pytest.mark.usefixtures('precondition_and_postcondition')
def test_register():
    print('Account registered successfully')


def test_login(precondition_and_postcondition):
    print('logged in successfully')


def test_change_picture(precondition_and_postcondition):
    print('picture changed successfully')
