import random

def generate_sorted(arr, file_name):
    with open(file_name, "w") as file:
        for number in arr:
            file.write(str(number) + "\n")

def generate_reversed(arr, file_name):
    arr.reverse()

    with open(file_name, "w") as file:
        for number in arr:
            file.write(str(number) + "\n")

def generate_random(arr, file_name):
    random.shuffle(arr)

    with open(file_name, "w") as file:
        for number in arr:
            file.write(str(number) + "\n")

def generate_array(size):
    return list(range(0, size))

def main():
    small_array = generate_array(500)
    medium_array = generate_array(5000)
    large_array = generate_array(50000)

    generate_sorted(small_array.copy(), "dataset/sorted_s.txt")
    generate_sorted(medium_array.copy(), "dataset/sorted_m.txt")
    generate_sorted(large_array.copy(), "dataset/sorted_l.txt")

    generate_reversed(small_array.copy(), "dataset/reversed_s.txt")
    generate_reversed(medium_array.copy(), "dataset/reversed_m.txt")
    generate_reversed(large_array.copy(), "dataset/reversed_l.txt")

    generate_random(small_array.copy(), "dataset/random_s.txt")
    generate_random(medium_array.copy(), "dataset/random_m.txt")
    generate_random(large_array.copy(), "dataset/random_l.txt")

if __name__ == "__main__":
    main()