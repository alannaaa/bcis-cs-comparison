def is_equal(arr, sl, sr):
    for k in range(sl+1, sr):
        if arr[k] != arr[sl]:
            swap(arr, k, sl)
            return k
    return -1

def insert_right(arr, current, sr, right):
    j = sr
    while j <= right and current > arr[j]:
        arr[j-1] = arr[j]
        j += 1
    arr[j-1] = current

def insert_left(arr, current, sl, left):
    j = sl
    while j >= left and current < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = current

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bcis(arr, left, right):
    sl = left
    sr = right
    while sl < sr:
        swap(arr, sr, sl+(sr+1-sl)//2)
        if arr[sl] == arr[sr] and is_equal(arr, sl, sr) == -1:
            return arr
        if arr[sl] > arr[sr]:
            swap(arr, sl, sr)
        if (sr-sl) >= 100:
            for i in range(sl+1, int((sr-sl)**(0.5)+1)):
                if arr[sr] < arr[i]:
                    swap(arr, sr, i)
                elif arr[sl] > arr[i]:
                    swap(arr, sl, i)
        i = sl+1
               
        lc = arr[sl]
        rc = arr[sr]
        while i < sr:
            current = arr[i]
            if current >= rc:
                arr[i] = arr[sr-1]
                insert_right(arr, current, sr, right)
                sr -= 1
            elif current <= lc:
                arr[i] = arr[sl+1]
                insert_left(arr, current, sl, left)
                sl += 1
                i += 1
            else:
                i += 1
        sl += 1
        sr -= 1
    return arr