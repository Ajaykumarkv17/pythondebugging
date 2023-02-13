from collections import Counter
ini_list = [10, 20, 30, 40, 40, 50, 50, 50]


result = [item for items, c in Counter(ini_list).most_common() for item in [items] * c]

print(str(result))