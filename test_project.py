from project import main_menu, game_menu, waiting, coins, days


def test_main_menu():
    # main_menu function returns an int which it converts from a str either it took through its parameter or the user if the string is one of these : "1", "2", "3"

    assert not main_menu("0")
    assert not main_menu("-9")
    assert not main_menu(2)
    assert main_menu("3") == 3
    assert main_menu("1") == 1


def test_game_menu():
    # main_menu function returns an int which it converts from a str either it took through its parameter or the user if the string is one of these : "1", "2", "3", "4"

    assert not game_menu("5")
    assert not game_menu("-5")
    assert not game_menu(3)
    assert game_menu("2") == 2
    assert game_menu("4") == 4


def test_waiting():
    global coins, days

    # we allow the programmer to override waiting function only once by passing it any argument except None, so first trying should return True and others should
    # return None per "project.py"

    assert waiting(5)

    assert waiting(2) == None

    assert waiting(3) == None

    assert waiting(10) == None

