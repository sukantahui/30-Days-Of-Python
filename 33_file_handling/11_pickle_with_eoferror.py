import pickle

data=[i for i in range(1,50) if i%2]
try:
    # Pickle the object
    with open('data.pickle', 'wb') as file:
        pickle.dump(data, file)

    # Unpickle the object
    with open('data.pickle', 'rb') as file:
        loaded_data = pickle.load(file)
except EOFError:
    # Code to handle the EOFError exception
    print("Error: End of file reached unexpectedly")
