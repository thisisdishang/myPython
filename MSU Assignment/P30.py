# Python program to match key values in two dictionary

dic1 = {
    'mouse': 500,
    'keyboard': 200,
    'headphone': 300,
    'printer': 450}

dic2 = {
    'keyboard': 200,
    'mouse': 500,
    'key': 100,
    'moniter': 100,
    'printer': 450}

for (k, v) in set(dic1.items()) & set(dic2.items()):
    print((k, v))