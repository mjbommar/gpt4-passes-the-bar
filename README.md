## GPT-4 Passes the Bar Exam
==================
  * __N.B.__: This is a preprint. 
  *  __Title__: GPT-4 Passes the Bar
  *  __Authors__: Daniel Martin Katz, Michael James Bommarito, Shang Gao, Pablo David Arredondo 
  * __Publication URL__: [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4389233), arXiv pending 
  * __Publication Date__: 2023-03-16

### Table of Contents

* [Abstract](#abstract)

### Abstract

In this paper, we experimentally evaluate the zero-shot performance of a preliminary version of GPT-4 against prior 
generations of GPT on the entire Uniform Bar Examination (UBE), including not only the multiple-choice Multistate Bar 
Examination (MBE), but also the open-ended Multistate Essay Exam (MEE) and Multistate Performance Test (MPT) 
components. On the MBE, GPT-4 significantly outperforms both human test-takers and prior models, demonstrating a 26% 
increase over ChatGPT and beating humans in five of seven subject areas. On the MEE and MPT, which have not previously 
been evaluated by scholars, GPT-4 scores an average of 4.2/6.0 as compared to much lower scores for ChatGPT. Graded 
across the UBE components, in the manner in which a human tast-taker would be, GPT-4 scores approximately 297 points, 
significantly in excess of the passing threshold for all UBE jurisdictions. These findings document not just the rapid
and remarkable advance of large language model performance generally, but also the potential for such models to support
the delivery of legal services in society.

### Preprint
This paper is a preprint and has not been peer-reviewed.  It was prepared during the preliminary testing period for 
GPT-4, and the results will be updated as additional testing with the generally-available models is completed.

### Data
A detailed data page is provided for each component of the Uniform Bar Exam (UBE).
 * [MBE](data/MBE.md)
 * [MEE](data/MEE.md)
 * [MPT](data/MPT.md)

While the exams themselves are generally protected by copyright and we do not reproduce them here, the interested reader
can follow the links on each page to purchase all required data for under 200 USD.


### Source
The source code for this paper is organized as follows:
  * `src/engines/`: abstraction layer for LLMs, e.g., chat vs non-chat completion API, T5, etc.
  * `src/exams/`: the exam runner and scoring for multiple-choice and open-ended exams
  * `publication/`: tables and figures from the paper

You must place an `.openai_key` file in the current working directory or the `src/engines/` folder with the key
for execution.  

**N.B.**: You almost certainly will need to change the list of models to run experiments, and most users will not have
access to the same models tested in the initial release of this paper.  Your results will obviously vary due to the 
stochastic nature of the model, but this introduces an additional source of variation to consider.

Exams can be run with `src/run_experiment.py` like this:
```shell
# MBE
$ poetry run python3 src/run_experiment.py --exam-type mbe --exam-id ncbe-pdf-002 --experiment-id 1

# MEE
$ poetry run python3 src/run_experiment.py --exam-type mee --exam-id ncbe-pdf-001 --experiment-id 2
```

Model IDs and parameters are set in the `src/run_experiment.py` module.  To add or change the model list, 
alter the `MODEL_SET` variable in the `run_experiment.py` module. 

Results can be analyzed with `src/analyze_results.py` like this:
```shell
# multiple-choice
$ poetry run python3 src/score_experiment.py --exam-type mbe --exam-id ncbe-pdf-002 --experiment-id 1

# essays
$ poetry run python3 src/summarize_essay_experiment.py --exam-type mee --exam-id ncbe-pdf-001 --experiment-id 1
```

### Results
The results from experiments are available for each component:
  * MBE: `results/mbe/`
  * MEE: `results/mee/`
  * MPT: `results/mpt/`

