import vk_scrapper
import pytest


@pytest.mark.parametrize("target, expected, epsilon", [
    ("fegor2004", 74, 5),
    ("dasdasdaatggrtefsdg", -1, 0),
    ("a_medvedev_01", 9937, 50)

])
def test_get_friends(target, expected, epsilon):
    """
    Test vk_scrapper.get_friends function
    """
    friends = vk_scrapper.get_friends(target, 9999)
    if type(friends) == int:
        assert friends == expected
    else:
        print(len(friends))
        assert abs(expected - len(friends)) <= epsilon


@pytest.mark.parametrize("target1, target2, expected", [
    ("fegor2004", "artemevaanzhela", 14),
    ("fegor2004", "dianovaarina", -1),
    ("asasdasd", "Sasadsadasdas", -1)  # There are no pages like that
])
def test_get_mutual(target1, target2, expected):
    """
    Test vk_scrapper.get_mutual_friends function
    """
    mutual = vk_scrapper.get_mutual_friends(target1, target2)
    if expected != -1:
        assert abs(len(mutual) - expected) <= 5;
    else:
        assert mutual == expected


@pytest.mark.parametrize("target, expected", [
    ("fegor2004", "Egor Fedorov"),
    ("adfafadf", -1)
])
def test_get_name(target, expected):
    """
    Test vk_scrapper.get_name function
    """
    name = vk_scrapper.get_name(target)
    if expected != -1:
        assert name['first_name'] + ' ' + name['last_name'] == expected
    else:
        assert name == expected


