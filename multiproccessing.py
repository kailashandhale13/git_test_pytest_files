import multiprocessing

def square(n):
    return n * n

if __name__ == '__main__':
    # Define a list of numbers
    numbers = [1, 2, 3, 4, 5]

    # Create a Pool of worker processes
    with multiprocessing.Pool() as pool:
        # Apply the square function to each number in parallel
        results = pool.map(square, numbers)

    # Print the results
    print("Original numbers:", numbers)
    print("Squared numbers:", results)
