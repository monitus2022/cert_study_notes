# Amazon SageMaker Built-in Algorithms

```text
├── Regression / Classification
│    ├── Linear Learner
│    ├── XGBoost
│    ├── LightGBM
│    └── Factorization Machines
├── Time Series Forecasting
│    └── DeepAR
├── Natural Language Processing (NLP)
│    ├── BlazingText
│    ├── Object2Vec
│    ├── Neural Topic Model (LDA)
│    └── Latent Dirichlet Allocation (LDA)
├── Computer Vision (Images)
│    ├── Object Detection
│    ├── Image Classification
│    └── Semantic Segmentation
├── Anomaly Detection
│    ├── Random Cut Forest
│    └── IP Insights
├── Dimensionality Reduction
│    └── Principal Component Analysis (PCA)
├── Clustering
│    └── K-Means Clustering
├── Nearest Neighbor Search
│    └── K-Nearest Neighbors (KNN)
├── Sequence Modeling
│    └── Seq2Seq
```

## 1. Regression & Classification

### Linear Learner

* **Use Case:** Continuous regression or binary/multiclass classification.
* **Input Formats:** `recordIO-protobuf` (float32, optimal performance) or `text/csv`.
* **Exam Triggers:** Requires feature normalization. Automatically fits multiple models with different hyperparameters (L1/L2 penalties) in parallel and selects the best one.

### XGBoost

* **Use Case:** Gradient-boosted decision trees for tabular classification and regression.
* **Input Formats:** `text/csv` or `recordIO-protobuf` (libsvm format).
* **Exam Triggers:** Default choice for structured tabular datasets. Automatically handles missing (`NaN`) values. Memory-bound (requires sufficient instance RAM).

### LightGBM

* **Use Case:** Fast, high-performance gradient boosting on large-scale tabular data.
* **Input Formats:** `text/csv` or `recordIO-protobuf`.
* **Exam Triggers:** Chosen over XGBoost when training speed and lower memory consumption on massive datasets are the primary constraints. Uses leaf-wise tree growth.

### Factorization Machines (FM)

* **Use Case:** Click-Through Rate (CTR) prediction and personalized recommendation systems.
* **Input Formats:** `recordIO-protobuf` with sparse float32 vectors.
* **Exam Triggers:** High-dimensional **sparse datasets** (e.g., large sparse user-item interaction matrices). Learns pairwise feature interactions efficiently.

---

## 2. Time Series Forecasting

### DeepAR

* **Use Case:** Forecasting multiple 1D scalar time series using Recurrent Neural Networks (RNN/LSTM).
* **Input Formats:** `JSON Lines` (`JSONL`), requiring `start` timestamp and `target` array fields.
* **Exam Triggers:** Outputs **probabilistic forecasts** (quantiles, e.g., 10th, 50th, 90th percentiles) rather than point estimates. Handles cold-start items (new products with little historical data) by learning across multiple related time series.

---

## 3. Natural Language Processing (NLP)

### BlazingText

* **Use Case:** Word embeddings (**Word2Vec**) and supervised **Text Classification**.
* **Input Formats:** Plain text files (one document per line, space-separated tokens). For classification, target labels must start with the prefix `__label__`.
* **Exam Triggers:** Ultra-fast text classification and word vector generation. Uses GPU or multi-core CPU optimizations (Skip-gram / CBOW).

### Object2Vec

* **Use Case:** High-dimensional pair-wise embedding representations (e.g., sentence similarity, customer-to-product matching).
* **Input Formats:** Integer-encoded token pairs in `JSON Lines`.
* **Exam Triggers:** Generalization of Word2Vec to arbitrary pairs of structured objects (e.g., Word-Sentence, User-Item).

### Neural Topic Model (NTM)

* **Use Case:** Unsupervised grouping of text documents into $k$ topics using Variational Autoencoders (Deep Learning).
* **Input Formats:** `recordIO-protobuf` or `text/csv` (Word-count or Bag-of-Words vectors).
* **Exam Triggers:** Neural network-based alternative to LDA; scales better to massive text corpora.

### Latent Dirichlet Allocation (LDA)

* **Use Case:** Unsupervised topic discovery in text collections using statistical probability distributions.
* **Input Formats:** `recordIO-protobuf` or `text/csv` (Word-count vectors).
* **Exam Triggers:** Non-neural network statistical algorithm. **CPU-only** (does not support GPU training).

---

## 4. Computer Vision (Images)

### Image Classification

* **Use Case:** Assigning a single categorical label to an entire input image.
* **Input Formats:** Apache MXNet `RecordIO` or raw images (`JPEG`/`PNG`) with image manifest files.
* **Exam Triggers:** Uses ResNet architecture. Supports **Transfer Learning** (fine-tuning pre-trained weights) or full training from scratch. **GPU instance required**.

### Object Detection

* **Use Case:** Locating and classifying multiple objects within an image using bounding boxes.
* **Input Formats:** `RecordIO` or `JPEG` with JSON annotation files.
* **Exam Triggers:** Output includes bounding box coordinates $[x_{\min}, y_{\min}, x_{\max}, y_{\max}]$ and confidence scores. Uses Single Shot multibox Detector (SSD). **GPU instance required**.

### Semantic Segmentation

* **Use Case:** Pixel-level classification of images (e.g., autonomous driving, medical imaging).
* **Input Formats:** `PNG` images alongside matching ground-truth mask images.
* **Exam Triggers:** Labels **every individual pixel** in an image. **GPU instance required**.

---

## 5. Anomaly Detection

### Random Cut Forest (RCF)

* **Use Case:** Unsupervised detection of anomalous points in streaming or batch data.
* **Input Formats:** `recordIO-protobuf` or `text/csv`.
* **Exam Triggers:** Assigns an **anomaly score** to each data point (high score = outlier). Does not require labeled training data.

### IP Insights

* **Use Case:** Unsupervised detection of suspicious IP address behavior in user logins.
* **Input Formats:** `text/csv` containing `(Entity_ID, IP_Address)` tuples.
* **Exam Triggers:** Uses neural network embeddings to catch anomalous access patterns given a user ID/account and an IP address.

---

## 6. Dimensionality Reduction & Clustering

### Principal Component Analysis (PCA)

* **Use Case:** Unsupervised linear feature reduction.
* **Input Formats:** `recordIO-protobuf` or `text/csv`.
* **Exam Triggers:** Reduces feature dimension while preserving maximum variance. Features two modes: `regular` (for small-to-medium datasets) and `randomized` (for high-dimensional datasets).

### K-Means Clustering

* **Use Case:** Unsupervised grouping of unlabeled data points into $k$ distinct clusters.
* **Input Formats:** `recordIO-protobuf` or `text/csv`.
* **Exam Triggers:** Requires specifying $k$ in advance. Uses Euclidean distance. Uses `web-scale k-means` to process large datasets.

---

## 7. Search & Sequence Modeling

### K-Nearest Neighbors (KNN)

* **Use Case:** Supervised classification or regression based on proximity to nearest $k$ data points.
* **Input Formats:** `recordIO-protobuf` or `text/csv` (first column = target).
* **Exam Triggers:** Non-parametric algorithm. Builds a searchable index (dimension reduction) for low-latency inference. Distance metrics: L2, Cosine, or Inner Product.

### Seq2Seq (Sequence-to-Sequence)

* **Use Case:** Supervised sequence translation (e.g., Machine Translation, Text Summarization, Speech-to-Text).
* **Input Formats:** `RecordIO-protobuf` containing integer-encoded tokens.
* **Exam Triggers:** Uses RNNs/CNNs with **Attention mechanisms**. Requires three separate input channels: training, validation, and vocabulary (`vocab.json`). **GPU instance required**.

---

## Quick Reference Summary Table

| Category | Algorithm | Supervised / Unsupervised | GPU Required? | Core Exam Keyword |
| --- | --- | --- | --- | --- |
| **Tabular** | XGBoost | Supervised | Optional | Default choice for tabular data; handles missing values |
| **Recommendation** | Factorization Machines | Supervised | Optional | Click-through rate prediction; sparse matrix |
| **Time Series** | DeepAR | Supervised | Optional | Probabilistic quantiles; `JSONL` format |
| **Text Vectors** | BlazingText | Both | Yes (Word2Vec) | Fast Word2Vec / text classification (`__label__`) |
| **Topic Modeling** | NTM vs. LDA | Unsupervised | NTM (GPU) / LDA (CPU) | Topic extraction; NTM scales better on large data |
| **Anomaly** | Random Cut Forest | Unsupervised | No (CPU) | Streaming data anomaly scores |
| **Security** | IP Insights | Unsupervised | Yes (GPU) | Login activity analysis on `(User, IP)` pairs |
| **Vision** | Object Detection | Supervised | Yes | Bounding box prediction $[x_{\min}, y_{\min}, x_{\max}, y_{\max}]$ |
| **Vision** | Semantic Segmentation | Supervised | Yes | Pixel-by-pixel mask classification |