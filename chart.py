import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ["Spam", "Legitimate"]
free_present = [240, 70]
free_absent = [60, 630]

x = np.arange(len(categories))
width = 0.35

plt.figure(figsize=(8, 5))

# Grouped bars
plt.bar(x - width/2, free_present, width, label="FREE Present")
plt.bar(x + width/2, free_absent, width, label="FREE Absent")

# Labels and title
plt.title("Distribution of FREE in Spam and Legitimate Emails")
plt.xlabel("Email Class")
plt.ylabel("Number of Emails")
plt.xticks(x, categories)
plt.legend()

# Add values on top of bars
for i, value in enumerate(free_present):
    plt.text(i - width/2, value + 10, str(value), ha='center')
for i, value in enumerate(free_absent):
    plt.text(i + width/2, value + 10, str(value), ha='center')

plt.tight_layout()
plt.savefig("free_distribution_chart.png", dpi=300, bbox_inches="tight")
plt.show()