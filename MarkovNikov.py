# Initializing values

S = ["walk", "run", "rest"]      # Hidden states
V = ["low", "med", "high"]       # Observations

pi = [0.5, 0.3, 0.2]             # Initial probabilities

A = [[0.6, 0.3, 0.1],
     [0.2, 0.5, 0.3],
     [0.3, 0.2, 0.5]]

B = [[0.6, 0.3, 0.1],
     [0.1, 0.3, 0.6],
     [0.7, 0.2, 0.1]]

O = ["high", "med", "low", "high"]

# Observation index
obs = {
    "low": 0,
    "med": 1,
    "high": 2
}

alpha = []

# ---------------- Initialization ----------------

print("Initialization")

first = []

for i in range(len(S)):
    value = round(pi[i] * B[i][obs[O[0]]], 3)
    first.append(value)

    print(f"α1({S[i]}) = {pi[i]} x {B[i][obs[O[0]]]} = {value}")

alpha.append(first)

# ---------------- Recursion ----------------

for t in range(1, len(O)):

    print(f"\nObservation {t+1}: {O[t]}")

    current = []

    for j in range(len(S)):

        total = 0

        for i in range(len(S)):
            total += alpha[t-1][i] * A[i][j]

        value = round(total * B[j][obs[O[t]]], 3)

        current.append(value)

        print(f"α{t+1}({S[j]}) = {value}")

    alpha.append(current)

# ---------------- Final Answer ----------------

print("\nAlpha Table")

for row in alpha:
    print(row)

probability = round(sum(alpha[-1]), 3)

print("\nProbability of Observation Sequence =", probability)