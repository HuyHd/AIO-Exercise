def max_kernel(num_list, k):
    """
    This function aim to check the k size of the sliding window must be greater than or equal to 1.
    Then calculate the maximum value for the each window and print it.

    Parameters:
    - num_list: Input list.
    - k: Input size of sliding window.

    Returns:
    Print each sliding window along with its maximum value and maximum list.
    """
    # Define sliding window and max values list
    window = []
    max_values = []

    # Check k size
    if k < 1:
        raise ValueError(
            "The size k of the sliding window must be greater than or equal to 1."
        )

    # Slide the window over the list and finding the maximum for each window.
    for i in range(len(num_list) + 1 - k):
        window.append(num_list[i: i + k])
        max_values.append(max(window[i]))
        print(f"{window[i]} => max {max_values[i]}")
    return max_values


# Testcases:
if __name__ == "__main__":
    assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5], "Test case 1 failed"
    print("Test cases passed.")
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    print(f"Out put: {max_kernel(num_list, k)}")
