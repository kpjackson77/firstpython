from unittest import TestCase
from exercise.modules.greet import greet

def test_greet(capsys):
    name = "Test"
    greet(name)
    out, err = capsys.readouterr()
    assert out.strip() == f"Hello {name}"

