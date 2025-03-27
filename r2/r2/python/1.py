"""
The following program implements the Fibonacci search algorithm to search for an element in a sorted array.

**TASK:**
1. The program takes a sorted array of integers and a search element as input.
2. It performs a Fibonacci search to find the index of the element in the array.
3. If the element is found, the program displays the index of the element.
4. If the element is not found, the program displays a message saying that the element isn't present in the array.

**OBJECTIVE:**
- Debug the program so that it correctly:
   - Performs the Fibonacci search.
   - Returns the correct index if the element is found.
   - Returns -1 if the element isn't found.

**FIBONACCI SEARCH EXPLANATION:**

The Fibonacci search algorithm is similar to binary search but uses Fibonacci numbers instead of halving the array. Here’s a step-by-step example of how it works.

### Example:
Array: `{10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100, 235}`
Target: `45`

1. **Generate Fibonacci Numbers**: 
   - Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
   - Find the smallest Fibonacci number greater than or equal to the size of the array (`n = 12`). 
     - The smallest Fibonacci number greater than or equal to `12` is `13` (i.e., `fib3 = 13`).

2. **Set the initial values**: 
   - `fib1 = 0`, `fib2 = 1`, `fib3 = 13`, `offset = -1`
   - We will compare the element at index `fib2 = 1` (second index) of the array with `45`.

3. **First iteration**:
   - We calculate the index to check: `i = min(offset + fib2, n - 1) = min(-1 + 1, 11) = 1`
   - The element at index `1` is `22`, which is less than `45`.
   - Therefore, move the left range forward by `fib2 = 1`. 
   - Now the new range is from index `1` to `11` and we reduce the Fibonacci numbers:
     - `fib3 = fib1 = 0`, `fib2 = fib2 - fib1 = 1`, `fib1 = fib3 - fib2 = 13 - 1 = 12`.

4. **Second iteration**:
   - We calculate the next index: `i = min(offset + fib2, n - 1) = min(1 + 1, 11) = 2`
   - The element at index `2` is `35`, which is still less than `45`.
   - Again, we move the left range forward by `fib2 = 1`:
     - `fib3 = fib1 = 1`, `fib2 = fib2 - fib1 = 2 - 1 = 1`, `fib1 = fib3 - fib2 = 3 - 1 = 2`.

5. **Third iteration**:
   - Now we calculate the next index: `i = min(offset + fib2, n - 1) = min(2 + 1, 11) = 3`
   - The element at index `3` is `40`, which is still less than `45`.
   - Again, move the left range forward by `fib2 = 1`:
     - `fib3 = fib1 = 2`, `fib2 = fib2 - fib1 = 1 - 1 = 0`, `fib1 = fib3 - fib2 = 3 - 2 = 1`.

6. **Fourth iteration**:
   - Now the index is: `i = min(offset + fib2, n - 1) = min(3 + 1, 11) = 4`
   - The element at index `4` is `45`, which **matches** the target element!
   - So, we return the index `4`.

### Final Output:
For the target `45`, the index returned is `4`.
"""
def fibonacciSearch(arr, n, x):
    if n == 0:
        return -1
    fib1 = 0
    fib2 = 1
    fib3 = fib1 + fib2

    while fib3 > n:
        fib1 = fib2
        fib2 = fib3
        fib3 = fib1 + fib2

    offset = -1
    while fib3 > 1:
        i = min(offset + fib2, n-1)

        if arr[i] < x:
            fib3 = fib1
            fib2 = fib1
            fib1 = fib3 - fib2
            offset = i
        elif arr[i] > x:
            fib3 = fib1
            fib2 = fib2 - fib1  
            fib1 = fib3 - fib2  
        else:
            return i

    if fib2 == 1 and arr[offset+1] == x:
        return offset + 1
    else:
        return 1

def main():
    arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100, 235]
    n = len(arr)
    x = int(input("Enter number to search: "))
    ind = fibonacciSearch(arr, n, x)
    if ind == -1:
        print(f"{x} isn't present in the array")
    else:
        print(f"Found at index: {ind}")