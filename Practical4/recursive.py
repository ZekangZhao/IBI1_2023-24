a = 4  # the first number of the sequence
i = 0  # this initialization is not necessary if using range()

# Repeat 5 times using a for loop
for i in range(5):  # 'i' will take on the values 0 to 4
    print(a)  # Display the current value of 'a'
    a = 2 * a + 3  # Calculate the next value in the sequence

# Note: The variable 'i' is not used after being incremented in the loop, so you could simplify the loop as follows:
for _ in range(5):
    print(a)
    a = 2 * a + 3