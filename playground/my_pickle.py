import pickle

data = {
    'a': [1, 2, 3],
    'b': ("string 1", "string 2"),
    'c': {None, True, False}
}

data_2 = {
    'a': [3, 4, 5],
    'b': ("string_3", "string_4"),
    'c': {None, True, False}
}


with open("data.pickle", "wb") as f:
    pickle.dump(data, f)
    pickle.dump(data_2, f)
    

with open("data.pickle", "rb") as f:
    data = [] 
    while True:
        try:
            data.append(pickle.load(f))
        except EOFError:
            break
    for obj in data:
        print(obj)
         