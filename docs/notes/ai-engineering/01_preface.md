# Preface

---

## The ChatGPT Surprise
- Scaling models to improve them was known long before ChatGPT, noted by AlexNet in 2012.
- What surprised the author was the sheer number of applications the capability boost unlocked.
- A small gain in model quality metrics produced an explosion of new possibilities.
- New capabilities raised demand for AI applications and lowered the entry barrier for developers.

---

## Old Foundations, New Scale
- AI adoption looks new but builds on techniques that have been around for a while.
- Language modeling papers appeared as early as the 1950s.
- RAG builds on retrieval technology that powered search and recommender systems long before the term existed.
- Traditional ML best practices—systematic experimentation, rigorous evaluation, optimization—still apply to foundation models.

---

## What the Book Covers
- Familiar, easy-to-use techniques can mislead people into thinking nothing is new in AI engineering.
- Improved model scale and capabilities introduce opportunities and challenges requiring new solutions.
- The book covers the end-to-end process of adapting foundation models to solve real-world problems.
- It draws on notes from over 100 conversations and interviews with researchers, framework developers, executives, and developers.

---

## What This Book Is About
- Provides a framework for adapting foundation models, including LLMs and LMMs, to specific applications.
- Outlines solutions and questions to evaluate the best solution for your needs.
- Helps answer questions about building, evaluating, hallucination, prompt engineering, RAG, agents, finetuning, data, speed/cost/security, feedback loops.
- Helps navigate AI landscape: model types, evaluation benchmarks, use cases, application patterns.

---

## Approach and Companion Reading
- Content illustrated with case studies, references, and expert review; draws on decade of language-model and ML-systems experience.
- Focuses on fundamentals of AI engineering instead of specific tools or APIs, which become outdated quickly.
- AIE can companion DMLS: DMLS covers traditional ML; AIE covers foundation models.
- Both books are self-contained and modular; real-world systems often involve both traditional ML and foundation models.

---

## What This Book Is Not

- Not a tutorial: mentions tools and pseudocode, but does not teach tool usage.
- Offers a framework for selecting tools, including trade-offs and evaluation questions.
- Tutorials for specific tools are easy to find online; AI chatbots help with popular tools.
- Not an ML theory book: no explanation of neural networks or training models from scratch.

---

## Practical Focus and Assumed Background

- A practical book focused on building successful AI applications for real-world problems.
- Explains theoretical concepts only when immediately relevant to the discussion.
- Foundation model applications are possible without ML expertise, but basics help.
- No prior ML background required; probabilistic concepts like sampling and distribution help.

---

## How the Book Approaches Problems

- Favors a start-simple approach, progressing to more complex solutions as challenges rise.
- Draws on an extensive network of researchers and engineers for important problems and solutions.
- Occasionally relies on Lindy's Law: future life expectancy proportional to current age.
- Some temporary concepts included when immediately useful or illustrative of problem-solving.

---

## Who This Book Is For
- For anyone who wants to leverage foundation models to solve real-world problems
- This is a technical book, geared toward technical roles
- Includes AI engineers, ML engineers, data scientists, engineering managers, technical product managers
- Relevant if you relate to one of the scenarios described next

---

## Scenarios That Fit
- Building or optimizing an AI application, from scratch or beyond the demo phase
- Facing hallucinations, security, latency, or costs and needing targeted solutions
- Wanting to streamline your team's AI development to be more systematic, faster, reliable
- Wanting to understand how your organization can leverage foundation models to improve the bottom line

---

## Background and Additional Readers
- Background concepts include supervision, self-supervision, log-likelihood, gradient descent, backpropagation, loss functions, hyperparameter tuning
- Architectures include feedforward, recurrent, and transformer networks
- Metrics include accuracy, F1, precision, recall, cosine similarity, cross entropy
- Also for tool developers seeking underserved areas and researchers wanting to understand AI use cases

---

## Navigating the Book
- Book follows typical AI application development process; modular, skip familiar sections.
- Audience: job candidates and those understanding AI capabilities/limitations.
- Technical sections flagged; readers can skip if too detailed.
- Chapter 1: decide if AI application is necessary and if AI is needed.

---

## Foundation Models and Evaluation
- Chapter 2: foundation model workings, design decisions, generation settings, and behaviors like hallucinations.
- Evaluation is hardest challenge; Chapters 3-4 cover methods and systematic pipeline.
- Response quality depends on instructions, context, and model itself.
- Chapters 5-6 optimize instructions and context: prompt engineering and RAG/agentic patterns.

---

## Finetuning, Data, Inference, and End-to-End
- Chapter 7: finetuning approaches, memory-intensive, model merging, memory footprint calculation.
- Chapter 8: data acquisition, annotation, synthesis, processing, and quality evaluation.
- Chapter 9: inference optimization for cheaper/faster at model and service levels.
- Chapter 10: end-to-end application and user feedback system design.

---

## Typographical Conventions

- *Italic* marks new terms, URLs, email addresses, filenames, and file extensions.
- Constant width is used for program listings and program elements within paragraphs.
- Constant width bold shows commands or text the user should type literally.
- Constant width italic shows text replaced with user-supplied or context-determined values.

---

## Constant Width in Paragraphs

- Program elements include variable and function names, databases, and data types.
- Also covers environment variables, statements, input prompts into models, and keywords.
- Bold constant width signals literal typing by the user.
- Italic constant width signals values supplied by the user or context.

---

## Supplemental Code and Resources
- Code examples and exercises are downloadable from the book’s GitHub repository.
- Repository URL: https://github.com/chiphuyen/aie-book
- It includes important papers, helpful tools, and topics too deep for the book.
- Behind-the-scenes information and statistics about writing the book are also included.

---

## Getting Help
- For technical questions or problems using the code examples, contact O’Reilly support.
- Email: support@oreilly.com

---

## Callout Conventions
- TIP marks a tip or suggestion.
- NOTE marks a general note.
- WARNING indicates a warning or caution.

---

## Using Example Code
- You may use example code in your programs and documentation without contacting O'Reilly.
- No permission needed unless reproducing a significant portion of the code.
- Selling or distributing examples from O'Reilly books does require permission.
- Quoting code to answer a question does not require permission.

---

## Attribution and Permissions
- Attribution is appreciated but generally not required.
- Typical attribution includes title, author, publisher, and ISBN.
- Example: "AI Engineering by Chip Huyen (O'Reilly), Copyright 2025 Developer Experience Advisory LLC, 978-1-098-16630-4."
- Contact permissions@oreilly.com if use falls outside fair use or stated permission.

---

## O'Reilly Online Learning
- For more than 40 years, O'Reilly Media has provided technology and business training.
- Its knowledge and insight help companies succeed.

---

## How to Contact Us

## Publisher Contact Details
- O’Reilly Media, Inc.
- 1005 Gravenstein Highway North, Sebastopol, CA 95472
- US/Canada: 800-889-8969; international/local: 707-827-7019
- Fax: 707-829-0104

## Online and Email Contacts
- Email: support@oreilly.com
- Contact page: https://oreilly.com/about/contact.html
- Address comments and questions about the book to the publisher

## O’Reilly Learning Platform
- Experts share knowledge through books, articles, and the online learning platform
- On-demand access to live training courses and in-depth learning paths
- Interactive coding environments included
- Vast collection of text and video from O’Reilly and 200+ publishers

---

## Book Resources and Contact
- Errata, examples, and additional information available at oreil.ly/aiengineering.
- O'Reilly news and courses at oreilly.com.
- Find O'Reilly on LinkedIn and YouTube.

---

## Acknowledgments: Technical Reviewers
- Tight timeline: two years for a 150,000-word book covering much ground.
- Luke Metz checked assumptions; Han-chung Lee pointed to missed resources.
- Vittorio Cretella and Andrei Lopatenko gave technical and executive feedback.
- Vicki Reyzelman grounded content for software engineering readers.

---

## Acknowledgments: Contributors and Team
- Eugene Yan, Shawn Wang, Sanyam Bhutani offered support, vibe check, and detailed feedback.
- Kyle Kranen and Mark Saroufim guided finetuning and efficiency chapters.
- Many others contributed examples on AI platforms, evaluation, architecture, and product perspectives.
- O'Reilly team (Melissa Potter, Corbin Collins, Jill Leonard, Elizabeth Kelly, Liz Wheeler, Nicole Butterfield) supported the book.

## Practice Questions

### Question 1: According to the preface, what surprised the author most when ChatG...

According to the preface, what surprised the author most when ChatGPT came out?

- [ ] A) The model's size and capabilities
- [ ] B) The sheer number of applications the capability boost unlocked
- [ ] C) The speed at which the model was trained
- [ ] D) The number of researchers who worked on it

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The author states that what surprised him wasn't the model's size or capabilities but "the sheer number of applications this capability boost unlocked."

### Question 2: According to the preface, what did the AlexNet authors note in thei...

According to the preface, what did the AlexNet authors note in their landmark 2012 paper?

- [ ] A) That scaling up a model rarely improves it
- [ ] B) That results can be improved simply by waiting for faster GPUs and bigger datasets
- [ ] C) That language modeling techniques date back to the 1950s
- [ ] D) That AI applications can be built without writing code

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The preface quotes the AlexNet paper: "All of our experiments suggest that our results can be improved simply by waiting for faster GPUs and bigger datasets to become available."

### Question 3: According to the preface, which of the following is true about the...

According to the preface, which of the following is true about the history of AI techniques?

- [ ] A) Papers about language modeling came out as early as the 1950s
- [ ] B) Retrieval-augmented generation was invented before search engines
- [ ] C) Foundation models introduced entirely new deployment best practices
- [ ] D) AI engineering techniques have no connection to traditional machine learning

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The preface states that "papers about language modeling came out as early as the 1950s," and that RAG builds on retrieval technology that long predates the term RAG.

### Question 4: Which best practices for traditional machine learning applications...

Which best practices for traditional machine learning applications does the preface say still apply to foundation model-based applications?

- [ ] A) Avoiding systematic experimentation and evaluation
- [ ] B) Systematic experimentation, rigorous evaluation, and relentless optimization for faster and cheaper models
- [ ] C) Building applications without writing any code
- [ ] D) Waiting for bigger datasets before deploying any model

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The preface says these traditional best practices "are still the best practices for working with foundation model-based applications."

### Question 5: According to the source, what is the primary purpose of the book?

According to the source, what is the primary purpose of the book?

- [ ] A) To provide a framework for adapting foundation models, including LLMs and LMMs, to specific applications
- [ ] B) To provide a complete guide to building traditional ML models using tabular data and feature engineering
- [ ] C) To survey the history of AI and predict which specific tools and APIs will last
- [ ] D) To replace Designing Machine Learning Systems with a tool-specific tutorial

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that the book provides a framework for adapting foundation models, which include both LLMs and LMMs, to specific applications.

### Question 6: Why does the book focus on fundamentals of AI engineering instead o...

Why does the book focus on fundamentals of AI engineering instead of any specific tool or API?

- [ ] A) Because specific tools and APIs are not useful for building AI applications
- [ ] B) Because tools become outdated quickly, while fundamentals should last longer
- [ ] C) Because the book only covers traditional ML models and not foundation models
- [ ] D) Because the book is intended only for readers who have already read DMLS

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says the book focuses on fundamentals instead of any specific tool or API because tools become outdated quickly, but fundamentals should last longer.

### Question 7: How does the source describe the difference in focus between AIE an...

How does the source describe the difference in focus between AIE and DMLS?

- [ ] A) AIE focuses on traditional ML models, while DMLS focuses on foundation models
- [ ] B) AIE focuses on foundation models with prompt engineering, context construction, and parameter-efficient finetuning, while DMLS focuses on traditional ML models with tabular data annotations, feature engineering, and model training
- [ ] C) AIE and DMLS both focus exclusively on foundation models and prompt engineering
- [ ] D) AIE focuses only on evaluation benchmarks, while DMLS focuses only on agents

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says DMLS focuses on traditional ML models involving tabular data annotations, feature engineering, and model training, while AIE focuses on foundation models involving prompt engineering, context construction, and parameter-efficient finetuning.

### Question 8: Which statement about reading AIE with DMLS is supported by the sou...

Which statement about reading AIE with DMLS is supported by the source?

- [ ] A) AIE and DMLS are both self-contained and modular, so you can read either book independently
- [ ] B) Readers must read DMLS before they can understand AIE
- [ ] C) DMLS covers every topic in AIE in greater detail
- [ ] D) AIE and DMLS are not related and share no concepts

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that both books are self-contained and modular, so you can read either book independently, and AIE can be a companion to DMLS.

### Question 9: According to the text, what is this book not?

According to the text, what is this book not?

- [ ] A) A tutorial
- [ ] B) A framework for selecting tools
- [ ] C) A practical book about AI applications
- [ ] D) A discussion of trade-offs between solutions

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text explicitly says, “This book isn’t a tutorial.” It says the book offers a framework for selecting tools rather than teaching how to use a tool.

### Question 10: What does the book offer instead of teaching you how to use a speci...

What does the book offer instead of teaching you how to use a specific tool?

- [ ] A) A step-by-step tutorial for popular tools
- [ ] B) A framework for selecting tools
- [ ] C) A complete ML theory course
- [ ] D) Instructions for building and training a model from scratch

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says the book “offers a framework for selecting tools” and discusses trade-offs and questions to ask when evaluating a solution.

### Question 11: What does the text say about ML theory in this book?

What does the text say about ML theory in this book?

- [ ] A) It explains what a neural network is and how to build one from scratch
- [ ] B) It is an ML theory book focused on training models
- [ ] C) It is not an ML theory book, though it explains relevant theoretical concepts
- [ ] D) It avoids all theoretical concepts

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text says the book “isn’t an ML theory book” and doesn’t explain what a neural network is or how to build and train a model from scratch, but it explains theoretical concepts immediately relevant to the discussion.

### Question 12: According to the text, Lindy’s Law infers that the future life expe...

According to the text, Lindy’s Law infers that the future life expectancy of a technology is proportional to what?

- [ ] A) Its current age
- [ ] B) Its complexity
- [ ] C) Its popularity among researchers
- [ ] D) Its number of available tutorials

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text states that Lindy’s Law infers “the future life expectancy of a technology is proportional to its current age.”

### Question 13: According to the source, which of the following is listed as a neur...

According to the source, which of the following is listed as a neural network architecture covered in the book?

- [ ] A) Convolutional only
- [ ] B) Feedforward, recurrent, and transformer
- [ ] C) Reinforcement learning and clustering
- [ ] D) Decision trees and random forests

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source lists feedforward, recurrent, and transformer as the neural network architectures covered.

### Question 14: The source states that the book is intended for readers who want to...

The source states that the book is intended for readers who want to do what?

- [ ] A) Only pursue academic research in ML theory
- [ ] B) Leverage foundation models to solve real-world problems
- [ ] C) Build hardware accelerators for training
- [ ] D) Avoid production deployment entirely

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The "Who This Book Is For" section opens by saying the book is for anyone who wants to leverage foundation models to solve real-world problems.

### Question 15: Which scenario does the source give as a reason the book is for you?

Which scenario does the source give as a reason the book is for you?

- [ ] A) You are facing issues like hallucinations, security, latency, or costs and need targeted solutions
- [ ] B) You want to design new programming languages
- [ ] C) You are studying for a medical licensing exam
- [ ] D) You want to learn accounting standards

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source lists facing hallucinations, security, latency, or cost issues as one scenario where the book applies.

### Question 16: Which group does the source say can also benefit from the book?

Which group does the source say can also benefit from the book?

- [ ] A) Only undergraduate students in linguistics
- [ ] B) Tool developers who want to identify underserved areas in AI engineering
- [ ] C) Professional athletes seeking training plans
- [ ] D) Hardware manufacturers of display panels

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source names tool developers seeking underserved areas in AI engineering as an additional group that can benefit.

### Question 17: According to “Navigating This Book,” which chapters are dedicated t...

According to “Navigating This Book,” which chapters are dedicated to evaluation methods and building a reliable evaluation pipeline?

- [ ] A) Chapters 1 and 2
- [ ] B) Chapters 3 and 4
- [ ] C) Chapters 5 and 6
- [ ] D) Chapters 8 and 9

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says the book dedicates two chapters, Chapters 3 and 4, to evaluation methods and creating a systematic evaluation pipeline.

### Question 18: What two major application patterns for context construction does C...

What two major application patterns for context construction does Chapter 6 discuss?

- [ ] A) Prompt engineering and prompt attacks
- [ ] B) RAG and agentic patterns
- [ ] C) Finetuning and model merging
- [ ] D) Data acquisition and data synthesis

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that Chapter 6 zooms into two major application patterns for context construction: RAG and agentic.

### Question 19: What does Chapter 9 cover, according to the text?

What does Chapter 9 cover, according to the text?

- [ ] A) Making inference cheaper and faster through optimization at the model level and inference service level
- [ ] B) Evaluating data quality and data annotations
- [ ] C) Designing a user feedback system for an end-to-end application
- [ ] D) Understanding how a foundation model is made and aligned to human preference

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says Chapter 9 is about making inference cheaper and faster and discusses optimization both at the model level and inference service level.

### Question 20: According to the conventions section, what does italic text indicate?

According to the conventions section, what does italic text indicate?

- [ ] A) Commands or text the user should type literally
- [ ] B) New terms, URLs, email addresses, filenames, and file extensions
- [ ] C) Text to be replaced with user-supplied values
- [ ] D) Program listings and program elements

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that italic indicates new terms, URLs, email addresses, filenames, and file extensions.

### Question 21: What is constant width used for in this book?

What is constant width used for in this book?

- [ ] A) Only for commands typed literally by the user
- [ ] B) Only for new terms and URLs
- [ ] C) Program listings and, within paragraphs, program elements such as variable or function names, databases, data types, environment variables, statements, input prompts into models, and keywords
- [ ] D) Text that should be replaced with user-supplied values or context-determined values

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says constant width is used for program listings and for program elements such as variable or function names, databases, data types, environment variables, statements, input prompts into models, and keywords.

### Question 22: What does constant width italic show?

What does constant width italic show?

- [ ] A) Text that should be replaced with user-supplied values or by values determined by context
- [ ] B) Commands or other text that should be typed literally by the user
- [ ] C) New terms, URLs, email addresses, filenames, and file extensions
- [ ] D) Program listings that should be typed exactly as shown

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source states that constant width italic shows text that should be replaced with user-supplied values or by values determined by context.

### Question 23: Where can readers download the supplemental material, such as code...

Where can readers download the supplemental material, such as code examples and exercises, for this book?

- [ ] A) From a mailing list run by support@oreilly.com
- [ ] B) From the GitHub repository at https://github.com/chiphuyen/aie-book
- [ ] C) From a companion site hosted by the publisher's bookstore
- [ ] D) From the author's personal blog

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that supplemental material is available for download at https://github.com/chiphuyen/aie-book.

### Question 24: According to the text, what does the GitHub repository contain besi...

According to the text, what does the GitHub repository contain besides code examples and exercises?

- [ ] A) Only the book's full manuscript in draft form
- [ ] B) Additional resources such as important papers, helpful tools, deeper topics, and behind-the-scenes information about writing the book
- [ ] C) A discussion forum moderated by O'Reilly editors
- [ ] D) Video lectures and graded quizzes

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says the repository contains additional resources including important papers and helpful tools, topics too deep for the book, and behind-the-scenes information and statistics about the book.

### Question 25: What should you do if you have a technical question or a problem us...

What should you do if you have a technical question or a problem using the code examples?

- [ ] A) Open an issue on the GitHub repository
- [ ] B) Send email to support@oreilly.com
- [ ] C) Contact the author through social media
- [ ] D) Consult the WARNING elements in the book

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text instructs readers with technical questions or problems using the code examples to send email to support@oreilly.com.

### Question 26: In this book's formatting conventions, what does a WARNING element...

In this book's formatting conventions, what does a WARNING element indicate?

- [ ] A) A tip or suggestion
- [ ] B) A general note
- [ ] C) A warning or caution
- [ ] D) A link to downloadable code

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text defines the WARNING element as one that indicates a warning or caution.

### Question 27: According to the text, which use of example code from this book doe...

According to the text, which use of example code from this book does NOT require permission?

- [ ] A) Writing a program that uses several chunks of code from the book
- [ ] B) Selling examples from O’Reilly books
- [ ] C) Distributing examples from O’Reilly books
- [ ] D) Incorporating a significant amount of example code into your product’s documentation

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says writing a program that uses several chunks of code from the book does not require permission.

### Question 28: According to the text, which action DOES require permission?

According to the text, which action DOES require permission?

- [ ] A) Answering a question by citing the book and quoting example code
- [ ] B) Writing a program that uses several chunks of code from the book
- [ ] C) Selling or distributing examples from O’Reilly books
- [ ] D) Using example code in your programs and documentation generally

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text states that selling or distributing examples from O’Reilly books does require permission.

### Question 29: What does the text say about attribution for use of example code?

What does the text say about attribution for use of example code?

- [ ] A) It is always required.
- [ ] B) It is appreciated but generally not required.
- [ ] C) It is required only when selling examples.
- [ ] D) It is not allowed.

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text says “We appreciate, but generally do not require, attribution.”

### Question 30: According to the text, what can you do at https://oreilly.com?

According to the text, what can you do at https://oreilly.com?

- [ ] A) Sign up for a free print subscription to O'Reilly books
- [ ] B) Get on-demand access to live training courses, learning paths, interactive coding environments, and a vast collection of text and video
- [ ] C) Contact the book's authors directly for technical support
- [ ] D) Download the book's source code and errata

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text states that O'Reilly's online learning platform gives on-demand access to live training courses, in-depth learning paths, interactive coding environments, and a vast collection of text and video.

### Question 31: How many other publishers' content is available through O'Reilly's...

How many other publishers' content is available through O'Reilly's online learning platform, according to the text?

- [ ] A) 200+
- [ ] B) 100+
- [ ] C) 50+
- [ ] D) 500+

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The text says the platform offers a vast collection of text and video from O'Reilly and 200+ other publishers.

### Question 32: Which phone number does the text list for contacting the publisher...

Which phone number does the text list for contacting the publisher from outside the United States or Canada?

- [ ] A) 800-889-8969
- [ ] B) 707-827-7019
- [ ] C) 707-829-0104
- [ ] D) 800-889-8969 ext. 7019

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The text lists 800-889-8969 for the United States or Canada and 707-827-7019 for international or local calls.

### Question 33: What is the email address given for addressing comments and questio...

What is the email address given for addressing comments and questions concerning the book?

- [ ] A) contact@oreilly.com
- [ ] B) books@oreilly.com
- [ ] C) support@oreilly.com
- [ ] D) publisher@oreilly.com

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The text instructs readers to address comments and questions concerning the book to the publisher, listing support@oreilly.com.

### Question 34: According to the source, where can readers access errata, examples,...

According to the source, where can readers access errata, examples, and additional information for the book?

- [ ] A) https://oreilly.com
- [ ] B) https://oreil.ly/aiengineering
- [ ] C) https://linkedin.com/company/oreilly-media
- [ ] D) https://youtube.com/oreillymedia

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source says the book’s web page lists errata, examples, and additional information at https://oreil.ly/aiengineering.

### Question 35: Who were the first to review the author’s drafts before they were s...

Who were the first to review the author’s drafts before they were sent to the next round of technical reviewers?

- [ ] A) Vittorio Cretella and Andrei Lopatenko
- [ ] B) Luke Metz and Han-chung Lee
- [ ] C) Kyle Kranen and Mark Saroufim
- [ ] D) Melissa Potter and Corbin Collins

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** B

    **Explanation:** The source states that Luke and Han were the first to review the author’s drafts before they went to the next round of technical reviewers.

### Question 36: Which two people are described as having led AI innovation at Fortu...

Which two people are described as having led AI innovation at Fortune 500 companies and provided feedback combining deep technical expertise with executive insights?

- [ ] A) Vittorio Cretella and Andrei Lopatenko
- [ ] B) Eugene Yan and Shawn Wang
- [ ] C) Kittipat “Bot” Kampa and Denys Linkov
- [ ] D) Aileen Bui and Todor Markov

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** A

    **Explanation:** The source says Vittorio Cretella and Andrei Lopatenko had led AI innovation at Fortune 500 companies and gave feedback combining technical expertise with executive insights.

### Question 37: Who not only gave thoughtful written feedback but also recorded vid...

Who not only gave thoughtful written feedback but also recorded videos to explain his feedback?

- [ ] A) Douglas Bailley
- [ ] B) Nutan Sahoo
- [ ] C) Sanyam Bhutani
- [ ] D) Mark Saroufim

??? tip "Reveal Answer & Explanation"
    **Correct Answer:** C

    **Explanation:** The source says Sanyam Bhutani gave thoughtful written feedback and also recorded videos to explain his feedback.
