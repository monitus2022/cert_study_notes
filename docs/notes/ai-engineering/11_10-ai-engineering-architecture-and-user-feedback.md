# 10. AI Engineering Architecture and User Feedback

---

## Bringing Techniques Together
- The chapter shows how to combine AI engineering techniques to build successful products
- Selecting among many techniques and tools can feel overwhelming
- A gradual approach simplifies the process
- Start with the simplest foundation model architecture, then add components to address its challenges

---

## Testing with Real Users
- Endless reasoning cannot reveal whether an application achieves its goal
- The only way to know is to put the application in front of users
- User feedback has always been invaluable for guiding product development
- For AI applications, feedback is even more crucial as a data source for improving models

---

## The Conversational Feedback Challenge
- Conversational interfaces make it easier for users to give feedback
- But they make it harder for developers to extract signals
- The chapter covers different types of conversational AI feedback
- It discusses designing a system to collect the right feedback without hurting user experience

---

## AI Engineering Architecture

- A full AI architecture can be complex; this section builds it up progressively from the simplest form.
- Despite their diversity, AI applications share many common components.
- The proposed architecture has been validated at multiple companies as general across applications.
- Certain applications might still deviate from this architecture.

---

## The Simplest Architecture

- The application receives a query and sends it to the model.
- The model generates a response, which is returned to the user.
- At this stage: no context augmentation, no guardrails, and no optimization.
- The *Model API* box covers third-party APIs (e.g., OpenAI, Google, Anthropic) and self-hosted models.

---

## Step 1. Enhance Context
- Start with a simple architecture and add components as needs arise.
- Construct relevant context via text, image, and tabular retrieval.
- Augment context with tools that gather information through APIs.
- Context construction is like feature engineering for foundation models.

---

## Context Construction Support
- Model API providers like OpenAI, Claude, and Gemini allow file uploads and tool use.
- Providers differ in supported document types and upload limits.
- A specialized RAG solution may allow uploads limited only by the vector database.
- Frameworks differ in retrieval algorithms, chunk sizes, and tool execution modes.

---

## Progression Beyond Step 1
- Add guardrails to protect your system and your users.
- Add model router and gateway for complex pipelines and more security.
- Optimize latency and costs with caching.
- Then add complex logic and write actions to maximize capabilities.

---

## Input Guardrails
- Input guardrails protect against leaking private information to external APIs and bad prompts.
- Sensitive data classes include personal information, human faces, and company keywords or privileged information.
- If sensitive data is found, block the query or remove sensitive information.
- Masking can replace data with placeholders; a reverse PII map can unmask responses.

---

## Output Guardrails
- Output guardrails catch output failures and specify policies for handling failure modes.
- Quality failures include malformed responses, factually inconsistent hallucinations, and generally bad responses.
- Security failures include toxic content, sensitive information, remote execution triggers, and brand-risk responses.
- Track false refusal rates, since overly secure systems can block legitimate requests.

---

## Guardrail Implementation Trade-offs
- Retry logic can mitigate failures, but retries add latency and cost.
- Parallel calls can reduce retry latency by choosing the better of multiple responses.
- Teams may fall back on humans for tricky requests, using phrases, sentiment, or turn count.
- Reliability versus latency trade-offs affect whether teams implement guardrails; streaming complicates output checks.

---

## System Caching: Exact Caching
- Caching reduces latency and cost; system caching includes exact and semantic mechanisms.
- Exact caching returns cached items only for identical requests, such as product summaries.
- Exact caching avoids redundant vector search by caching query results.
- Caching suits multi-step or time-consuming queries like retrieval, SQL, or web search.

---

## Exact Cache: Storage, Eviction, and Risks
- Implement exact cache in memory, databases like PostgreSQL or Redis, or tiered storage.
- Eviction policies such as LRU, LFU, and FIFO manage cache size and performance.
- Avoid caching user-specific or time-sensitive queries; teams may train a classifier.
- Improper caching can leak data, e.g., returning one user's personalized answer to another.

---

## Semantic Caching
- Semantic caching reuses cached items for semantically similar, not identical, queries.
- It uses embeddings, vector search, and a similarity threshold to match queries.
- It can increase hit rate and reduce cost but may reduce model performance.
- Its value is dubious due to failure-prone components, threshold tuning, and compute cost.

---

## Step 5. Add Agent Patterns

- Earlier applications follow a simple sequential flow for each query.
- Agentic patterns enable loops, parallel execution, and conditional branching.
- Example: the system decides its output did not accomplish the task.
- It performs another retrieval and passes the original response plus new context onward.

---

## Loops via Feedback

- The generated response is fed back into the system, creating a loop.
- The combined response and retrieved context go to the same or a different model.
- This enables more complex application patterns than a sequential flow.

---

## Write Actions

- Model outputs can invoke write actions: composing email, placing orders, bank transfers.
- Write actions let a system make changes to its environment directly.
- They make a system vastly more capable but expose it to significantly more risk.
- Giving a model access to write actions should be done with the utmost care.

---

## Monitoring and Observability
- Observability should be integral to product design, not an afterthought; complexity makes it more crucial.
- Monitoring mitigates application failures, security attacks, and drifts; it also discovers improvements and cost savings.
- Observability metrics include MTTD, MTTR, and CFR; unknown CFR suggests redesigning for observability.
- Evaluation and monitoring must work closely; monitoring issues should feed the evaluation pipeline.

---

## Metrics, Logs, and Traces
- Design metrics around failure modes: format failures, factual consistency, safety, user signals, latency, and costs.
- Metrics are aggregated; logs are append-only event records; log everything with tags and IDs.
- Traces link related events into a request timeline, showing steps, time, and cost when measurable.
- Use traces to pinpoint the exact step where a query failed.

---

## Drift Detection
- More system parts mean more things can change; monitor for drift as a risk.
- System prompts can change via template updates or typo fixes; simple logic can catch changes.
- Users adapt behavior over time, potentially causing gradual changes such as shorter responses.
- Metrics alone may not explain changes; logs and traces support debugging.

---

## AI Pipeline Orchestration: Two Steps
- An orchestrator specifies how models, data sources, and tools work together in an end-to-end pipeline.
- **Components definition:** declare the models, external data sources, tools, and evaluation/monitoring components your system uses.
- A model gateway can make it easier to add a model.
- **Chaining:** function composition that defines the steps from user query to completed task.

---

## Chaining: Example Pipeline Steps
- Process the raw query, then retrieve relevant data based on it.
- Combine query and retrieved data into a prompt in the model's expected format; the model generates a response.
- Evaluate the response: return it if good, otherwise route to a human operator.
- The orchestrator passes data between components and should notify you when data flow is disrupted.

---

## Designing and Choosing an Orchestrator
- For strict latency requirements, do as much in parallel as possible, e.g. routing and PII removal together.
- An AI pipeline orchestrator differs from general workflow orchestrators like Airflow or Metaflow.
- Consider starting without an orchestrator: tools add complexity and can obscure critical details.
- Evaluate integration and extensibility, support for complex pipelines, and ease of use, performance, scalability.

---

## User Feedback in AI Applications
- User feedback evaluates application performance and informs development, as in all software.
- In AI, feedback is even more significant: it is proprietary data and competitive advantage.
- A well-designed feedback system is necessary to create the data flywheel.
- Feedback personalizes models for users and trains future model iterations.

---

## User Feedback as User Data
- User feedback is user data; leveraging it requires the same cautions as any data.
- User privacy should be respected when using feedback.
- Users have the right to know how their data is being used.
- As data becomes scarce, proprietary feedback from early users helps improve models continually.

---

## Explicit vs. Implicit Feedback
- Explicit feedback: users respond to direct requests—thumbs up/down, ratings, yes/no answers.
- Implicit feedback: information inferred from user actions, highly application-dependent.
- Conversational interfaces make feedback easier, conveyed through everyday dialogue language.
- Extracted conversational feedback supports evaluation, development, and personalization.

---

## Natural Language Feedback Signals
- Early termination—stopping generation, exiting the app, or leaving the agent hanging—suggests trouble.
- Error correction cues like "No, …" or "I meant, …" indicate the response missed the mark.
- User edits are strong signals and create preference data: edit wins, original loses.
- Complaints, negative sentiment, and model refusal rate also reveal how conversations are going.

---

## Action-Based Feedback and Trade-offs
- Regeneration may signal dissatisfaction, a desire to compare options, or a consistency check.
- Delete, rename, share, and bookmark indicate conversation quality; length and diversity add context.
- Explicit feedback is easier to interpret but sparse and prone to response biases.
- Implicit feedback is more abundant but noisier and harder to interpret.

---

## When to Collect Feedback
- Collect feedback throughout the user journey, but keep it nonintrusive and optional where possible.
- Early feedback can calibrate apps, such as face ID, voice recognition, or language skill level.
- When failures occur, let users downvote, regenerate, switch models, edit outputs, or reach humans.
- Low-confidence models can show side-by-side options for comparative preference feedback.

---

## Designing Feedback Collection
- Integrate feedback into workflow so users can provide it easily and ignore it easily.
- Midjourney infers preference from upscale, variation, or regenerate choices after each prompt.
- GitHub Copilot lets users accept with Tab or ignore by continuing typing.
- Standalone apps struggle to track downstream use; integrated products can capture richer context.

---

## Context, Clarity, and Visibility
- Feedback context, such as recent dialogue turns, helps diagnosis but may require consent or data donation.
- Explain how feedback is used; reassure privacy only when true.
- Avoid impossible or ambiguous requests; add icons/tooltips and allow “I don’t know.”
- Private signals can be more candid; public signals can aid discoverability but affect behavior.

---

## Feedback Biases
- User feedback carries biases; design your feedback system around them.
- Leniency bias: people rate more positively than warranted to avoid conflict or extra work.
- Randomness: users lacking motivation give random feedback, such as clicking options arbitrarily.
- Position bias: first suggestions get more clicks; randomize positions or model true success rate.

---

## Leniency Bias in Ratings
- On five-star scales, users may feel pressured to give five stars.
- Uber 2015: average driver rating was 4.8; below 4.6 risked deactivation.
- Inspect the distribution of user ratings to detect leniency bias.
- Descriptive options instead of numbers can reduce the negative connotation of low ratings.

---

## Degenerate Feedback Loops
- Feedback is incomplete: you only get feedback on what you show users.
- Predictions influence feedback, which influences the next model, amplifying initial biases.
- Higher-ranked videos get more clicks, reinforcing the system's belief they are best.
- Known as exposure bias, popularity bias, or filter bubbles.

## Practice Questions

### Question 1: What approach does the chapter take to help with selecting among th...

What approach does the chapter take to help with selecting among the wide range of AI engineering techniques and tools?

- [ ] A) It starts with the most complex architecture and removes components until it works.
- [ ] B) It starts with the simplest architecture, highlights its challenges, and gradually adds components to address them.
- [ ] C) It recommends choosing tools based only on user feedback before building any architecture.
- [ ] D) It avoids discussing architecture and focuses only on model adaptation techniques.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The chapter says it takes a gradual approach: starting with the simplest architecture, highlighting challenges, and gradually adding components to address them.

### Question 2: According to the source text, what is the only way to find out if a...

According to the source text, what is the only way to find out if an application actually achieves its goal?

- [ ] A) By reasoning carefully about the architecture before launch
- [ ] B) By selecting the right AI engineering tools in advance
- [ ] C) By putting the application in front of users
- [ ] D) By avoiding conversational interfaces

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states that we can spend eternity reasoning about how to build a successful application, but the only way to find out if it achieves its goal is to put it in front of users.

### Question 3: Why does the source text say user feedback has an even more crucial...

Why does the source text say user feedback has an even more crucial role for AI applications than for other products?

- [ ] A) It makes the conversational interface harder for users to use.
- [ ] B) It serves as a data source for improving models.
- [ ] C) It eliminates the need for any architecture.
- [ ] D) It replaces the need to put applications in front of users.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says user feedback has always been invaluable for guiding product development, but for AI applications it is even more crucial as a data source for improving models.

### Question 4: What tradeoff does the source text identify about the conversationa...

What tradeoff does the source text identify about the conversational interface and feedback?

- [ ] A) It makes it harder for users to give feedback but easier for developers to extract signals.
- [ ] B) It makes it easier for users to give feedback but harder for developers to extract signals.
- [ ] C) It makes feedback collection equally easy for users and developers.
- [ ] D) It prevents developers from collecting any user feedback.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that the conversational interface makes it easier for users to give feedback but harder for developers to extract signals.

### Question 5: In the simplest form of an AI application architecture described in...

In the simplest form of an AI application architecture described in the text, what happens after the application receives a query?

- [ ] A) The query is augmented with retrieved context before being sent to the model
- [ ] B) The query is sent to the model, which generates a response that is returned to the user
- [ ] C) The query is first passed through guardrails and then optimized before reaching the model
- [ ] D) The query is stored and batched for later processing by an inference server

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that in its simplest form the application receives a query and sends it to the model, which generates a response returned to the user.

### Question 6: According to the text, what does the Model API box refer to?

According to the text, what does the Model API box refer to?

- [ ] A) Only third-party APIs such as OpenAI, Google, and Anthropic
- [ ] B) Only self-hosted models running on an inference server
- [ ] C) Both third-party APIs and self-hosted models
- [ ] D) A database used to store user queries and responses

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says the Model API box refers to both third-party APIs (e.g., OpenAI, Google, Anthropic) and self-hosted models.

### Question 7: What does the text say about the generality of the proposed AI arch...

What does the text say about the generality of the proposed AI architecture?

- [ ] A) It is specific to a single company and cannot be reused elsewhere
- [ ] B) It has been validated at multiple companies as general for a wide range of applications, though certain applications might deviate
- [ ] C) It applies only to applications that use third-party model APIs
- [ ] D) It requires context augmentation and guardrails in every deployment

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states the architecture has been validated at multiple companies to be general for a wide range of applications, but certain applications might deviate.

### Question 8: Where does the text say building an inference server for self-hoste...

Where does the text say building an inference server for self-hosted models is discussed?

- [ ] A) Chapter 9
- [ ] B) Chapter 10
- [ ] C) Chapter 8
- [ ] D) Chapter 11

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text explicitly notes that building an inference server for self-hosted models is discussed in Chapter 9.

### Question 9: According to the source, what does the initial expansion of a platf...

According to the source, what does the initial expansion of a platform usually involve?

- [ ] A) Adding guardrails to protect the system and users
- [ ] B) Adding mechanisms to construct the relevant context needed by the model for each query
- [ ] C) Adding a model router and gateway for complex pipelines
- [ ] D) Optimizing latency and costs with caching

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that the initial expansion usually involves adding mechanisms to allow the system to construct the relevant context needed by the model to answer each query.

### Question 10: How does the source describe context construction?

How does the source describe context construction?

- [ ] A) It is like feature engineering for foundation models
- [ ] B) It is a replacement for monitoring and observability
- [ ] C) It is mainly a way to reduce model API costs
- [ ] D) It is only useful for text retrieval, not tools or APIs

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source explicitly says, “Context construction is like feature engineering for foundation models,” because it gives the model the necessary information to produce an output.

### Question 11: According to the source, how do model API providers differ in their...

According to the source, how do model API providers differ in their context construction support?

- [ ] A) They are identical in document upload limits and tool execution modes
- [ ] B) They may differ in document type and upload limits, and in supported tool types and execution modes
- [ ] C) They differ only in whether they allow text retrieval
- [ ] D) They do not support tools for gathering information through APIs

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source notes that providers may limit what types and how many documents you can upload, and that tool-use solutions differ in supported tools and execution modes such as parallel function execution or long-running jobs.

### Question 12: According to the text, input guardrails typically protect against w...

According to the text, input guardrails typically protect against which two types of risks?

- [ ] A) Leaking private information to external APIs and executing bad prompts that compromise the system
- [ ] B) Malformatted responses and factually inconsistent responses
- [ ] C) High latency and increased API cost
- [ ] D) Toxic responses and brand-risk responses

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states input guardrails typically protect against leaking private information to external APIs and executing bad prompts that compromise your system.

### Question 13: What are the two main functions of output guardrails described in t...

What are the two main functions of output guardrails described in the text?

- [ ] A) Reducing latency and lowering API cost
- [ ] B) Catching output failures and specifying the policy to handle different failure modes
- [ ] C) Masking PII and unmasking PII with a reverse dictionary
- [ ] D) Deciding whether to self-host models or use third-party APIs

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says output guardrails have two main functions: catch output failures and specify the policy to handle different failure modes.

### Question 14: What trade-off do some teams cite when deciding not to implement gu...

What trade-off do some teams cite when deciding not to implement guardrails?

- [ ] A) Reliability versus latency, because guardrails can significantly increase application latency
- [ ] B) Self-hosting versus third-party APIs, because third-party APIs always remove all guardrails
- [ ] C) Stream completion versus batch completion, because streaming makes all guardrails unnecessary
- [ ] D) Human fallback versus retry logic, because retries eliminate the need for human operators

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text describes a reliability versus latency trade-off and notes that some teams decided not to implement guardrails because they can significantly increase latency.

### Question 15: According to the text, what are the two main benefits of using a ro...

According to the text, what are the two main benefits of using a router instead of one model for all queries?

- [ ] A) Lower latency and higher accuracy on all queries
- [ ] B) Specialized models that may perform better on specific queries, and cost savings by routing simpler queries to cheaper models
- [ ] C) Automatic fine-tuning of models and reduced storage costs
- [ ] D) Better guardrails and improved caching

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states routing allows specialized models that can outperform a general-purpose model for specific queries, and lets simpler queries go to cheaper models to save costs.

### Question 16: A router typically consists of which component that predicts what t...

A router typically consists of which component that predicts what the user is trying to do and routes the query accordingly?

- [ ] A) A next-action predictor
- [ ] B) A scorer
- [ ] C) An intent classifier
- [ ] D) A model gateway

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says a router typically consists of an intent classifier that predicts the user's intent, and the query is routed to the appropriate solution based on that prediction.

### Question 17: Which of the following is described as the most basic functionality...

Which of the following is described as the most basic functionality of a model gateway?

- [ ] A) Training intent classifiers from scratch
- [ ] B) Providing a unified interface to different models, including self-hosted models and models behind commercial APIs
- [ ] C) Truncating query context to fit model context limits
- [ ] D) Detecting ambiguous queries and asking for clarification

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states the most basic functionality of a model gateway is to provide a unified interface to different models, including self-hosted and commercial API models.

### Question 18: According to the text, which of the following does a model gateway...

According to the text, which of the following does a model gateway provide in addition to a unified interface?

- [ ] A) Access control and cost management, plus fallback policies for rate limits or API failures
- [ ] B) Automatic prompt engineering and model fine-tuning
- [ ] C) Intent classification and next-action prediction
- [ ] D) Context truncation and memory hierarchy selection

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says a gateway provides access control and cost management, and can implement fallback policies to overcome rate limits or API failures.

### Question 19: With exact caching, when are cached items used?

With exact caching, when are cached items used?

- [ ] A) Only when the exact items are requested
- [ ] B) Whenever a semantically similar query is received
- [ ] C) Only for time-sensitive queries
- [ ] D) Only for user-specific queries

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** Exact caching uses cached items only when those exact items are requested, such as checking for an existing summary of the exact product.

### Question 20: Which of the following is listed as a common cache eviction policy?

Which of the following is listed as a common cache eviction policy?

- [ ] A) Least Recently Used (LRU)
- [ ] B) KV caching
- [ ] C) Retrieval-augmented generation
- [ ] D) SQL execution

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists LRU, LFU, and FIFO as common eviction policies for managing cache size and performance.

### Question 21: Semantic caching works only if you have a reliable way of determini...

Semantic caching works only if you have a reliable way of determining what?

- [ ] A) Whether two queries are similar
- [ ] B) Whether a query is time-sensitive
- [ ] C) Whether a cache uses in-memory storage
- [ ] D) Whether a model API provider implements prompt caching

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** Semantic caching reuses cached results for semantically similar queries, so it depends on reliably determining similarity between queries.

### Question 22: According to the warning in the source, caching that is not properl...

According to the warning in the source, caching that is not properly handled can cause what?

- [ ] A) Data leaks
- [ ] B) Lower cache hit rates only
- [ ] C) Mandatory use of FIFO eviction
- [ ] D) Elimination of vector search

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source warns that improper caching can return cached responses containing one user’s information to another user, causing data leaks.

### Question 23: According to the source, what can agentic patterns help an applicat...

According to the source, what can agentic patterns help an application flow include?

- [ ] A) Only a single sequential step
- [ ] B) Loops, parallel execution, and conditional branching
- [ ] C) Only caching and retrieval
- [ ] D) Only model API calls without feedback

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says agentic patterns can help build complex applications with loops, parallel execution, and conditional branching.

### Question 24: In the retrieval-loop example, what happens after the system genera...

In the retrieval-loop example, what happens after the system generates an output and determines it has not accomplished the task?

- [ ] A) The output is discarded and the query is rejected
- [ ] B) The original response and newly retrieved context are passed into the same model or a different one
- [ ] C) The system only writes the response to the cache
- [ ] D) The system switches permanently to a sequential flow

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source describes feeding the original response together with newly retrieved context into the same or a different model, creating a loop.

### Question 25: What does the source say about giving a model access to write actions?

What does the source say about giving a model access to write actions?

- [ ] A) Write actions cannot change the system’s environment
- [ ] B) Write actions should be added without any special care
- [ ] C) Write actions can make a system more capable but also expose it to significantly more risks
- [ ] D) Write actions are limited to reading cached responses

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states that write actions can make a system vastly more capable but also expose it to significantly more risks, so access should be given with the utmost care.

### Question 26: According to the source, what distinguishes observability from trad...

According to the source, what distinguishes observability from traditional monitoring?

- [ ] A) Monitoring assumes internal states can be inferred from external outputs, while observability makes no such assumption.
- [ ] B) Observability assumes a system’s internal states can be inferred from external outputs, so logs and metrics can help determine what went wrong without shipping new code.
- [ ] C) Monitoring is only for AI applications, while observability is only for traditional software.
- [ ] D) Observability means collecting only numerical metrics, while monitoring means collecting only logs.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says monitoring makes no assumption about the relationship between internal state and outputs, while observability assumes internal states can be inferred from external outputs and debugged via logs and metrics without new code.

### Question 27: Which set lists the three metrics derived from the DevOps community...

Which set lists the three metrics derived from the DevOps community that can help evaluate the quality of a system’s observability?

- [ ] A) MTTD, MTTR, and CFR
- [ ] B) TTFT, TPOT, and TPS
- [ ] C) DAU, session duration, and subscriptions
- [ ] D) Context relevance, context precision, and toxicity

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source identifies MTTD, MTTR, and CFR as the three observability-quality metrics derived from the DevOps community.

### Question 28: According to the source, what is the purpose of a metric?

According to the source, what is the purpose of a metric?

- [ ] A) To maximize an application’s output relevancy score regardless of whether it serves a purpose
- [ ] B) To tell you when something is wrong and to identify opportunities for improvement
- [ ] C) To replace logs and traces entirely
- [ ] D) To guarantee that no application failures occur

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that metrics themselves are not the goal; their purpose is to tell you when something is wrong and to identify opportunities for improvement.

### Question 29: According to the source, how do logs differ from traces?

According to the source, how do logs differ from traces?

- [ ] A) Logs are aggregated numerical measurements, while traces are append-only records of events.
- [ ] B) Logs are an append-only record of events, while traces link related events into a complete timeline of a request or process.
- [ ] C) Logs record only model outputs, while traces record only system prompts.
- [ ] D) Logs are used only for cost tracking, while traces are used only for latency tracking.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source defines logs as an append-only record of events and traces as reconstructed by linking related events to form a complete timeline of a transaction or process.

### Question 30: At a high level, what are the two steps an AI pipeline orchestrator...

At a high level, what are the two steps an AI pipeline orchestrator operates in?

- [ ] A) Components definition and chaining
- [ ] B) Retrieval and generation
- [ ] C) Evaluation and monitoring
- [ ] D) Routing and PII removal

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that an orchestrator operates in two steps: components definition and chaining.

### Question 31: Why might you want to start building your AI application without an...

Why might you want to start building your AI application without an orchestration tool first?

- [ ] A) External tools add complexity and can abstract away critical details, making the system hard to understand and debug
- [ ] B) Orchestrators cannot support any models or databases
- [ ] C) Orchestrators are only useful for batch processing
- [ ] D) Orchestrators are required to meet strict latency requirements

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source warns that any external tool brings additional complexity and that an orchestrator can abstract away critical details, making the system hard to understand and debug.

### Question 32: When designing a pipeline for an application with strict latency re...

When designing a pipeline for an application with strict latency requirements, what does the source recommend?

- [ ] A) Do as much in parallel as possible
- [ ] B) Avoid chaining components together
- [ ] C) Use a general workflow orchestrator like Airflow or Metaflow
- [ ] D) Route every query to a human operator

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source advises that when designing for strict latency requirements, you should try to do as much in parallel as possible.

### Question 33: How does the source distinguish an AI pipeline orchestrator from a...

How does the source distinguish an AI pipeline orchestrator from a general workflow orchestrator?

- [ ] A) An AI pipeline orchestrator is different from a general workflow orchestrator like Airflow or Metaflow
- [ ] B) An AI pipeline orchestrator is the same as Airflow or Metaflow
- [ ] C) A general workflow orchestrator is only for model evaluation
- [ ] D) An AI pipeline orchestrator cannot pass data between components

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source explicitly warns that an AI pipeline orchestrator is different from a general workflow orchestrator, such as Airflow or Metaflow.

### Question 34: According to the text, why does user feedback take on an even more...

According to the text, why does user feedback take on an even more significant role in AI applications than in traditional software applications?

- [ ] A) Because user feedback is proprietary data, and data is a competitive advantage.
- [ ] B) Because user feedback eliminates the need for model evaluation.
- [ ] C) Because user feedback removes all privacy concerns from application development.
- [ ] D) Because user feedback is only useful for fixing software bugs.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that in AI applications user feedback is proprietary data, and data is a competitive advantage. It also says a well-designed feedback system is necessary to create the data flywheel.

### Question 35: What does the text say a well-designed user feedback system is nece...

What does the text say a well-designed user feedback system is necessary to create?

- [ ] A) A hidden API orchestration layer.
- [ ] B) The data flywheel discussed in Chapter 8.
- [ ] C) A latency-free application architecture.
- [ ] D) A replacement for proprietary data.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source explicitly says a well-designed user feedback system is necessary to create the data flywheel discussed in Chapter 8.

### Question 36: What caution does the text emphasize when leveraging user feedback?

What caution does the text emphasize when leveraging user feedback?

- [ ] A) User feedback should never be used to personalize models.
- [ ] B) User feedback should only be collected after competitors catch up.
- [ ] C) User feedback is user data, so user privacy should be respected and users have the right to know how their data is being used.
- [ ] D) User feedback should be avoided because it introduces latency to applications.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says user feedback is user data and requires the same cautions as leveraging any data, including respecting privacy and informing users how their data is used.

### Question 37: According to the text, which statement about explicit and implicit...

According to the text, which statement about explicit and implicit feedback is correct?

- [ ] A) Explicit feedback is inferred from user actions and is highly application-dependent.
- [ ] B) Implicit feedback is standard across applications and easier to interpret.
- [ ] C) Explicit feedback is better understood but can be sparse and suffer from response biases.
- [ ] D) Implicit feedback is always more reliable than explicit feedback.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states explicit feedback is better understood but demands extra effort, can be sparse, and suffers from response biases. Implicit feedback is inferred from actions, application-dependent, and noisier.

### Question 38: Which of the following is an example of early termination as a natu...

Which of the following is an example of early termination as a natural language feedback signal?

- [ ] A) A user says “No, I meant…” to correct the model.
- [ ] B) A user stops a response generation halfway.
- [ ] C) A user complains “Uggh” without explanation.
- [ ] D) A user regenerates a response to compare options.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text defines early termination as stopping a response generation halfway, exiting the app, telling the model to stop, or leaving the agent hanging.

### Question 39: What can be inferred from user edits to model responses, according...

What can be inferred from user edits to model responses, according to the text?

- [ ] A) They are weak signals that should be ignored for model evaluation.
- [ ] B) They provide preference data where the original response is the losing response and the edited response is the winning response.
- [ ] C) They indicate the model’s response was correct and needs no improvement.
- [ ] D) They are only useful for creative tasks like image generation.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says user edits are a strong signal that the original response isn’t quite right and serve as preference data: original generated response is losing, edited response is winning.

### Question 40: How should conversation length be interpreted as a feedback signal?

How should conversation length be interpreted as a feedback signal?

- [ ] A) It is always a positive signal for all applications.
- [ ] B) It is always a negative signal for all applications.
- [ ] C) It depends on the application: for AI companions a long conversation might be positive, but for productivity chatbots it might indicate inefficiency.
- [ ] D) It is unrelated to dialogue diversity and should be ignored.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text explains that whether conversation length is positive or negative depends on the application; for AI companions long conversations might indicate enjoyment, while for productivity chatbots they might indicate inefficiency.

### Question 41: According to the text, what does Apple’s human interface guideline...

According to the text, what does Apple’s human interface guideline warn against regarding feedback?

- [ ] A) Asking for both positive and negative feedback
- [ ] B) Collecting feedback only at signup
- [ ] C) Using implicit signals from conversations
- [ ] D) Letting users transfer to human agents

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says Apple’s human interface guideline warns against asking for both positive and negative feedback.

### Question 42: In Midjourney’s workflow described in the text, which option gives...

In Midjourney’s workflow described in the text, which option gives the strongest positive signal about a chosen image?

- [ ] A) Regenerate
- [ ] B) Generate variations for an image
- [ ] C) Generate an unscaled version of an image
- [ ] D) Continue typing to ignore a suggestion

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says option 1, generating an unscaled version, gives the strongest positive signal about the chosen photo.

### Question 43: Why does the text say standalone AI applications like ChatGPT and C...

Why does the text say standalone AI applications like ChatGPT and Claude face a challenge in collecting high-quality feedback?

- [ ] A) They cannot show side-by-side responses.
- [ ] B) They are not integrated into the user’s daily workflow.
- [ ] C) They are prohibited from using service agreements.
- [ ] D) They always require explicit user consent for thumbs up/down.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says standalone AI applications aren’t integrated into the user’s daily workflow, making it hard to collect high-quality feedback the way integrated products like GitHub Copilot can.

### Question 44: According to the text, what is a potential benefit of making feedba...

According to the text, what is a potential benefit of making feedback signals private?

- [ ] A) It increases discoverability of liked content.
- [ ] B) It guarantees users will give positive feedback.
- [ ] C) Users tend to be more candid, which can result in higher-quality signals.
- [ ] D) It eliminates the need for user consent when collecting context.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says users tend to be more candid in private, with a lower chance of being judged, which can result in higher-quality signals.

### Question 45: According to the source text, what is leniency bias in user feedback?

According to the source text, what is leniency bias in user feedback?

- [ ] A) The tendency for users to rate items more positively than warranted, often to avoid conflict or extra work
- [ ] B) The tendency for users to click the first suggestion more often than later suggestions
- [ ] C) The tendency for users to favor the answer they see last in a comparison
- [ ] D) The tendency for users to provide random feedback because they lack motivation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text defines leniency bias as people rating items more positively than warranted, often because they feel compelled to be nice or because it is the easiest option.

### Question 46: How can position bias be mitigated when designing a feedback system...

How can position bias be mitigated when designing a feedback system, according to the source text?

- [ ] A) By removing the strong negative connotation associated with low ratings
- [ ] B) By randomly varying the positions of suggestions or modeling a suggestion’s true success rate based on its position
- [ ] C) By showing users longer responses in side-by-side comparisons
- [ ] D) By hiding likes so users are not confused about why certain tweets appear

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that position bias can be mitigated by randomly varying the positions of suggestions or by building a model to compute a suggestion’s true success rate based on its position.

### Question 47: What is a degenerate feedback loop as described in the source text?

What is a degenerate feedback loop as described in the source text?

- [ ] A) A loop where users always give five-star ratings because they feel pressured
- [ ] B) A loop where predictions influence feedback, which then influences the next model iteration, amplifying initial biases
- [ ] C) A loop where users compare two long responses and randomly click one without reading both
- [ ] D) A loop where feedback is collected only from users who are in a hurry

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text defines a degenerate feedback loop as occurring when predictions themselves influence feedback, which in turn influences the next iteration of the model, amplifying initial biases.

### Question 48: According to the text, what can happen if user feedback is used ind...

According to the text, what can happen if user feedback is used indiscriminately?

- [ ] A) It can eliminate all model biases automatically.
- [ ] B) It can perpetuate biases and destroy your product.
- [ ] C) It can make observability unnecessary.
- [ ] D) It can prevent the system from generating cat photos.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that user feedback is crucial, but if used indiscriminately, it can perpetuate biases and destroy your product.

### Question 49: What do Sharma et al. (2023) show about AI models trained on human...

What do Sharma et al. (2023) show about AI models trained on human feedback?

- [ ] A) They tend toward sycophancy and are more likely to present responses matching the user’s view.
- [ ] B) They always prioritize accuracy over user satisfaction.
- [ ] C) They become immune to explicit content.
- [ ] D) They stop collecting conversational feedback.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says Sharma et al. (2023) show that models trained on human feedback tend toward sycophancy and are more likely to present user responses matching the user’s view.

### Question 50: According to the summary, which statement about separating componen...

According to the summary, which statement about separating components in an AI application architecture is correct?

- [ ] A) Components must never overlap in functionality.
- [ ] B) Guardrails can only be implemented as a standalone component.
- [ ] C) Separation is fluid, and components can overlap in functionalities.
- [ ] D) Additional components always reduce system complexity.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says separation is necessary for modularity and maintainability but is fluid, with many ways components can overlap in functionalities.

### Question 51: Why are more AI engineers becoming involved in user feedback design?

Why are more AI engineers becoming involved in user feedback design?

- [ ] A) Because user feedback is no longer useful for improving models.
- [ ] B) Because feedback is a crucial source of data for continuously improving AI models and supports the data flywheel.
- [ ] C) Because observability tools have eliminated the need for product experience.
- [ ] D) Because open source applications make feedback collection easier.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says user feedback is a crucial source of data for continuously improving AI models, so more AI engineers are involved to ensure they receive the data they need.
