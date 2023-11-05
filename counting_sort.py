def counting_sort(array_a):
    k = max(array_a)
    n = len(array_a)
    
    # Initialize count array
    array_c = [0] * (k + 1)
    
    for j in range(0, n):
        array_c[array_a[j]] += 1

    # Calculate cumulative sum
    for i in range(1, k+1):
        array_c[i] += array_c[i - 1]
 
    array_b = [0] * n
 
    for j in range(n-1, -1, -1):
        array_b[array_c[array_a[j]] - 1] = array_a[j]
        array_c[array_a[j]] -= 1
 
    return array_b