fibonacci_sequence = [0, 1]

for i in range(2, 20):
    next_term = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
    fibonacci_sequence.append(next_term)

print(fibonacci_sequence)
