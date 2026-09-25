# Domain 1 Flashcards

<details>
  <summary><b>Q: What are data structures?</b></summary>
  <p><b>A:</b> They represent data relationships and refer to the way data is organized and stored in a computer’s memory. They provide methods of sorting and accessing data effectively.</p>
</details>

<details>
  <summary><b>Q: What are examples of data structures?</b></summary>
  <p><b>A:</b> They include relational databases, NoSQL databases, data warehouses, distributed file systems, message queues, tree data, and hash tables.</p>
</details>

<details>
  <summary><b>Q: What is an algorithm?</b></summary>
  <p><b>A:</b> Sets of instructions or rules that computer software, webpages, programs, and hardware use to complete a task. They provide a way to access data and respond to a command to complete a task.</p>
</details>

<details>
  <summary><b>Q: What factors might influence an analytics workload’s most suitable storage solution on AWS?</b></summary>
  <p><b>A:</b> Factors include compute, access patterns (random or sequential), required throughput, access frequency (online, offline, archival), data durability requirements, archival requirements, and create, read, update, and delete (CRUD) operation requirements.</p>
</details>

<details>
  <summary><b>Q: How can you retrieve more data when you pass SQL expressions to Amazon S3 in a request?</b></summary>
  <p><b>A:</b> You can use the AWS CLI or the API.</p>
</details>

<details>
  <summary><b>Q: Which input mode gives you the ability to stream data directly from Amazon S3?</b></summary>
  <p><b>A:</b> Pipe mode uses the optimized protobuf recordIO data format and gives you the ability to directly stream your input data from Amazon S3.</p>
</details>

<details>
  <summary><b>Q: What is a benefit of Pipe mode?</b></summary>
  <p><b>A:</b> It offers better read throughput than File mode, which downloads data to the local Amazon EBS volume before starting the model training. This means your training jobs start sooner, finish quicker, and need less disk space, reducing your overall cost to train ML models on SageMaker.</p>
</details>

<details>
  <summary><b>Q: What is AWS Database Migration Service (AWS DMS)?</b></summary>
  <p><b>A:</b> It is a service to migrate relational databases, data warehouses, NoSQL databases, and other types of data stores.</p>
</details>

<details>
  <summary><b>Q: What does SageMaker Clarify help do?</b></summary>
  <p><b>A:</b></p>
  <ul>
    <li>Detect bias and help explain your model predictions.</li>
    <li>Identify types of bias in pre-training data.</li>
    <li>Identify types of bias in post-training data that can emerge during training or when your model is in production.</li>
  </ul>
</details>

<details>
  <summary><b>Q: Can you use the k-nearest neighbors (k-NN) algorithm to detect anomalies?</b></summary>
  <p><b>A:</b> No, this algorithm is used only for classification or regression problems.</p>
</details>

<details>
  <summary><b>Q: What is the softmax activation function?</b></summary>
  <p><b>A:</b> It is a mathematical equation that converts a vector of real numbers into a vector of a probability distribution with a sum that is equal to 1.</p>
</details>

<details>
  <summary><b>Q: What is the rectified linear unit (ReLU) function?</b></summary>
  <p><b>A:</b> It will convert inputs into the range of 0 (positive input value) and not into a probability distribution.</p>
</details>

<details>
  <summary><b>Q: What is the Sigmoid function?</b></summary>
  <p><b>A:</b> It squashes inputs as 0 (the more negative a number gets) or 1 (the more positive a number gets). This activation function is used mainly for binary classification problems.</p>
</details>

<details>
  <summary><b>Q: What is the hyperbolic tangent (tanh) function?</b></summary>
  <p><b>A:</b> It is like the Sigmoid function. However, it is centered around 0, and Sigmoid functions are centered around 0.5. Most of the time, this function is preferable. With this function, the model can converge faster to a minimum because its derivatives are larger and steeper than a Sigmoid function.</p>
</details>

<details>
  <summary><b>Q: What is the SageMaker input File mode?</b></summary>
  <p><b>A:</b> It presents a file system view of the dataset to the training container. This is the default input mode if you don't explicitly specify one of the other two options.</p>
</details>

<details>
  <summary><b>Q: What is the SageMaker input Fast file mode?</b></summary>
  <p><b>A:</b> It provides file system access to an Amazon S3 data source while using the performance advantage of Pipe mode. At the start of training, this mode identifies the data files but does not download them. Training can start without waiting for the entire dataset to download. This means that the training startup takes less time when there are fewer files in the Amazon S3 prefix provided.</p>
</details>

<details>
  <summary><b>Q: How does Fast file mode work?</b></summary>
  <p><b>A:</b> It works with random access to the data. However, it works best when data is read sequentially.</p>
</details>

<details>
  <summary><b>Q: How does SageMaker use Amazon S3 Express One Zone as a data source?</b></summary>
  <p><b>A:</b> It is a high-performance, single Availability Zone storage class. It can deliver consistent, single-digit millisecond data access for the most latency-sensitive applications, including SageMaker model training. It helps to collocate their object storage and compute resources in a single Availability Zone, optimizing both compute performance and costs with increased data processing speed. To further increase access speed and support hundreds of thousands of requests each second, data is stored in a new bucket type, an S3 directory bucket.</p>
</details>

<details>
  <summary><b>Q: How does SageMaker use Amazon FSx for Lustre as a data source?</b></summary>
  <p><b>A:</b> When starting a training job, SageMaker mounts the FSx for Lustre file system to the training instance file system and then starts your training script. Mounting itself is a relatively fast operation that doesn't depend on the size of the dataset stored in FSx for Lustre. To access FSx for Lustre, your training job must connect to an Amazon VPC. You need to specify an Amazon VPC subnet that maps to this Availability Zone ID when running the training job.</p>
</details>

<details>
  <summary><b>Q: How does SageMaker use Amazon EFS as a data source?</b></summary>
  <p><b>A:</b> The data must already reside in Amazon EFS before training. SageMaker mounts the specified EFS file system to the training instance, and then starts your training script. Your training job must connect to a VPC to access Amazon EFS.</p>
</details>

<details>
  <summary><b>Q: What is Amazon Forecast?</b></summary>
  <p><b>A:</b> It is a time-series forecasting service based on ML and built for business metrics analysis.</p>
</details>

<details>
  <summary><b>Q: Does Forecast provide filling methods?</b></summary>
  <p><b>A:</b> Yes, Forecast provides middle filling, back filling, and future filling.</p>
</details>

<details>
  <summary><b>Q: What is quantile binning transformation?</b></summary>
  <p><b>A:</b> It is a process used to discover non-linearity in the variable’s distribution by grouping observed values together. It won’t help normalize features with wide-ranging differences.</p>
</details>

<details>
  <summary><b>Q: What is n-gram transformation used for?</b></summary>
  <p><b>A:</b> It is used for splitting sentences into a list of words.</p>
</details>

<details>
  <summary><b>Q: What is an orthogonal sparse bigram (OSB) transformation?</b></summary>
  <p><b>A:</b> Like the n-gram transformation, this transformation is intended to aid in text string analysis and is an alternative to the bi-gram transformation.</p>
</details>