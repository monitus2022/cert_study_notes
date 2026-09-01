# Machine Learning & Generative AI Model Architectures (AIF-C01)

Understanding the fundamental model architectures and algorithms helps you distinguish traditional ML from Generative AI, select appropriate model families for specific business tasks, and identify built-in AWS algorithm capabilities.

---

## 1. GPT (Generative Pre-trained Transformer)
* **Architecture**: **Decoder-only** Transformer architecture.
* **How It Works**: Operates **autoregressively**—predicts the single most likely next token in a sequence based strictly on preceding tokens (left-to-right processing).
* **Primary Use Cases**: Text generation, conversational dialogue (chatbots), creative content creation, code generation, and step-by-step reasoning.
* **Exam Key Concept**: Primary architecture behind modern Large Language Models (LLMs) specialized in natural language generation tasks.

---

## 2. BERT (Bidirectional Encoder Representations from Transformers)
* **Architecture**: **Encoder-only** Transformer architecture.
* **How It Works**: Processes text **bidirectionally**—reads the entire sequence of words simultaneously to evaluate both left and right context at once.
* **Primary Use Cases**: Text classification, sentiment analysis, Named Entity Recognition (NER), semantic search, and generating contextual embeddings (e.g., used in BERTScore).
* **Exam Key Concept**: Used for understanding and scoring text meaning rather than generating new generative text passages.

---

## 3. RNN (Recurrent Neural Network)
* **Architecture**: Traditional Deep Learning architecture for sequential data.
* **How It Works**: Processes sequential inputs step-by-step while maintaining an internal state (memory) to pass information from previous time steps to future ones.
* **Primary Use Cases**: Historical time-series forecasting, basic sequence-to-sequence translation, and speech recognition.
* **Exam Key Concept**: Pre-dates Transformers. Limited by sequential processing speed (cannot easily parallelize on GPUs) and struggles with long-range dependencies due to the **vanishing gradient problem**.

---

## 4. ResNet (Residual Network)
* **Architecture**: Deep Convolutional Neural Network (CNN) for Computer Vision.
* **How It Works**: Introduces **skip connections** (residual blocks) that allow gradient signals to bypass intermediate layers during backpropagation.
* **Primary Use Cases**: High-accuracy image classification, object detection, image segmentation, and visual feature extraction.
* **Exam Key Concept**: Solved the "degrading accuracy / vanishing gradient" issue in extremely deep neural networks, enabling computer vision models to train hundreds of layers deep.

---

## 5. SVM (Support Vector Machine)
* **Architecture**: Traditional Supervised Machine Learning algorithm.
* **How It Works**: Constructs an optimal decision boundary (**hyperplane**) in a high-dimensional feature space to maximize the margin between different data classes.
* **Primary Use Cases**: Binary/multiclass classification, fraud detection, spam filtering, and regression on structured tabular datasets.
* **Exam Key Concept**: Non-generative, traditional ML algorithm ideal for small to medium-sized structured datasets with clear separation margins.

---

## 6. WaveNet
* **Architecture**: Deep autoregressive neural network for raw audio generation.
* **How It Works**: Uses dilated causal convolutions to model raw audio waveforms sample-by-sample, generating highly natural sound textures.
* **Primary Use Cases**: High-fidelity Text-to-Speech (TTS) synthesis, synthetic voice generation, and realistic music generation.
* **Exam Key Concept**: Underpins modern neural voice generation systems (e.g., Amazon Polly Neural TTS) to produce human-like speech rather than robotic audio.

---

## 7. GAN (Generative Adversarial Network)
* **Architecture**: Deep Learning Generative framework consisting of two competing neural networks.
* **How It Works**: 
  * **Generator**: Creates synthetic data samples from random noise.
  * **Discriminator**: Evaluates whether the data sample is real (from training set) or fake (from Generator).
  * Both train simultaneously in a zero-sum game until the Generator produces realistic samples that fool the Discriminator.
* **Primary Use Cases**: Synthetic image generation, image-to-image translation, deepfake detection, and super-resolution upscaling.
* **Exam Key Concept**: A non-Transformer generative AI framework primarily used for media and visual synthesis.

---

## 8. XGBoost (eXtreme Gradient Boosting)
* **Architecture**: Traditional Supervised ML algorithm based on Gradient Boosted Decision Trees (GBDT).
* **How It Works**: Combines predictions from an ensemble of weak decision trees, where each consecutive tree is trained to correct the errors/residuals made by previous trees.
* **Primary Use Cases**: High-performance classification, regression, customer churn prediction, credit scoring, and ranking on structured tabular data.
* **Exam Key Concept**: One of the most common built-in, highly optimized algorithms in **Amazon SageMaker** for structured tabular business data.

---

## Exam Quick-Recall Matrix

| Model / Algorithm | Category | Primary Data Type | Key AIF-C01 Trigger |
| :--- | :--- | :--- | :--- |
| **GPT** | GenAI (Decoder Transformer) | Text | Natural language text generation & conversational response |
| **BERT** | DL (Encoder Transformer) | Text | Bidirectional text understanding, classification & embeddings |
| **RNN** | Traditional Deep Learning | Sequential / Time-Series | Sequential step-by-step processing (legacy NLP/time-series) |
| **ResNet** | Deep Learning (CNN) | Image / Vision | Computer vision & image classification with skip connections |
| **SVM** | Traditional Machine Learning | Structured / Tabular | Finding hyperplanes for classification on tabular data |
| **WaveNet** | Generative AI (Audio) | Raw Audio Waveforms | Text-to-Speech (TTS) & human-like voice synthesis |
| **GAN** | Generative AI (Adversarial) | Images / Synthetic Data | Generator vs. Discriminator dual-network image synthesis |
| **XGBoost** | Traditional ML (Ensemble) | Structured / Tabular | Gradient boosted trees for tabular prediction in SageMaker |