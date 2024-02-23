def count_letters(k):
    # Initial values
    number_of_A = 1
    number_of_B = 0

    # Counting letters after K button presses
    for _ in range(k):
        new_A = number_of_B
        new_B = number_of_A + number_of_B

        # Update counts
        number_of_A = new_A
        number_of_B = new_B

    return number_of_A, number_of_B

# Input
k = int(input())

# Calculate the number of letters A and B
result_A, result_B = count_letters(k)

# Output
print(f"{result_A} {result_B}")
