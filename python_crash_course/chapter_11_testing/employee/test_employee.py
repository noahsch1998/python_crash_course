import pytest
from class_employee import Employee

@pytest.fixture
def employee():
    """Default employee for testing"""
    employee = Employee('John', 'Smith', 50000)
    return employee

def test_give_default_raise(employee):
    """Test that a default raise is given properly"""
    employee.give_raise()
    assert employee.salary == 55000

def test_give_custom_raise(employee):
    """Test that a custom raise is given properly"""
    employee.give_raise(10000)
    assert employee.salary == 60000