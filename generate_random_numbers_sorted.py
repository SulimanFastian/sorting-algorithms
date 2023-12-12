import random

class SortedNumberGenerator:
    def __init__(self, size, upper_range):
        self.size = size
        self.upper_range = upper_range

    def generate_and_write_to_file(self, file_name="SortedData.txt"):
        try:
            with open(file_name, "w") as file:
                sorted_numbers = [random.randint(1, self.upper_range -1)]
                for _ in range(self.size - 1):
                    difference = random.randint(1, 10)  # Generate a random difference
                    next_number = sorted_numbers[-1] + difference
                    sorted_numbers.append(next_number)

                file.write("\n".join(map(str, sorted_numbers)))
            print(f"Sorted numbers with random differences written to {file_name}")
        except IOError as e:
            print(f"Error writing to {file_name}: {e}")

# Usage example:
if __name__ == "__main__":
    size = int(input("Enter the number of sorted numbers: "))
    upper_range = int(input("Enter the upper range for random numbers: "))
    file_name = input("Enter the output file name (e.g., SortedData.txt): ")

    generator = SortedNumberGenerator(size, upper_range)
    generator.generate_and_write_to_file(file_name)

