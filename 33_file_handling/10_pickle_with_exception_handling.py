import pickle

data = {'name': 'Sukanta Hui', 'age': 47, 'city': 'Barrackpore'}

try:
    # Pickle the object
    with open('my_file.data', 'wb') as file:
        pickle.dump(data, file)
except pickle.PickleError as e:
    # Handle pickle-related errors
    print(f"Error occurred while pickling: {e}")
except IOError as e:
    # Handle file-related errors
    print(f"Error occurred while accessing the file: {e}")

try:
    # Unpickle the object
    with open('my_file.data2', 'rb') as file:
        loaded_data = pickle.load(file)
        print(loaded_data)  # Output: {'name': 'Sukanta Hui', 'age': 47, 'city': 'Barrackpore'}
except pickle.PickleError as e:
    # Handle pickle-related errors
    print(f"Error occurred while unpickling: {e}")
        
except IOError as e:
    # Handle file-related errors
    print(f"Error occurred while accessing the file: {e}")
except:
    print('I dont know')    


