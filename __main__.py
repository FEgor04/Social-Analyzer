import vk_scrapper
import social_graph

if __name__ == '__main__':
    all_friends = social_graph.get_all_friends("fegor2004", 2)
    print(len(all_friends))
    for person in all_friends:
        print(person)
