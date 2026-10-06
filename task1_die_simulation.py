import numpy as np
import matplotlib.pyplot as plt
# Fix the random seed for reproducible results
np.random.seed(42)
# Roll a fair six-sided die 1000 times
rolls = np.random.randint(1, 7, size=1000)
# Print first 10 rolls
print("First 10 rolls:", rolls[:10])
# Count occurrences of each face
faces, counts = np.unique(rolls, return_counts=True)
print("\nFace Count Empirical P Theoretical P")
for face, count in zip(faces, counts):
    empirical_probability = count / 1000
    theoretical_probability = 1 / 6
    print(
        f"{face:>4} "
        f"{count:>5} "
        f"{empirical_probability:>10.4f} "
        f"{theoretical_probability:>14.4f}"
    )
# Create histogram
plt.figure(figsize=(7, 5))
plt.hist(
    rolls,
    bins=np.arange(0.5, 7.5, 1),
    edgecolor="black",
    rwidth=0.85
)
plt.xticks(range(1, 7))
plt.xlabel("Die Face")
plt.ylabel("Frequency")
plt.title("Fair Die Rolls - 1000 Simulations")
plt.tight_layout()
# Save histogram
plt.savefig("die_rolls.png", dpi=150)
plt.close()
print("\nSaved die_rolls.png")