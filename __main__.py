import vk_scrapper

if __name__ == '__main__':
    mutual = vk_scrapper.get_mutual_friends("fegor2004", "13arton")
    if mutual != -1:
        for i in mutual:
            name = vk_scrapper.get_name(i)
            print(f"{name['first_name']} {name['last_name']} (id: {i})")
        # print(mutual)
    else:
        print("No mutual friends")
    print("Success")
