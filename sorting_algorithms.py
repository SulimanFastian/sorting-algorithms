import math, time, sys

# 👇️ 1000
print(sys.getrecursionlimit())

# 👇️ set recursion limit to 2000
sys.setrecursionlimit(2000000)

class Sorting:
    def __init__(self):
        self.data = []

    def load_data(self, file_name):

        try:
            with open(file_name, 'r') as file:
                self.data = [int(line.strip()) for line in file]

        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    def insertion_sort(self):
        start_time = time.time()
        sorted_list = self.data.copy()
        for i in range(1, len(sorted_list)):
            key = sorted_list[i]
            j = i - 1
            while j >= 0 and key < sorted_list[j]:
                sorted_list[j + 1] = sorted_list[j]
                j -= 1
            sorted_list[j + 1] = key
        end_time = time.time()
        return sorted_list, end_time - start_time
    


    def merge_sort(self):
        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])
            return result

        start_time = time.time()
        def merge_sort_helper(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            left_sorted = merge_sort_helper(left_half)
            right_sorted = merge_sort_helper(right_half)

            return merge(left_sorted, right_sorted)

        sorted_list = merge_sort_helper(self.data.copy())
        end_time = time.time()
        return sorted_list, end_time - start_time
    

    def quick_sort(self):
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1

            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1

        def quick_sort_helper(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quick_sort_helper(arr, low, pi - 1)
                quick_sort_helper(arr, pi + 1, high)

        start_time = time.time()
        sorted_list = self.data.copy()
        quick_sort_helper(sorted_list, 0, len(sorted_list) - 1)
        end_time = time.time()
        return sorted_list, end_time - start_time



    def bucket_sort(self):

        def merge_sort(arr):
            def merge(left, right):
                result = []
                i = j = 0

                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        result.append(left[i])
                        i += 1
                    else:
                        result.append(right[j])
                        j += 1

                result.extend(left[i:])
                result.extend(right[j:])
                return result

            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            left_sorted = merge_sort(left_half)
            right_sorted = merge_sort(right_half)
            return merge(left_sorted, right_sorted)
        # --------------------------------------------------------------------<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        sorted_list = self.data.copy()
        # Divide each element by 100 to make them fall within the range 0-1

        # Calculate the division factor based on the number of digits in the maximum value
        max_value = max(sorted_list)
        num_digits = len(str(abs(max_value)))
        division_factor = 10 ** (num_digits - 1)

        print (division_factor)

    # Divide each element by the calculated division factor
        normalized_data = [num / division_factor for num in sorted_list]

        start_time = time.time()

        # Define the number of buckets (0-9)
        num_buckets = 10
        # Create empty buckets
        buckets = [[] for _ in range(num_buckets)]
        
        
        for num in normalized_data:
            # Calculate the bucket index using floor function
            bucket_index = min(int(math.floor(num * num_buckets)), num_buckets - 1)
            buckets[bucket_index].append(num)

        # Apply Merge Sort to buckets with more than one element and measure execution time
        start_time = time.time()
        for i in range(num_buckets):
            if len(buckets[i]) > 1:
                buckets[i]= merge_sort(buckets[i])
        end_time = time.time()

        # Concatenate the sorted buckets to get the final sorted list
        sorted_list = [math.floor(num*100) for bucket in buckets for num in bucket]
        return sorted_list, end_time - start_time


    def radix_sort(self):
        def counting_sort(arr, exp):
            n = len(arr)
            output = [0] * n
            count = [0] * 10

            for i in range(n):
                index = (arr[i] // exp)
                count[index % 10] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            i = n - 1
            while i >= 0:
                index = (arr[i] // exp)
                output[count[index % 10] - 1] = arr[i]
                count[index % 10] -= 1
                i -= 1

            i = 0
            for i in range(0, len(arr)):
                arr[i] = output[i]

        start_time = time.time()

        sorted_list = self.data.copy()       
        if len(sorted_list) > 0:
            max_num = max(sorted_list)

            exp = 1
            while max_num // exp > 0:
                counting_sort(sorted_list, exp)
                exp *= 10

        end_time = time.time()
        return sorted_list, end_time - start_time



def main():
    sorting = Sorting()
    file_name = input("Enter the name of the text file containing numbers: ")
    sorting.load_data(file_name)

    while True:
        print("\nChoose a sorting algorithm:")
        print("1. Insertion Sort")
        print("2. Merge Sort")
        print("3. Quick Sort")
        print("4. Bucket Sort")
        print("5. Radix Sort")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            sorted_list, execution_time = sorting.insertion_sort()
            #print("Insertion Sort Result:", sorted_list)
            print(f"Execution Time: {execution_time} seconds")

        elif choice == '2':
            sorted_list, execution_time = sorting.merge_sort()
            #print("Merge Sort Result:", sorted_list)
            print(f"Execution Time: {execution_time} seconds")

        elif choice == '3':
            sorted_list, execution_time = sorting.quick_sort()
            #print("Quick Sort Result:", sorted_list)
            print(f"Execution Time: {execution_time} seconds")

        elif choice == '4':
            sorted_list, execution_time = sorting.bucket_sort()
            #print("Bucket Sort Result:", sorted_list)
            print(f"Execution Time: {execution_time} seconds")

        elif choice == '5':
            sorted_list, execution_time = sorting.radix_sort()
            #print("Radix Sort Result:", sorted_list)
            print(f"Execution Time: {execution_time} seconds")

        elif choice == '6':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid option (1-6).")

if __name__ == "__main__":
    main()
