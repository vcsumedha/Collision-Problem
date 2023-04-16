import random

def collision_classical(F, N):
    # Choose a random subset of size k = c * sqrt(N)
    c = 1.18  # constant factor for subset size
    k = int(c * (N ** 0.5))
    subset = random.sample(range(N), k)

    # Evaluate the function F on the subset
    pairs = [(x, F(x)) for x in subset]

    # Sort the pairs by the second entry (F(x))
    pairs_sorted = sorted(pairs, key=lambda pair: pair[1])

    # Check for collisions in the sorted pairs
    for i in range(k-1):
        if pairs_sorted[i][1] == pairs_sorted[i+1][1]:
            return (pairs_sorted[i][0], pairs_sorted[i+1][0])

    # No collisions found
    return None

def main():
    # Example usage
    N = 10000
    def F(x):
        return x**2 % N
    collision = collision_classical(F, N)
    if collision is not None:
        print("Collision found: {} and {}".format(collision[0], collision[1]))
    else:
        print("No collision found.")

main()