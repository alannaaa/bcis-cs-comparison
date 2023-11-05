from bcis import bcis
from counting_sort import counting_sort
from time import time
import tracemalloc

def dataset_to_array(file_name):
    arr = []
    with open(file_name, 'r') as arr_file:
        for line in arr_file:
            arr.append(int(line.strip()))
    return arr

def run_algorithms(arr):
    # BCIS
    arr_copy = arr.copy()
    right_index = len(arr)-1

    t0 = time()
    tracemalloc.start()

    bcis(arr_copy, 0, right_index)

    bcis_mem = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()

    t1 = time()
    bcis_time = str(t1-t0)

    # COUNTING SORT
    t0 = time()
    tracemalloc.start()

    counting_sort(arr)

    cs_mem = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()

    t1 = time()
    cs_time = str(t1-t0)

    return bcis_time, bcis_mem, cs_time, cs_mem

def main():
    sorted_s = dataset_to_array("dataset/sorted_s.txt")
    sorted_m = dataset_to_array("dataset/sorted_m.txt")
    sorted_l = dataset_to_array("dataset/sorted_l.txt")
    reversed_s = dataset_to_array("dataset/reversed_s.txt")
    reversed_m = dataset_to_array("dataset/reversed_m.txt")
    reversed_l = dataset_to_array("dataset/reversed_l.txt")
    random_s = dataset_to_array("dataset/random_s.txt")
    random_m = dataset_to_array("dataset/random_m.txt")
    random_l = dataset_to_array("dataset/random_l.txt")
    
    with open("results.txt", 'w') as file:
        # Sorted arrays
        file.write("=====SORTED ARRAYS=====\n")
        file.write("# SMALL ARRAY\n")
        bcis_time, bcis_mem, cs_time, cs_mem = run_algorithms(sorted_s)
        file.write("BCIS time: " + bcis_time + "\n")
        file.write("CS time  : " + cs_time + "\n")
        file.write("BCIS memory: " + bcis_mem + "\n")
        file.write("CS memory  : " + cs_mem + "\n")
        
        file.write("\n# MEDIUM ARRAY\n")
        bcis_time, bcis_mem, cs_time, cs_mem = run_algorithms(sorted_m)
        file.write("BCIS time: " + bcis_time + "\n")
        file.write("CS time  : " + cs_time + "\n")
        file.write("BCIS memory: " + bcis_mem + "\n")
        file.write("CS memory  : " + cs_mem + "\n")

        file.write("\n# LARGE ARRAY\n")
        bcis_time, bcis_mem, cs_time, cs_mem = run_algorithms(sorted_l)
        file.write("BCIS time: " + bcis_time + "\n")
        file.write("CS time  : " + cs_time + "\n")
        file.write("BCIS memory: " + bcis_mem + "\n")
        file.write("CS memory  : " + cs_mem + "\n")

        # Reversed arrays
        file.write("\n=====REVERSED ARRAYS=====\n")
        file.write("# SMALL ARRAY\n")
        bcis_time, bcis_mem, cs_time, cs_mem = run_algorithms(reversed_s)
        file.write("BCIS time: " + bcis_time + "\n")
        file.write("CS time  : " + cs_time + "\n")
        file.write("BCIS memory: " + bcis_mem + "\n")
        file.write("CS memory  : " + cs_mem + "\n")

        file.write("\n# MEDIUM ARRAY\n")
        bcis_time, bcis_mem, cs_time, cs_mem = run_algorithms(reversed_m)
        file.write("BCIS time: " + bcis_time + "\n")
        file.write("CS time  : " + cs_time + "\n")
        file.write("BCIS memory: " + bcis_mem + "\n")
        file.write("CS memory  : " + cs_mem + "\n")
        
        file.write("\n# LARGE ARRAY\n")
        bcis_time, bcis_mem, cs_time, cs_mem = run_algorithms(reversed_l)
        file.write("BCIS time: " + bcis_time + "\n")
        file.write("CS time  : " + cs_time + "\n")
        file.write("BCIS memory: " + bcis_mem + "\n")
        file.write("CS memory  : " + cs_mem + "\n")

        # Random arrays
        file.write("\n=====RANDOM ARRAYS=====\n")
        file.write("# SMALL ARRAY\n")
        bcis_time, bcis_mem, cs_time, cs_mem = run_algorithms(random_s)
        file.write("BCIS time: " + bcis_time + "\n")
        file.write("CS time  : " + cs_time + "\n")
        file.write("BCIS memory: " + bcis_mem + "\n")
        file.write("CS memory  : " + cs_mem + "\n")

        file.write("\n# MEDIUM ARRAY\n")
        bcis_time, bcis_mem, cs_time, cs_mem = run_algorithms(random_m)
        file.write("BCIS time: " + bcis_time + "\n")
        file.write("CS time  : " + cs_time + "\n")
        file.write("BCIS memory: " + bcis_mem + "\n")
        file.write("CS memory  : " + cs_mem + "\n")

        file.write("\n# LARGE ARRAY\n")
        bcis_time, bcis_mem, cs_time, cs_mem = run_algorithms(random_l)
        file.write("BCIS time: " + bcis_time + "\n")
        file.write("CS time  : " + cs_time + "\n")
        file.write("BCIS memory: " + bcis_mem + "\n")
        file.write("CS memory  : " + cs_mem + "\n")

if __name__ == "__main__":
    main()