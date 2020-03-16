from typing import Union, Set
import requests
import settings


def get_id_by_domain(target: str) -> int:
    """
    Get target's id by domain
    :param target: VK domain
    :return target's ID by his domain
    """
    r = requests.get("https://api.vk.com/method/users.get", params={
        "v": settings.version,
        "access_token": settings.token,
        "user_ids": target,
        "fields": "id",
        "name_case": "nom"
    })
    try:
        return r.json()['response'][0]['id']
    except KeyError:
        pass


def get_friends(target: str, count: int = 10000) -> Union[int, list]:
    """

    :param target: VK id
    :param count: count of friends you want to get
    :return: dict with target's friends
    """
    all_data = []
    target_id = get_id_by_domain(target)
    r = requests.get("https://api.vk.com/method/friends.get", params={
        "v": settings.version,
        "access_token": settings.token,
        "user_id": target_id,
        "order": "random",
        "count": count,
    })
    r = r.json()
    try:
        data = r['response']['items']
        all_data.extend(data)
    except KeyError:
        return -1
    return all_data


def get_mutual_friends(target1: str, target2: str) -> Union[Set[int], int]:
    """
    Get mutual friends of target1 and target2
    :param target1: Target1
    :param target2: Target2
    :return: List of mutual friends
    """
    friends1 = get_friends(target1)
    friends2 = get_friends(target2)
    if friends1 != -1 and friends2 != -1:
        mutual: Set[int] = set(friends1) & set(friends2)
    else:
        mutual: int = -1
    return mutual


def get_name(target):
    """

    :param target: VK id
    :return target's name
    """
    r = requests.get("https://api.vk.com/method/users.get", params={
        "v": settings.version,
        "access_token": settings.token,
        "user_ids": target,
        "fields": "bdate",
        "name_case": "nom"
    })
    try:
        return r.json()['response'][0]
    except KeyError:
        return -1
