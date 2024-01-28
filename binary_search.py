def binary_search(arr, x):
    array = sorted(arr) 
    low = 0
    high = len(arr) - 1
    mid = 0
    counter = 0
    high_boundary = array[-1]
    if high_boundary < x: 
        return -1
    
    
    while low <= high:
 
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if array[mid] < x:
            low = mid + 1
            counter += 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif array[mid] > x:
            high_boundary = array[mid]
            high = mid - 1
            counter += 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            counter += 1
            return mid, counter
 
    # якщо елемент не знайдений
    return high_boundary, counter

arr = [2, 3, 4, 10, 40, 50, 60, 70, 80, 90, 100]
x = 35
result = binary_search(arr, x)
if result != -1:
    print(f"Element is present at index \ the closest value, iterations needed for search {result}")
    
else:
    print("Element is not present in array")