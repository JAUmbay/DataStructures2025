def demonstrate_array():
    arr = [10, 20, 30, 40]
    arr.append(50)
    arr.remove(20)
    print(f"Array after operations: {arr}")
    print(f"Element at index 2: {arr[2]}")
    print(f"Is 30 in the array? {30 in arr}")

demonstrate_array()
