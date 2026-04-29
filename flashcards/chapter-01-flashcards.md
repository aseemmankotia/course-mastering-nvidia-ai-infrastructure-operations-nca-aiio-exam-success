## Chapter 1: The AI Revolution: Foundations of Modern Intelligence — Flashcards

| # | Front (Question) | Back (Answer) |
|---|-----------------|---------------|
| 1 | What is Artificial Intelligence (AI)? | The broad field of computer science focused on creating systems that can perform tasks requiring human-like intelligence, such as reasoning, learning, and decision-making |
| 2 | How does Machine Learning differ from Traditional Programming? | Traditional programming uses explicit rules written by humans; ML systems learn patterns from data to make predictions without being explicitly programmed |
| 3 | What is Deep Learning and how does it relate to ML? | Deep Learning is a subset of ML that uses neural networks with multiple layers (deep architectures) to automatically learn hierarchical representations from data |
| 4 | What is the AI hierarchy from broadest to most specific? | AI → Machine Learning → Deep Learning (DL is a subset of ML, which is a subset of AI) |
| 5 | What is Training in AI workflows? | The resource-intensive process of teaching a model by exposing it to large datasets, adjusting weights/parameters to minimize errors |
| 6 | What is Inference in AI workflows? | Using a trained model to make predictions on new, unseen data; requires far fewer computational resources than training |
| 7 | Why do GPUs accelerate AI workloads better than CPUs? | GPUs have thousands of smaller cores optimized for parallel processing, ideal for matrix operations in neural networks; CPUs have fewer cores optimized for sequential tasks |
| 8 | How many cores typically exist in a CPU vs GPU? | CPUs: 4-64 cores optimized for complex sequential tasks; GPUs: thousands of cores (e.g., 10,000+) optimized for simple parallel operations |
| 9 | When should you use a CPU over a GPU? | For tasks requiring complex logic, branching decisions, low-latency single-threaded operations, or when workloads are not parallelizable |
| 10 | Name three industries leveraging AI and their use cases | Healthcare: medical imaging/diagnosis; Automotive: autonomous driving; Finance: fraud detection and algorithmic trading |
| 11 | What are key factors driving enterprise AI adoption? | Availability of big data, improved GPU computing power, cloud accessibility, open-source frameworks, and proven ROI in business applications |
| 12 | What is data mining in the context of AI? | The process of discovering patterns, correlations, and insights from large datasets using statistical and computational techniques |
| 13 | Why does training require far more resources than inference? | Training processes entire datasets multiple times (epochs), calculates gradients, and updates millions/billions of parameters; inference only performs forward passes |
| 14 | What type of mathematical operations make GPUs ideal for deep learning? | Matrix multiplications and tensor operations, which can be parallelized across thousands of GPU cores simultaneously |
| 15 | What is the role of data visualization in AI projects? | To explore data distributions, identify patterns/anomalies, communicate insights to stakeholders, and validate model performance |

### Key Terms

| Term | Definition |
|------|-----------|
| Artificial Intelligence | Broad field creating systems that simulate human intelligence capabilities |
| Machine Learning | Subset of AI where systems learn patterns from data rather than following explicit rules |
| Deep Learning | Subset of ML using multi-layer neural networks to learn hierarchical data representations |
| Training | Process of teaching a model by iteratively adjusting parameters using large datasets |
| Inference | Using a trained model to generate predictions on new data |
| Parallel Processing | Simultaneous execution of multiple calculations, enabling GPU acceleration of AI workloads |
| Epoch | One complete pass through the entire training dataset |
| Data Mining | Extracting patterns and insights from large datasets using computational methods |

### Memory Tricks
- **"AI-ML-DL Nesting Dolls"**: Picture Russian nesting dolls—AI is the largest, ML fits inside it, DL is the smallest inside ML
- **"Training = Teacher, Inference = Test"**: Training is like studying (resource-heavy), Inference is like taking the exam (quick application)
- **"GPU = Grocery store checkout"**: GPUs are like 1000 cashiers handling simple transactions simultaneously; CPUs are like 8 expert accountants handling complex individual cases
- **"THAI drives AI"**: **T**echnology advances, **H**uge data availability, **A**ffordable cloud compute, **I**ndustry ROI proof = factors driving enterprise adoption