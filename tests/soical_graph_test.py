import pytest

import social_graph
import vk_scrapper


@pytest.mark.parametrize("target, cnt, deviation, expected", [
    ("fegor2004", 1, -1, 1),
    ("fegor2004", 2, 500, 9171),
    ("dasdasdsadasd", 12, -1, 0)
])
def test_get_all_friends(target, cnt, deviation, expected):
    """Test social_graph.get_all_friends function
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
        assert abs(summary_len - expected) <= deviation
        return


@pytest.mark.parametrize("target, cnt, deviation, expected", [
    ("fegor2004", 1, 10, [75, 76]),
    ("sasdasdsad", 1, 0, -1)
])
def test_get_friends_nx_graph(target, cnt, deviation, expected):
    """Test social_graph.get_friends_nx_graph() function
    :param expected: list with expected nodes and edges
    """

    graph = social_graph.get_friends_nx_graph(target, cnt)
    if expected == -1:
        assert graph == expected
    else:
        assert abs(graph.number_of_nodes() - deviation) <= expected[0] and abs(graph.number_of_edges() - deviation) <= \
               expected[1]
