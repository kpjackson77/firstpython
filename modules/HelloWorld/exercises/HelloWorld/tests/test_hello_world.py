def test_hello_world(capsys):
    """
    Test main prints "Hello World!"
    """
    from ..exercise import main

    out, err = capsys.readouterr()
    assert out.strip() == "Hello World!"


