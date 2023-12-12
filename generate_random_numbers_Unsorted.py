import random

class RandomNumberGenerator:
    def generate_and_write_to_file(self):
        try:
            size = int(input("Enter the number of random numbers: "))
            inRange = int (input ("Enter the upper range in with you want to make random numbers: "))
            file_name = input("Enter the output file name (e.g., Data.txt): ")

            with open(file_name, "w") as file:
                random_numbers = [random.randint(1, inRange-1) for _ in range(size)]
                file.write("\n".join(map(str, random_numbers)))
            print(f"Random numbers written to {file_name}")
        except (ValueError, IOError) as e:
            print(f"Error: {e}")

# Usage example:
if __name__ == "__main__":
    generator = RandomNumberGenerator()
    generator.generate_and_write_to_file()
