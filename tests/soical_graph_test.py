import vk_scrapper
import pytest
import social_graph


@pytest.mark.parametrize("target, cnt, epsilon, expected", [
    ("fegor2004", 1, -1, 1),
    ("fegor2004", 2, 500, 9171),
    ("dasdasdsadasd", 12, -1, 0)
])
def test_get_all_friends(target, cnt, epsilon, expected):
    """
    Test social_graph.get_all_friends function
    """
    all_friends = social_graph.get_all_friends(target, cnt)
    if cnt == 1:
        friends = vk_scrapper.get_friends(target)
        assert len(all_friends) == len(friends)
        return
    if expected == 0:
        assert len(all_friends) == expected
        return
    if expected != 0:
        print(all_friends)
        summary_len = len(all_friends)
        assert abs(summary_len - expected) <= epsilon
        return
