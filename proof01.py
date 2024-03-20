def sum_of_natural_numbers(n):
    """
    Calculate the sum of the first n natural numbers using the formula n*(n+1)/2
    """
    return n * (n + 1) // 2

def prove_sum_of_natural_numbers(n):
    """
    Prove that the sum of the first n natural numbers is equal to n*(n+1)/2
    """
    # Calculate the sum of the first n natural numbers using a loop
    sum1 = sum(range(1, n + 1))

    # Calculate the sum of the first n natural numbers using the formula
    sum2 = sum_of_natural_numbers(n)

    # Check if the two sums are equal
    if sum1 == sum2:
        print(f"Proof succeeded for n = {n}")
    else:
        print(f"Proof failed for n = {n}")

if __name__ == "__main__":
    for n in range(1, 101):
        prove_sum_of_natural_numbers(n)