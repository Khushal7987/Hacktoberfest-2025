def fibonacci_sequence(n_terms):
    if n_terms <= 0:
        return []
    if n_terms == 1:
        return [0]

    sequence = [0, 1]
    
    # Loop to generate the sequence
    for _ in range(2, n_terms):
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
        
    return sequence

# Example Usage
N_TERMS = 8
print(f"Fibonacci Sequence ({N_TERMS} terms): {fibonacci_sequence(N_TERMS)}")
# Output: [0, 1, 1, 2, 3, 5, 8, 13]
