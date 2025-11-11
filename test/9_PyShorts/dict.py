

def make_dict_functional():
    """
    this is a test function docstring updated \n
    Demonstrates various methods to merge two dictionaries in Python.
    Methods shown:
    1. Iterating over key-value pairs
    2. Using the update() method
    3. Using the unpacking operator (**)
    4. Using collections.ChainMap
    5. Unpacking the second dictionary in dict() constructor
    6. Merging more than two dictionaries
    7. Using dictionary comprehension
    8. Using itertools.chain
    9. Using dict.union() method (Python 3.9+)
    10. Using functools.reduce
    11. Using a custom merge function
    12. Using json.loads and json.dumps
    13. Using pandas DataFrame (for large datasets)
    14. Using dict.fromkeys() and dict comprehension
    15. Using a for loop with setdefault()
    16. Using the walrus operator (Python 3.8+)
    17. Using map() function
    18. Using a generator expression  
    """
    dict1 = {   'key1': 'val1','key2': 'val2','key3': 'val3'}
    dict2 = {   'key4': 'val4','key5': 'val5','key6': 'val6'}

    #?1️⃣--Iterating over the key-value pairs of the second dictionary with the first one 
    #?----------------------------------------------------------------------------------
    dict3 = dict1.copy()
    for key, value in dict2.items():
        dict3[key] = value

    print(dict3) #{'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4', 'key5': 'val5', 'key6': 'val6'}
    #?----------------------------------------------------------------------------------

    #*2️⃣-- Using the update method 
    #*----------------------------------------------------------------------------------
    dict4 = dict1.copy()
    dict4.update(dict2)
    print(dict4) #{'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4', 'key5': 'val5', 'key6': 'val6'}
    #*----------------------------------------------------------------------------------

    #!3️⃣--Using unpacking operator
    #!----------------------------------------------------------------------------------
    dict5 = {**dict1, **dict2}
    print(dict5) #{'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4', 'key5': 'val5', 'key6': 'val6'}
    #!----------------------------------------------------------------------------------

    #?4️⃣--Using collections.ChainMap
    #?----------------------------------------------------------------------------------
    from collections import ChainMap
    dict6 = ChainMap(dict1, dict2)
    print(dict6) #{'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4', 'key5': 'val5', 'key6': 'val6'}
    #?----------------------------------------------------------------------------------

    #5️⃣--Unpacking the second dictionary
    #----------------------------------------------------------------------------------
    dict7 = dict(dict1, **dict2)
    print(dict7) #{'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4', 'key5': 'val5', 'key6': 'val6'}
        #----------------------------------------------------------------------------------#The methods below could be implemented to merge more than 2 dictionaries at once.

    dict1 = {   'key1': 'val1','key2': 'val2','key3': 'val3'}
    dict2 = {   'key4': 'val4','key5': 'val5','key6': 'val6'}

    #?1️⃣--Iterating over the key-value pairs of the second dictionary with the first one 
    #?----------------------------------------------------------------------------------
    dict3 = dict1.copy()
    for key, value in dict2.items():
        dict3[key] = value

    print(dict3) #{'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4', 'key5': 'val5', 'key6': 'val6'}
    #?----------------------------------------------------------------------------------

    #*2️⃣-- Using the update method 
    #*----------------------------------------------------------------------------------
    dict4 = dict1.copy()
    dict4.update(dict2)
    print(dict4) #{'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4', 'key5': 'val5', 'key6': 'val6'}
    #*----------------------------------------------------------------------------------

    #!3️⃣--Using unpacking operator
    #!----------------------------------------------------------------------------------
    dict5 = {**dict1, **dict2}
    print(dict5) #{'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4', 'key5': 'val5', 'key6': 'val6'}
    #!----------------------------------------------------------------------------------

    #?4️⃣--Using collections.ChainMap
    #?----------------------------------------------------------------------------------
    from collections import ChainMap
    dict6 = ChainMap(dict1, dict2)
    print(dict6) #{'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4', 'key5': 'val5', 'key6': 'val6'}
    #?----------------------------------------------------------------------------------

    #5️⃣--Unpacking the second dictionary
    #----------------------------------------------------------------------------------
    dict7 = dict(dict1, **dict2)
    print(dict7) #{'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4', 'key5': 'val5', 'key6': 'val6'}
    #----------------------------------------------------------------------------------