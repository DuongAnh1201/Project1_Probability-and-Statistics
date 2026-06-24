# Probability Analysis of Spam Email Detection Using the Word "FREE"

## Overview

This project analyzes a dataset of **1,000 emails** to investigate whether the presence of the word **"FREE"** can be used as an indicator of spam. Using concepts from Probability and Statistics, the project computes marginal, joint, and conditional probabilities, evaluates event independence, and assesses the performance of a simple spam classifier.

The study demonstrates how probabilistic reasoning can be applied to real-world classification problems such as spam filtering.

---

## Problem Statement

Given a dataset of 1,000 emails:

* 300 Spam emails
* 700 Legitimate emails
* 240 Spam emails contain the word **FREE**
* 70 Legitimate emails contain the word **FREE**

The objective is to determine whether the occurrence of the word **FREE** is associated with spam emails and whether it can be used as a useful feature for spam classification.

---

## Learning Objectives

This project applies the following Probability and Statistics concepts:

* Marginal Probability
* Joint Probability
* Conditional Probability
* Addition Rule
* Multiplication Rule
* Event Independence
* Confusion Matrix Analysis
* Classification Metrics

  * Accuracy
  * Precision
  * Recall
  * F1 Score
  * False Positive Rate

---

## Dataset

| Email Type | FREE    | No FREE | Total    |
| ---------- | ------- | ------- | -------- |
| Spam       | 240     | 60      | 300      |
| Legitimate | 70      | 630     | 700      |
| **Total**  | **310** | **690** | **1000** |

---

## Key Results

### Probability of Spam Given FREE

[
P(\text{Spam}|\text{FREE})=\frac{240}{310}=0.7742
]

An email containing the word **FREE** has a **77.42% probability** of being spam.

### Independence Test

[
P(\text{Spam} \cap \text{FREE})=0.24
]

[
P(\text{Spam})P(\text{FREE})=0.30\times0.31=0.093
]

Since:

[
0.24 \neq 0.093
]

Spam and FREE are **not independent events**.

### Classifier Performance

Using the rule:

> Predict Spam whenever the word FREE appears.

| Metric    | Value  |
| --------- | ------ |
| Accuracy  | 87.00% |
| Precision | 77.42% |
| Recall    | 80.00% |
| F1 Score  | 78.69% |

---

## Repository Structure

```text
.
├── README.md
├── report/
│   └── Report_Project_1.pdf
│
├── slides/
│   └── Probability_Spam_Filter_Presentation.pptx
│
├── handwritten-work/
│   ├── page1.jpg
│   ├── page2.jpg
│   └── page3.jpg
│
├── figures/
│   ├── confusion_matrix.png
│   └── free_distribution_chart.png
│
└── code/
    ├── confusion_matrix.py
    └── distribution_chart.py
```

---

## Visualizations

### Confusion Matrix

The confusion matrix summarizes the performance of the FREE-based spam classifier.

* True Positives (TP): 240
* False Positives (FP): 70
* False Negatives (FN): 60
* True Negatives (TN): 630

### Distribution Chart

A bar chart is included to visualize the distribution of FREE and non-FREE emails across spam and legitimate categories.

---

## Files Included

### Report

A complete written report describing:

* Dataset analysis
* Probability computations
* Independence testing
* Spam classification evaluation
* Interpretation of results

### Slides

Presentation slides summarizing:

* Problem statement
* Dataset
* Probability analysis
* Independence testing
* Confusion matrix
* Conclusions

### Handwritten Work

Original handwritten calculations used to derive probability formulas and verify results.

### Source Code

Python scripts used to generate:

* Confusion matrix heatmap
* Distribution bar chart

---

## Conclusion

The analysis shows that the word **FREE** is strongly associated with spam emails. Although the classifier achieves an accuracy of **87%**, relying on a single keyword can still produce false positives and false negatives. In practice, modern spam filters combine many features to improve classification performance and reliability.

---

## Author

**Duong Anh (Tom) Nguyen**

**Course:** Probability and Statistics
**Instructor:** Satarupa Mukherjee
**Date:** June 2026
