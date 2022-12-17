k = int(input())
cat_url_set = []
while (k != 0):
    print("Enter the category to be added: ")
    cat = input()
    if cat not in cat_url_set:
        cat_url_set.append(cat)
        i = cat_url_set.index(cat)
        cat_url_set.append(set())
    print(cat_url_set)
    print("Enter url")
    url = input()
    i = cat_url_set.index(cat)
    cat_url_set[i+1].add(url)
    k = k-1 
print(cat_url_set)


