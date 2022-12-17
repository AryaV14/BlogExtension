k = int(input())
cat_url_set = []
while (k != 0):
    print("Enter the category value to be added: ")
    value = input()
    cat_url_set.append(set())#travel
    cat_url_set.append(set())#food
    cat_url_set.append(set())#tech
    cat_url_set.append(set())#music
    print(cat_url_set)
    index = int(value)
    print("Enter url")
    url = input()
    cat_url_set[index].add(url)
    k = k-1 
print(cat_url_set)


