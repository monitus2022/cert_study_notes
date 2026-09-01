# Model Performance, Metrics & Evaluation (AIF-C01)

Evaluating machine learning model performance requires choosing the right metric for the task type (Classification vs. Regression), identifying model fit issues (Overfitting vs. Underfitting), and understanding the Tradeoffs between Bias and Variance.

---

## 1. Model Fit: Overfitting vs. Underfitting

Model fit describes how well a trained machine learning model generalizes to unseen test data.

* **Underfitting (High Bias)**:
  * **What Happens**: The model is too simple to capture the underlying patterns in the training data.
  * **Performance**: Performs poorly on **both** training data and testing data.
  * **Fixes**: Increase model complexity, add more relevant features, reduce regularization penalties, or train for more epochs.
* **Overfitting (High Variance)**:
  * **What Happens**: The model memorizes training noise and details rather than general patterns.
  * **Performance**: High accuracy on training data, but poor performance on unseen test data.
  * **Fixes**: Add more training data, apply regularization (L1/L2), implement dropout, simplify model architecture, or use early stopping.
* **Ideal (Balanced) Fit**:
  * Low training error and low generalization test error.

---

## 2. Bias-Variance Tradeoff

* **Bias**: Error introduced by approximating a real-world complex problem with a simplified model. High bias leads to **underfitting**.
* **Variance**: Model's sensitivity to small fluctuations/noise in the training dataset. High variance leads to **overfitting**.
* **The Tradeoff**: As you increase model complexity, bias decreases but variance increases. Goal is to find the sweet spot minimizing total error.

---

## 3. Confusion Matrix & Classification Metrics

A Confusion Matrix evaluates binary and multiclass classification performance by comparing Actual vs. Predicted labels.

### Matrix Structure
* **True Positive (TP)**: Correctly predicted positive class (e.g., predicted Fraud, actually Fraud).
* **True Negative (TN)**: Correctly predicted negative class (e.g., predicted Legitimate, actually Legitimate).
* **False Positive (FP - Type I Error)**: Incorrectly predicted positive class (e.g., predicted Fraud, actually Legitimate).
* **False Negative (FN - Type II Error)**: Incorrectly predicted negative class (e.g., predicted Legitimate, actually Fraud).

### Key Classification Formulas & Exam Anchors

* **Accuracy**:
  * *Formula*: (TP + TN) / (TP + TN + FP + FN)
  * *Best Used*: Balanced datasets where positive and negative classes are equal.
  * *Exam Trap*: Misleading for imbalanced datasets (e.g., 99% accuracy in fraud detection where 99% of data is non-fraud).
* **Precision**:
  * *Formula*: TP / (TP + FP)
  * *Focus*: Minimizing **False Positives**.
  * *Exam Anchor*: Use when the cost of a False Positive is high (e.g., Spam filtering—marking an important email as spam is bad).
* **Recall (Sensitivity)**:
  * *Formula*: TP / (TP + FN)
  * *Focus*: Minimizing **False Negatives**.
  * *Exam Anchor*: Use when the cost of a False Negative is catastrophic (e.g., Disease diagnosis or Fraud detection—missing a true fraud/disease case is dangerous).
* **Specificity**:
  * *Formula*: TN / (TN + FP)
  * *Focus*: Proportion of actual negative cases correctly identified.
* **F1-Score**:
  * *Formula*: 2 * (Precision * Recall) / (Precision + Recall)
  * *Focus*: Harmonic mean balancing Precision and Recall.
  * *Exam Anchor*: Best single metric for **imbalanced classification datasets**.

---

## 4. AUC-ROC Curve

* **ROC Curve (Receiver Operating Characteristic)**: Plots the **True Positive Rate (Recall)** against the **False Positive Rate (1 - Specificity)** across all possible decision thresholds ($0.0$ to $1.0$).
* **AUC (Area Under the Curve)**: Single numerical value ($0.0$ to $1.0$) measuring the model's ability to distinguish between positive and negative classes across all thresholds.
  * **AUC = 0.5**: Random guessing (no discriminative power).
  * **AUC = 1.0**: Perfect classification model.
* **Exam Anchor**: Ideal when evaluating model performance across multiple decision thresholds or when ranking predictions regardless of a fixed cut-off threshold.

---

## 5. Regression Evaluation Metrics

Regression metrics evaluate continuous numerical predictions (e.g., predicting housing prices, stock values, or server load).

* **MAE (Mean Absolute Error)**:
  * *Mechanism*: Average of absolute differences between actual values and predicted values.
  * *Key Property*: Measures average magnitude of error in the same units as the target variable. **Robust to outliers**.
* **MAPE (Mean Absolute Percentage Error)**:
  * *Mechanism*: Average of absolute percentage errors relative to actual values.
  * *Key Property*: Expresses error as a percentage (e.g., 5% error), making it easy to interpret across different scales.
* **RMSE (Root Mean Squared Error)**:
  * *Mechanism*: Square root of average squared differences between actual and predicted values.
  * *Key Property*: Heavily penalizes **large errors and outliers** because differences are squared before averaging. Same units as target variable.
* **R-Squared ($R^2$ / Coefficient of Determination)**:
  * *Mechanism*: Measures the proportion of variance in the target variable that is explained by the regression model ($0.0$ to $1.0$ or $0\%$ to $100\%$).
  * *Key Property*: $R^2 = 1.0$ means the model explains 100% of the target variability.

---

## 6. Exam Selection Cheat Sheet

| Business Problem / Scenario | Primary Metric to Select | Key Exam Trigger |
| :--- | :--- | :--- |
| **Imbalanced Classification Dataset** | **F1-Score** | "Unbalanced class labels", "Harmonic mean of precision/recall" |
| **Cost of False Positives is High** | **Precision** | "Minimize false alarms (e.g., spam detection)" |
| **Cost of False Negatives is High** | **Recall** | "Minimize missed positive detections (e.g., disease/fraud)" |
| **Threshold-independent evaluation** | **AUC-ROC** | "Evaluating performance across various classification thresholds" |
| **Regression penalizing large errors** | **RMSE** | "Heavy penalty for large prediction outliers" |
| **Regression robust to outliers** | **MAE** | "Linear scale of absolute errors, less sensitive to extreme values" |
| **Model explaining variance percentage** | **R-Squared ($R^2$)** | "Percentage of target variable variance explained" |