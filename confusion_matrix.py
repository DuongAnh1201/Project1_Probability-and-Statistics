import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

cm = np.array([
    [240, 60],
    [70, 630]
])

labels = np.array([
    ["TP\n240", "FN\n60"],
    ["FP\n70", "TN\n630"]
])

plt.figure(figsize=(7, 6))

sns.heatmap(
    cm,
    annot=labels,
    fmt="",
    cmap="Blues",
    cbar=True,
    linewidths=1,
    linecolor="white",
    xticklabels=["Predicted Spam", "Predicted Legitimate"],
    yticklabels=["Actual Spam", "Actual Legitimate"]
)

plt.title("Confusion Matrix of FREE-Based Spam Classifier", fontsize=14)
plt.xlabel("Predicted Class")
plt.ylabel("Actual Class")

plt.tight_layout()

# Save high-quality figure for report
plt.savefig("confusion_matrix.png", dpi=300, bbox_inches="tight")

plt.show()