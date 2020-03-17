# import matplotlib
import vk_scrapper
import queue
from numpy import unique
import numpy as np

# import networkx


def get_all_friends(target: str, cnt: int = 2) -> np.ndarray:
    """
    Get all friends, and friends of their friends and etc. It will just return list of them. There will be no connections between them
    :param target: Target
    :param cnt: How much friends of friends do you want to get
    :return: list with friends of friend and so on
    """
    was = {target: 1}
    cnt -= 1
    pred_cnt = {target: 0}
    q = queue.Queue()
    q.put(target)
    all_friends = []
    while not q.empty():
        now = q.get()
        print(pred_cnt[now])
        if pred_cnt[now] == cnt + 1:
            break
        friends = vk_scrapper.get_friends(now)
        if friends != -1:
            all_friends.extend(friends)
            for person in friends:
                was_l = 1
                try:
                    was_l = was[person]
                except:
                    was_l = 0
                if was_l != 1:
                    q.put(person)
                    was[person] = 1
                    pred_cnt[person] = pred_cnt[now] + 1
    all_friends = unique(all_friends)
    return all_friends

