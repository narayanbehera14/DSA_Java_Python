#  Basic Linear Search Code
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i  # return index where key is found
    return -1  # if not found

# Example usage
arr = [10, 20, 30, 40, 50]
key = 30

result = linear_search(arr, key)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

# ### Linear Search for Strings

#It works for any type of iterable (numbers, strings, characters, etc.)

names = ["liju","bob","ram","raju"]
key = "bob"

for i in range(len(names)):
    if names[i] == key:
        print(f"{key} found at index {i}")

        break
    else :
        print("not found")


### Linear Search That Returns All Occurrences

#Sometimes a value may appear multiple times.

def linear_search_all(arr,key):
    indices = []
    for i in range(len(arr)):
        if arr[i] == key:
            indices.append(i)
    return indices

arr = [2,4,8,9,10,10,10,10]
key = 10
print(linear_search_all(arr ,key))