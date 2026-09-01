Question 1
Multiple Choice
Time to answer:
32 seconds
Answer status:
Correct
Question
A company wants to use an open source foundation model (FM) to evaluate if contracts adhere to compliance rules.


Which AWS service will meet these requirements?

Answer options
Option
Correct answer
Your selection
Rationale
A. Amazon Textract
Not selected
Amazon Textract is a service that you can use to add document text detection and analysis to applications. You can use Amazon Textract to identify handwritten text, to extract text from documents, and to extract specific information from documents. Amazon Textract does not provide access to FMs.


Learn more about Amazon Textract .

B. Amazon SageMaker JumpStart
Correct
Selected
SageMaker JumpStart is a feature of SageMaker AI that provides pre-trained, open source models for you to use. SageMaker JumpStart offers FMs that you can use for summarization use cases.


Learn more about SageMaker JumpStart .

C. Amazon Q Business
Not selected
Amazon Q Business is a generative AI virtual assistant that can answer questions, summarize content, generate content, and complete tasks based on the data that is provided. Amazon Q Business does not provide access to FMs. Amazon Q is not open source.


Learn more about Amazon Q Business .

D. Amazon Kendra
Not selected
Amazon Kendra is an intelligent search service that provides answers to questions based on the data that is provided. Amazon Kendra uses semantic and contextual understanding to provide specific answers. Amazon Kendra does not provide access to FMs.


Learn more about Amazon Kendra .

Question 2
Multiple Choice
Time to answer:
8 seconds
Answer status:
Correct
Question
A company uses Amazon SageMaker AI for its ML models. The company wants to implement a solution for model owners to create a record of model information. The model information should include intended uses, risk ratings, training details, and evaluation results.


Which SageMaker AI feature will meet these requirements?

Answer options
Option
Correct answer
Your selection
Rationale
A. SageMaker Model Cards
Correct
Selected
You can use SageMaker Model Cards to create records and to document details about ML models in a single place. SageMaker Model Cards support transparent and explainable model development by providing comprehensive, immutable documentation of essential model information.


Learn more about SageMaker Model Cards .

B. SageMaker Model Dashboard
Not selected
SageMaker Model Dashboard is a central place to view, search, and explore all models in an AWS account. SageMaker Model Dashboard provides insights into model deployment, usage, performance tracking, and monitoring. You cannot use SageMaker Model Dashboard to create a record of essential model information, such as risk ratings, training details, and evaluation results.


Learn more about SageMaker Model Dashboard .

C. SageMaker Model Monitor
Not selected
SageMaker Model Monitor monitors the quality of ML models and data in production. You cannot use SageMaker Model Monitor to create a record of essential model information such as risk ratings, training details, and evaluation results.


Learn more about SageMaker Model Monitor .

D. SageMaker Role Manager
Not selected
You can use SageMaker Role Manager to define user permissions for ML activities. You cannot use SageMaker Role Manager to create a record of essential model information.


Learn more about SageMaker Role Manager .

Question 3
Multiple Choice
Time to answer:
5 seconds
Answer status:
Correct
Question
A company wants to assess the performance of a foundation model (FM) for text generation.


Which technique or metric will meet these requirements?

Answer options
Option
Correct answer
Your selection
Rationale
A. Recall-Oriented Understudy for Gisting Evaluation (ROUGE)
Correct
Selected
ROUGE is a metric that you can use to evaluate the quality of text summarization and text generation. You can use ROUGE to assess the performance of an FM for text generation.


Learn more about ROUGE .

B. Fine-tuning
Not selected
Fine-tuning is a process that can customize an FM by fine-tuning the model on a company-specific or domain-specific dataset. The purpose of fine-tuning is to help the model make better predictions and generalize for specific business needs. You can use fine-tuning to improve the model, not to assess the performance of the FM.


Learn more about fine-tuning .

C. F1 score
Not selected
You can use the F1 score to evaluate a model's accuracy for binary classification. F1 scores use precision and recall to evaluate how accurate a model correctly classifies the correct class. You cannot use the F1 score to assess the performance of an FM for text generation.


Learn more about F1 score .

D. Reinforcement learning
Not selected
Reinforcement learning is a technique to train an ML model to achieve a goal and maximize cumulative reward. Reinforcement learning uses a trial-and-error process and a reward-based system. You cannot use reinforcement learning to assess the performance of an FM for text generation.


Learn more about reinforcement learning .

Question 4
Ordering
Time to answer:
5 seconds
Answer status:
Correct
Question
Select and order the Amazon SageMaker AI inference options from the following list from LOWEST latency to HIGHEST latency. Each SageMaker AI inference option should be selected one time.

Answer options
Option
Correct answer
Your selection
Selection 1
Real-time inference
Real-time inference
Selection 2
Asynchronous inference
Asynchronous inference
Selection 3
Batch transform
Batch transform
Rationale
Real-time inference is suitable for use cases with low latency or high throughput requirements. Real-time inference supports processing times of 60 seconds. Real-time inference provides a persistent and fully managed endpoint to handle traffic. Real-time inference offers the lowest latency requirements because of the 60-second processing times.

Asynchronous inference is suitable for use cases with larger datasets and processing times of up to 1 hour. Asynchronous inference can queue incoming requests for inference processing. Asynchronous inference provides moderate latency requirements because of the processing times of up to 1 hour.

Batch transform is suitable for offline processing when data can be processed in batches. Batch transform can support processing times of days. Therefore, batch transform provides the highest latency requirements of these options.

Learn more about inference options .

Question 5
Multiple Choice
Time to answer:
20 seconds
Answer status:
Correct
Question
A company wants to gain insights from diverse data sources to improve business operations. The data sources include audio from call centers.


Which solution will improve transcription accuracy for domain-specific speech?

Answer options
Option
Correct answer
Your selection
Rationale
A. Use a custom bot in Amazon Lex.
Not selected
Amazon Lex is an AI service that you can use to create conversational interfaces for applications. Amazon Lex uses natural language understanding and automatic speech recognition to create chatbots. A solution that creates a custom bot in Amazon Lex will not improve transcription accuracy for domain-specific speech.


Learn more about Amazon Lex .

B. Use batch language identification in Amazon Transcribe.
Not selected
Amazon Transcribe is a service that you can use to convert speech into text. You can use batch language identification to automatically identify the language of audio files. You can use batch language identification to convert files that are in a specific language that you select. You cannot use this feature to improve transcription for domain-specific speech.


Learn more about Amazon Transcribe language identification .

C. Use a custom language model in Amazon Translate.
Not selected
Amazon Translate is a service that you can use to provide translation between multiple languages. You cannot use Amazon Translate to improve transcription for domain-specific speech.


Learn more about Amazon Translate .

D. Use a custom language model in Amazon Transcribe.
Correct
Selected
Amazon Transcribe is a service that you can use to convert speech into text. You can use Amazon Transcribe to facilitate the transcription of audio recordings. If media contains domain-specific or non-standard terms, you can use a custom vocabulary or a custom model to improve the accuracy of the transcriptions. Examples of domain-specific or non-standard terms include brand names, acronyms, technical words, and jargon. A solution that uses a custom language model in Amazon Transcribe can improve transcription accuracy for domain-specific speech.


Learn more about how to improve transcriptions by using a custom vocabulary .

Question 6
Multiple Choice
Time to answer:
1 minutes 3 seconds
Answer status:
Correct
Question
A marketing company wants to generate personalized product descriptions for an ecommerce client's website. The product descriptions must align with the unique style and tone of the existing website.


Which prompt engineering technique will meet these requirements with the LEAST operational effort?

Answer options
Option
Correct answer
Your selection
Rationale
A. Zero-shot prompting without any examples
Not selected
Zero-shot prompting without examples is less effective for tasks that require a specific writing style or format. Zero-shot prompting without examples might cause the model to struggle to infer the desired output.


Learn more about zero-shot prompting .

B. Few-shot prompting with examples of well-written product descriptions
Correct
Selected
Few-shot prompting with examples can help the language model learn the desired style and format for product descriptions. Few-shot prompting with examples is suitable for this scenario and requires the least operational effort.


Learn more about few-shot prompting .

C. Continued pre-training on a different domain
Not selected
Continued pre-training is a method that provides unlabeled data to a foundation model (FM) so the model can train on a specific domain or topic. Continued pre-training on a different domain is not the most effective and requires additional operational effort.


Learn more about continued pre-training .

D. Fine-tuning to optimize the descriptions based on customer engagement metrics
Not selected
You can use fine-tuning to optimize language models for specific metrics. Fine-tuning requires more operational effort and is not necessary to generate product descriptions.


Learn more about fine-tuning .

Question 7
Multi-Select
Time to answer:
11 seconds
Answer status:
Correct
Question
A company is building a generative AI application by using a foundation model (FM). The company decides to customize its own FM by using proprietary datasets instead of using a pre-trained, ready to use FM.


What are the tradeoffs of customizing the FM?

Answer options
Option
Correct answer
Your selection
Rationale
A. Higher latency
Not selected
Latency is the time the model takes to provide output after receiving an input. Customizing an FM with proprietary data and use case–specific data does not lead to higher latency during inference or operation.


Learn more about inference and latency .

B. Reduced accuracy
Not selected
Customizing an FM often leads to higher accuracy and improved performance on the task that the model is designed for. However, you must ensure that the task is well represented by the re-training data. By customizing the model with relevant use case–specific training data, the model can learn to better represent the data and perform the requested task.


Learn more about model customization by using Amazon Bedrock .

C. Increased risk of hallucination
Not selected
Hallucination in the context of generative AI refers to models that provide inaccurate or misleading responses. Customizing an FM with proprietary data and use case–specific data reduces the risk of hallucination.


Learn more about model customization by using Amazon Bedrock .

D. Higher implementation complexity
Correct
Selected
Customizing an FM requires skilled and experienced ML engineers. The process involves more implementation complexity and more effort than using the pre-trained FM. You must prepare the training data, set up the re-training, and evaluate the model to ensure that the model performs well.


Learn more about model customization by using Amazon Bedrock .


Learn more about best practices to create generative AI applications .

E. Higher cost
Correct
Selected
Customizing an FM requires a higher budget than using the public pre-trained FM. Customizing an FM requires computational resources and experienced ML engineers to perform the task.


Learn more about model customization by using Amazon Bedrock .


Learn more about best practices to create generative AI applications .

Question 8
Matching
Time to answer:
12 seconds
Answer status:
Correct
Question
Select the correct AWS service or feature from the following list for each task. Each AWS service or feature should be selected one or more times.

Matching results
Statement
Correct answer
Your selection
Implement identity verification and resource-level access control.
AWS Identity and Access Management (IAM)
AWS Identity and Access Management (IAM)
Set policies to avoid specific topics in a generative AI application.
Amazon Bedrock Guardrails
Amazon Bedrock Guardrails
Filter harmful content based on defined thresholds for categories.
Amazon Bedrock Guardrails
Amazon Bedrock Guardrails
Define user roles and permissions to access Amazon Bedrock.
AWS Identity and Access Management (IAM)
AWS Identity and Access Management (IAM)
Rationale
You can use Amazon Bedrock guardrails to control the content that is generated by Amazon Bedrock. You can use Amazon Bedrock to ensure that the content aligns with safety and compliance policies. You can use Amazon Bedrock guardrails to avoid specific topics, filter harmful content, and monitor user inputs for violations. You can use Amazon Bedrock guardrails to maintain a safe and compliant environment for generative AI applications. Amazon Bedrock guardrails help implement safeguards that are customizable to your use cases and responsible AI policies.


IAM is a service that you can use for access control and identity management in AWS environments, including Amazon Bedrock. You can use IAM to define user roles and to set permissions to access resources. IAM provides a secure method to manage who can use specific features.


Learn more about IAM .


Learn more about Amazon Bedrock guardrails .

Question 9
Multi-Select
Time to answer:
1 minutes 34 seconds
Answer status:
Correct
Question
A company wants to identify custom labels to categorize new product images based on historic product images.


Which combination of steps will meet this requirement?

Answer options
Option
Correct answer
Your selection
Rationale
A. Provide the unlabeled historic images to the model training.
Not selected
Amazon Rekognition is a deep learning image and video analysis service. You can use Amazon Rekognition to analyze and extract insights from visual content. One of the use cases for Amazon Rekognition is the classification of products into categories by using custom labels and training a model. To train the model, you must provide labeled images to the dataset. Therefore, this solution does not meet the requirements.


Learn more about how to classify images by using Amazon Rekognition .

B. Create a training model project in Amazon Rekognition.
Correct
Selected
Amazon Rekognition is a deep learning image and video analysis service. You can use Amazon Rekognition to analyze and extract insights from visual content. One of the use cases for Amazon Rekognition is the classification of products into categories by using custom labels and training a model. To meet the requirements, you must provide labeled images for training.


Learn more about how to classify images by using Amazon Rekognition .

C. Create a custom model in Amazon Comprehend.
Not selected
Amazon Comprehend is a service that uses natural language processing (NLP) to extract insights from documents. You can build custom models in Amazon Comprehend. However, you cannot use Amazon Comprehend to identify new product categories based on images.


Learn more about Amazon Comprehend .

D. Label the historic images by category and provide the labeled images to the model training.
Correct
Selected
Amazon Rekognition is a deep learning image and video analysis service. You can use Amazon Rekognition to analyze and extract insights from visual content. One of the use cases for Amazon Rekognition is the classification of products into categories by using custom labels and training a model. To train the model, you must provide labeled images to the dataset. Additionally, you should label the images by category for the model to use for training.


Learn more about how to classify images by using Amazon Rekognition .

E. Create a training model project in Amazon Textract.
Not selected
Amazon Textract is a service that you can use to extract text and data from scanned documents, PDFs, and images. You cannot use Amazon Textract to identify new product categories based on historic images.


Learn more about Amazon Textract .

Question 10
Multiple Choice
Time to answer:
3 seconds
Answer status:
Correct
Question
What is a foundation model (FM) in the context of generative AI?

Answer options
Option
Correct answer
Your selection
Rationale
A. A basic architecture that serves as a starting point to design more complex neural networks.
Not selected
FMs are large models that are pre-trained on a vast amount of data and that can perform several tasks. FMs can be fine-tuned for downstream tasks by using smaller datasets. FMs are not an architecture that serves as the starting point for more complex neural networks.

B. A task-specific model that is trained on a narrow domain, such as finance or medicine, to serve as a foundation in that area.
Not selected
FMs are large models that are pre-trained on a vast amount of data and that can perform several tasks. FMs can be fine-tuned for downstream tasks by using smaller datasets. FMs are not task-specific models trained on narrow domains.

C. A large, general-purpose model that is pre-trained on diverse datasets that can be fine-tuned for downstream tasks.
Correct
Selected
FMs are large models that are pre-trained on a vast amount of data and that can perform several tasks. FMs can be fine-tuned for downstream tasks by using smaller datasets.


Learn more about FMs .


Learn more about key concepts and FMs .

D. A theoretical framework to understand how different types of models learn representations.
Not selected
FMs are large models that are pre-trained on a vast amount of data and that can perform several tasks. FMs can be fine-tuned for downstream tasks by using smaller datasets. FMs are not a theoretical framework.

Question 11
Multiple Choice
Time to answer:
9 seconds
Answer status:
Correct
Question
A data scientist notices that a model has high accuracy on training data, but has low accuracy on testing data.


What is causing these results?

Answer options
Option
Correct answer
Your selection
Rationale
A. Underfitting
Not selected
Underfitting occurs when a model does not identify the relationships in the training data. Underfitting would lead to low accuracy on both the training data and the testing data.

B. Too much training data
Not selected
Too much training data does not limit the accuracy of a model by itself. Too much training data does not explain why a model has high accuracy on training data but has low accuracy on testing data.

C. Overfitting
Correct
Selected
Overfitting is when a model learns from the training data but is unable to perform well when given new data. Overfitting explains why the model has high accuracy on the training data but has low accuracy on the testing data.


Learn more about overfitting and underfitting .

D. Not enough training time
Not selected
Not enough training time would lead to low accuracy on both the training data and the testing data. Not enough training time does not explain why the model would have high accuracy on the training data.

Question 12
Multiple Choice
Time to answer:
14 seconds
Answer status:
Correct
Question
A travel company wants to use a pre-trained generative AI model to generate background images for marketing materials. The company does not have ML expertise. Additionally, the company does not want to customize and host the ML model.


Which AWS service will meet these requirements?

Answer options
Option
Correct answer
Your selection
Rationale
A. Amazon Comprehend
Not selected
Amazon Comprehend is a natural language processing service that extracts insights from documents. Amazon Comprehend extracts insights from key phrases, language, and sentiments. Amazon Comprehend is not an image generation service.


Learn more about Amazon Comprehend .

B. Amazon Personalize
Not selected
Amazon Personalize is a fully managed ML service that targets recommendations, such as search results or user segments based on interaction data. You can use Amazon Personalize to target a marketing campaign. For example, Amazon Personalize can recommend segments of users who are most likely to respond to a promotion. However, Amazon Personalize is not an image generation service.


Learn more about Amazon Personalize .

C. Amazon Bedrock
Correct
Selected
Amazon Bedrock is a fully managed service that provides a unified API to access popular foundation models (FMs). Amazon Bedrock supports image generation models from providers such as Stability AI or AWS. You can use Amazon Bedrock to consume FMs through a unified API without the need to train, host, or manage ML models. This is the most suitable solution for a company that does not want to train or manage ML models for image generation.


Learn more about Amazon Bedrock .

D. Amazon Rekognition
Not selected
Amazon Rekognition is a fully managed AI service that uses deep learning to analyze images and videos. Amazon Rekognition can perform object-detection tasks. However, Amazon Rekognition does not modify or generate new images.


Learn more about Amazon Rekognition .

Question 13
Multiple Choice
Time to answer:
11 seconds
Answer status:
Correct
Question
What is a valid data format for instruction-based fine-tuning?

Answer options
Option
Correct answer
Your selection
Rationale
A. Audio files with transcriptions
Not selected
Instruction-based fine-tuning improves the performance of a pre-trained foundation model (FM) on domain-specific tasks. Instruction-based fine-tuning uses labeled examples that are formatted as prompt-response pairs and that are phrased as instructions. Audio files with transcriptions do not conform to the necessary prompt-response pair format.

B. Images that are labeled with categories
Not selected
Instruction-based fine-tuning improves the performance of a pre-trained foundation model (FM) on domain-specific tasks. Instruction-based fine-tuning uses labeled examples that are formatted as prompt-response pairs and that are phrased as instructions. Images that are labeled with categories do not conform to the necessary prompt-response pair format.

C. Playlists that are curated with recommended music
Not selected
Instruction-based fine-tuning improves the performance of a pre-trained foundation model (FM) on domain-specific tasks. Instruction-based fine-tuning uses labeled examples that are formatted as prompt-response pairs and that are phrased as instructions. Playlists that are curated with recommended music do not conform to the necessary prompt-response pair format.

D. Prompt-response text pairs
Correct
Selected
Instruction-based fine-tuning improves the performance of a pre-trained foundation model (FM) on domain-specific tasks. Instruction-based fine-tuning uses labeled examples that are formatted as prompt-response pairs and that are phrased as instructions.


Learn more about instruction-based fine-tuning .

Question 14
Multiple Choice
Time to answer:
28 seconds
Answer status:
Correct
Question
A company has a containerized frontend application for its AI application. The company must implement a solution to assess its AWS environment's security posture. The solution must identify potential security vulnerabilities across Amazon EC2 instances and Amazon Elastic Container Registry (Amazon ECR) repositories for the application. The solution should provide recommendations for remediation.


Which AWS service will meet these requirements?

Answer options
Option
Correct answer
Your selection
Rationale
A. AWS Artifact
Not selected
AWS Artifact provides on-demand access to security and compliance documents. AWS Artifact does not identify security vulnerabilities across EC2 instances and Amazon ECR repositories. AWS Artifact does not provide recommendations for remediation.


Learn more about AWS Artifact .

B. AWS CloudTrail
Not selected
You can use CloudTrail to log actions that are taken by a user, role, or service in your account. Actions are recorded as events in CloudTrail. CloudTrail can track user activity and changes that are made to AWS resources. However, CloudTrail does not directly assess the security posture of your environment or identify potential security vulnerabilities. Instead, CloudTrail provides a history of AWS API calls for auditing, compliance, and troubleshooting purposes.


Learn more about CloudTrail .

C. AWS Config
Not selected
AWS Config provides a detailed view of your AWS resource configurations. AWS Config helps track resource configurations and changes. However, AWS Config does not assess security vulnerabilities or compliance against specific regulations or standards. Instead, AWS Config focuses on monitoring resource configurations for compliance with desired configurations and best practices.


Learn more about AWS Config .

D. Amazon Inspector
Correct
Selected
Amazon Inspector is a vulnerability management service that continuously scans workloads for software vulnerabilities and unintended network exposure. Amazon Inspector assesses the security and compliance of your AWS resources by performing automated security checks based on best practices and common vulnerabilities. Amazon Inspector can assess EC2 instances and Amazon ECR repositories to provide detailed findings and recommendations for remediation. You can use Amazon Inspector to maintain a secure and compliant AWS environment.


Learn more about Amazon Inspector .

Question 15
Multiple Choice
Time to answer:
39 seconds
Answer status:
Correct
Question
A company wants to increase the consistency and quality of large language model (LLM) responses by providing the model with access to external sources of knowledge.


Which technique will meet the requirement with the LEAST development effort?

Answer options
Option
Correct answer
Your selection
Rationale
A. Continued pre-training
Not selected
Continued pre-training is the process of providing unlabeled data to a pre-trained model to expose a model to specific topic areas. Continued pre-training does not increase the consistency of an LLM by providing the model with access to external sources of knowledge.


Learn more about prompt engineering .

B. Fine-tuning
Not selected
Fine-tuning is the process to further train and refine a pre-trained LLM on a smaller, targeted dataset. The purpose of fine-tuning a pre-trained LLM is to maintain the original capability of the model and adapt to more specialized use cases. Fine-tuning requires additional development effort to train the model.


Learn more about fine-tuning .

C. Retrieval augmented generation (RAG)
Correct
Selected
RAG is the process of improving the quality and consistency of LLMs by referencing an external knowledge base that is outside of the LLM's training data sources. RAG references the external knowledge base before generating a response. You can use RAG to provide the model with access to external sources of knowledge with minimal development effort.


Learn more about RAG .

D. In-context learning
Not selected
In-context learning is the process of providing a few examples to help an LLM better align responses to an expected format or output. In-context learning is also referred to as few-shot prompting. In-context learning does not increase the consistency and quality of an LLM by providing the model with access to external sources of knowledge.


Learn more about few-shot prompting .

Question 16
Multiple Choice
Time to answer:
6 seconds
Answer status:
Correct
Question
A company is developing a solution on AWS that uses Amazon Bedrock.


Which AWS service can the company use to secure access to Amazon Bedrock?

Answer options
Option
Correct answer
Your selection
Rationale
A. Amazon Rekognition
Not selected
Amazon Rekognition provides scalable image and video analysis. Amazon Rekognition provides features such as object and scene detection, facial analysis, and text detection. Amazon Rekognition does not directly address the security concerns of unauthorized access or misuse of Amazon Bedrock.


Learn more about Amazon Rekognition .

B. AWS Identity and Access Management (IAM)
Correct
Selected
You can use IAM to control access to AWS resources through users, roles, and policies. You can use IAM to control which users or services have access to Amazon Bedrock. You can use IAM to control what actions the user or service can perform. You can use IAM to secure access to Amazon Bedrock.


Learn more about IAM .

C. AWS Config
Not selected
AWS Config provides a detailed view of the configuration of AWS resources within your account. AWS Config illustrates the interconnections and historical configurations of your AWS resources. You can use AWS Config to monitor the change of configurations and relationships over time. You cannot use AWS Config to secure the access and operations of Amazon Bedrock.


Learn more about AWS Config .

D. Amazon Macie
Not selected
You can use Macie to discover, classify, and protect sensitive data that is stored in Amazon S3. Macie is useful for data security. However, Macie primarily focuses on data at rest. You cannot use Macie to secure the access and operations of Amazon Bedrock.


Learn more about Macie .

Question 17
Multiple Choice
Time to answer:
26 seconds
Answer status:
Correct
Question
A company wants to use generative AI to create product descriptions on its website.


What is a limitation of generative AI that the company should be aware of?

Answer options
Option
Correct answer
Your selection
Rationale
A. Generative AI models might produce biased or inappropriate content that requires human review and editing.
Correct
Selected
Generative AI models can produce human-like text. However, generative AI models can exhibit biases or generate inappropriate content that requires human oversight and editing. Therefore, this option is a limitation of current generative AI systems.


Learn more about the limitations and capabilities of generative AI .

B. Generative AI cannot generate text in the multiple languages that is required for an ecommerce website.
Not selected
You can train generative AI models on multilingual data. Generative AI models can generate text in multiple languages. A limitation of generative AI is the potential for biased or inappropriate output.

C. Generative AI models lack the ability to understand and incorporate product specifications and details.
Not selected
Generative AI models can incorporate and understand product specifications and details when you train the models on relevant data. A limitation of generative AI is the potential for biased or inappropriate output.

D. Generative AI cannot handle the large volumes of data that is required for product descriptions.
Not selected
Modern generative AI models are designed to handle large volumes of data and can generate text at scale. A limitation of generative AI is the potential for biased or inappropriate output.

Question 18
Multiple Choice
Time to answer:
11 seconds
Answer status:
Correct
Question
A company wants to record API calls that are made to Amazon Bedrock in log files. For compliance purposes, the company wants these logs to include the API call, the user who made the call, and the time that the call was made.


Which AWS service will meet these requirements?

Answer options
Option
Correct answer
Your selection
Rationale
A. AWS Trusted Advisor
Not selected
Trusted Advisor provides information on how to optimize account environments for cost and performance, while maintaining high security standards. Trusted Advisor does not monitor API calls to Amazon Bedrock.


Learn more about Trusted Advisor .

B. AWS CloudTrail
Correct
Selected
You can use CloudTrail to monitor and log API calls in AWS accounts. CloudTrail records contain the API event, the user who made the API call, and the time that the call was made.


Learn more about how to log Amazon Bedrock API calls by using CloudTrail .

C. Amazon CloudWatch
Not selected
You can use CloudWatch to gather and view metrics that relate to account resources. You can use CloudWatch to view the number of API calls to Amazon Bedrock. However, CloudWatch does not provide a mechanism to examine which user made the API call.


Learn more about how to monitor Amazon Bedrock by using CloudWatch .

D. Amazon Inspector
Not selected
Amazon Inspector checks AWS resources for security exposures and vulnerabilities in configurations. Some examples of resources that Amazon Inspector checks include Amazon EC2 instances, Amazon Elastic Container Registry (Amazon ECR), and AWS Lambda. Amazon Inspector does not monitor API calls to Amazon Bedrock.


Learn more about Amazon Inspector .

Question 19
Multiple Choice
Time to answer:
16 seconds
Answer status:
Correct
Question
Which AWS service can detect text and handwriting from invoices that are stored in PNG format?

Answer options
Option
Correct answer
Your selection
Rationale
A. Amazon Kendra
Not selected
Amazon Kendra is an intelligent search service that uses semantic and contextual understanding to provide relevant responses to a search query. You cannot use Amazon Kendra to detect and extract text, handwriting, and data from invoice images.


Learn more about Amazon Kendra .

B. Amazon Textract
Correct
Selected
Amazon Textract is fully managed service that can detect and extract text and data from scanned documents, PDFs, and images. One of the use cases for Amazon Textract is to process invoices and receipts. For example, Amazon Textract can detect billing and shipping addresses automatically from images.


Learn more about how to analyze invoices and receipts in Amazon Textract .

C. Amazon Polly
Not selected
Amazon Polly is a text-to-speech (TTS) service that can convert text into lifelike speech. You cannot use Amazon Polly to detect and extract text, handwriting, and data from invoice images.


Learn more about Amazon Polly .

D. Amazon Comprehend
Not selected
Amazon Comprehend is a natural language processing (NLP) service that can extract insights and relationships from text data. You cannot use Amazon Comprehend to process textual information from images that are provided in PNG format. Amazon Comprehend requires text as input.


Learn more about Amazon Comprehend .

Question 20
Multi-Select
Time to answer:
11 seconds
Answer status:
Correct
Question
A data science team wants to improve a model's performance. The data science team wants to increase the number of variables in the training dataset.


Which ML pipeline steps will meet these requirements?

Answer options
Option
Correct answer
Your selection
Rationale
A. Data collection
Correct
Selected
Data collection is a step to label, ingest, and aggregate data that you will use for ML model training. During data collection, you ingest and aggregate data from multiple sources. Then, you label the data. The data collection stage involves gathering additional raw data, which can increase the number of variables in the training dataset.


Learn more about data collection .

B. Hyperparameter tuning
Not selected
Hyperparameter tuning is a method to adjust the behavior of an ML algorithm. You can make changes to an ML model by using hyperparameter tuning to modify the behavior of the algorithm. However, hyperparameter tuning does not increase the number of variables in the training dataset.


Learn more about model training and tuning .

C. Model evaluation
Not selected
Model evaluation is a step in the ML development pipeline that occurs after model training. You can use model evaluation to evaluate a model's performance and metrics. Model evaluation does not increase the number of variables in the training dataset or modify the behavior of the algorithm.


Learn more about model evaluation .

D. Feature engineering
Correct
Selected
Feature engineering is a method to select and transform variables when you create a predictive model. Feature engineering includes feature creation, feature transformation, feature extraction, and feature selection. Feature engineering enhances the data by increasing the number of variables in the training dataset to ultimately improve model performance.


Learn more about feature engineering .

E. Model monitoring
Not selected
Model monitoring is a component of the ML lifecycle that captures data and compares the data to the training data. You can use model monitoring to identify data quality issues, model quality issues, bias drift, and feature attribution drift. Model monitoring does not increase the number of variables in the training dataset or modify the behavior of the algorithm.


Learn more about model monitoring .