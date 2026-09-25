

# Content Domain 2: ML Model Development
<a name="machine-learning-engineer-associate-01-domain2"></a>

**Topics**

- [Content Domain 2: ML Model Development](#content-domain-2-ml-model-development)
  - [Task 2.1: Choose a modeling approach](#task-21-choose-a-modeling-approach)
  - [Task 2.2: Train and refine models](#task-22-train-and-refine-models)
  - [Task 2.3: Analyze model performance](#task-23-analyze-model-performance)
  - [See also](#see-also)

## Task 2.1: Choose a modeling approach
<a name="machine-learning-engineer-associate-01-domain2-task1"></a>

Knowledge of:

+ Capabilities and appropriate uses of ML algorithms to solve business problems
+ How to use AWS artificial intelligence (AI) services (for example, Amazon Translate, Amazon Transcribe, Amazon Rekognition, Amazon Bedrock) to solve specific business problems
+ How to consider interpretability during model selection or algorithm selection
+ Amazon SageMaker AI built-in algorithms and when to apply them

Skills in:

+ Assessing available data and problem complexity to determine the feasibility of an ML solution
+ Comparing and selecting appropriate ML models or algorithms to solve specific problems
+ Choosing built-in algorithms, foundation models, and solution templates (for example, in SageMaker JumpStart and Amazon Bedrock)
+ Selecting models or algorithms based on costs
+ Selecting AI services to solve common business needs

## Task 2.2: Train and refine models
<a name="machine-learning-engineer-associate-01-domain2-task2"></a>

Knowledge of:

+ Elements in the training process (for example, epoch, steps, batch size)
+ Methods to reduce model training time (for example, early stopping, distributed training)
+ Factors that influence model size
+ Methods to improve model performance
+ Benefits of regularization techniques (for example, dropout, weight decay, L1 and L2)
+ Hyperparameter tuning techniques (for example, random search, Bayesian optimization)
+ Model hyperparameters and their effects on model performance (for example, number of trees in a tree-based model, number of layers in a neural network)
+ Methods to integrate models that were built outside SageMaker AI into SageMaker AI

Skills in:

+ Using SageMaker AI built-in algorithms and common ML libraries to develop ML models
+ Using SageMaker AI script mode with SageMaker AI supported frameworks to train models (for example, TensorFlow, PyTorch)
+ Using custom datasets to fine-tune pre-trained models (for example, Amazon Bedrock, SageMaker JumpStart)
+ Performing hyperparameter tuning (for example, by using SageMaker AI automatic model tuning [AMT])
+ Integrating automated hyperparameter optimization capabilities
+ Preventing model overfitting, underfitting, and catastrophic forgetting (for example, by using regularization techniques, feature selection)
+ Combining multiple training models to improve performance (for example, ensembling, stacking, boosting)
+ Reducing model size (for example, by altering data types, pruning, updating feature selection, compression)
+ Managing model versions for repeatability and audits (for example, by using the SageMaker Model Registry)

## Task 2.3: Analyze model performance
<a name="machine-learning-engineer-associate-01-domain2-task3"></a>

Knowledge of:

+ Model evaluation techniques and metrics (for example, confusion matrix, heat maps, F1 score, accuracy, precision, recall, Root Mean Square Error [RMSE], receiver operating characteristic [ROC], Area Under the ROC Curve [AUC])
+ Methods to create performance baselines
+ Methods to identify model overfitting and underfitting
+ Metrics available in SageMaker Clarify to gain insights into ML training data and models
+ Convergence issues

Skills in:

+ Selecting and interpreting evaluation metrics and detecting model bias
+ Assessing tradeoffs between model performance, training time, and cost
+ Performing reproducible experiments by using AWS services
+ Comparing the performance of a shadow variant to the performance of a production variant
+ Using SageMaker Clarify to interpret model outputs
+ Using SageMaker Model Debugger to debug model convergence

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Certification. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-certification` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).