# 6. RAG and Agents

---

## Context and RAG
- Models need instructions and information; missing context increases mistakes and hallucination.
- Instructions are common to all queries; context is specific to each query.
- This chapter focuses on constructing relevant context for each query.
- RAG retrieves relevant information from external data sources.

---

## Agents and Tools
- The agentic pattern uses tools such as web search and news APIs.
- RAG chiefly constructs context; agents can do much more.
- External tools address model shortcomings and expand capabilities.
- Tools let models interact with the world and automate aspects of life.

---

## What Is RAG?

- RAG enhances a model's generation by retrieving relevant information from external memory sources.
- External memory can be an internal database, a user's previous chat sessions, or the internet.
- The retrieve-then-generate pattern was introduced in "Reading Wikipedia to Answer Open-Domain Questions" (Chen et al., 2017).
- The system retrieves five relevant Wikipedia pages, then a model reads them to generate an answer.

---

## Origins and Benefits

- The term retrieval-augmented generation was coined in "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (Lewis et al., 2020).
- Proposed for knowledge-intensive tasks where all available knowledge can't be input into the model directly.
- Only information most relevant to the query, as determined by the retriever, is retrieved.
- Relevant information helps models generate more detailed responses while reducing hallucinations.

---

## Why RAG Persists

- RAG constructs context specific to each query, instead of using the same context for all queries.
- This helps manage user data, including data specific to a user only in related queries.
- Context construction for foundation models is equivalent to feature engineering for classical ML models.
- Long context won't end RAG: data grows, long contexts are used poorly, and extra tokens cost.

---

## RAG Architecture: Core Components
A RAG system has two components: a retriever and a generator.
The retriever pulls information from external memory sources.
The generator produces a response based on the retrieved information.

---

## Training the Retriever and Generator
In the original RAG paper, Lewis et al. trained both components together.
Today, the two components are often trained separately.
Many teams build RAG systems using off-the-shelf retrievers and models.
Finetuning the whole RAG system end-to-end can significantly improve performance.

---

## Retriever Quality and Functions
The success of a RAG system depends on the quality of its retriever.
A retriever has two main functions: indexing and querying.
Indexing processes data so it can be quickly retrieved later.
Retrieval reduces input tokens while potentially increasing model performance.

---

## Indexing and Querying

- How you index data depends on how you want to retrieve it later.
- Retrieving the data relevant to a query is called querying.
- Indexing and retrieval are therefore paired design decisions.
- Table 6-1 shows a simplified example of an inverted index.

---

## A RAG Walkthrough

- Assume external memory is a database of documents: memos, contracts, meeting notes.
- A document can be as short as 10 tokens or as long as 1 million.
- Naively retrieving whole documents can make your context arbitrarily long.
- Split documents into chunks, retrieve the most relevant chunks, post-process, then prompt.

---

## Terminology: “Document” and “Chunk”

- In this chapter, “document” refers to both a full document and a chunk
- Technically, a chunk of a document is also a document
- This keeps terminology consistent with classical NLP and information retrieval (IR) usage

---

## Retrieval Is Not Unique to RAG
- Information retrieval is a century-old idea, predating RAG by decades.
- It is the backbone of search engines, recommender systems, and log analytics.
- Many retrieval algorithms built for traditional retrieval systems also work for RAG.
- RAG inherits from a mature field rather than starting from scratch.

---

## Scope of This Section
- Information retrieval is a fertile research area with a large supporting industry.
- It cannot be sufficiently covered within a few pages.
- This section therefore covers only the broad strokes of retrieval algorithms.
- In-depth resources are listed in the book's GitHub repository.

---

## Core Idea of Retrieval

- Retrieval ranks documents by their relevance to a given query.
- Retrieval algorithms differ in how relevance scores are computed.
- Two common mechanisms: term-based retrieval and embedding-based retrieval.
- This chapter uses the terms retrieval and search interchangeably.

---

## Two Retrieval Mechanisms

- Term-based retrieval and embedding-based retrieval are the two common mechanisms introduced.
- Each computes relevance scores differently, which is what distinguishes the algorithms.
- Term-based retrieval matches query terms against documents.

---

## Semantic Retrieval

- Embedding-based retrieval is also called semantic retrieval.
- It computes relevance scores differently from term-based retrieval.

---

## Sparse Versus Dense Retrieval

- Sparse vectors have mostly zero values; dense vectors have mostly nonzero values.
- This book uses term-based versus embedding-based categories instead of sparse versus dense.
- Term-based retrieval is sparse: each term can be a one-hot vector.
- One-hot vector size equals vocabulary length, with 1 at the term's index.

---

## One-Hot Vector Example

- Given the dictionary `{"food": 0, "banana": 1, "slug": 2}`:
- "food" is `[1, 0, 0]`
- "banana" is `[0, 1, 0]`
- "slug" is `[0, 0, 1]`

---

## Why the Division Matters

- Embedding-based retrieval is typically dense, since embeddings are generally dense vectors.
- SPLADE uses sparse embeddings: BERT-generated embeddings regularized toward zero for efficiency.
- Sparse-versus-dense grouping miscategorizes SPLADE with term-based algorithms.
- SPLADE's operations, strengths, and weaknesses resemble dense embedding retrieval more closely.

---

## Term-Based Retrieval: TF and IDF
- Lexical retrieval finds documents containing query keywords, but many matches may exceed context space.
- Term frequency (TF): number of times a term appears in a document; higher TF assumed more relevant.
- Inverse document frequency (IDF): term importance inversely proportional to number of documents containing it.
- IDF(t) = log(N / C(t)); common words like "for" and "at" have low IDF.

---

## TF-IDF, Elasticsearch, and BM25
- TF-IDF score sums IDF(tᵢ) × f(tᵢ, D) across query terms.
- Elasticsearch (built on Lucene) uses an inverted index mapping terms to documents, plus term frequency and document count.
- Okapi BM25 (Robertson et al., 1980s) modifies TF-IDF by normalizing term frequency by document length.
- BM25 and variants (BM25+, BM25F) remain widely used and serve as formidable baselines.

---

## Tokenization and N-Gram Overlap
- Tokenization breaks queries into terms; simple word splitting can break multi-word terms like "hot dog".
- Treating common n-grams (e.g., the bigram "hot dog") as terms helps preserve meaning.
- Pipelines may lowercase, remove punctuation, and eliminate stop words; NLTK, spaCy, CoreNLP offer tokenization.
- N-gram overlap retrieval works best when query and documents are of similar lengths.

---

## Embedding-Based (Semantic) Retrieval
- Term-based retrieval matches lexical text, not meaning, so it can return irrelevant documents.
- Embedding-based retrieval, or semantic retrieval, ranks documents by how closely meanings align with the query.
- Indexing converts data chunks into embeddings stored in a vector database.
- Querying embeds the query with the same model, then fetches the k closest chunks.

---

## Semantic Retrieval Workflow and Vector Search
- Real systems may add a reranker over retrieved candidates and caches to reduce latency.
- Retrieval fails if the embedding model is bad.
- Vector databases must index and store vectors so vector search is fast and efficient.
- Vector search is framed as nearest-neighbor search and is used beyond generative AI.

---

## k-NN Versus Approximate Nearest Neighbor
- Naive k-NN computes similarity to all vectors, ranks them, and returns the top k.
- k-NN is precise but computationally heavy and slow; use it only for small datasets.
- Large datasets typically use approximate nearest neighbor (ANN) algorithms.
- Popular libraries include FAISS, Google's ScaNN, Spotify's Annoy, and Hnswlib.

---

## Comparing Retrieval Algorithms
- Term-based retrieval is much faster during indexing and querying, and works well out of the box.
- It has fewer components to tweak, and term ambiguity can retrieve wrong documents.
- Embedding-based retrieval can outperform term-based retrieval with finetuning of models and retriever.
- Embeddings can obscure keywords like error codes or product names, making them harder to search.

---

## Evaluating Retrieval Quality
- Context precision: of all documents retrieved, what percentage is relevant to the query?
- Context recall: of all relevant documents, what percentage is retrieved?
- Ranking metrics include NDCG, MAP, and MRR; context recall needs annotating all documents.
- For semantic retrieval, also evaluate embeddings independently, e.g., with the MTEB benchmark.

---

## Indexing, Querying, and Trade-offs
- Detailed indexes give accurate, fast queries but cost more time and memory to build.
- HNSW is accurate and fast at query time; LSH builds faster but queries slower and less accurately.
- ANN-Benchmarks compares algorithms using recall, QPS, build time, and index size.
- BEIR is an evaluation harness supporting retrieval systems across 14 common benchmarks.

---

## Hybrid Search

- Production retrieval systems typically combine several retrieval algorithms with distinct advantages.
- Combining term-based retrieval and embedding-based retrieval is called *hybrid search*.
- Term-based retrieval matches exact terms; embedding-based (semantic) retrieval ranks by meaning.
- Different algorithms can be combined in sequence or in parallel.

---

## Sequential Retrieval and Reranking

- First, a cheap, less precise retriever such as a term-based system fetches candidates.
- Then a more precise but more expensive mechanism, such as k-nearest neighbors, finds the best candidates.
- This second step is also called *reranking*.
- Example: fetch all documents containing "transformer," then vector search for the relevant ones.

---

## Parallel Ensembles and RRF

- Multiple retrievers can fetch candidates simultaneously as an ensemble.
- Retriever rankings are combined to generate a final ranking.
- Reciprocal rank fusion (RRF) scores each document based on its ranking by a retriever.
- Ranked first scores 1/1 = 1; ranked second scores ½ = 0.5 — higher rank, higher score.

---

## Retrieval Optimization: Four Tactics
- Four tactics increase the chance of fetching relevant documents: chunking strategy, reranking, query rewriting, contextual retrieval.
- Chunking strategy significantly impacts retrieval system performance; indexing depends on how you intend to retrieve.
- Reranking refines initial rankings; query rewriting makes ambiguous queries self-contained.
- Contextual retrieval augments each chunk with relevant context to ease retrieval.

---

## Chunking Strategy
- Simplest: equal-length chunks by characters, words, sentences, or paragraphs.
- Recursive splitting uses increasingly smaller units until each chunk fits the maximum size.
- Overlapping chunks prevent losing boundary information; e.g., 2,048-character chunks with 20-character overlap.
- Chunk size must not exceed the generative model's context length or the embedding model's limit.

---

## Chunk Size Trade-offs
- Smaller chunks allow more diverse information and fit more chunks into the model's context.
- Halving chunk size lets you fit twice as many chunks, giving a wider range of information.
- Small chunks risk losing important information and increase computational overhead for embedding-based retrieval.
- There is no universal best chunk size or overlap size; you must experiment.

---

## Reranking
- Initial rankings from the retriever can be reranked to be more accurate.
- Useful to reduce retrieved documents to fit the model's context or cut input tokens.
- A cheap, less precise retriever fetches candidates; a precise, expensive mechanism reranks them.
- Documents can be reranked by time, weighting recent data for news, email chat, or stock analysis.

---

## Query Rewriting
- Also called query reformulation, query normalization, and sometimes query expansion.
- Ambiguous follow-ups like "How about Emily Doe?" must be rewritten to stand alone.
- Other AI models can rewrite using a prompt describing the conversation and last user input.
- Identity resolution may require database lookups; the model should admit unsolvable queries rather than hallucinate.

---

## Contextual Retrieval
- Augment each chunk with relevant context so relevant chunks are easier to retrieve.
- Simple technique: add metadata like tags, keywords, descriptions, reviews, titles, or captions.
- Metadata can include automatically extracted entities, such as error codes, retrievable by keyword.
- Chunks can be augmented with the questions they answer, useful for customer support articles.

---

## Anthropic's Contextual Retrieval
- Chunks split from a document may lack context about what the chunk is about.
- Augment each chunk with the original document's title, summary, or generated context.
- Anthropic used AI models to generate 50-100 tokens situating each chunk in the document.
- Generated context is prepended to each chunk, then the augmented chunk is indexed.

---

## Evaluating Retrieval Solutions

- Check which retrieval mechanisms are supported, including hybrid search.
- For vector databases, verify supported embedding models and vector search algorithms.
- Assess scalability for data storage and query traffic, and fit with your traffic patterns.
- Consider indexing time, bulk processing limits, query latency, and managed pricing structure.

---

## Multimodal RAG

- Multimodal generators can augment contexts with images, videos, and audio, not just text.
- Given a query, the retriever fetches relevant texts and images to help answer.
- Images with metadata—titles, tags, captions—can be retrieved using that metadata.
- For content-based image retrieval, use a multimodal embedding model like CLIP for both images and queries.

---

## RAG with Tabular Data

- Many queries need information from data tables, requiring a workflow different from classic RAG.
- Workflow: text-to-SQL determines the query from user query and schemas.
- Then execute the SQL query, and generate a response from the result and original query.
- Text-to-SQL can use the same generator or a specialized model; predict tables if schemas don't fit.

---

## Agents and Tool Use
- Tools like retrievers and SQL executors help models handle more queries and generate higher-quality responses.
- Tool use is a core characteristic of the agentic pattern.
- Russell and Norvig define AI research as "the study and design of rational agents."
- Intelligent agents are considered by many to be the ultimate goal of AI.

---

## Agentic Applications
- Foundation models' unprecedented capabilities enable previously unimaginable agentic applications.
- Autonomous, intelligent agents can act as assistants, coworkers, and coaches.
- Examples: create a website, gather data, plan a trip, do market research, manage accounts.
- Potential economic value of these agents is enormous.

---

## Agent Overview: Definition

- An agent is anything that can perceive its environment and act upon that environment.
- Agents are characterized by their *environment* and their *set of actions*.
- Environment is defined by the use case: a game, the internet, a kitchen, a road system.
- The set of actions an agent can perform is augmented by its *tools*.

---

## Agents, Tools, and Environment

- ChatGPT is an agent: it can search the web, execute Python, and generate images.
- RAG systems are agents; retrievers and SQL executors are their tools.
- There's a strong dependency: the environment determines which tools are potentially usable.
- Tool inventory also restricts the environment—a swimming-only robot is confined to water.
- AI is the brain: it processes the task and feedback, plans actions, and checks completion.

---

## Agent Workflow and Model Requirements

- SWE-agent's environment is the computer; actions include navigate repo, search, view, edit lines.
- Kitty Vogue RAG agent has three actions: response generation, SQL generation, SQL execution.
- It reasons, invokes tools, reasons over outputs, and decides when the task is complete.
- Compound mistakes: accuracy drops with steps—95% per step becomes 60% over 10 steps.

---

## Tools and Agent Capabilities
- External tools vastly expand agent capabilities; success depends on tool inventory and AI planner strength.
- Tools enable perception (read-only actions) and action (write actions) on the environment.
- More tools increase capabilities but make understanding and utilization harder; experimentation finds the right set.
- Three categories: knowledge augmentation, capability extension, and tools to act upon the environment.

---

## Knowledge Augmentation and Capability Extension
- Knowledge augmentation tools include retrievers, SQL executors, people search, inventory APIs, and web browsing for current information.
- Web browsing reduces staleness and hallucinations but exposes agents to unreliable internet content; select APIs carefully.
- Capability extension tools address model limitations: calculators, converters, translators, and code interpreters.
- Tool use can outperform prompting or finetuning; Chameleon with 13 tools improved ScienceQA by 11.37% and TabMWP by 17%.

---

## Write Actions and Risks
- Write actions let agents modify data sources, e.g., SQL changes, email responses, or bank transfers.
- Write actions enable automation of workflows like customer outreach, from research to order updates.
- Giving AI write access is risky; unreliable agents should not initiate bank transfers or delete production databases.
- Trust in capabilities and security is crucial; protect systems from bad actors manipulating agents into harmful actions.

---

## Why Agent Safety Matters
- An AI system can cause harm without any presence in the physical world.
- It can manipulate the stock market, steal copyrights, and violate privacy.
- It can also reinforce biases and spread misinformation and propaganda.
- Any organization leveraging AI must take safety and security seriously.

---

## Tools Extend Model Capabilities
- The right tools make humans vastly more productive—think Excel or cranes.
- Tools likewise enable models to accomplish many more tasks.
- Many model providers support tool use, often called function calling.
- Function calling with a wide set of tools is expected to become common.

---

## Trusting Autonomous Systems
- Safety concerns don't mean AI should never be allowed to act.
- People already trust machines to take us into space.
- Humans can fail too; a self-driving car may beat the average stranger.

---

## Planning: Task, Goal, and Constraints

- A task is defined by its goal and its constraints.
- Example: a two-week San Francisco–to–India trip with a $5,000 budget.
- The goal is the two-week trip; the budget is the constraint.
- Complex tasks require planning before execution.

---

## What a Plan Is

- The output of planning is a plan: a roadmap of steps to accomplish a task.
- Effective planning requires understanding the task and considering different options.
- The model then chooses the most promising option.
- Planning is hard and is a well-studied computational problem.

---

## Planning: Decomposition and Efficiency

- A task can be decomposed in many ways, but not all lead to success.
- Among correct solutions, some are more efficient than others.
- Example: find companies with $1B raised, then filter by revenue — more efficient.
- Coupling planning with execution risks long, fruitless runs without oversight.

---

## Decoupling Planning from Execution

- Generate a plan first; execute it only after the plan is validated.
- Validate with heuristics: eliminate invalid actions or plans exceeding X steps.
- AI judges can assess whether a plan seems reasonable or how to improve it.
- Bad plans are regenerated; good plans execute, and outputs are evaluated again.

---

## Parallel Plans and Intent Classification

- Generate several plans in parallel and let an evaluator pick the most promising.
- This is a latency/cost trade-off: parallel generation incurs extra costs.
- Planning requires understanding intent: what is the user trying to do?
- Intent classification helps the agent pick the right tools for the query.

---

## Planning: Generating, Validating, Executing

- Agents can automate three stages: generating plans, validating plans, and executing plans.
- Humans can be involved at any stage to aid the process and mitigate risks.
- A human expert can provide a high-level plan that the agent expands upon.
- For risky operations, systems can require explicit human approval before execution.

---

## Decoupling Planning and Execution

- Clearly define the level of automation an agent can have for each action.
- Risky operations include updating a database or merging a code change.
- Systems can ask for human approval or let humans execute these operations.
- Only validated plans should be executed.

---

## The Four Core Processes

- Plan generation: come up with a sequence of manageable actions, also called task decomposition.
- Reflection and error correction: evaluate the generated plan; if bad, generate a new one.
- Execution: take the actions outlined in the plan, often involving calling specific functions.
- Reflection and error correction: evaluate outcomes, correct mistakes, and replan if incomplete.

---

## Reflection Is Optional but Valuable

- Reflection isn't mandatory for an agent but significantly boosts performance.
- Asking a model to "think step by step" is asking it to decompose a task.
- Asking a model to "verify if your answer is correct" is asking it to reflect.
- Intent classifiers should label out-of-scope requests IRRELEVANT so agents reject them politely.

---

## Foundation Models as Planners: The Debate

- LeCun states autoregressive LLMs can't plan; Kambhampati argues LLMs extract knowledge, not plans.
- Kambhampati warns LLM-generated plans may look reasonable but cause execution-time errors.
- Anecdotal evidence of poor planning exists, but the cause remains unclear.
- Unclear whether LLMs lack ability or lack the right tooling and prompting.

---

## Planning Is a Search Problem

- Planning means searching paths to a goal, predicting each path's reward, and picking the best.
- Search often requires backtracking: abandon a weak action and try an alternative.
- Autoregressive models can effectively backtrack by revising the path or starting over.
- Planning needs outcome knowledge per action, not just action sequences like chain-of-thought.

---

## FM Planners Versus RL Planners

- RL agents and FM agents are both characterized by environments and possible actions.
- In RL agents, the planner is trained by an RL algorithm, requiring much time and resources.
- In FM agents, the model itself is the planner, promptable or finetunable with fewer resources.
- Nothing prevents FM agents from incorporating RL algorithms; the two may eventually merge.

---

## Plan Generation Basics
- Prompt engineering is the simplest way to turn a model into a plan generator.
- An example prompt for plan generation is provided for illustration.
- Production prompts are likely more complex than the example prompt.

---

## Example: Kitty Vogue Agent
- The example agent helps customers learn about products at Kitty Vogue.
- The agent has access to three external tools.
- Tools retrieve products by price, top products, and product information.
- The example prompt is for illustration only.

---

## Planning with a System Prompt
- The system prompt asks the model to propose a plan to solve the task.
- Five actions are available: get_today_date, fetch_top_products, fetch_product_info, generate_query, generate_response.
- The plan must be a sequence of valid actions.
- Examples show plans for product information and best-selling product tasks.

---

## Example Plans
- Task "Tell me about Fruity Fedora" maps to fetch_product_info, generate_query, generate_response.
- Task "What was the best selling product last week?" maps to fetch_top_products, generate_query, generate_response.
- The prompt ends with Task: {USER INPUT} for the user's request.
- Plans chain tool calls before generating the final response.

---

## Decoupling Planning and Execution
- Planning can be separated from execution.
- Only validated plans are executed.

---

## Plan Structure and Parameters
- A plan is a list of functions whose parameters the agent infers.
- This format is one of many ways to structure agent control flow.
- Tool output at each step is added to the task's history.
- `generate_query` uses current history and recent tool outputs to build a query.

---

## Ambiguity and Hallucinated Plans
- Exact parameters are hard to predict; they are often extracted from previous tool outputs.
- If `get_time()` outputs "2030-09-13", the agent can derive the next call's dates.
- Ambiguous requests leave unclear how many products or which time range.
- Models must guess, and hallucinated plans can call invalid functions or wrong parameters.

---

## Improving Planning
- Write a better system prompt with more examples.
- Give better descriptions of tools and their parameters.
- Refactor complex functions into simpler ones; use a stronger model.
- Finetune a model for plan generation.

---

## Function Calling and Tools
- Many model providers offer tool use, turning models into agents.
- A tool is a function; invoking a tool is called function calling.
- APIs differ, but function calling generally follows a tool inventory workflow.
- A tool inventory declares each tool’s entry point, parameters, and documentation.

---

## Specifying Tools per Query
- Different queries might need different tools.
- Many APIs let you specify declared tools per query.
- Some APIs offer further settings to control tool use.
- Figure 6-10 shows a model using two simple tools.

---

## Tool Use: `required`

- The `required` setting forces the model to use at least one tool.
- It is a tool-choice option controlling whether tool calls must occur.
- Use it when a response must involve tool invocation rather than plain text.

---

## Tool Use Modes

- `none`: the model shouldn’t use any tool.
- `auto`: the model decides which tools to use.
- Function calling is shown in Figure 6-10 as pseudocode, representative of multiple APIs.
- Given a query, the agent generates which tools to use and their parameters.

---

## Example: Pounds to Kilograms

- Query: “How many kilograms are 40 pounds?”
- The agent selects `lbs_to_kg_tool` with one parameter value of 40.
- The response has `finish_reason` `'tool_calls'` and a `ToolCall` with function `lbs_to_kg`.
- Arguments are `'{"lbs":40}'`, so you can evoke `lbs_to_kg(lbs=40)`.

---

## Limits of Function Calling APIs

- Some APIs ensure only valid functions are generated.
- They cannot guarantee the correct parameter values.
- The tool output is then used to generate a response to the user.

---

## Inspecting Agent Function Calls
- Ask agents to report parameter values used for each function call.
- Inspect reported values to verify they are correct.
- Use this practice when working with agents.

---

## Planning Granularity
- A plan is a roadmap of steps needed to accomplish a task
- Plans can be at different granularity levels: yearly, quarterly, monthly, weekly
- A quarter-by-quarter plan is higher-level than a month-by-month plan
- Planning/execution trade-off: detailed plans are harder to generate but easier to execute

---

## Hierarchical Planning
- Higher-level plans are easier to generate but harder to execute
- Circumvent the trade-off by planning hierarchically
- First, a planner generates a high-level plan, such as quarter-to-quarter
- Then, the same or a different planner generates a month-to-month plan per quarter

---

## Natural Language Plans
- Using exact function names is very granular and breaks when tool inventories change
- Renaming `get_time()` to `get_current_time()` requires updating prompts, examples, and finetuning
- Natural language plans are more robust to tool API changes and less prone to hallucination
- Downside: a translator is needed, but translating is simpler than planning for weaker models

---

## Control Flow in Complex Plans
- Control flow is the order in which plan actions can be executed.
- Sequential is one control flow; plans can also use parallel, if statement, and for loop.
- Figure 6-11 shows examples of different plan execution orders.

---

## Sequential and Parallel Execution
- Sequential: execute task B after task A is complete, often because B depends on A.
- Example: execute the SQL query only after translating it from natural language input.
- Parallel: execute tasks A and B at the same time.
- Example: retrieve top 100 best-selling products, then retrieve each product’s price.

---

## Control Flows in Plans

- Plans can include non-sequential control flows, not just fixed step sequences.
- *If statement*: execute task B or C depending on the previous step's output.
- Example: check NVIDIA's earnings report, then decide to sell or buy stocks.
- *For loop*: repeat task A until a specific condition is met.

---

## Non-Sequential Plans Are Harder

- Example of a loop: keep generating random numbers until a prime number appears.
- In traditional software engineering, control flow conditions are exact.
- With AI-powered agents, AI models determine the control flows.
- Plans with non-sequential control flows are harder to generate and translate into commands.

---

## Evaluating Agent Frameworks

- Check which control flows an agent framework supports before adopting it.
- Consider whether tasks can run simultaneously, such as browsing ten websites at once.
- Parallel execution can significantly reduce the latency perceived by users.

---

## Reflection and Error Correction
- Reflection evaluates and adjusts plans; necessary for agent success, though not strictly necessary to operate.
- Use it after a query, plan generation, each execution step, and full execution.
- Reflection uncovers errors; error correction fixes them; use self-critique or a specialized scorer.
- In multi-agent reflection, one agent plans and acts; another evaluates outcomes.

---

## ReAct: Reasoning and Action
- ReAct interleaves reasoning and action: Thought, Act, Observation, until reflection determines finish.
- Yao et al. used “reasoning” to encompass both planning and reflection.
- The agent explains thinking, takes actions, then analyzes observations until finished.
- ReAct prompts use examples to encourage the required output format.

---

## Reflexion and Tradeoffs
- Reflexion separates an evaluator that evaluates outcomes from a self-reflection module analyzing what went wrong.
- The authors call a plan a “trajectory”; after evaluation and self-reflection, the agent proposes a new trajectory.
- Reflection is relatively easy to implement and can bring surprisingly good performance improvement.
- Downsides are latency and cost; thoughts, observations, and examples consume tokens and context.

---

## Tool Selection: Trade-offs

- Tools are essential to task success, so choosing them needs careful consideration.
- The right tools depend on the environment, the task, and the AI model.
- More tools add capability, but make efficient use harder and lengthen descriptions.
- Growing tool descriptions may not fit into a model's context window.

---

## Evaluating Your Tool Set

- Compare agent performance across different sets of tools.
- Run an ablation study: remove a tool and check for performance drops.
- Remove tools that can be dropped without hurting performance.
- Plot tool-call distributions; replace tools the agent frequently misuses.

---

## Tasks and Models Differ

- Agent literature spans wide inventories: Toolformer used five tools, Chameleon thirteen, Gorilla 1,645 APIs.
- Different tasks need different tools: ScienceQA relies on knowledge retrieval more than TabMWP.
- Different models prefer different tools: GPT-4 selects a wider set than ChatGPT.
- ChatGPT favors image captioning; GPT-4 favors knowledge retrieval.

---

## Evaluating Agent Frameworks
- Evaluate what planners and tools a framework supports.
- Different frameworks focus on different tool categories.
- AutoGPT focuses on social media APIs; Composio on enterprise APIs.
- Assess how easily you can extend the agent with new tools.

---

## Tool Creation and Transition
- Humans create more powerful tools from simpler ones; can AI?
- Chameleon studies tool transition: after tool X, how likely is tool Y?
- Frequently co-used tools can be combined into a bigger tool.
- An agent aware of this can build more complex tools continually.

---

## Agent Failure Modes
- Evaluation detects failures; complex tasks create more failure points.
- Agents have unique failures from planning, tool execution, and efficiency.
- Identify failure modes and measure how often each occurs.
- Benchmarks include Berkeley Function Calling Leaderboard, AgentOps harness, TravelPlanner.

---

## Planning Failures
- Tool use failures include invalid tools, invalid parameters, and incorrect parameter values.
- Goal failures: plan doesn’t solve task or violates constraints like budget or time.
- Reflection errors: agent believes task is complete when it is not.
- Evaluate with `(task, tool inventory)` tuples and generated plans.

---

## Tool Failures and Efficiency
- Tool failures occur when correct tool is used but output is wrong.
- Translation errors and missing tools can also cause tool failures.
- Test each tool independently; print tool calls and outputs.
- Track steps, cost, and action time to evaluate efficiency.

---

## Three Memory Mechanisms

- Internal knowledge: what the model retains from training data; changes only when the model is updated.
- Short-term memory: the model's context; fast but limited, and does not persist across tasks.
- Long-term memory: external data accessed via retrieval; persists across tasks and can be deleted without retraining.
- Choose by frequency of use: essential information via training, rare information in long-term memory.

---

## Why Memory Matters

- Manage information overflow within a session by storing excess information in long-term memory.
- Persist information between sessions, letting agents personalize actions using conversation history.
- Boost consistency: referencing previous answers helps a model calibrate future answers.
- Maintain data structural integrity by storing structured data such as tables or queues.

---

## Memory Management

- A memory system has two functions: memory management and memory retrieval.
- Memory retrieval resembles RAG retrieval, since long-term memory is an external data source.
- Management means adding and deleting memory; short-term memory needs a strategy due to context limits.
- FIFO is simplest but can lose important early information; summarization and reflection reduce redundancy.

---

## RAG Recap
- RAG retrieves relevant external information, then generates more accurate responses.
- Retriever quality determines RAG success; term-based methods are lighter strong baselines.
- Embedding-based retrievers are more compute-intensive but may outperform term-based algorithms.
- RAG addresses context limits and improves response quality while reducing costs.

---

## Agents Recap
- RAG can be a special case of an agent, with the retriever as a tool.
- An agent is defined by its environment and accessible tools; AI acts as planner.
- Reflection and memory help models plan complex tasks and track progress.
- More tools expand capabilities, but automated failures can be catastrophic; security defenses are needed.

---

## Shared Themes and Limits
- Both RAG and agents manage information often exceeding the model’s maximum context length.
- A memory system is needed to manage and use all this information.
- Both are prompt-based methods that affect model quality through inputs, not model modification.
- Contradictory information can confuse agents but also offer different perspectives; handling depends on use case.

## Practice Questions

### Question 1: According to the text, what are the two dominating patterns for con...

According to the text, what are the two dominating patterns for context construction?

- [ ] A) RAG and agents
- [ ] B) Instructions and context
- [ ] C) Web search and news APIs
- [ ] D) Hallucination and mistakes

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that the two dominating patterns for context construction are RAG, or retrieval-augmented generation, and agents.

### Question 2: What does the RAG pattern allow the model to do?

What does the RAG pattern allow the model to do?

- [ ] A) Retrieve relevant information from external data sources
- [ ] B) Use tools such as web search and news APIs
- [ ] C) Write good instructions for all queries
- [ ] D) Directly interact with the world

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says the RAG pattern allows the model to retrieve relevant information from external data sources.

### Question 3: According to the text, what is a key difference between the RAG pat...

According to the text, what is a key difference between the RAG pattern and the agentic pattern?

- [ ] A) RAG is chiefly used for constructing context, while the agentic pattern can do much more, including interacting with the world
- [ ] B) RAG uses tools such as web search, while agents retrieve from external data sources
- [ ] C) RAG is for writing instructions, while agents are for constructing context
- [ ] D) RAG automates aspects of our lives, while agents only retrieve information

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that the RAG pattern is chiefly used for constructing context, while the agentic pattern can do much more, and external tools give models the ability to directly interact with the world.

### Question 4: What does RAG enhance a model's generation with?

What does RAG enhance a model's generation with?

- [ ] A) Fine-tuning on user-specific data
- [ ] B) Retrieving relevant information from external memory sources
- [ ] C) Increasing the model's parameter count
- [ ] D) Compressing the model's context window

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text defines RAG as a technique that enhances a model's generation by retrieving the relevant information from external memory sources.

### Question 5: Who coined the term retrieval-augmented generation?

Who coined the term retrieval-augmented generation?

- [ ] A) Chen et al., 2017
- [ ] B) Lewis et al., 2020
- [ ] C) The document reader paper
- [ ] D) The Wikipedia question-answering study

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that the term retrieval-augmented generation was coined in "RetrievalAugmented Generation for Knowledge-Intensive NLP Tasks" (Lewis et al., 2020).

### Question 6: According to the author, why won't a sufficiently long context end...

According to the author, why won't a sufficiently long context end RAG?

- [ ] A) RAG is cheaper to train than long-context models
- [ ] B) Long contexts cannot be evaluated properly
- [ ] C) Some applications require context longer than any model's limit, and long context doesn't guarantee good use of that context
- [ ] D) Retrievers are always more accurate than foundation models

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text argues that some applications will require context longer than any model's limit, and that a model able to process long context doesn't necessarily use it well, with extra tokens adding cost and latency.

### Question 7: According to the source, what are the two components of a RAG system?

According to the source, what are the two components of a RAG system?

- [ ] A) A retriever and a generator
- [ ] B) An indexer and a tokenizer
- [ ] C) A prompt and a knowledge base
- [ ] D) A long-context model and a fine-tuned model

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that a RAG system has a retriever that retrieves information from external memory sources and a generator that generates a response based on the retrieved information.

### Question 8: How did the original RAG paper by Lewis et al. train the retriever...

How did the original RAG paper by Lewis et al. train the retriever and generative model?

- [ ] A) They trained them separately using off-the-shelf components.
- [ ] B) They trained the retriever and the generative model together.
- [ ] C) They used only a retriever without a generative model.
- [ ] D) They avoided fine-tuning the whole RAG system.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says that in the original RAG paper, Lewis et al. trained the retriever and the generative model together, while today’s systems often train them separately.

### Question 9: What are the two main functions of a retriever in a RAG system?

What are the two main functions of a retriever in a RAG system?

- [ ] A) Indexing and querying
- [ ] B) Generating and summarizing
- [ ] C) Tokenizing and embedding
- [ ] D) Prompting and fine-tuning

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that a retriever has two main functions: indexing, which processes data so it can be quickly retrieved later, and querying.

### Question 10: According to the text, what is the process of retrieving data relev...

According to the text, what is the process of retrieving data relevant to a query called?

- [ ] A) Indexing
- [ ] B) Chunking
- [ ] C) Querying
- [ ] D) Post-processing

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states that retrieving data relevant to a query is called querying.

### Question 11: Why does the text recommend splitting each document into more manag...

Why does the text recommend splitting each document into more manageable chunks?

- [ ] A) To reduce the storage cost of the document database
- [ ] B) To avoid the context becoming arbitrarily long from naively retrieving whole documents
- [ ] C) To make the generative model produce longer responses
- [ ] D) To eliminate the need for post-processing

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text explains that naively retrieving whole documents can cause the context to be arbitrarily long, so documents are split into chunks to avoid this.

### Question 12: What is the purpose of the minor post-processing described in the t...

What is the purpose of the minor post-processing described in the text?

- [ ] A) To index the documents before retrieval
- [ ] B) To split documents into workable chunks
- [ ] C) To join the retrieved data chunks with the user prompt to generate the final prompt
- [ ] D) To train the generative model on the retrieved data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states that minor post-processing is often needed to join the retrieved data chunks with the user prompt to generate the final prompt.

### Question 13: According to the text, what determines how data should be indexed?

According to the text, what determines how data should be indexed?

- [ ] A) The size of the generative model
- [ ] B) How you want to retrieve the data later on
- [ ] C) The number of users submitting queries
- [ ] D) The length of the user prompt

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says that how to index data depends on how you want to retrieve it later on.

### Question 14: In this chapter, what does the term "document" refer to?

In this chapter, what does the term "document" refer to?

- [ ] A) Only full, unprocessed source files
- [ ] B) Both "document" and "chunk"
- [ ] C) Only chunks retrieved by a vector database
- [ ] D) Only documents stored in a classical IR system

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The note states that "document" is used to refer to both "document" and "chunk."

### Question 15: Why does the author use "document" to refer to a chunk as well?

Why does the author use "document" to refer to a chunk as well?

- [ ] A) Because chunks are always larger than documents
- [ ] B) Because technically, a chunk of a document is also a document
- [ ] C) Because chunks are never stored as separate records
- [ ] D) Because classical IR systems do not recognize chunks

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The note explains that a chunk of a document is technically also a document.

### Question 16: The author keeps the chapter's terminology consistent with the term...

The author keeps the chapter's terminology consistent with the terminologies of which fields?

- [ ] A) Classical NLP and information retrieval (IR)
- [ ] B) Computer vision and signal processing
- [ ] C) Database systems and distributed computing
- [ ] D) Compiler design and programming languages

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The note says the terminology is kept consistent with classical NLP and information retrieval (IR) terminologies.

### Question 17: According to the source text, why is retrieval not unique to RAG?

According to the source text, why is retrieval not unique to RAG?

- [ ] A) It is a century-old idea and the backbone of search engines, recommender systems, and log analytics.
- [ ] B) It was invented specifically for RAG systems.
- [ ] C) It is only used in recommender systems.
- [ ] D) It has no supporting industry.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states retrieval is a century-old idea and the backbone of search engines, recommender systems, log analytics, etc.

### Question 18: What does the source text say about retrieval algorithms developed...

What does the source text say about retrieval algorithms developed for traditional retrieval systems?

- [ ] A) They cannot be used for RAG.
- [ ] B) Many of them can also be used for RAG.
- [ ] C) They are only useful for log analytics.
- [ ] D) They are unrelated to information retrieval.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says many retrieval algorithms developed for traditional retrieval systems can also be used for RAG.

### Question 19: Why does the section cover only the broad strokes of information re...

Why does the section cover only the broad strokes of information retrieval?

- [ ] A) Because information retrieval is a fertile research area with a large supporting industry that can hardly be sufficiently covered within a few pages.
- [ ] B) Because RAG does not use retrieval algorithms.
- [ ] C) Because search engines are the only retrieval system.
- [ ] D) Because the GitHub repository has no resources.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text explains that information retrieval is a fertile research area with a large supporting industry that can hardly be sufficiently covered within a few pages.

### Question 20: Where does the source text point readers for more in-depth resource...

Where does the source text point readers for more in-depth resources on information retrieval?

- [ ] A) This book’s GitHub repository
- [ ] B) A recommender systems manual
- [ ] C) A log analytics dashboard
- [ ] D) A search engine patent

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says to see this book’s GitHub repository for more in-depth resources on information retrieval.

### Question 21: According to the text, what does retrieval do at its core?

According to the text, what does retrieval do at its core?

- [ ] A) It ranks documents based on their relevance to a given query.
- [ ] B) It clusters documents according to their length.
- [ ] C) It generates new documents from a query.
- [ ] D) It trains embedding models on a database.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that at its core, retrieval works by ranking documents based on their relevance to a given query.

### Question 22: According to the text, what causes retrieval algorithms to differ?

According to the text, what causes retrieval algorithms to differ?

- [ ] A) How relevance scores are computed
- [ ] B) The number of users accessing the system
- [ ] C) The physical location of the database
- [ ] D) The programming language used by the query

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says retrieval algorithms differ based on how relevance scores are computed.

### Question 23: Which two retrieval mechanisms does the chapter start with?

Which two retrieval mechanisms does the chapter start with?

- [ ] A) Term-based retrieval and embedding-based retrieval
- [ ] B) Keyword retrieval and graph retrieval
- [ ] C) Semantic retrieval and hybrid retrieval
- [ ] D) SQL retrieval and NoSQL retrieval

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text explicitly says it will start with two retrieval mechanisms: term-based retrieval and embedding-based retrieval.

### Question 24: According to the note, how does retrieval typically differ from sea...

According to the note, how does retrieval typically differ from search?

- [ ] A) Retrieval is typically limited to one database or system, while search involves retrieval across various systems.
- [ ] B) Retrieval always uses embeddings, while search always uses terms.
- [ ] C) Retrieval is for documents, while search is only for databases.
- [ ] D) Retrieval requires multiple systems, while search is limited to one database.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The note states that retrieval is typically limited to one database or system, whereas search involves retrieval across various systems.

### Question 25: According to the source text, what categorization of retrieval algo...

According to the source text, what categorization of retrieval algorithms does the book use instead of sparse versus dense?

- [ ] A) Lexical versus semantic retrieval
- [ ] B) Term-based versus embedding-based retrieval
- [ ] C) Exact versus approximate retrieval
- [ ] D) One-hot versus dense retrieval

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that the book opted for term-based versus embedding-based categorization rather than the sparse versus dense division found in the literature.

### Question 26: With the dictionary {"food": 0, "banana": 1, "slug": 2}, what is th...

With the dictionary {"food": 0, "banana": 1, "slug": 2}, what is the one-hot vector for “banana”?

- [ ] A) [1, 0, 0]
- [ ] B) [0, 0, 1]
- [ ] C) [0, 1, 0]
- [ ] D) [1, 1, 0]

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text gives the one-hot vectors as “food” = [1, 0, 0], “banana” = [0, 1, 0], and “slug” = [0, 0, 1].

### Question 27: What does the text say about SPLADE?

What does the text say about SPLADE?

- [ ] A) It is a term-based retrieval algorithm that uses one-hot vectors.
- [ ] B) It is a retrieval algorithm that works using sparse embeddings generated by BERT with regularization pushing most embedding values to 0.
- [ ] C) It is a dense retriever that cannot produce sparse vectors.
- [ ] D) It is a retrieval algorithm that avoids embeddings entirely.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text describes SPLADE as working with sparse embeddings, leveraging BERT-generated embeddings and regularization to push most values to 0.

### Question 28: Why does the text say the sparse versus dense division miscategoriz...

Why does the text say the sparse versus dense division miscategorizes SPLADE?

- [ ] A) SPLADE is grouped with term-based algorithms even though its operations, strengths, and weaknesses are much more similar to dense embedding retrieval.
- [ ] B) SPLADE is grouped with dense retrieval even though it uses only one-hot vectors.
- [ ] C) SPLADE cannot be represented with any vector.
- [ ] D) SPLADE is not a retrieval algorithm at all.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that sparse versus dense division groups SPLADE with term-based algorithms, although SPLADE is more similar to dense embedding retrieval.

### Question 29: In the source text, what two metrics does TF-IDF combine?

In the source text, what two metrics does TF-IDF combine?

- [ ] A) Term frequency (TF) and inverse document frequency (IDF)
- [ ] B) Term frequency (TF) and document length
- [ ] C) Inverse document frequency (IDF) and n-gram overlap
- [ ] D) Tokenization and stop word removal

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that TF-IDF combines term frequency and inverse document frequency.

### Question 30: According to the text, what does BM25 normalize term frequency scor...

According to the text, what does BM25 normalize term frequency scores by, compared with naive TF-IDF?

- [ ] A) Document length
- [ ] B) Query length
- [ ] C) Number of stop words
- [ ] D) N-gram overlap

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says BM25 normalizes term frequency scores by document length, since longer documents are more likely to contain a term and have higher term frequency values.

### Question 31: What is an inverted index as described in the text?

What is an inverted index as described in the text?

- [ ] A) A dictionary that maps from terms to documents that contain them
- [ ] B) A list of documents sorted by length
- [ ] C) A table of embedding vectors for documents
- [ ] D) A set of stop words removed from queries

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text describes an inverted index as a dictionary mapping terms to the documents containing them, allowing fast retrieval of documents given a term.

### Question 32: In embedding-based retrieval, what is the first step when querying?

In embedding-based retrieval, what is the first step when querying?

- [ ] A) Fetch k data chunks whose embeddings are closest to the query embedding
- [ ] B) Convert the query into an embedding using the same embedding model used during indexing
- [ ] C) Rerank all retrieved candidates
- [ ] D) Compute similarity scores between the query embedding and all vectors in the database

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that querying consists of two steps, the first being to convert the query into an embedding using the same embedding model used during indexing.

### Question 33: What is a limitation of using k-nearest neighbors (k-NN) for vector...

What is a limitation of using k-nearest neighbors (k-NN) for vector search?

- [ ] A) It only works with cosine similarity
- [ ] B) It is computationally heavy and slow, so it should be used only for small datasets
- [ ] C) It requires product quantization to function
- [ ] D) It cannot guarantee precise results

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says the naive k-NN solution ensures precise results but is computationally heavy and slow, and should be used only for small datasets.

### Question 34: Which vector search algorithm constructs a multi-layer graph where...

Which vector search algorithm constructs a multi-layer graph where nodes represent vectors and edges connect similar vectors?

- [ ] A) LSH (locality-sensitive hashing)
- [ ] B) HNSW (Hierarchical Navigable Small World)
- [ ] C) Product Quantization
- [ ] D) IVF (inverted file index)

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text describes HNSW as constructing a multi-layer graph where nodes represent vectors and edges connect similar vectors, allowing nearest-neighbor searches by traversing graph edges.

### Question 35: According to the source, which statement best describes term-based...

According to the source, which statement best describes term-based retrieval compared with embedding-based retrieval?

- [ ] A) It is generally much faster during both indexing and query.
- [ ] B) It can be significantly improved over time by finetuning the embedding model.
- [ ] C) It often obscures keywords such as specific error codes or product names.
- [ ] D) It requires vector storage and vector search, which can be expensive.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states term-based retrieval is generally much faster than embedding-based retrieval during both indexing and query. It also says term extraction is faster than embedding generation.

### Question 36: In RAG evaluation, what does context precision measure?

In RAG evaluation, what does context precision measure?

- [ ] A) Out of all documents retrieved, what percentage is relevant to the query?
- [ ] B) Out of all documents relevant to the query, what percentage is retrieved?
- [ ] C) The fraction of nearest neighbors found by an ANN algorithm.
- [ ] D) The number of queries an algorithm can handle per second.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source defines context precision as the percentage of retrieved documents that are relevant to the query. Context recall instead measures the percentage of relevant documents that are retrieved.

### Question 37: If you care about the ranking of retrieved documents, which metrics...

If you care about the ranking of retrieved documents, which metrics does the source mention?

- [ ] A) Context precision and context recall
- [ ] B) NDCG, MAP, and MRR
- [ ] C) QPS and build time
- [ ] D) MTEB and BEIR

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says that if ranking matters, you can use metrics such as NDCG, MAP, and MRR. Context precision and recall are used to evaluate retrieval quality more generally.

### Question 38: According to the source, which index is described as providing high...

According to the source, which index is described as providing high accuracy and fast query times but requiring significant time and memory to build?

- [ ] A) LSH
- [ ] B) HNSW
- [ ] C) BM25
- [ ] D) Elasticsearch

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that a detailed index like HNSW provides high accuracy and fast query times but requires significant time and memory to build. In contrast, LSH is quicker and less memory-intensive to create but leads to slower and less accurate queries.

### Question 39: Combining term-based retrieval and embedding-based retrieval is cal...

Combining term-based retrieval and embedding-based retrieval is called what?

- [ ] A) Ensemble search
- [ ] B) Hybrid search
- [ ] C) Reranking
- [ ] D) Reciprocal rank fusion

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that combining term-based retrieval and embedding-based retrieval is called hybrid search.

### Question 40: In a sequential retrieval setup, what is the second step called whe...

In a sequential retrieval setup, what is the second step called when a more precise but more expensive mechanism finds the best candidates?

- [ ] A) Hybrid search
- [ ] B) Candidate fetching
- [ ] C) Reranking
- [ ] D) Reciprocal rank fusion

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says the second step, where a more precise but more expensive mechanism such as k-nearest neighbors finds the best candidates, is also called reranking.

### Question 41: Under reciprocal rank fusion, what score does a document receive if...

Under reciprocal rank fusion, what score does a document receive if it ranks second by a retriever?

- [ ] A) 1
- [ ] B) 0.5
- [ ] C) 0.25
- [ ] D) 2

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that if a document ranks second, its score is ½ = 0.5.

### Question 42: What is the primary purpose of using overlapping chunks in a chunki...

What is the primary purpose of using overlapping chunks in a chunking strategy?

- [ ] A) To reduce computational overhead by decreasing the number of chunks
- [ ] B) To ensure important boundary information is included in at least one chunk
- [ ] C) To increase the number of chunks for more diverse information
- [ ] D) To allow the model to process documents faster

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that overlapping ensures important boundary information is included in at least one chunk, preventing loss of critical context when a document is split.

### Question 43: How does context reranking differ from traditional search reranking?

How does context reranking differ from traditional search reranking?

- [ ] A) Context reranking prioritizes the exact position of items, while search reranking does not.
- [ ] B) Context reranking gives higher weight to more recent data, while search reranking does not.
- [ ] C) Context reranking considers the exact position of items less critical as long as the document is included, while search ranking treats rank as crucial.
- [ ] D) Context reranking uses a cheaper retriever first, while search reranking uses a more expensive mechanism.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source explains that in context reranking, the exact position of items is less critical than in search, where rank (e.g., first or fifth) is crucial; as long as a document is included, its order has less impact.

### Question 44: Why is query rewriting necessary for a query like “How about Emily...

Why is query rewriting necessary for a query like “How about Emily Doe?” in a conversation?

- [ ] A) Because the query is too short to be processed by the retriever.
- [ ] B) Because the query lacks context and would likely retrieve irrelevant results if used verbatim.
- [ ] C) Because the query contains a name that requires identity resolution before retrieval.
- [ ] D) Because the query is not in English and needs translation.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that “How about Emily Doe?” is ambiguous without context, and using it verbatim would likely yield irrelevant results, so it must be rewritten to reflect what the user is actually asking.

### Question 45: In multimodal RAG, how can images be retrieved if they have metadat...

In multimodal RAG, how can images be retrieved if they have metadata such as titles, tags, and captions?

- [ ] A) By retrieving an image if its caption is considered relevant to the query
- [ ] B) By executing a SQL query against the image table
- [ ] C) By summing image units across all orders
- [ ] D) By using only a text-only embedding model on the query

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that if images have metadata, they can be retrieved using that metadata, for example if an image’s caption is relevant to the query.

### Question 46: When using CLIP as a multimodal embedding model for multimodal RAG,...

When using CLIP as a multimodal embedding model for multimodal RAG, what is the first step in the retriever workflow?

- [ ] A) Execute a text-to-SQL query
- [ ] B) Generate CLIP embeddings for all data, both texts and images, and store them in a vector database
- [ ] C) Generate only the final response from the original user query
- [ ] D) Predict which tables to use for each query

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source lists generating CLIP embeddings for all text and image data and storing them in a vector database as the first retrieval step.

### Question 47: For RAG with tabular data, what is the correct order of the workflo...

For RAG with tabular data, what is the correct order of the workflow described?

- [ ] A) Generation, SQL execution, text-to-SQL
- [ ] B) SQL execution, generation, text-to-SQL
- [ ] C) Text-to-SQL, SQL execution, generation
- [ ] D) Text-to-SQL, generation, SQL execution

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source describes the workflow as text-to-SQL based on the user query and table schemas, then SQL execution, then generation based on the SQL result and original query.

### Question 48: According to the source, what is a core characteristic of the agent...

According to the source, what is a core characteristic of the agentic pattern?

- [ ] A) Retrieval
- [ ] B) Tool use
- [ ] C) SQL execution
- [ ] D) Fine-tuning

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that tool use is a core characteristic of the agentic pattern.

### Question 49: How does the classic book by Stuart Russell and Peter Norvig define...

How does the classic book by Stuart Russell and Peter Norvig define the field of artificial intelligence research?

- [ ] A) The study and design of rational agents
- [ ] B) The study of foundation model capabilities
- [ ] C) The design of retrievers and SQL executors
- [ ] D) The automation of data entry

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source quotes Russell and Norvig defining AI research as “the study and design of rational agents.”

### Question 50: According to the source, what have the unprecedented capabilities o...

According to the source, what have the unprecedented capabilities of foundation models opened the door to?

- [ ] A) Only improved SQL execution
- [ ] B) Agentic applications that were previously unimaginable
- [ ] C) The elimination of autonomous agents
- [ ] D) A narrower definition of AI research

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says foundation model capabilities have opened the door to agentic applications that were previously unimaginable.

### Question 51: According to the source, what characterizes an agent?

According to the source, what characterizes an agent?

- [ ] A) The environment it operates in and the set of actions it can perform
- [ ] B) The size of its training dataset and number of parameters
- [ ] C) The user interface it presents and the API it exposes
- [ ] D) The prompt template it uses and its output schema

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that an agent is anything that can perceive its environment and act upon it, so it is characterized by its environment and its set of actions.

### Question 52: What does the source say about the relationship between an agent’s...

What does the source say about the relationship between an agent’s environment and its tools?

- [ ] A) The environment has no effect on which tools an agent can use.
- [ ] B) Tools determine the environment, but the environment does not affect tools.
- [ ] C) There is a strong dependency: the environment determines possible tools, and the tool inventory restricts the environment.
- [ ] D) Tools and environment are unrelated because agents do not use tools.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says there is a strong dependency between environment and tools: the environment determines what tools an agent can potentially use, while the agent’s tool inventory restricts the environment it can operate in.

### Question 53: Why do agents typically require more powerful models than non-agent...

Why do agents typically require more powerful models than non-agent use cases?

- [ ] A) Because agents cannot receive feedback from the environment
- [ ] B) Because compound mistakes make overall accuracy decrease as the number of steps increases
- [ ] C) Because agents always perform exactly one step per task
- [ ] D) Because agents do not need to plan a sequence of actions

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source explains that agents often need multiple steps, and overall accuracy decreases as the number of steps increases, giving the example of 95% per-step accuracy dropping over many steps.

### Question 54: According to the source, what are actions that allow an agent to pe...

According to the source, what are actions that allow an agent to perceive the environment called, and what are actions that allow it to act upon the environment called?

- [ ] A) Read-only actions and write actions
- [ ] B) Knowledge augmentation and capability extension
- [ ] C) Retrieval actions and planning actions
- [ ] D) Perception actions and memory actions

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that actions allowing an agent to perceive the environment are read-only actions, while actions allowing it to act upon the environment are write actions.

### Question 55: What tradeoff does the source describe about an agent’s tool invent...

What tradeoff does the source describe about an agent’s tool inventory?

- [ ] A) More tools always make an agent easier to understand and utilize.
- [ ] B) More tools give an agent more capabilities, but the more tools there are, the more challenging it is to understand and utilize them well.
- [ ] C) Fewer tools give an agent more capabilities but reduce security risks.
- [ ] D) Tool inventory only affects an agent’s speed, not its capabilities.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says more tools give an agent more capabilities, but more tools make it more challenging to understand and utilize them well.

### Question 56: Which category of tools addresses inherent limitations of AI models...

Which category of tools addresses inherent limitations of AI models, such as giving a model access to a calculator because models are bad at math?

- [ ] A) Knowledge augmentation
- [ ] B) Capability extension
- [ ] C) Write actions
- [ ] D) Web browsing

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source describes capability extension as tools that address inherent limitations of AI models and gives access to a calculator as an example.

### Question 57: According to the source, why can an AI system cause harm even witho...

According to the source, why can an AI system cause harm even without a presence in the physical world?

- [ ] A) Because it can manipulate the stock market, steal copyrights, violate privacy, reinforce biases, and spread misinformation
- [ ] B) Because it must always be embodied in a robot to affect people
- [ ] C) Because it can only cause harm through direct physical contact
- [ ] D) Because it cannot influence human behavior without physical form

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists stock market manipulation, copyright theft, privacy violations, bias reinforcement, and misinformation as harms AI can cause without physical presence.

### Question 58: What does the author conclude about giving AI systems the ability t...

What does the author conclude about giving AI systems the ability to act in the real world?

- [ ] A) AI systems should never be allowed to act in the real world because harm is possible
- [ ] B) Safety and security concerns are valid, but they do not mean AI should never be given real-world acting ability
- [ ] C) Only humans should use tools, because models cannot benefit from them
- [ ] D) Autonomous AI systems are already trusted more than humans in all situations

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says safety and security must be taken seriously, but this doesn’t mean AI systems should never be given the ability to act in the real world.

### Question 59: What does the source say about function calling?

What does the source say about function calling?

- [ ] A) It is a feature many model providers already support for tool use and is expected to become common with most models
- [ ] B) It is a security measure that prevents AI systems from causing harm
- [ ] C) It is a method for giving AI systems physical bodies
- [ ] D) It is a replacement for human productivity tools such as Excel and cranes

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that many model providers already support tool use, often called function calling, and expects function calling with a wide set of tools to be common with most models.

### Question 60: According to the text, what two elements define a task?

According to the text, what two elements define a task?

- [ ] A) A goal and a budget
- [ ] B) A goal and constraints
- [ ] C) A plan and a roadmap
- [ ] D) A model and a foundation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states: "A task is defined by its goal and constraints."

### Question 61: What is the output of the planning process?

What is the output of the planning process?

- [ ] A) A goal
- [ ] B) A constraint
- [ ] C) A plan
- [ ] D) A model

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says: "The output of the planning process is a plan, which is a roadmap outlining the steps needed to accomplish a task."

### Question 62: Effective planning typically requires the model to do which of the...

Effective planning typically requires the model to do which of the following?

- [ ] A) Understand the task, consider different options, and choose the most promising one
- [ ] B) Ignore constraints and focus only on the goal
- [ ] C) Avoid planning meetings and rely on intuition
- [ ] D) Generate multiple plans without evaluating them

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states: "Effective planning typically requires the model to understand the task, consider different options to achieve this task, and choose the most promising one."

### Question 63: In the example query “How many companies without revenue have raise...

In the example query “How many companies without revenue have raised at least $1 billion?”, which planning approach is described as more efficient?

- [ ] A) Find all companies without revenue, then filter them by the amount raised.
- [ ] B) Find all companies that have raised at least $1 billion, then filter them by revenue.
- [ ] C) Find all companies with revenue, then filter them by the amount raised.
- [ ] D) Find all companies that have raised less than $1 billion, then filter them by revenue.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says option 2 is more efficient because there are vastly more companies without revenue than companies that have raised at least $1 billion.

### Question 64: Why does the source recommend decoupling planning from execution?

Why does the source recommend decoupling planning from execution?

- [ ] A) To allow the model to generate 1,000-step plans without validation.
- [ ] B) To avoid fruitless execution of an unvalidated plan that may waste time and money.
- [ ] C) To ensure every plan is executed sequentially rather than in parallel.
- [ ] D) To eliminate the need for an intent classifier.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** Decoupling lets a plan be validated before execution, avoiding hours of wasted time and API calls on a plan that does not accomplish the goal.

### Question 65: Which of the following is given as a heuristic for validating a gen...

Which of the following is given as a heuristic for validating a generated plan?

- [ ] A) Eliminating plans that contain any external tools.
- [ ] B) Eliminating plans with invalid actions, such as requiring a tool the agent cannot access.
- [ ] C) Requiring every plan to be an end-to-end plan for the whole task.
- [ ] D) Requiring the planner to generate plans only sequentially.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source mentions eliminating plans with invalid actions, such as requiring Google Search when the agent lacks access, and eliminating plans with more than X steps.

### Question 66: What is described as the latency/cost trade-off when generating sev...

What is described as the latency/cost trade-off when generating several plans in parallel?

- [ ] A) It removes the need for plan validation.
- [ ] B) It incurs extra costs while potentially speeding up the process by letting an evaluator pick the most promising plan.
- [ ] C) It guarantees the most efficient plan will always be chosen.
- [ ] D) It prevents the use of AI judges for evaluation.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says generating multiple plans simultaneously incurs extra costs but can speed up the process by having an evaluator choose the most promising plan.

### Question 67: According to the text, what should an intent classifier do when a q...

According to the text, what should an intent classifier do when a query is out of the scope of the agent?

- [ ] A) Classify it as IRRELEVANT so the agent can politely reject it instead of wasting FLOPs
- [ ] B) Automatically expand the query into a high-level plan
- [ ] C) Ask the human to execute all parts of the plan
- [ ] D) Merge a code change without approval

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The tip says the intent classifier should classify out-of-scope requests as IRRELEVANT so the agent can politely reject them rather than wasting FLOPs on impossible solutions.

### Question 68: For risky operations such as updating a database or merging a code...

For risky operations such as updating a database or merging a code change, what does the text say the system can do?

- [ ] A) Skip reflection because the operation is risky
- [ ] B) Ask for explicit human approval before executing or let humans execute these operations
- [ ] C) Classify the operation as IRRELEVANT and reject it
- [ ] D) Require the agent to generate the whole plan without human input

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that if a plan involves risky operations, the system can ask for explicit human approval before executing or let humans execute these operations.

### Question 69: In the summary of processes for solving a task, which process is de...

In the summary of processes for solving a task, which process is described as not mandatory but able to significantly boost the agent’s performance?

- [ ] A) Plan generation
- [ ] B) Execution
- [ ] C) Reflection and error correction
- [ ] D) Intent classification

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The summary notes that reflection isn’t mandatory for an agent, but it will significantly boost the agent’s performance.

### Question 70: According to the source, what does Yann LeCun state about autoregre...

According to the source, what does Yann LeCun state about autoregressive LLMs?

- [ ] A) They are excellent planners when given enough tooling.
- [ ] B) They can plan only if they use backtracking.
- [ ] C) They can’t plan.
- [ ] D) They can plan better than RL agents.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says Meta’s Chief AI Scientist Yann LeCun states unequivocally that autoregressive LLMs can’t plan.

### Question 71: How does the source describe planning at its core?

How does the source describe planning at its core?

- [ ] A) A search problem among different paths to the goal.
- [ ] B) A process that requires only chain-of-thought prompting.
- [ ] C) A method that avoids predicting outcomes.
- [ ] D) A technique that only reinforcement learning can perform.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that planning, at its core, is a search problem: you search among different paths to the goal, predict the outcome of each path, and pick the most promising one.

### Question 72: According to the source, what is the main difference between how pl...

According to the source, what is the main difference between how planners work in RL agents and FM agents?

- [ ] A) RL agents do not use environments, while FM agents do.
- [ ] B) In an RL agent, the planner is trained by an RL algorithm; in an FM agent, the model is the planner.
- [ ] C) FM agents cannot be prompted or finetuned to improve planning.
- [ ] D) RL planners require fewer resources than FM planners.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says the main difference is in how their planners work: an RL agent’s planner is trained by an RL algorithm, while in an FM agent the model is the planner.

### Question 73: According to the text, what is the simplest way to turn a model int...

According to the text, what is the simplest way to turn a model into a plan generator?

- [ ] A) Fine-tuning the model on planning datasets
- [ ] B) Prompt engineering
- [ ] C) Training a separate planning model from scratch
- [ ] D) Using reinforcement learning with human feedback

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that the simplest way to turn a model into a plan generator is with prompt engineering.

### Question 74: In the Kitty Vogue example, how many external tools is the agent gi...

In the Kitty Vogue example, how many external tools is the agent given access to?

- [ ] A) Two
- [ ] B) Three
- [ ] C) Four
- [ ] D) Five

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says the agent is given access to three external tools.

### Question 75: Which of the following is one of the external tools given to the Ki...

Which of the following is one of the external tools given to the Kitty Vogue agent in the example?

- [ ] A) Retrieve products by price
- [ ] B) Process customer payments
- [ ] C) Send promotional emails
- [ ] D) Generate product images

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text lists retrieve products by price, retrieve top products, and retrieve product information as the three tools.

### Question 76: What does the text say about the example plan generation prompt?

What does the text say about the example plan generation prompt?

- [ ] A) It is the exact prompt used in production
- [ ] B) It is for illustration purposes only, and production prompts are likely more complex
- [ ] C) It should never be modified
- [ ] D) It requires no external tools

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text notes the prompt is for illustration purposes only and that production prompts are likely more complex.

### Question 77: In the system prompt, what is the model asked to propose?

In the system prompt, what is the model asked to propose?

- [ ] A) A plan to solve the task
- [ ] B) A final answer without tools
- [ ] C) A new set of actions
- [ ] D) A database schema

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The prompt begins “Propose a plan to solve the task.” It is focused on planning, not directly answering.

### Question 78: Which plan matches the example task “Tell me about Fruity Fedora”?

Which plan matches the example task “Tell me about Fruity Fedora”?

- [ ] A) [get_today_date, generate_query, generate_response]
- [ ] B) [fetch_top_products, generate_query, generate_response]
- [ ] C) [fetch_product_info, generate_query, generate_response]
- [ ] D) [generate_query, generate_response]

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source gives this exact example plan for “Tell me about Fruity Fedora.” It starts with fetch_product_info.

### Question 79: Which plan matches the example task “What was the best selling prod...

Which plan matches the example task “What was the best selling product last week?”

- [ ] A) [fetch_product_info, generate_query, generate_response]
- [ ] B) [fetch_top_products, generate_query, generate_response]
- [ ] C) [get_today_date, fetch_product_info, generate_response]
- [ ] D) [generate_query, generate_response]

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source gives this exact example plan for finding the best selling product last week. It starts with fetch_top_products.

### Question 80: What constraint does the system prompt place on the plan?

What constraint does the system prompt place on the plan?

- [ ] A) It must contain exactly two actions
- [ ] B) It must be a sequence of valid actions
- [ ] C) It must avoid generate_response
- [ ] D) It must start with get_today_date

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The prompt states “The plan must be a sequence of valid actions.” It does not require a fixed number or a specific starting action.

### Question 81: According to the text, what is true about the plan format that uses...

According to the text, what is true about the plan format that uses a list of functions whose parameters are inferred by the agent?

- [ ] A) It is the only valid way to structure agent control flow.
- [ ] B) It is one of many ways to structure the agent control flow.
- [ ] C) It requires all function parameters to be known before planning begins.
- [ ] D) It eliminates the need for a response generator.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that this plan format is “just one of many ways to structure the agent control flow.”

### Question 82: Why can the exact parameters for functions in an agent plan be hard...

Why can the exact parameters for functions in an agent plan be hard to predict in advance?

- [ ] A) Because function parameters are always fixed by the user input.
- [ ] B) Because parameters are often extracted from previous tool outputs.
- [ ] C) Because the agent cannot call more than one function.
- [ ] D) Because tool outputs are never added to the task’s history.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says exact parameters are hard to predict because they are often extracted from previous tool outputs.

### Question 83: What does the text say can happen because both the action sequence...

What does the text say can happen because both the action sequence and associated parameters are generated by AI models?

- [ ] A) They can be hallucinated, causing invalid function calls or valid calls with wrong parameters.
- [ ] B) They are guaranteed to be correct if the system prompt is short.
- [ ] C) They cannot be improved by using a stronger model.
- [ ] D) They remove the need to describe tools and parameters.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that generated action sequences and parameters can be hallucinated, leading to invalid functions or wrong parameters.

### Question 84: Which of the following is listed as an approach to make an agent be...

Which of the following is listed as an approach to make an agent better at planning?

- [ ] A) Avoiding examples in the system prompt.
- [ ] B) Making tool descriptions vaguer so the model must guess.
- [ ] C) Refactoring a complex function into two simpler functions.
- [ ] D) Using a weaker model for plan generation.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text lists rewriting functions to make them simpler, such as refactoring a complex function into two simpler functions, as a planning improvement.

### Question 85: According to the text, what is invoking a tool often called?

According to the text, what is invoking a tool often called?

- [ ] A) Tool inventory creation
- [ ] B) Function calling
- [ ] C) Parameter specification
- [ ] D) Documentation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that a tool is a function, so invoking a tool is often called function calling.

### Question 86: In the first step of function calling, what must each tool in the t...

In the first step of function calling, what must each tool in the tool inventory be described by?

- [ ] A) Only its function name
- [ ] B) Only its parameters
- [ ] C) Its execution entry point, parameters, and documentation
- [ ] D) Only its documentation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says each tool is described by its execution entry point, its parameters, and its documentation.

### Question 87: What does the text say about specifying which tools an agent can us...

What does the text say about specifying which tools an agent can use per query?

- [ ] A) All declared tools must be used for every query
- [ ] B) Many APIs let you specify a list of declared tools to be used per query
- [ ] C) Tools cannot be specified per query
- [ ] D) Only one tool can be used per query

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that many APIs let you specify a list of declared tools to be used per query, and some allow further control.

### Question 88: In the tool-use configuration described, what does the `required` s...

In the tool-use configuration described, what does the `required` setting specify?

- [ ] A) The model must use at least one tool.
- [ ] B) The model is forbidden from using any tool.
- [ ] C) The model must use every available tool.
- [ ] D) The model decides freely whether to use a tool.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that under `required`, the model must use at least one tool.

### Question 89: Under the `required` setting, what is the minimum number of tools t...

Under the `required` setting, what is the minimum number of tools the model must use?

- [ ] A) Exactly one, with no possibility of using more
- [ ] B) Zero
- [ ] C) At least one
- [ ] D) All available tools

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** `required` sets a floor of at least one tool, not an exact count of one or a requirement to use all tools.

### Question 90: Which statement accurately reflects the `required` tool-use setting?

Which statement accurately reflects the `required` tool-use setting?

- [ ] A) Tool use is optional for the model.
- [ ] B) The model cannot respond without using at least one tool.
- [ ] C) The model may use tools only after answering.
- [ ] D) The model must avoid tools unless explicitly asked.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** Because the model must use at least one tool, a response with no tool use does not satisfy the `required` setting.

### Question 91: In the context of tool use, what does the setting `none` indicate?

In the context of tool use, what does the setting `none` indicate?

- [ ] A) The model decides which tools to use.
- [ ] B) The model should not use any tool.
- [ ] C) The model must use all available tools.
- [ ] D) The model uses tools only if explicitly asked.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that `none` means “The model shouldn’t use any tool.”

### Question 92: What does the setting `auto` mean for tool use?

What does the setting `auto` mean for tool use?

- [ ] A) The model should not use any tool.
- [ ] B) The model must use a specific tool.
- [ ] C) The model decides which tools to use.
- [ ] D) The model uses tools only after user confirmation.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states that `auto` means “The model decides which tools to use.”

### Question 93: For the query “How many kilograms are 40 pounds?”, what tool and pa...

For the query “How many kilograms are 40 pounds?”, what tool and parameter might the agent decide to use?

- [ ] A) `kg_to_lbs_tool` with parameter 40
- [ ] B) `lbs_to_kg_tool` with parameter 40
- [ ] C) `lbs_to_kg_tool` with parameter 100
- [ ] D) No tool, because the model can convert directly

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source gives this example: the agent might decide it needs `lbs_to_kg_tool` with one parameter value of 40.

### Question 94: According to the source, what can some function calling APIs guaran...

According to the source, what can some function calling APIs guarantee about generated functions?

- [ ] A) They guarantee correct parameter values but not valid function names.
- [ ] B) They guarantee only valid functions are generated, but not correct parameter values.
- [ ] C) They guarantee both valid functions and correct parameter values.
- [ ] D) They guarantee neither valid functions nor correct parameter values.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says some APIs “will make sure that only valid functions are generated, though they won’t be able to guarantee the correct parameter values.”

### Question 95: When working with agents, what should you always ask the system to...

When working with agents, what should you always ask the system to report?

- [ ] A) The parameter values it uses for each function call
- [ ] B) The total number of agents available
- [ ] C) The list of all possible user questions
- [ ] D) The final answer only, without intermediate details

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The tip says to always ask the system to report what parameter values it uses for each function call.

### Question 96: After an agent system reports the parameter values for each functio...

After an agent system reports the parameter values for each function call, what should you do?

- [ ] A) Ignore them unless the final answer is wrong
- [ ] B) Inspect them to make sure they are correct
- [ ] C) Replace them with default values
- [ ] D) Share them without reviewing them

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says to inspect these values to make sure they are correct.

### Question 97: What is the purpose of having an agent system report the parameter...

What is the purpose of having an agent system report the parameter values used for each function call?

- [ ] A) To reduce the number of function calls
- [ ] B) To verify that the parameter values are correct
- [ ] C) To avoid inspecting the agent’s behavior
- [ ] D) To hide how the function call was made

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The reported values are meant to be inspected so you can make sure they are correct.

### Question 98: According to the text, what is the planning/execution trade-off?

According to the text, what is the planning/execution trade-off?

- [ ] A) A detailed plan is harder to generate but easier to execute, while a higher-level plan is easier to generate but harder to execute.
- [ ] B) A detailed plan is easier to generate and easier to execute, while a higher-level plan is harder to generate and harder to execute.
- [ ] C) A detailed plan is easier to generate but harder to execute, while a higher-level plan is harder to generate but easier to execute.
- [ ] D) Planning granularity has no effect on either generation or execution difficulty.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that detailed plans are harder to generate but easier to execute, whereas higher-level plans are easier to generate but harder to execute.

### Question 99: What approach does the text suggest to circumvent the planning/exec...

What approach does the text suggest to circumvent the planning/execution trade-off?

- [ ] A) Always generate the most detailed plan possible in one step.
- [ ] B) Avoid planning entirely and execute actions directly.
- [ ] C) Plan hierarchically by first generating a high-level plan and then generating more detailed plans for each part.
- [ ] D) Use only exact function names in every plan.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says an approach is to plan hierarchically: first generate a high-level plan, then use the same or a different planner to generate more detailed plans for each part.

### Question 100: Why can generating plans in natural language instead of exact funct...

Why can generating plans in natural language instead of exact function names be beneficial?

- [ ] A) It makes plans more granular and always easier to execute directly.
- [ ] B) It helps the plan generator be robust to changes in tool APIs and reduces the need to update prompts, examples, or finetuning when tools change.
- [ ] C) It eliminates the need for any translator or executable commands.
- [ ] D) It guarantees the agent will never hallucinate.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says natural language plans help the plan generator become robust to changes in tool APIs and avoid updating prompts, examples, and finetuning when tool names change.

### Question 101: What does the text call the order in which actions can be executed?

What does the text call the order in which actions can be executed?

- [ ] A) The control flow
- [ ] B) The SQL translation
- [ ] C) The natural language input
- [ ] D) The product price

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that the order in which actions can be executed is called a control flow.

### Question 102: In the sequential control flow example, when can the SQL query be e...

In the sequential control flow example, when can the SQL query be executed?

- [ ] A) At the same time as retrieving product prices
- [ ] B) Only after it’s been translated from the natural language input
- [ ] C) Before the natural language input is received
- [ ] D) Only after top 100 best-selling products are retrieved

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says sequential means task B after task A, and gives the example that the SQL query can be executed only after it’s been translated from the natural language input.

### Question 103: Which example does the text give for the parallel control flow?

Which example does the text give for the parallel control flow?

- [ ] A) Translating a natural language input into SQL before executing the SQL query
- [ ] B) Executing task B only after task A is complete
- [ ] C) Retrieving the top 100 best-selling products and, for each, retrieving its price
- [ ] D) Repeating a task with a for loop

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text describes parallel as executing tasks A and B at the same time and gives the example of retrieving top 100 best-selling products and retrieving each product’s price.

### Question 104: In the source text, what does the “if statement” control flow allow...

In the source text, what does the “if statement” control flow allow an agent to do?

- [ ] A) Execute task B or task C depending on the output from the previous step
- [ ] B) Repeat task A until a specific condition is met
- [ ] C) Execute all tasks simultaneously without conditions
- [ ] D) Translate a plan into exact traditional software commands

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text defines the if statement as executing task B or task C depending on the previous step’s output.

### Question 105: What example is given for a “for loop” control flow?

What example is given for a “for loop” control flow?

- [ ] A) Checking NVIDIA’s earnings report and then buying or selling stocks
- [ ] B) Browsing ten websites simultaneously
- [ ] C) Keeping on generating random numbers until a prime number
- [ ] D) Evaluating what control flows an agent framework supports

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says a for loop repeats task A until a condition is met, such as generating random numbers until a prime number.

### Question 106: According to the source text, what should you check when evaluating...

According to the source text, what should you check when evaluating an agent framework?

- [ ] A) Whether it uses only exact conditions from traditional software engineering
- [ ] B) What control flows it supports
- [ ] C) Whether it avoids parallel execution
- [ ] D) Whether it can generate earnings reports

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text advises checking what control flows an agent framework supports when evaluating it.

### Question 107: According to the text, which of the following is NOT listed as a po...

According to the text, which of the following is NOT listed as a point during a task process where reflection can be useful?

- [ ] A) After receiving a user query, to evaluate if the request is feasible
- [ ] B) After the initial plan generation, to evaluate whether the plan makes sense
- [ ] C) Before the agent is deployed, to evaluate whether its underlying model should be retrained
- [ ] D) After the whole plan has been executed, to determine if the task has been accomplished

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text lists reflection after the user query, after plan generation, after each execution step, and after the whole plan is executed—not before deployment or model retraining.

### Question 108: In the ReAct framework first proposed by Yao et al., what does the...

In the ReAct framework first proposed by Yao et al., what does the agent do at each step?

- [ ] A) It generates a score for each outcome using a specialized scorer before acting
- [ ] B) It explains its thinking (planning), takes actions, then analyzes observations (reflection)
- [ ] C) It skips reflection entirely and executes the full plan without intermediate checks
- [ ] D) It hands off all planning to a separate evaluator agent and only executes actions

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states the agent is asked to explain its thinking (planning), take actions, then analyze observations (reflection) until the task is considered finished.

### Question 109: In the Reflexion framework (Shinn et al., 2023), how is reflection...

In the Reflexion framework (Shinn et al., 2023), how is reflection structured?

- [ ] A) As a single self-critique prompt applied only after the entire task is complete
- [ ] B) As two modules: an evaluator that evaluates the outcome and a self-reflection module that analyzes what went wrong
- [ ] C) As a specialized scorer that outputs a numeric score with no analysis of failures
- [ ] D) As a fine-tuning step in which the agent's weights are updated after each failure

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says Reflexion separates reflection into an evaluator module and a self-reflection module, with the agent proposing a new trajectory after each step.

### Question 110: What does the text identify as the downside of reflection?

What does the text identify as the downside of reflection?

- [ ] A) It is difficult to implement and rarely improves performance
- [ ] B) It cannot be combined with error correction
- [ ] C) Latency and cost, since thoughts, observations, and sometimes actions consume many tokens, and example-heavy prompts increase input token cost and reduce available context space
- [ ] D) It requires retraining the model, which is prohibitively expensive

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states reflection is relatively easy to implement with good performance gains, but its downside is latency and cost from token-heavy outputs and example-heavy prompts.

### Question 111: According to the passage, what is a key trade-off when giving an ag...

According to the passage, what is a key trade-off when giving an agent more tools?

- [ ] A) More tools always improve performance without increasing context needs.
- [ ] B) More tools reduce the agent’s capabilities but make selection easier.
- [ ] C) More tools add capabilities but make efficient use harder and can increase tool descriptions beyond context limits.
- [ ] D) More tools eliminate the need for experimentation and analysis.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The passage states that more tools give more capabilities, but they are harder to use efficiently and increase tool descriptions that may not fit into a model’s context.

### Question 112: What does the passage recommend doing if removing a tool from an ag...

What does the passage recommend doing if removing a tool from an agent’s inventory causes no performance drop?

- [ ] A) Add more tools to compensate.
- [ ] B) Remove that tool.
- [ ] C) Finetune the model on that tool.
- [ ] D) Keep it because all tools are valuable.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The passage recommends an ablation study and says that if a tool can be removed without a performance drop, it should be removed.

### Question 113: What did experiments by Lu et al. (2023) demonstrate about tool use?

What did experiments by Lu et al. (2023) demonstrate about tool use?

- [ ] A) All tasks rely equally on knowledge retrieval tools.
- [ ] B) Different models have identical tool preferences.
- [ ] C) ScienceQA relies more on knowledge retrieval than TabMWP, and different models can prefer different tools.
- [ ] D) ChatGPT selects a wider set of tools than GPT-4.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The passage says different tasks require different tools, and different models have different tool preferences, with ScienceQA relying more on knowledge retrieval than TabMWP.

### Question 114: According to the TIP, what should you evaluate an agent framework for?

According to the TIP, what should you evaluate an agent framework for?

- [ ] A) The planners and tools it supports
- [ ] B) The number of social media accounts it can create
- [ ] C) The size of its training dataset only
- [ ] D) The color scheme of its user interface

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The TIP says to evaluate what planners and tools an agent framework supports, and different frameworks may focus on different tool categories.

### Question 115: Which framework is described as focusing on enterprise APIs such as...

Which framework is described as focusing on enterprise APIs such as Google Apps, GitHub, and Slack?

- [ ] A) AutoGPT
- [ ] B) Composio
- [ ] C) Chameleon
- [ ] D) Reddit

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that Composio focuses on enterprise APIs, including Google Apps, GitHub, and Slack.

### Question 116: What does Chameleon propose studying?

What does Chameleon propose studying?

- [ ] A) Tool transition: after tool X, how likely is the agent to call tool Y?
- [ ] B) How to replace all tools with a single social media API
- [ ] C) How to train a planner without any tools
- [ ] D) How to evaluate only the cost of an agent framework

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** Chameleon proposes the study of tool transition, meaning the likelihood that an agent calls tool Y after using tool X.

### Question 117: According to the text, what is the core approach to evaluating an a...

According to the text, what is the core approach to evaluating an agent?

- [ ] A) Measure only final task success and ignore intermediate steps
- [ ] B) Identify its failure modes and measure how often each failure mode happens
- [ ] C) Compare its tool inventory with a human expert's tool inventory
- [ ] D) Count how many skills are added to the skill library

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that to evaluate an agent, identify its failure modes and measure how often each of these failure modes happens.

### Question 118: Which example illustrates the planning failure "valid tool, invalid...

Which example illustrates the planning failure "valid tool, invalid parameters"?

- [ ] A) The agent calls bing_search, which is not in its tool inventory
- [ ] B) The agent calls lbs_to_kg with two parameters even though it requires only one
- [ ] C) The agent calls lbs_to_kg with one parameter but uses 100 lbs instead of 120
- [ ] D) The agent plans a trip to Ho Chi Minh City instead of Hanoi

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text gives calling lbs_to_kg with two parameters as the example of a valid tool with invalid parameters; A is an invalid tool, C is an incorrect parameter value, and D is goal failure.

### Question 119: According to the text, which statement about tool failures is correct?

According to the text, which statement about tool failures is correct?

- [ ] A) Tool failures occur only when the agent chooses an invalid tool
- [ ] B) Tool failures are tool-dependent, so each tool needs to be tested independently
- [ ] C) Tool failures can be evaluated with a single benchmark for all tools
- [ ] D) Missing tool failures are easy to detect without knowing what tools should be used

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says tool failures are tool-dependent and each tool needs to be tested independently; detecting missing tool failures requires understanding what tools should be used.

### Question 120: What are the three main memory mechanisms of an AI model described...

What are the three main memory mechanisms of an AI model described in the source?

- [ ] A) Internal knowledge, short-term memory, and long-term memory
- [ ] B) Training data, finetuning data, and retrieval data
- [ ] C) Instructions, examples, and tool outputs
- [ ] D) Context, prompts, and reflections

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that an AI model typically has three main memory mechanisms: internal knowledge, short-term memory, and long-term memory.

### Question 121: Which statement best describes a model’s short-term memory accordin...

Which statement best describes a model’s short-term memory according to the source?

- [ ] A) It is external data that persists across tasks and can be deleted without updating the model.
- [ ] B) It is the knowledge retained from training data and changes only when the model is updated.
- [ ] C) It is the model’s context, which is fast to access but limited in capacity and does not persist across tasks.
- [ ] D) It is a structured storage system used mainly to maintain data structural integrity.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says a model’s context can be considered short-term memory because it does not persist across tasks, is fast to access, and has limited capacity.

### Question 122: What does the FIFO memory management strategy do?

What does the FIFO memory management strategy do?

- [ ] A) It removes redundancy by summarizing the conversation and tracking named entities.
- [ ] B) It moves the first information added to short-term memory to external storage first.
- [ ] C) It merges new information with existing memory or replaces other memory.
- [ ] D) It reserves 30% of context for long-term memory retrieval.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source describes FIFO as “first in, first out,” where the first item added to short-term memory is the first moved to external storage. It also notes that this can cause the model to lose track of important information.

### Question 123: Which benefit of memory systems is illustrated by an AI coach not r...

Which benefit of memory systems is illustrated by an AI coach not requiring the user to explain their whole life story every time?

- [ ] A) Managing information overflow within a session
- [ ] B) Boosting a model’s consistency
- [ ] C) Maintaining data structural integrity
- [ ] D) Persisting information between sessions

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** D

    **Explanation:** The source uses the AI coach example to show that memory can persist information between sessions, so users do not have to repeat everything each time.

### Question 124: According to the summary, what was RAG originally developed to over...

According to the summary, what was RAG originally developed to overcome?

- [ ] A) A model’s context limitations
- [ ] B) A model’s inability to use tools
- [ ] C) Security risks from tool use
- [ ] D) The need for a memory system

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says RAG was originally developed to overcome a model’s context limitations, and it also enables more efficient use of information.

### Question 125: What does the success of a RAG system depend on?

What does the success of a RAG system depend on?

- [ ] A) The quality of its retriever
- [ ] B) The number of agents in the workflow
- [ ] C) The size of the model’s memory system
- [ ] D) The model’s ability to reflect on its progress

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The summary states that the success of a RAG system depends on the quality of its retriever.

### Question 126: How does the text characterize the RAG pattern in relation to an ag...

How does the text characterize the RAG pattern in relation to an agent?

- [ ] A) As a special case of an agent where the retriever is a tool the model can use
- [ ] B) As a replacement for agents that avoids tool use
- [ ] C) As a method that modifies the underlying model
- [ ] D) As a type of memory system separate from agents

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says the RAG pattern can be seen as a special case of an agent where the retriever is a tool the model can use.

### Question 127: According to the summary, what is a risk of making an agent more au...

According to the summary, what is a risk of making an agent more automated?

- [ ] A) Its failures can become more catastrophic
- [ ] B) It can no longer use external memory
- [ ] C) It loses the ability to plan
- [ ] D) It becomes a prompt-based method

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says that the more automated the agent becomes, the more catastrophic its failures can be.
