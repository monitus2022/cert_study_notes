# 1. Introduction to Building AI Applications with Foundation Models

---

## Scale Defines Post-2020 AI
- One word describes AI post-2020: *scale*
- Models like ChatGPT, Gemini, and Midjourney operate at massive scale
- They consume a nontrivial portion of world electricity
- Public internet training data risks running out

---

## Two Consequences of Scaling
- Models grow more powerful, enabling more applications and productivity
- Training LLMs needs data, compute, and talent few organizations can afford
- This produced *model as a service*: models offered for others to use
- Builders avoid upfront investment in building their own model

---

## Rise of AI Engineering
- Demand for AI applications increased while barrier to entry decreased
- *AI engineering*: building applications on top of readily available models
- It is one of the fastest-growing engineering disciplines
- Building on ML models isn't new; new scale brings new possibilities and challenges

---

## From Language Models to AI Engineering
- Foundation models evolved from large language models, which originated as language models.
- ChatGPT and Copilot are culminations of decades of technology advancements, not sudden arrivals.
- The first language models emerged in the 1950s.
- This section traces breakthroughs from language models to AI engineering.

---

## Language Models and Self-Supervision
- Self-supervision enabled language models to grow to today’s scale.
- A language model encodes statistical information about one or more languages.
- It indicates how likely a word is to appear in a given context.
- Example: “My favorite color is __” should predict “blue” more often than “car”.

---

## Language Models and Tokens
- A language model encodes statistical information about languages and predicts likely words in context.
- A token is the basic unit: a character, word, or word part; tokenization splits text into tokens.
- Vocabulary is all tokens a model can work with; tokenization and vocabulary size are developer decisions.
- GPT-4 tokenizes a phrase into nine tokens; an average token is about ¾ of a word.

---

## Two Language Model Types
- Masked language models predict missing tokens anywhere, using context from both before and after.
- BERT is a well-known masked language model, commonly used for nongenerative tasks like classification.
- Autoregressive models predict the next token using only preceding tokens and can continually generate text.
- Autoregressive models are preferred for text generation; in this book, “language model” means autoregressive.

---

## Self-Supervision and Scale
- Self-supervision infers labels from input data, overcoming the expensive data-labeling bottleneck.
- Language modeling is self-supervised: each input sequence provides both labels and contexts for prediction.
- The sentence “I love street food.” gives six training samples, as shown in Table 1-1.
- Self-supervision enables massive text data, scaling models to LLMs; size is measured by parameters.

---

## From LLMs to Multimodal Models
- Language models are limited to text; extended to incorporate more data modalities
- GPT-4V and Claude 3 can understand images and texts
- A multimodal model works with more than one data modality
- Generative multimodal models are called large multimodal models (LMMs)

---

## Foundation Models
- "Foundation" signifies importance and that models can be built upon for different needs
- Book uses foundation models for both LLMs and large multimodal models
- CLIP used natural language supervision: 400 million (image, text) pairs
- CLIP is an embedding model, backbone of Flamingo, LLaVA, Gemini

---

## General-Purpose Models and Adaptation
- Foundation models mark transition from task-specific to general-purpose models
- Prompt engineering, RAG, and finetuning adapt models to specific needs
- Adapting existing models is easier than building from scratch
- Task-specific models can be smaller, faster, and cheaper

---

## From Foundation Models to AI Engineering
- AI engineering builds applications on top of foundation models; ML engineering develops models.
- AI engineering leverages existing foundation models rather than developing new ML models.
- Three factors create ideal conditions for AI engineering's rapid growth.
- Foundation models enable more tasks, not just better performance on existing ones.

---

## Capabilities, Investment, and Access
- General-purpose capabilities let AI automate any task requiring communication, expanding the user base.
- AI investment could approach $100 billion in the US and $200 billion globally by 2025.
- One in three S&P 500 companies mentioned AI in Q2 2023 earnings calls, triple the prior year.
- Model-as-a-service APIs give access to powerful models via single API calls, lowering barriers.

---

## Rapid Growth and Naming
- AI can write code and be used in plain English, letting anyone develop AI applications.
- Only big corporations, governments, and well-funded startups can develop foundation models.
- Four open source AI engineering tools gained more GitHub stars than Bitcoin within two years.
- "AI engineering" was chosen over ML engineering and "Ops" terms; most surveyed developers preferred it.

---

## Categorizing Foundation Model Use Cases
- AWS groups enterprise generative AI use cases into customer experience, employee productivity, and process optimization.
- A 2024 O’Reilly survey used eight categories, including programming, data analysis, customer support, and marketing copy.
- Deloitte categorizes use cases by value capture: cost reduction, process efficiency, growth, and accelerating innovation.
- Gartner found 7% of 2,500 executives cited business continuity as their motivation for adopting generative AI.

---

## Occupational Exposure to AI
- Eloundou et al. define a task as exposed if AI reduces completion time by at least 50%.
- An occupation’s exposure is the share of its tasks that are exposed to AI.
- High-exposure occupations include interpreters and translators, tax preparers, web designers, and writers.
- Cooks, stonemasons, and athletes are among occupations with no exposure.

---

## Common Use Cases and Distribution
- The author interviewed 50 companies and read over 100 case studies to understand enterprise use cases.
- Consumer analysis examined 205 open source AI applications with at least 500 GitHub stars.
- Eight categories include coding, image/video production, writing, education, chatbots, information aggregation, data organization, and workflow automation.
- Low open-source shares for education, data organization, and writing may reflect enterprise suitability.

---

## Coding: The Most Popular Use Case
- Coding is the most popular generative AI use case across multiple surveys.
- AI is genuinely good at coding; early AI engineers are coders themselves.
- GitHub Copilot reached $100 million annual recurring revenue two years after launch.
- AI coding startups raised heavily: Magic $320 million, Anysphere $60 million (August 2024).

---

## Specialized Coding Tasks
- Extracting structured data from web pages and PDFs (AgentGPT).
- Converting English to code (DB-GPT, SQL Chat, PandasAI).
- Generating websites from designs or screenshots (screenshot-to-code, draw-a-ui).
- Also: language translation, documentation, tests, and commit messages.

---

## Will AI Replace Software Engineers?
- Jensen Huang predicts AI will replace human software engineers.
- AWS CEO Matt Garman says most developers will stop coding, but jobs will change.
- Many engineers believe they will never be replaced, for technical and emotional reasons.
- McKinsey: AI doubles productivity for documentation, 25–50% for code generation and refactoring.

---

## Image and Video Production

- AI excels at creative tasks due to its probabilistic nature
- Successful startups include Midjourney, Adobe Firefly, Runway, Pika Labs, and Sora
- Midjourney reached $200 million annual recurring revenue at one and a half years old
- Half of top 10 free Graphics & Design apps had "AI" in their names

---

## AI-Generated Profile Pictures

- Common for social media profiles, from LinkedIn to TikTok
- Candidates believe AI headshots increase chances of landing a job
- Perception shifted: Facebook banned AI profile photos in 2019
- By 2023, many social media apps provide AI profile photo tools

---

## AI in Ads and Marketing

- Enterprises have been quick to incorporate AI into ads and marketing
- AI generates promotional images and videos, or first drafts for experts
- Multiple ad variations can be tested to find what works best
- AI adapts ads to seasons and locations, like fall leaves or winter snow

---

## Why Writing Suits AI
- AI has long aided writing via autocorrect and auto-completion on smartphones
- Writing is frequent, tedious, and tolerant of mistakes users can ignore
- LLMs suit writing because they are trained for text completion
- MIT study: 453 professionals; ChatGPT cut time 40%, raised quality 18%

---

## Study Findings and Consumer Uses
- ChatGPT narrows quality gaps, helping those less inclined to write
- Exposed workers 2x as likely to use it two weeks later; 1.6x two months later
- Consumers use AI to soften angry emails and expand bullet points into paragraphs
- Students write essays; startups generate children's, fan fiction, romance, fantasy books

---

## Tools, Abuse, and Enterprise
- Interactive AI books change plot by reader preference; apps target a child's trouble words
- Google Docs, Notion, Gmail assist writing; Grammarly finetunes for fluent, coherent, clear text
- Abuse: 2023 NYT reported Amazon flooded with shoddy AI-generated travel guidebooks
- Enterprises use AI in sales, marketing, performance reports, cold emails, ad copy, product descriptions

---

## Education: From Banning to Integrating AI

- Schools like NYC Public Schools and LA Unified initially banned ChatGPT, then reversed decisions months later.
- Instead of banning AI, schools can use it to help students learn faster.
- AI can summarize textbooks and generate personalized lecture plans for each student.
- AI adapts materials to formats best suited to each student, unlike one-size-fits-all education.

---

## Personalization and Language Learning

- Auditory learners can ask AI to read materials aloud; others can adapt visualizations or translate equations into code.
- AI is especially helpful for language learning through roleplay of different practice scenarios.
- Pajak and Bicknell (Duolingo, 2022) found lesson personalization benefits most from AI among four course-creation stages.

---

## AI as Teacher and Debate Partner

- AI can generate multiple-choice and open-ended quizzes and evaluate the answers.
- AI can serve as a debate partner, presenting different views better than the average human.
- Khan Academy offers AI-powered teaching assistants to students and course assistants to teachers.
- Teachers assign AI-generated essays for students to find and correct mistakes.

---

## Education Disrupted by AI
- Chegg share price fell from $28 at ChatGPT launch in Nov 2022 to $2 in Sept 2024.
- Students have been turning to AI for help with homework.
- Many education companies embrace AI to build better products.
- Some education companies find their lunches taken by AI.

---

## AI as Tutor and Skill Learning
- Risk: AI can replace many skills.
- Opportunity: AI can tutor people to learn any skill.
- AI helps someone get up to speed quickly.
- Learners can continue on their own to become better than AI.

---

## Conversational Bots
- Bots help find information, explain concepts, and brainstorm ideas.
- AI can be companion and therapist, emulating personalities as digital copies.
- Digital girlfriends and boyfriends became popular quickly; many talk to bots more than humans.
- Some worry AI will ruin dating; researchers use bot groups to simulate society (Park et al., 2023).

---

## Information Aggregation: Overview
- Keeping up with emails, Slack messages, and news can sometimes be overwhelming.
- AI can aggregate and summarize information, helping people filter and digest it.
- Salesforce's 2023 Generative AI Snapshot Research: 74% of generative AI users distill complex ideas and summarize.
- Information aggregation and distillation are essential for enterprise operations.

---

## Consumer Use Cases
- Talk-to-your-docs: applications process contracts, disclosures, and papers, letting users retrieve information conversationally.
- AI can summarize websites and research, and create reports on topics of your choice.
- While writing this book, the author found AI helpful for summarizing and comparing papers.

---

## Enterprise Use Cases
- More efficient information aggregation can make an organization leaner by reducing the burden on middle management.
- Instacart's popular "Fast Breakdown" prompt summarizes meeting notes, emails, and Slack conversations.
- It extracts facts, open questions, and action items, which can be inserted into project tracking tools and assigned.
- AI can surface critical information about potential customers and run analyses on competitors.

---

## Why Data Organization Matters

- Data production keeps growing: photos, videos, logs, and PDFs accumulate continuously.
- Information aggregation goes hand in hand with data organization.
- Photos, videos, logs, and PDFs are unstructured or semistructured data.
- Data must be organized so it can be searched later.

---

## AI for Organizing Unstructured Data

- AI can automatically generate text descriptions about images and videos.
- AI can match text queries with visuals that match those queries.
- Google Photos already uses AI to surface images matching search queries.
- Google Image Search can generate images when none match users' needs.

---

## AI for Data Analysis

- AI is very good with data analysis.
- It can write programs to generate data visualization and identify outliers.
- It can make predictions such as revenue forecasts.
- Enterprises can use AI to extract structured information from unstructured data.

---

## Workflow Automation: End Users and Enterprises

- AI should ultimately automate as much as possible, handling boring daily tasks for end users.
- End-user examples: booking restaurants, requesting refunds, planning trips, filling out forms.
- Enterprise examples: lead management, invoicing, reimbursements, customer requests, data entry.
- IDP industry estimated to reach $12.81 billion by 2030, growing 32.9% yearly.

---

## Data Synthesis and Labeling

- One exciting use case is using AI models to synthesize data.
- Synthesized data can then be used to improve the models themselves.
- AI can create labels for your data.
- Humans can be looped in to improve those labels.

---

## Agents and Access to External Tools

- Many tasks require access to external tools to be accomplished.
- Booking a restaurant may need search, phone calls, and calendar access.
- AIs that can plan and use tools are called agents.
- Interest around agents borders on obsession.

---

## Planning AI Applications

- AI agents could make every person vastly more productive and generate vastly more economic value.
- Agents are a central topic in Chapter 6.
- Not all applications should be built; consider key questions before building an AI application.
- If you only want to learn and have fun, jump right in—building is one of the best ways to learn.

---

## Learning vs. Building for a Living

- Early foundation model leaders encouraged teams to experiment with AI applications to upskill themselves.
- If you're doing this for a living, step back and consider why you're building and how.
- It's easy to build a cool demo with foundation models.
- It's hard to create a profitable product.

---

## Use Case Evaluation: Why Build?

- Ask first why you want to build the application—AI responds to risks and opportunities.
- Highest priority: AI poses existential threat; competitors with AI could make you obsolete.
- Most common: boost profits and productivity—cheaper acquisition, retention, sales, research.
- Some invest to avoid being left behind, funding R&D to understand AI's impact.

---

## Role of AI and Humans

- Critical vs complementary: the more core AI is, the higher the accuracy bar.
- Reactive features respond to requests and often need speed; proactive features can be precomputed.
- Dynamic features update continually with feedback; static features update periodically.
- Human-in-the-loop: AI can suggest, route complex requests, or respond directly.
- Crawl-Walk-Run framework gradually increases automation as AI quality improves.

---

## AI Product Defensibility

- Low entry barrier cuts both ways: what's easy for you is easy for competitors.
- Apps built atop foundation models risk being subsumed as models gain capabilities.
- Three competitive advantages: technology, data, and distribution.
- Foundation models make core technology similar; distribution favors big companies.
- Data can be a startup's moat if it reaches market first and gathers usage data.

---

## Features Can Become Companies
- Calendly could have been a feature of Google Calendar.
- Mailchimp could have been a feature of Gmail.
- Photoroom could have been a feature of Google Photos.
- Startups can overtake bigger competitors by building overlooked features.

---

## Setting Expectations
- After deciding to build the AI application yourself, define what success looks like.
- The most important metric is impact on your business.
- For a customer support chatbot, measure automated messages, processing capacity, response speed, and labor saved.
- Track customer satisfaction and feedback; answering more messages does not guarantee happy users.

---

## Usefulness Thresholds
- Define how good the product must be before it reaches customers.
- Quality metrics measure the quality of the chatbot's responses.
- Latency metrics: TTFT, TPOT, and total latency; acceptable latency depends on use case.
- Cost metrics: cost per inference request; other metrics include interpretability and fairness.

---

## Milestone Planning
- After setting measurable goals, build a plan to reach them.
- Evaluate existing models first: stronger off-the-shelf models mean less work.
- Example: a model already automating 30% of tickets needs less effort than one automating none.
- Goals may change after evaluation, for example if resources exceed potential return.

---

## The Last Mile Challenge
- Initial success with foundation models can be misleading; a good demo doesn't promise a good product.
- A demo may take a weekend; a product may take months or years.
- UltraChat (Ding et al., 2023): "the journey from 0 to 60 is easy," but 60 to 100 is exceedingly challenging.
- LinkedIn (2024): one month to reach 80%, four more months to surpass 95%, slowed by kinks and hallucinations.

---

## Maintenance: Riding the Bullet Train

- AI moves incredibly fast; building on foundation models commits you to constant change.
- Many changes are good: longer context, better outputs, faster and cheaper inference.
- Figure 1-11 shows inference cost dropping and MMLU performance rising, 2022–2024.
- Even good changes create friction; run cost-benefit analysis on each technology investment.

---

## Adapting to Model and Provider Changes

- The best option today may become the worst tomorrow; in-house may lose to cheaper providers.
- Third-party providers can go out of business, disrupting tailored infrastructure.
- Providers converging on the same API makes swapping models easier.
- Each model has quirks; swapping requires adjusting workflows, prompts, and data—plus versioning and evaluation.

---

## Regulatory and IP Risks

- Regulation is harder to adapt to; AI resources like compute, talent, and data are heavily regulated.
- GDPR compliance was estimated to cost businesses $9 billion.
- Compute availability can change overnight; a banned GPU vendor leaves you in trouble.
- IP rules are still evolving; IP-heavy companies hesitate to use AI for fear of losing IP.

---

## AI Engineering’s Origins
- AI engineering evolved out of ML engineering.
- Companies experimenting with foundation models often have existing ML teams lead.
- Some companies treat AI engineering the same as ML engineering.
- Rapid growth brings many new tools, techniques, models, and applications.

---

## Roles and Overlap
- Some companies have separate job descriptions for AI engineering.
- AI engineers and ML engineers have significant overlap regardless of organizational positioning.
- Existing ML engineers can add AI engineering skills to expand job prospects.
- Some AI engineers have no previous ML experience.

---

## Three Layers of the AI Stack
- Application development: prompts, context, rigorous evaluation, and good interfaces.
- Model development: frameworks for modeling, training, finetuning, inference optimization, and dataset engineering.
- Infrastructure: tooling for model serving, managing data and compute, and monitoring.
- Start from top layer and move down as needed.

---

## Evolution of the AI Stack Landscape
- March 2024 GitHub search found 920 AI-related repositories with at least 500 stars.
- Big jump in AI tooling in 2023 after Stable Diffusion and ChatGPT.
- Highest increases in 2023: applications and application development categories.
- Infrastructure growth was much less; core infrastructural needs remain the same.

---

## Enduring ML Engineering Principles
- Classical ML engineering experiments with hyperparameters; foundation models require experimenting with models, prompts, retrieval algorithms, and sampling variables.
- Making models run faster and cheaper remains a goal.
- Setting up a feedback loop to iteratively improve applications with production data is still important.
- Much of what ML engineers learned and shared over the last decade remains applicable.

---

## Innovations Unique to AI Engineering
- This collective ML experience makes it easier for everyone to begin building AI applications.
- Built on top of these enduring principles are many innovations unique to AI engineering.
- These innovations are explored throughout the book.

---

## AI Engineering vs ML Engineering
- AI engineering uses models trained by others, focusing less on modeling and training.
- It emphasizes model adaptation over model development.
- Foundation models are bigger, use more compute, and incur higher latency.
- Open-ended outputs make evaluation a much bigger problem.

---

## Model Adaptation Techniques
- Prompt-based techniques adapt models without updating model weights.
- Prompt engineering is easier, needs less data, and enables more model experimentation.
- Prompt engineering may not suffice for complex tasks or strict performance requirements.
- Finetuning updates model weights, is more complex, but can improve quality, latency, and cost.

---

## Model Development in ML Engineering
- Model development is the layer most commonly associated with traditional ML engineering.
- It has three main responsibilities: modeling and training, dataset engineering, and inference optimization.
- Evaluation is also required for model development.
- Evaluation is discussed in the next section, within application development.

---

## Modeling and Training

- Modeling and training covers designing a model architecture, training it, and finetuning it.
- Common tools include Google's TensorFlow, Hugging Face's Transformers, and Meta's PyTorch.
- Traditional ML development requires specialized knowledge of algorithms, architectures, and how models learn.
- That knowledge includes gradient descent, loss functions, and regularization concepts.

---

## ML Knowledge with Foundation Models

- With foundation models, ML knowledge is no longer a must-have for building AI applications.
- Many successful AI application builders are not interested in learning about gradient descent.
- ML knowledge remains extremely valuable, expanding the tools available to builders.
- It also helps troubleshooting when a model doesn't work as expected.

---

## Training Terminology

- Training always involves changing model weights, but not all weight changes are training.
- Quantization reduces weight precision and technically changes weight values, but isn't training.
- "Training" is often used in place of pre-training, finetuning, and post-training.
- These terms refer to different training phases.

---

## Pre-training: Definition and Cost

- Pre-training means training a model from scratch, with weights randomly initialized.
- For LLMs, pre-training often involves training a model for text completion.
- It is typically the most resource-intensive training step by a long shot.
- For InstructGPT, pre-training consumed up to 98% of overall compute and data resources.

---

## Pre-training: Risk and Expertise

- Pre-training takes a long time to complete.
- A small mistake during pre-training can cause significant financial loss and major project setbacks.
- Because it is so resource-intensive, pre-training has become an art practiced by few.
- Those with expertise in pre-training large models are heavily sought after.

---

## Finetuning: Definition
- Finetuning means continuing to train a model that has already been trained
- The starting model weights are obtained from the previous training process
- The model already carries certain knowledge from pre-training

---

## Why Finetuning Costs Less
- Finetuning typically requires fewer resources than pre-training
- Fewer resources means less data and less compute
- Existing pre-trained knowledge reduces what the model must learn anew

---

## Post-Training Versus Finetuning

- Post-training and finetuning are conceptually the same and often used interchangeably.
- Post-training usually refers to work done by model developers, such as improving instruction following.
- Finetuning usually refers to work done by application developers adapting a model to their needs.
- Pre-training and post-training form a spectrum, with very similar processes and tooling.

---

## Training Is Not Prompt Engineering

- Some people use "training" to describe prompt engineering, which is technically incorrect.
- Teaching a model via context input into the model is prompt engineering.
- Colloquial usage of "training" can be correct, but technically it means prompt engineering.
- "Finetuning" is also sometimes misused when the actual activity is prompt engineering.

---

## AI Engineering Versus ML Engineering: Dataset Engineering

- Dataset engineering: curating, generating, and annotating data for training and adapting AI models.
- Traditional ML use cases are close-ended; foundation models are open-ended.
- Annotating open-ended queries is much harder than annotating close-ended ones.
- Example: judging whether an email is spam is easier than writing an essay.

---

## Data Types and Manipulation

- Traditional ML engineering works more with tabular data; foundation models use unstructured data.
- AI engineering data work includes deduplication, tokenization, context retrieval, and quality control.
- Quality control covers removing sensitive information and toxic data.
- Dataset engineering is the focus of Chapter 8.

---

## Data Volume and Model Insight

- Some argue models are commodities, making data the main differentiator.
- Data needs depend on adapter technique: training from scratch needs most, then finetuning, then prompt engineering.
- Data expertise helps examine a model, since training data hints at strengths and weaknesses.

---

## Inference Optimization
- Inference optimization means making models faster and cheaper.
- It has always mattered, but foundation models make it even more important.
- Foundation models are often autoregressive: tokens are generated sequentially.
- A 10 ms per-token model takes one second for 100 tokens, challenging 100 ms latency expectations.

---

## How Responsibilities Change
- Modeling and training: ML knowledge shifts from required to nice-to-have.
- Dataset engineering: less feature engineering; more deduplication, tokenization, context retrieval, quality control.
- Inference optimization: important with traditional ML, even more important with foundation models.

---

## AI Engineering Versus ML Engineering

- Traditional ML: teams build applications with proprietary models, so model quality differentiates.
- Foundation models: many teams use the same model, so differentiation shifts to application development.
- Application development becomes the key source of competitive advantage.
- The application development layer has three responsibilities: evaluation, prompt engineering, and AI interface.

---

## Responsibilities of Application Development

- Evaluation: assessing application and model behavior.
- Prompt engineering: shaping model outputs through prompts.
- AI interface: designing how users interact with AI.
- These responsibilities define the application development layer with foundation models.

---

## Evaluation Is More Important with Foundation Models

- Evaluation mitigates risks and uncovers opportunities throughout model adaptation
- Needed for model selection, benchmarking, deployment readiness, and production monitoring
- Foundation models' open-ended nature makes evaluation harder than closed-ended ML tasks
- Chatbots have too many valid responses to curate exhaustive ground truths

---

## Many Adaptation Techniques Complicate Evaluation

- A system may perform poorly with one technique and much better with another
- Google's Gemini launch claimed superiority over ChatGPT on MMLU benchmark
- Gemini was evaluated with CoT@32 (32 examples), ChatGPT with only 5 examples
- When both were shown five examples, ChatGPT performed better

---

## Prompt Engineering and Context Construction

- Prompt engineering elicits desirable behaviors from input alone, without changing model weights
- Gemini Ultra's MMLU performance rose from 83.7% to 90.04% with a different technique
- Prompt engineering also means giving the model necessary context and tools
- Complex long-context tasks may need memory management to track history

---

## AI Interface: Definition and Shift

- AI interface means building the end-user interface for interacting with AI applications.
- Before foundation models, only well-resourced organizations could develop AI applications.
- Those applications were often embedded in existing products, such as fraud detection and recommender systems.
- With foundation models, anyone can build AI applications, standalone or embedded.

---

## Where AI Interfaces Appear

- Standalone web, desktop, and mobile apps, such as ChatGPT and Perplexity.
- Browser extensions, like Grammarly for Google Docs, and plug-ins such as GitHub Copilot in VSCode.
- Chatbots integrated into Slack, Discord, WeChat, and WhatsApp; Midjourney works via web or Discord.
- Product APIs (VSCode, Shopify, Microsoft 365) enable plug-ins, add-ons, and agent interaction.

---

## Interface Modalities and Feedback

- Chat is the most commonly used interface, but voice-based and embodied (AR/VR) interfaces also exist.
- Conversation interfaces make it easier for users to give feedback in natural language.
- However, that natural-language feedback is harder to extract.
- User feedback design is covered in Chapter 10.

---

## Shifting Priorities with Foundation Models
- AI interfaces are less important in traditional ML, important with foundation models.
- Prompt engineering is not applicable to traditional ML but important with foundation models.
- Evaluation is important in traditional ML and more important with foundation models.

---

## Closer to Full-Stack Engineering
- Emphasis on application development and interfaces brings AI engineering closer to full-stack development.
- Interfaces’ rising importance shifts AI tooling design to attract more frontend engineers.
- ML engineering is traditionally Python-centric; pre-foundation-model frameworks mostly supported Python APIs.
- Python remains popular, but JavaScript API support is increasing via LangChain.js, Transformers.js, OpenAI Node, Vercel AI SDK.

---

## Changing Engineer Backgrounds
- Many AI engineers come from traditional ML backgrounds.
- More are increasingly coming from web development or full-stack backgrounds.

---

## Chapter Purpose and AI Evolution
- The chapter explains AI engineering’s emergence due to foundation models.
- It overviews the process of building applications on foundation models.
- Language models became large language models through self-supervision.
- Models incorporated other data modalities and became foundation models.

---

## AI Engineering Workflow and Stack
- AI engineering evolved from ML engineering; many ML principles still apply.
- It brings new challenges, solutions, and changes to the AI engineering stack.
- Traditional ML often starts with data and model; product comes last.
- With foundation models, build product first and invest in data/models later.

---

## Navigating a Fast-Moving Field
- Foundation models enable consumer and enterprise application patterns; AI engineering is early.
- Before building, ask whether you should build and consider key factors.
- Community energy, creativity, and talent make updates hard to track.
- AI can summarize updates, but a framework is still needed; start with foundation models.

## Practice Questions

### Question 1: According to the text, what is the one word the author would use to...

According to the text, what is the one word the author would use to describe AI post-2020?

- [ ] A) Scale
- [ ] B) Speed
- [ ] C) Safety
- [ ] D) Cost

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The author states that if only one word could describe AI post-2020, it would be "scale."

### Question 2: What is described as the second major consequence of scaling up AI...

What is described as the second major consequence of scaling up AI models?

- [ ] A) AI models have become less expensive to train for all organizations
- [ ] B) Training LLMs requires data, compute, and specialized talent that only a few organizations can afford, leading to model as a service
- [ ] C) Publicly available internet data has increased dramatically
- [ ] D) AI applications no longer require machine learning models

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says the second consequence is that training LLMs requires resources only a few organizations can afford, which led to the emergence of model as a service.

### Question 3: How does the text define AI engineering?

How does the text define AI engineering?

- [ ] A) The process of training foundation models from scratch
- [ ] B) The process of building applications on top of readily available models
- [ ] C) The process of collecting publicly available internet data
- [ ] D) The process of manufacturing compute hardware for AI

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text explicitly defines AI engineering as "the process of building applications on top of readily available models."

### Question 4: Which of the following is listed in the text as an application AI w...

Which of the following is listed in the text as an application AI was already powering long before LLMs became prominent?

- [ ] A) Autonomous driving
- [ ] B) Product recommendations
- [ ] C) Medical diagnosis
- [ ] D) Language translation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text lists product recommendations, fraud detection, and churn prediction as pre-LLM AI applications.

### Question 5: According to the text, what has allowed language models to grow to...

According to the text, what has allowed language models to grow to the scale they are today?

- [ ] A) Self-supervision
- [ ] B) Reinforcement learning from human feedback
- [ ] C) Symbolic reasoning
- [ ] D) Manual rule-based parsing

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that language models have only been able to grow to today’s scale with self-supervision.

### Question 6: What does a language model encode?

What does a language model encode?

- [ ] A) Statistical information about one or more languages
- [ ] B) Only the grammar rules of a language
- [ ] C) Exact translations between all languages
- [ ] D) Programming syntax for foundation models

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text defines a language model as encoding statistical information about one or more languages.

### Question 7: Given the context “My favorite color is __”, what should an English...

Given the context “My favorite color is __”, what should an English language model predict?

- [ ] A) “blue” more often than “car”
- [ ] B) “car” more often than “blue”
- [ ] C) “blue” and “car” equally often
- [ ] D) Neither “blue” nor “car”

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says an English language model should predict “blue” more often than “car” in that context.

### Question 8: According to the text, what is the basic unit of a language model?

According to the text, what is the basic unit of a language model?

- [ ] A) A character
- [ ] B) A word
- [ ] C) A token
- [ ] D) A parameter

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states that the basic unit of a language model is token, which can be a character, a word, or part of a word depending on the model.

### Question 9: Which statement describes a masked language model?

Which statement describes a masked language model?

- [ ] A) It predicts missing tokens anywhere in a sequence using context from both before and after the missing tokens.
- [ ] B) It predicts the next token using only the preceding tokens.
- [ ] C) It generates text by continually producing one token after another.
- [ ] D) It is commonly used today for text generation.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** A masked language model is trained to fill in the blank using context from both before and after the missing token, unlike an autoregressive model.

### Question 10: Why are autoregressive language models the models of choice for tex...

Why are autoregressive language models the models of choice for text generation?

- [ ] A) They predict missing tokens anywhere in a sequence.
- [ ] B) They can continually generate one token after another using only preceding tokens.
- [ ] C) They require explicit labels for every token.
- [ ] D) They cannot use a fixed vocabulary.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says autoregressive models predict the next token using only preceding tokens and can continually generate one token after another, making them popular for text generation.

### Question 11: How does self-supervision help overcome the data labeling bottlenec...

How does self-supervision help overcome the data labeling bottleneck for language models?

- [ ] A) It requires expensive human labels for each training example.
- [ ] B) It infers labels from the input data, allowing models to learn from massive amounts of text.
- [ ] C) It eliminates the need for any text sequences.
- [ ] D) It is the same as unsupervised learning, where no labels are needed at all.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** In self-supervision, the model infers labels from the input data, so language models can learn from text sequences without explicit labeling and scale up to LLMs.

### Question 12: According to the source, why are Gemini and GPT-4V better character...

According to the source, why are Gemini and GPT-4V better characterized as foundation models rather than simply LLMs?

- [ ] A) They are trained only on text data.
- [ ] B) They incorporate more data modalities and can be built upon for different needs.
- [ ] C) They are smaller than task-specific models.
- [ ] D) They require manual labeling for every task.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says foundation signifies both the importance of these models and that they can be built upon for different needs, and it notes they are extended beyond text.

### Question 13: What training approach did OpenAI use for CLIP?

What training approach did OpenAI use for CLIP?

- [ ] A) Manual labeling of each image
- [ ] B) Natural language supervision using co-occurring image and text pairs
- [ ] C) Reinforcement learning from human feedback
- [ ] D) Task-specific sentiment analysis labels

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states OpenAI used a variant of self-supervision called natural language supervision and found co-occurring (image, text) pairs on the internet.

### Question 14: What is a multimodal model?

What is a multimodal model?

- [ ] A) A model that can work with more than one data modality
- [ ] B) A model that works only with text
- [ ] C) A model trained only for sentiment analysis
- [ ] D) A model that cannot generate outputs

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source defines a model that can work with more than one data modality as a multimodal model.

### Question 15: Which three common AI engineering techniques does the source mentio...

Which three common AI engineering techniques does the source mention for adapting a foundation model to your needs?

- [ ] A) Prompt engineering, RAG, and finetuning
- [ ] B) STT, TTS, and NLP
- [ ] C) Object detection, image classification, and translation
- [ ] D) Self-supervision, natural language supervision, and CLIP

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says prompt engineering, retrieval-augmented generation (RAG), and finetuning are three very common AI engineering techniques for adapting a model.

### Question 16: According to the source, what does AI engineering refer to?

According to the source, what does AI engineering refer to?

- [ ] A) Developing foundation models from scratch
- [ ] B) Building applications on top of foundation models
- [ ] C) Managing traditional ML operations only
- [ ] D) Creating programming languages for AI models

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source defines AI engineering as the process of building applications on top of foundation models. It contrasts this with traditional ML engineering, which involves developing ML models.

### Question 17: Which factor is described as making it easier to leverage AI becaus...

Which factor is described as making it easier to leverage AI because models are exposed via APIs that receive queries and return outputs?

- [ ] A) General-purpose AI capabilities
- [ ] B) Increased AI investments
- [ ] C) Low entrance barrier to building AI applications
- [ ] D) The use of only open source AI tools

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source describes the model-as-a-service approach, where models are exposed via APIs, as part of the low entrance barrier to building AI applications. These APIs provide access to powerful models via single API calls.

### Question 18: Why did the author choose the term “AI engineering” rather than ter...

Why did the author choose the term “AI engineering” rather than terms ending in “Ops”?

- [ ] A) Because there are no operational components in building foundation model applications
- [ ] B) Because the focus is more on tweaking foundation models to do what you want
- [ ] C) Because “Ops” terms are used only for traditional ML models
- [ ] D) Because most surveyed people preferred every “Ops” term

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The author says he did not choose terms ending in “Ops” because, while there are operational components, the focus is more on tweaking engineering foundation models to do what you want. He also notes that most surveyed people preferred “AI engineering.”

### Question 19: According to the source, what did Sam Altman say is the biggest opp...

According to the source, what did Sam Altman say is the biggest opportunity for the vast majority of people?

- [ ] A) Developing new foundation models independently
- [ ] B) Adapting foundation models for specific applications
- [ ] C) Replacing all software engineering tools with AI
- [ ] D) Building the infrastructure to host and serve models

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that Sam Altman said the biggest opportunity for the vast majority of people will be to adapt foundation models for specific applications. It also notes that developing foundation models requires resources available mainly to big corporations, governments, and well-funded startups.

### Question 20: According to the source, how did Amazon Web Services (AWS) categori...

According to the source, how did Amazon Web Services (AWS) categorize enterprise generative AI use cases?

- [ ] A) Customer experience, employee productivity, and process optimization
- [ ] B) Programming, data analysis, customer support, marketing copy, other copy, research, web design, and art
- [ ] C) Cost reduction, process efficiency, growth, and accelerating innovation
- [ ] D) Coding, image and video production, writing, education, conversational bots, information aggregation, data organization, and workflow automation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that AWS categorized enterprise generative AI use cases into customer experience, employee productivity, and process optimization.

### Question 21: In Eloundou et al. (2023), a task is defined as exposed to AI if AI...

In Eloundou et al. (2023), a task is defined as exposed to AI if AI and AI-powered software can do what?

- [ ] A) Replace the occupation entirely within one year
- [ ] B) Reduce the time needed to complete the task by at least 50%
- [ ] C) Reduce the cost of the task by at least 80%
- [ ] D) Complete the task without any human involvement

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says a task is exposed if AI and AI-powered software can reduce the time needed to complete it by at least 50%.

### Question 22: According to the 2024 a16z Growth report cited in the source, which...

According to the 2024 a16z Growth report cited in the source, which applications are companies faster to deploy?

- [ ] A) External-facing applications such as customer support chatbots
- [ ] B) Internal-facing applications such as internal knowledge management
- [ ] C) Open source applications with at least 500 GitHub stars
- [ ] D) Applications with 100% exposure to AI models directly

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that companies are faster to deploy internal-facing applications, such as internal knowledge management, than external-facing applications like customer support chatbots.

### Question 23: According to multiple generative AI surveys cited in the text, whic...

According to multiple generative AI surveys cited in the text, which is the most popular use case?

- [ ] A) Coding
- [ ] B) Social media
- [ ] C) Documentation
- [ ] D) Frontend development

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states coding is “hands down the most popular use case” in multiple generative AI surveys.

### Question 24: Which tool is described as one of the earliest successes of foundat...

Which tool is described as one of the earliest successes of foundation models in production and had annual recurring revenue cross $100 million two years after launch?

- [ ] A) Magic
- [ ] B) GitHub Copilot
- [ ] C) Anysphere
- [ ] D) PentestGPT

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source identifies GitHub Copilot as an early production success and says its ARR crossed $100 million only two years after launch.

### Question 25: According to McKinsey researchers cited in the text, AI can help de...

According to McKinsey researchers cited in the text, AI can help developers be how much more productive for documentation?

- [ ] A) 25–50% more productive
- [ ] B) Twice as productive
- [ ] C) Minimally more productive
- [ ] D) Not productive at all

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says McKinsey researchers found AI can help developers be twice as productive for documentation.

### Question 26: Which application is mentioned in the source as an example of AI fo...

Which application is mentioned in the source as an example of AI for video generation?

- [ ] A) Midjourney
- [ ] B) Adobe Firefly
- [ ] C) Runway
- [ ] D) LinkedIn

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source lists Runway, Pika Labs, and Sora as examples of video generation applications.

### Question 27: According to the source, by late 2023, Midjourney had reached what...

According to the source, by late 2023, Midjourney had reached what amount in annual recurring revenue at one and a half years old?

- [ ] A) $20 million
- [ ] B) $200 million
- [ ] C) $2 billion
- [ ] D) $200,000

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that in late 2023, at one and a half years old, Midjourney had already generated $200 million in annual recurring revenue.

### Question 28: What change does the source describe regarding AI-generated profile...

What change does the source describe regarding AI-generated profile pictures?

- [ ] A) Facebook began requiring AI-generated profile pictures in 2019.
- [ ] B) In 2019 Facebook banned accounts using AI-generated profile photos, while in 2023 many social media apps provide tools to generate them.
- [ ] C) AI-generated profile pictures have never been accepted by social media apps.
- [ ] D) LinkedIn banned AI-generated profile pictures in 2023.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says Facebook banned accounts using AI-generated profile photos in 2019, but by 2023 many social media apps provide tools for users to generate profile photos with AI.

### Question 29: For enterprise ads and marketing, which use of AI does the source m...

For enterprise ads and marketing, which use of AI does the source mention?

- [ ] A) Generating promotional images and videos and creating ad variations by season and location
- [ ] B) Replacing all human experts entirely
- [ ] C) Banning seasonal advertising
- [ ] D) Generating only social media profile pictures

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says AI can generate promotional images and videos, help brainstorm or draft ideas, test multiple ads, and generate variations according to seasons and locations.

### Question 30: In the MIT study by Noy and Zhang (2023) on ChatGPT and writing, wh...

In the MIT study by Noy and Zhang (2023) on ChatGPT and writing, what happened to average time taken and output quality for participants exposed to ChatGPT?

- [ ] A) Average time decreased by 40% and output quality rose by 18%.
- [ ] B) Average time decreased by 18% and output quality rose by 40%.
- [ ] C) Average time increased by 40% and output quality fell by 18%.
- [ ] D) Average time and output quality both stayed the same.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that among those exposed to ChatGPT, average time taken decreased by 40% and output quality rose by 18%.

### Question 31: According to the source, why is writing an ideal application for AI?

According to the source, why is writing an ideal application for AI?

- [ ] A) Because people rarely write, find it enjoyable, and expect perfect suggestions.
- [ ] B) Because we do it a lot, it can be tedious, and we have a high tolerance for mistakes.
- [ ] C) Because AI writing never makes mistakes and users must accept its suggestions.
- [ ] D) Because writing tasks are always too complex for humans to handle.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says writing is ideal for AI because we do it a lot, it can be tedious, and we have a high tolerance for mistakes.

### Question 32: What does the source say makes AI-generated books different from tr...

What does the source say makes AI-generated books different from traditional books?

- [ ] A) They cannot include author bios or websites.
- [ ] B) They are always written by students.
- [ ] C) They can be interactive, with a plot that changes depending on a reader’s preference.
- [ ] D) They are only used for travel guidebooks.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states that AI-generated books can be interactive because a book’s plot can change depending on a reader’s preference.

### Question 33: According to the source, what did several education boards such as...

According to the source, what did several education boards such as New York City Public Schools and Los Angeles Unified School District do after initially banning ChatGPT?

- [ ] A) They permanently expanded the ban to all AI tools.
- [ ] B) They reversed their decisions a few months later.
- [ ] C) They required students to use ChatGPT for homework.
- [ ] D) They banned only AI-generated essays.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says these education boards were quick to ban ChatGPT but reversed their decisions just a few months later.

### Question 34: According to Pajak and Bicknell (Duolingo, 2022), which stage of co...

According to Pajak and Bicknell (Duolingo, 2022), which stage of course creation can benefit the most from AI?

- [ ] A) Lesson personalization
- [ ] B) Advertising sales
- [ ] C) SEO optimization
- [ ] D) Content farm creation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that out of four stages of course creation, lesson personalization is the stage that can benefit the most from AI.

### Question 35: What innovative teaching method does the source describe involving...

What innovative teaching method does the source describe involving AI-generated essays?

- [ ] A) Teachers use AI-generated essays to rank websites on Google.
- [ ] B) Students ask AI to roleplay language-learning scenarios only.
- [ ] C) Teachers assign AI-generated essays for students to find and correct mistakes.
- [ ] D) Schools ban AI-generated essays to prevent cheating.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source describes an innovative teaching method in which teachers assign AI-generated essays for students to find and correct mistakes.

### Question 36: How does the source say AI can help adapt educational materials to...

How does the source say AI can help adapt educational materials to individual students?

- [ ] A) By making all students use the same lecture plan.
- [ ] B) By banning personalized ads in schools.
- [ ] C) By helping auditory learners have materials read out loud and translating math equations into code.
- [ ] D) By replacing teachers with SEO-optimized content farms.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source gives examples such as asking AI to read materials out loud for auditory learners and translate math equations into code for students who find code easier to read.

### Question 37: According to the source, which of the following is a use of convers...

According to the source, which of the following is a use of conversational bots mentioned in the text?

- [ ] A) Helping find information, explain concepts, and brainstorm ideas
- [ ] B) Only replacing human tutors in schools
- [ ] C) Only predicting stock prices
- [ ] D) Only simulating dating relationships

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says conversational bots are versatile and can help us find information, explain concepts, and brainstorm ideas.

### Question 38: What does the source say about digital girlfriends and boyfriends?

What does the source say about digital girlfriends and boyfriends?

- [ ] A) They have become weirdly popular in an incredibly short amount of time
- [ ] B) They are used only for academic research
- [ ] C) They have completely ended human dating
- [ ] D) They are less popular than talking to humans

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that digital girlfriends and boyfriends have become weirdly popular very quickly, and some worry AI will ruin dating.

### Question 39: In the research mentioned, what can a group of conversational bots...

In the research mentioned, what can a group of conversational bots be used to do?

- [ ] A) Simulate a society to conduct studies on social dynamics
- [ ] B) Replace all education companies
- [ ] C) Automatically raise a company’s share price
- [ ] D) Stop students from using AI for homework

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says researchers found they can use a group of conversational bots to simulate a society and study social dynamics (Park et al., 2023).

### Question 40: What happened to Chegg’s share price after ChatGPT launched in Nove...

What happened to Chegg’s share price after ChatGPT launched in November 2022?

- [ ] A) It fell from $28 to $2 by September 2024
- [ ] B) It rose from $2 to $28 by September 2024
- [ ] C) It stayed exactly the same
- [ ] D) It doubled within a month

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says Chegg saw its share price plummet from $28 when ChatGPT launched to $2 in September 2024.

### Question 41: According to Salesforce’s 2023 Generative AI Snapshot Research, wha...

According to Salesforce’s 2023 Generative AI Snapshot Research, what percentage of generative AI users use it to distill complex ideas and summarize information?

- [ ] A) 74%
- [ ] B) 15%
- [ ] C) 16%
- [ ] D) 50%

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that 74% of generative AI users use it to distill complex ideas and summarize information.

### Question 42: In Instacart’s internal prompt marketplace, the “Fast Breakdown” te...

In Instacart’s internal prompt marketplace, the “Fast Breakdown” template asks AI to summarize meeting notes, emails, and Slack conversations into which set of elements?

- [ ] A) Facts, open questions, and action items
- [ ] B) Customer profiles, competitor analyses, and reports
- [ ] C) Contracts, disclosures, and papers
- [ ] D) Storylines, dialogues, and simple actions

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says “Fast Breakdown” summarizes meeting notes, emails, and Slack conversations with facts, open questions, and action items.

### Question 43: What is the use case called when applications process your document...

What is the use case called when applications process your documents—such as contracts, disclosures, and papers—and let you retrieve information in a conversational manner?

- [ ] A) Smart NPCs
- [ ] B) Talk-to-your-docs
- [ ] C) Product copilots
- [ ] D) Customer support bots

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source explicitly says this use case is also called talk-to-your-docs.

### Question 44: According to the text, why is organizing data becoming more important?

According to the text, why is organizing data becoming more important?

- [ ] A) Because people and companies will continue producing more and more data
- [ ] B) Because unstructured data is no longer useful
- [ ] C) Because AI cannot work with large amounts of information
- [ ] D) Because contracts are always structured data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says we’ll continue producing more data, and it is essential to organize it so it can be searched later.

### Question 45: Which examples does the text give of unstructured or semistructured...

Which examples does the text give of unstructured or semistructured data?

- [ ] A) Photos, videos, logs, and PDFs
- [ ] B) Only spreadsheets and databases
- [ ] C) Only contracts and revenue forecasts
- [ ] D) Search queries and image descriptions only

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source explicitly lists photos, videos, logs, and PDFs as unstructured or semistructured data.

### Question 46: How can AI help with visual data organization and search?

How can AI help with visual data organization and search?

- [ ] A) By automatically generating text descriptions and matching text queries with relevant visuals
- [ ] B) By deleting all images that do not match a query
- [ ] C) By converting all videos into contracts
- [ ] D) By preventing users from taking more photos

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says AI can generate text descriptions about images and videos and help match text queries with visuals.

### Question 47: What can enterprises use AI to do with unstructured data?

What can enterprises use AI to do with unstructured data?

- [ ] A) Extract structured information from it to help organize and search it
- [ ] B) Replace all unstructured data with revenue forecasts
- [ ] C) Stop producing logs and PDFs
- [ ] D) Avoid using data visualization

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that enterprises can use AI to extract structured information from unstructured data to organize it and help search it.

### Question 48: According to the text, what are AIs that can plan and use tools cal...

According to the text, what are AIs that can plan and use tools called?

- [ ] A) IDP systems
- [ ] B) Agents
- [ ] C) Foundation models
- [ ] D) Workflow automators

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that AIs that can plan and use tools are called agents.

### Question 49: Which task is listed as an enterprise repetitive task that AI can a...

Which task is listed as an enterprise repetitive task that AI can automate?

- [ ] A) Booking restaurants
- [ ] B) Planning trips
- [ ] C) Invoicing
- [ ] D) Filling out forms

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text lists invoicing among enterprise repetitive tasks, while booking restaurants, planning trips, and filling out forms are given as end-user examples.

### Question 50: What does the text describe as an especially exciting workflow auto...

What does the text describe as an especially exciting workflow automation use case?

- [ ] A) Using AI models to synthesize data to improve the models themselves
- [ ] B) Using AI to eliminate the need for external tools
- [ ] C) Using AI only to extract data from credit cards
- [ ] D) Using AI to replace all human involvement in labeling

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says one especially exciting use case is using AI models to synthesize data, which can then be used to improve the models themselves.

### Question 51: According to the text, what should you do if you just want to learn...

According to the text, what should you do if you just want to learn and have fun?

- [ ] A) Jump right in
- [ ] B) Take a step back and avoid building
- [ ] C) Wait until you can create a profitable product
- [ ] D) Focus only on planning and not experimentation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says that if you just want to learn and have fun, you should jump right in, because building is one of the best ways to learn.

### Question 52: In the early days of foundation models, what did several heads of A...

In the early days of foundation models, what did several heads of AI encourage their teams to do?

- [ ] A) Avoid experimenting with AI applications
- [ ] B) Experiment with AI applications to upskill themselves
- [ ] C) Build only profitable products
- [ ] D) Stop using foundation models

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that several heads of AI encouraged their teams to experiment with AI applications to upskill themselves.

### Question 53: If you are building AI applications for a living, what does the tex...

If you are building AI applications for a living, what does the text say might be worthwhile?

- [ ] A) Skipping planning because demos are easy
- [ ] B) Taking a step back to consider why you’re building and how you should go about it
- [ ] C) Building only cool demos
- [ ] D) Assuming a profitable product is easy to create

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says that if you’re doing this for a living, it might be worthwhile to take a step back and consider why you’re building this and how you should go about it.

### Question 54: According to the source, which reason for embracing AI is listed as...

According to the source, which reason for embracing AI is listed as the highest level of risk?

- [ ] A) If you don’t do this, competitors with AI can make you obsolete.
- [ ] B) If you don’t do this, you’ll miss opportunities to boost profits and productivity.
- [ ] C) You’re unsure where AI will fit into your business yet, but you don’t want to be left behind.
- [ ] D) You want to reduce the cost of customer support by replacing human agents.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source orders risks from high to low and lists competitors with AI making you obsolete as the highest-risk reason.

### Question 55: What does the source say about whether AI is critical or complement...

What does the source say about whether AI is critical or complementary to an application?

- [ ] A) If AI is complementary, it must be more accurate and reliable than if it is critical.
- [ ] B) The more critical AI is to the application, the more accurate and reliable the AI part has to be.
- [ ] C) Critical AI features are always proactive, while complementary features are reactive.
- [ ] D) Complementary AI features cannot use foundation models.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that the more critical AI is to the application, the more accurate and reliable the AI part has to be.

### Question 56: Which statement about proactive AI features is consistent with the...

Which statement about proactive AI features is consistent with the source?

- [ ] A) They are generated only in response to users’ requests or specific actions.
- [ ] B) They usually need to happen faster than reactive features because users ask for them directly.
- [ ] C) They can be precomputed and shown opportunistically, so latency is less important, but they typically have a higher quality bar.
- [ ] D) They are less likely to be viewed as intrusive or annoying if quality is low.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says proactive features can be precomputed and shown opportunistically, making latency less important, and that they typically have a higher quality bar.

### Question 57: In Microsoft’s Crawl-Walk-Run framework, what does “Walk” mean?

In Microsoft’s Crawl-Walk-Run framework, what does “Walk” mean?

- [ ] A) Human involvement is mandatory.
- [ ] B) AI can directly interact with internal employees.
- [ ] C) AI directly interacts with external users with no human involvement.
- [ ] D) AI is used only to generate suggestions for human agents.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source defines Crawl as mandatory human involvement, Walk as AI directly interacting with internal employees, and Run as increased automation potentially including external users.

### Question 58: According to the text, after deciding to build an AI application yo...

According to the text, after deciding to build an AI application yourself, what is the next step?

- [ ] A) Choosing a foundation model provider
- [ ] B) Figuring out what success looks like and how to measure it
- [ ] C) Hiring a larger engineering team
- [ ] D) Replacing all human customer support

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says the next step is to figure out what success looks like and how success will be measured.

### Question 59: For a customer support chatbot, which of the following is given as...

For a customer support chatbot, which of the following is given as a possible business metric?

- [ ] A) The number of foundation model parameters
- [ ] B) The percentage of customer messages the chatbot automates
- [ ] C) The number of features Google Calendar offers
- [ ] D) The startup’s office location

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text lists “What percentage of customer messages do you want the chatbot to automate?” as a business metric example.

### Question 60: Why does the text say it is important to track customer satisfactio...

Why does the text say it is important to track customer satisfaction and customer feedback?

- [ ] A) Because a chatbot answering more messages does not necessarily mean users will be happy
- [ ] B) Because customer feedback is required to train every foundation model
- [ ] C) Because business metrics are less important than model size
- [ ] D) Because chatbots should replace all customer messages

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text notes that a chatbot can answer more messages, but that does not mean it will make users happy, so satisfaction and feedback should be tracked.

### Question 61: Once measurable goals have been set, what does milestone planning s...

Once measurable goals have been set, what does milestone planning say you should do to understand where you are starting from?

- [ ] A) Evaluate existing models to understand their capabilities
- [ ] B) Launch the product to customers immediately
- [ ] C) Skip evaluation and build the final product
- [ ] D) Set the usefulness threshold only after launch

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says that once measurable goals are set, you need a plan, and how to get to the goals depends on where you start, so you should evaluate existing models to understand their capabilities.

### Question 62: What does the source mean by the “last mile challenge” in planning...

What does the source mean by the “last mile challenge” in planning an AI product?

- [ ] A) A good initial demo guarantees a good end product
- [ ] B) Initial success with foundation models can be misleading because a demo may take a weekend while a product may take months or years
- [ ] C) Foundation models cannot be used to build demos
- [ ] D) The last mile is only about reducing inference cost

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source warns that impressive base capabilities make it easy to build a fun demo, but a good initial demo does not promise a good end product and building a product can take much longer.

### Question 63: According to LinkedIn (2024), after taking one month to achieve 80%...

According to LinkedIn (2024), after taking one month to achieve 80% of the experience they wanted, how much additional time did it take them to finally surpass 95%?

- [ ] A) One week
- [ ] B) One month
- [ ] C) Four more months
- [ ] D) One year

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states that LinkedIn took one month to achieve 80% of the desired experience and then found it took four more months to finally surpass 95%.

### Question 64: According to the text, what adds a challenge to maintaining an AI p...

According to the text, what adds a challenge to maintaining an AI product?

- [ ] A) The fast pace of change in AI
- [ ] B) The lack of any model providers
- [ ] C) The complete stability of foundation models
- [ ] D) The absence of regulations around AI

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says maintenance of an AI product has the added challenge of AI’s fast pace of change.

### Question 65: Which example does the text give of a good change that can still ca...

Which example does the text give of a good change that can still cause friction in workflows?

- [ ] A) Building a model in-house because it seems cheaper, then model providers drop prices and make in-house expensive
- [ ] B) Model providers refusing to offer APIs
- [ ] C) Context lengths getting shorter over time
- [ ] D) Inference becoming slower and more expensive

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text uses this example to show that the best option today might become the worst option tomorrow.

### Question 66: According to the text, which type of change is especially hard to a...

According to the text, which type of change is especially hard to adapt to?

- [ ] A) Changes around regulations
- [ ] B) Changes that make model APIs easier to swap
- [ ] C) Changes that improve model outputs
- [ ] D) Changes that make inference faster and cheaper

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says some changes are harder to adapt to, especially those around regulations.

### Question 67: Why do many IP-heavy companies hesitate to use AI, according to the...

Why do many IP-heavy companies hesitate to use AI, according to the text?

- [ ] A) Because they fear losing their IP later as IP and AI usage regulations are still evolving
- [ ] B) Because foundation models cannot be maintained
- [ ] C) Because model inference is too fast
- [ ] D) Because context lengths are too long

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says IP-heavy companies hesitate for fear of losing their IPs later on, given evolving IP and AI usage regulations.

### Question 68: According to the source text, AI engineering evolved out of which f...

According to the source text, AI engineering evolved out of which field?

- [ ] A) ML engineering
- [ ] B) Data engineering
- [ ] C) DevOps
- [ ] D) Prompt engineering

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that “AI engineering evolved out of ML engineering.”

### Question 69: What does the source text say about how companies position AI engin...

What does the source text say about how companies position AI engineering and ML engineering?

- [ ] A) All companies treat them as completely unrelated roles.
- [ ] B) Some companies put them under the same umbrella, while some have separate job descriptions.
- [ ] C) No companies have separate job descriptions for AI engineering.
- [ ] D) Companies only hire AI engineers with previous ML experience.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text notes that some companies treat AI engineering the same as ML engineering, while others have separate job descriptions for AI engineering.

### Question 70: What does the source text say about the roles of AI engineers and M...

What does the source text say about the roles of AI engineers and ML engineers?

- [ ] A) Their roles have significant overlap.
- [ ] B) Their roles have no overlap at all.
- [ ] C) AI engineers must always have previous ML experience.
- [ ] D) ML engineers cannot add AI engineering to their skills.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says that regardless of where organizations position them, “their roles have significant overlap.”

### Question 71: What are the three layers of the AI application stack described in...

What are the three layers of the AI application stack described in the text?

- [ ] A) Application development, model development, infrastructure
- [ ] B) Data engineering, model training, deployment
- [ ] C) Prompt engineering, fine-tuning, serving
- [ ] D) Business metrics, ML metrics, evaluation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text explicitly states that there are three layers: application development, model development, and infrastructure.

### Question 72: According to the GitHub repository analysis in the text, which cate...

According to the GitHub repository analysis in the text, which categories saw the highest increases in 2023?

- [ ] A) Infrastructure and model development
- [ ] B) Applications and application development
- [ ] C) Model development and infrastructure
- [ ] D) All categories equally

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says that in 2023, the categories with the highest increases were applications and application development.

### Question 73: What does the text say about core infrastructural needs as models a...

What does the text say about core infrastructural needs as models and applications change?

- [ ] A) They change rapidly
- [ ] B) They remain the same
- [ ] C) They become less important
- [ ] D) They require entirely new tools

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that even though models and applications have changed, the core infrastructural needs—resource management, serving, monitoring, etc.—remain the same.

### Question 74: According to the text, what do you experiment with when working wit...

According to the text, what do you experiment with when working with foundation models, compared with classical ML engineering?

- [ ] A) Only different hyperparameters
- [ ] B) Different models, prompts, retrieval algorithms, and sampling variables
- [ ] C) Only the size of the training dataset
- [ ] D) Only the model's architecture and weights

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that with classical ML engineering you experiment with hyperparameters, whereas with foundation models you experiment with models, prompts, retrieval algorithms, sampling variables, and more.

### Question 75: What does the text say about what ML engineers have learned and sha...

What does the text say about what ML engineers have learned and shared over the last decade?

- [ ] A) It is no longer relevant to building AI applications
- [ ] B) Much of it is still applicable to AI engineering
- [ ] C) It applies only to foundation models, not classical ML
- [ ] D) It removes the need for a feedback loop

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says much of what ML engineers have learned and shared over the last decade is still applicable, even though AI engineering adds new innovations on top.

### Question 76: According to the text, why is it easier for everyone to begin build...

According to the text, why is it easier for everyone to begin building AI applications?

- [ ] A) Because foundation models no longer require experimentation
- [ ] B) Because of the collective experience ML engineers have built and shared over the last decade
- [ ] C) Because feedback loops are now automatic
- [ ] D) Because sampling variables have been eliminated

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that this collective experience makes it easier for everyone to begin building AI applications.

### Question 77: How does the text describe the innovations unique to AI engineering...

How does the text describe the innovations unique to AI engineering in relation to enduring principles?

- [ ] A) They replace the enduring principles entirely
- [ ] B) They are built on top of those enduring principles
- [ ] C) They are unrelated to anything in ML engineering
- [ ] D) They make feedback loops unnecessary

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says that built on top of these enduring principles are many innovations unique to AI engineering.

### Question 78: According to the text, how does AI engineering differ from traditio...

According to the text, how does AI engineering differ from traditional ML engineering in terms of model development?

- [ ] A) AI engineering focuses less on modeling and training and more on model adaptation.
- [ ] B) AI engineering focuses more on training models from scratch for each application.
- [ ] C) AI engineering avoids using pretrained models entirely.
- [ ] D) AI engineering focuses mainly on collecting labeled datasets.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that with AI engineering you use a model someone else has trained, so the focus shifts from modeling and training to model adaptation.

### Question 79: Why does the text say evaluation is a much bigger problem in AI eng...

Why does the text say evaluation is a much bigger problem in AI engineering?

- [ ] A) Because foundation models cannot be used for many tasks.
- [ ] B) Because AI engineering models produce open-ended outputs, which are harder to evaluate.
- [ ] C) Because traditional ML models never require evaluation.
- [ ] D) Because prompt engineering eliminates the need for evaluation.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says open-ended outputs give models flexibility but are harder to evaluate, making evaluation a bigger problem in AI engineering.

### Question 80: Which statement best reflects the text’s comparison of prompt-based...

Which statement best reflects the text’s comparison of prompt-based techniques and finetuning?

- [ ] A) Prompt-based techniques update model weights, while finetuning does not.
- [ ] B) Prompt-based techniques adapt a model without updating weights, while finetuning requires updating model weights.
- [ ] C) Both prompt-based techniques and finetuning avoid changing the model.
- [ ] D) Finetuning is always easier and requires less data than prompt engineering.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text defines prompt-based techniques as adapting a model without updating weights and finetuning as requiring updates to model weights.

### Question 81: What does the text identify as a consequence of AI engineering work...

What does the text identify as a consequence of AI engineering working with bigger, more compute-intensive models?

- [ ] A) There is less need for inference optimization.
- [ ] B) There is more pressure for efficient training and inference optimization.
- [ ] C) Companies need fewer GPUs and smaller compute clusters.
- [ ] D) Latency is lower than in traditional ML engineering.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says these models consume more compute and incur higher latency, creating more pressure for efficient training and inference optimization.

### Question 82: Which layer is most commonly associated with traditional ML enginee...

Which layer is most commonly associated with traditional ML engineering?

- [ ] A) Model development
- [ ] B) Application development
- [ ] C) Foundation model selection
- [ ] D) Prompt engineering

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that model development is the layer most commonly associated with traditional ML engineering.

### Question 83: What are the three main responsibilities of model development?

What are the three main responsibilities of model development?

- [ ] A) Modeling and training, dataset engineering, and inference optimization
- [ ] B) Evaluation, deployment, and monitoring
- [ ] C) Application development, prompt engineering, and evaluation
- [ ] D) Data collection, model selection, and user interface design

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists modeling and training, dataset engineering, and inference optimization as the three main responsibilities of model development.

### Question 84: Why does the source discuss evaluation in the next section rather t...

Why does the source discuss evaluation in the next section rather than under model development?

- [ ] A) Because most people will come across evaluation first in the application development layer
- [ ] B) Because evaluation is not required for model development
- [ ] C) Because evaluation belongs only to dataset engineering
- [ ] D) Because evaluation is part of inference optimization

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says evaluation is also required, but it is discussed in the next section because most people will come across it first in the application development layer.

### Question 85: According to the text, what does "modeling and training" refer to?

According to the text, what does "modeling and training" refer to?

- [ ] A) The process of deploying models to production and monitoring their performance
- [ ] B) The process of coming up with a model architecture, training it, and finetuning it
- [ ] C) The process of collecting and labeling data for machine learning models
- [ ] D) The process of reducing the precision of model weights

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text defines modeling and training as the process of coming up with a model architecture, training it, and finetuning it.

### Question 86: How does the availability of foundation models change the need for...

How does the availability of foundation models change the need for ML knowledge when building AI applications?

- [ ] A) ML knowledge becomes completely unnecessary for all AI application builders
- [ ] B) ML knowledge is no longer a must-have, but it is still extremely valuable
- [ ] C) ML knowledge becomes more important than ever before
- [ ] D) ML knowledge is only needed for troubleshooting, not for expanding tools

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that with foundation models, ML knowledge is no longer a must-have, but it remains extremely valuable because it expands the set of tools and helps troubleshooting.

### Question 87: Which of the following changes model weights but is NOT considered...

Which of the following changes model weights but is NOT considered training, according to the text?

- [ ] A) Pre-training
- [ ] B) Finetuning
- [ ] C) Quantization
- [ ] D) Post-training

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text explains that quantization reduces the precision of model weights and technically changes weight values but is not considered training.

### Question 88: What does pre-training refer to in the context of foundation models?

What does pre-training refer to in the context of foundation models?

- [ ] A) Fine-tuning a model on a small task-specific dataset
- [ ] B) Training a model from scratch with randomly initialized weights
- [ ] C) Aligning a model's outputs with human preferences
- [ ] D) Compressing a large model for deployment

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that pre-training refers to training a model from scratch—the model weights are randomly initialized.

### Question 89: According to the source, what proportion of overall compute and dat...

According to the source, what proportion of overall compute and data resources did pre-training consume for the InstructGPT model?

- [ ] A) Up to 50%
- [ ] B) Up to 75%
- [ ] C) Up to 98%
- [ ] D) Up to 100%

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says that for InstructGPT, pre-training takes up to 98% of the overall compute and data resources.

### Question 90: Which statement about pre-training is best supported by the source...

Which statement about pre-training is best supported by the source text?

- [ ] A) Pre-training is inexpensive and quick to complete.
- [ ] B) Small mistakes during pre-training have little financial impact.
- [ ] C) Pre-training is resource-intensive and only a few practice it.
- [ ] D) Expertise in pre-training large models is not in demand.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source describes pre-training as resource-intensive, an art that only a few practice, and notes that experts are heavily sought after.

### Question 91: What does finetuning mean in the source text?

What does finetuning mean in the source text?

- [ ] A) Training a model from scratch without any prior weights
- [ ] B) Continuing to train a previously trained model
- [ ] C) Removing all learned knowledge from a model
- [ ] D) Evaluating a model without changing its weights

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that finetuning means continuing to train a previously trained model.

### Question 92: In finetuning, where do the model weights come from?

In finetuning, where do the model weights come from?

- [ ] A) They are randomly initialized for each finetuning run
- [ ] B) They are obtained from the previous training process
- [ ] C) They are supplied only by the user at inference time
- [ ] D) They are discarded before finetuning begins

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says the model weights are obtained from the previous training process.

### Question 93: Why does finetuning typically require fewer resources than pre-trai...

Why does finetuning typically require fewer resources than pre-training?

- [ ] A) Because the model already has certain knowledge from pre-training
- [ ] B) Because finetuning does not use any data
- [ ] C) Because finetuning always uses a smaller model architecture
- [ ] D) Because finetuning avoids training the model at all

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source explains that the model already has certain knowledge from pre-training, so finetuning typically requires fewer resources such as data and compute.

### Question 94: According to the text, how are post-training and finetuning related...

According to the text, how are post-training and finetuning related conceptually?

- [ ] A) They are unrelated processes with different tooling.
- [ ] B) They are conceptually the same and can be used interchangeably.
- [ ] C) Post-training only applies to application developers, while finetuning only applies to model developers.
- [ ] D) Finetuning happens before pre-training, while post-training happens after.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says post-training and finetuning are conceptually the same and can be used interchangeably, though people sometimes use them differently to signify different goals.

### Question 95: In the text’s typical usage distinction, who usually does post-trai...

In the text’s typical usage distinction, who usually does post-training and who usually does finetuning?

- [ ] A) Post-training is usually done by application developers; finetuning is usually done by model developers.
- [ ] B) Post-training is usually done by model developers; finetuning is usually done by application developers.
- [ ] C) Both are usually done only by application developers.
- [ ] D) Both are usually done only by model developers.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says it is usually post-training when done by model developers and finetuning when done by application developers.

### Question 96: The Business Insider author said she “trained” ChatGPT to mimic her...

The Business Insider author said she “trained” ChatGPT to mimic her younger self by feeding it childhood journal entries. Technically, what was she doing according to the text?

- [ ] A) Pre-training
- [ ] B) Post-training
- [ ] C) Prompt engineering
- [ ] D) Model development

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says that teaching a model what to do via context input is technically prompt engineering, even though people colloquially call it training.

### Question 97: What does the text say about pre-training and post-training as a sp...

What does the text say about pre-training and post-training as a spectrum?

- [ ] A) Their processes and toolings are very similar.
- [ ] B) They use completely different processes and toolings.
- [ ] C) Post-training replaces pre-training entirely.
- [ ] D) Pre-training is only for application developers.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that pre-training and post-training make up a spectrum and that their processes and toolings are very similar.

### Question 98: What does dataset engineering refer to in the source text?

What does dataset engineering refer to in the source text?

- [ ] A) Curating, generating, and annotating the data needed for training and adapting AI models
- [ ] B) Designing hardware for training foundation models
- [ ] C) Writing prompts for open-ended queries only
- [ ] D) Deploying models into production

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text defines dataset engineering as curating, generating, and annotating the data needed for training and adapting AI models.

### Question 99: Why is data annotation a bigger challenge for AI engineering than f...

Why is data annotation a bigger challenge for AI engineering than for traditional ML engineering?

- [ ] A) Foundation models are close-ended, while traditional ML models are open-ended
- [ ] B) Foundation models are open-ended, and annotating open-ended queries is harder than annotating close-ended queries
- [ ] C) Traditional ML engineering uses only unstructured data
- [ ] D) AI engineering does not require any annotation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says foundation models are open-ended, and it is easier to determine whether an email is spam than to write an essay.

### Question 100: According to the text, what does how much data you need depend on?

According to the text, what does how much data you need depend on?

- [ ] A) The adapter technique you use
- [ ] B) The number of predefined output labels
- [ ] C) Whether the data is tabular or unstructured only
- [ ] D) The model’s deployment environment

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that how much data you need depends on the adapter technique you use, with training from scratch generally requiring more data than finetuning, which requires more than prompt engineering.

### Question 101: In AI engineering, data manipulation is more about which of the fol...

In AI engineering, data manipulation is more about which of the following?

- [ ] A) Deduplication, tokenization, context retrieval, and quality control
- [ ] B) Only collecting tabular data
- [ ] C) Avoiding unstructured data
- [ ] D) Reducing model outputs to predefined values

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says AI engineering data manipulation is more about deduplication, tokenization, context retrieval, and quality control, including removing sensitive information and toxic data.

### Question 102: What does inference optimization mean in the source text?

What does inference optimization mean in the source text?

- [ ] A) Making models faster and cheaper
- [ ] B) Training a model from scratch
- [ ] C) Deduplicating training data
- [ ] D) Performing feature engineering for tabular data

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text defines inference optimization as making models faster and cheaper.

### Question 103: Why has inference optimization become even more important with foun...

Why has inference optimization become even more important with foundation models?

- [ ] A) Foundation models are always smaller and cheaper to run
- [ ] B) Foundation models scale up to incur higher inference cost and latency
- [ ] C) Users prefer slower model responses
- [ ] D) Foundation models eliminate the need for latency optimization

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says foundation models scale up to incur even higher inference cost and latency, making inference optimization more important.

### Question 104: What challenge does autoregressive generation create for foundation...

What challenge does autoregressive generation create for foundation models?

- [ ] A) Tokens are generated sequentially, which can make latency high
- [ ] B) Tokens are generated all at once, so latency is eliminated
- [ ] C) It removes the need for inference optimization
- [ ] D) It only affects data deduplication

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text explains that autoregressive models generate tokens sequentially, so longer outputs take more time and create latency challenges.

### Question 105: According to Table 1-4, how does the importance of inference optimi...

According to Table 1-4, how does the importance of inference optimization change when building with foundation models compared with traditional ML?

- [ ] A) It changes from important to even more important
- [ ] B) It changes from unimportant to optional
- [ ] C) It remains unimportant in both cases
- [ ] D) It changes from even more important to unimportant

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** Table 1-4 lists inference optimization as “Important” for traditional ML and “Even more important” for foundation models.

### Question 106: According to the source, in traditional ML engineering where teams...

According to the source, in traditional ML engineering where teams build applications using their proprietary models, what is the differentiation?

- [ ] A) Model quality
- [ ] B) The application development process
- [ ] C) Prompt engineering
- [ ] D) The AI interface

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that with traditional ML engineering, model quality is a differentiation.

### Question 107: With foundation models, where many teams use the same model, how mu...

With foundation models, where many teams use the same model, how must differentiation be gained?

- [ ] A) Through proprietary model quality
- [ ] B) Through the application development process
- [ ] C) Through model architecture choices
- [ ] D) Through data labeling

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says that with foundation models, differentiation must be gained through the application development process.

### Question 108: Which responsibilities make up the application development layer?

Which responsibilities make up the application development layer?

- [ ] A) Evaluation, prompt engineering, and AI interface
- [ ] B) Training, deployment, and monitoring
- [ ] C) Data collection, labeling, and feature engineering
- [ ] D) Model architecture, optimization, and serving

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists evaluation, prompt engineering, and AI interface as the responsibilities of the application development layer.

### Question 109: According to the source, when is evaluation necessary in the model...

According to the source, when is evaluation necessary in the model adaptation process?

- [ ] A) Only after deployment
- [ ] B) Only before selecting a model
- [ ] C) Throughout the whole model adaptation process
- [ ] D) Only when using foundation models

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source states evaluation is necessary throughout the whole model adaptation process, including model selection, benchmarking progress, deployment readiness, and production issue detection.

### Question 110: Why does the source say evaluation is even more important with foun...

Why does the source say evaluation is even more important with foundation models?

- [ ] A) Foundation models always have clear ground truths
- [ ] B) Foundation models’ open-ended nature and expanded capabilities make evaluation challenging
- [ ] C) Foundation models require no benchmarking
- [ ] D) Foundation models cannot be used in production

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says the challenges of evaluating foundation models chiefly arise from their open-ended nature and expanded capabilities.

### Question 111: What does the Gemini MMLU example illustrate about evaluation?

What does the Gemini MMLU example illustrate about evaluation?

- [ ] A) A model’s performance can vary greatly depending on the prompt engineering or adaptation technique used
- [ ] B) ChatGPT and Gemini always perform identically with the same number of examples
- [ ] C) MMLU is only useful for chatbots
- [ ] D) Prompt engineering does not affect benchmark results

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source uses the Gemini example to show that different prompts can cause models to perform very differently, such as Gemini Ultra’s MMLU performance changing from 83.7% to 90.04%.

### Question 112: How does the source define prompt engineering?

How does the source define prompt engineering?

- [ ] A) Changing model weights to improve behavior
- [ ] B) Getting AI models to express desirable behaviors from the input alone without changing model weights
- [ ] C) Building an exhaustive list of ground truths for every prompt
- [ ] D) Replacing evaluation with benchmark claims

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source defines prompt engineering as getting AI models to express desirable behaviors from the input alone, without changing the model weights.

### Question 113: According to the text, what does "AI interface" refer to?

According to the text, what does "AI interface" refer to?

- [ ] A) Creating an interface for end users to interact with AI applications
- [ ] B) Training foundation models from scratch
- [ ] C) Embedding fraud detection into payment products
- [ ] D) Collecting user feedback through surveys

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The section defines AI interface as creating an interface for end users to interact with AI applications.

### Question 114: Before foundation models, which organizations could develop AI appl...

Before foundation models, which organizations could develop AI applications?

- [ ] A) Only organizations with sufficient resources to develop AI models
- [ ] B) Any individual developer with a browser extension
- [ ] C) Only open-source communities
- [ ] D) Only organizations using chat interfaces

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that before foundation models, only organizations with sufficient resources to develop AI models could develop AI applications.

### Question 115: Which AI interface is described as the most commonly used?

Which AI interface is described as the most commonly used?

- [ ] A) Voice-based interface
- [ ] B) Embodied interface
- [ ] C) Chat interface
- [ ] D) Browser extension

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says that while the chat interface is the most commonly used, AI interfaces can also be voice-based or embodied.

### Question 116: According to Table 1-6, which category is rated “More important” fo...

According to Table 1-6, which category is rated “More important” for building with foundation models than for building with traditional ML?

- [ ] A) AI interface
- [ ] B) Prompt engineering
- [ ] C) Evaluation
- [ ] D) Data collection

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The table lists Evaluation as “Important” for traditional ML and “More important” for foundation models.

### Question 117: What change in AI tooling is described as a result of the rising im...

What change in AI tooling is described as a result of the rising importance of interfaces?

- [ ] A) Tooling has become exclusively Python-centric.
- [ ] B) There is increasing support for JavaScript APIs alongside Python.
- [ ] C) Frontend engineers are no longer targeted by AI tooling.
- [ ] D) ML frameworks have stopped supporting Python APIs.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says Python remains popular, but there is increasing support for JavaScript APIs such as LangChain.js, Transformers.js, OpenAI’s Node library, and Vercel’s AI SDK.

### Question 118: According to the section, where are more AI engineers increasingly...

According to the section, where are more AI engineers increasingly coming from?

- [ ] A) Only traditional ML backgrounds
- [ ] B) Web development or full-stack backgrounds
- [ ] C) Only academic research backgrounds
- [ ] D) Only frontend design backgrounds

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that while many AI engineers come from traditional ML backgrounds, more are increasingly coming from web development or full-stack backgrounds.

### Question 119: According to Table 1-6, what is the status of prompt engineering wh...

According to Table 1-6, what is the status of prompt engineering when building with traditional ML?

- [ ] A) Important
- [ ] B) More important
- [ ] C) Less important
- [ ] D) Not applicable

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** D

    **Explanation:** The table marks prompt engineering as “Not applicable” for building with traditional ML and “Important” for building with foundation models.

### Question 120: According to the source, what advantage do full-stack engineers hav...

According to the source, what advantage do full-stack engineers have over traditional ML engineers?

- [ ] A) They can avoid using foundation models entirely.
- [ ] B) They can quickly turn ideas into demos, get feedback, and iterate.
- [ ] C) They focus only on gathering data and training models.
- [ ] D) They rarely get involved in product decisions.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that full-stack engineers’ advantage is their ability to quickly turn ideas into demos, get feedback, and iterate.

### Question 121: In the new AI engineering workflow described in the source, what be...

In the new AI engineering workflow described in the source, what becomes possible with AI models readily available today?

- [ ] A) Building the product first and investing in data and models only once the product shows promise.
- [ ] B) Training a model first and building the product last.
- [ ] C) Avoiding product feedback until after model training is complete.
- [ ] D) Separating model development from product development entirely.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says that with AI models readily available, it is possible to start with building the product first and invest in data and models once the product shows promise.

### Question 122: What does the chapter summary say about the current stage of AI eng...

What does the chapter summary say about the current stage of AI engineering?

- [ ] A) It has already reached its final stage, with few innovations remaining.
- [ ] B) It is still in the early stages, with countless more innovations yet to be built.
- [ ] C) It is no longer related to ML engineering in any way.
- [ ] D) It has eliminated the need for a framework to navigate new updates.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The summary states that despite many AI applications already in production, we are still in the early stages of AI engineering, with countless more innovations yet to be built.

### Question 123: According to the source, how does AI engineering relate to ML engin...

According to the source, how does AI engineering relate to ML engineering?

- [ ] A) AI engineering evolved out of ML engineering, and many ML engineering principles are still applicable.
- [ ] B) AI engineering is completely unrelated to ML engineering.
- [ ] C) ML engineering evolved out of AI engineering and replaces all its principles.
- [ ] D) AI engineering applies only to consumer applications, while ML engineering applies only to enterprises.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says AI engineering evolved out of ML engineering, which is the overarching discipline for building applications with all ML models, and that many ML engineering principles still apply.
