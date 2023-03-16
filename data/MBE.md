## GPT-4 Passes the Bar Exam
### MBE Data

#### Summary
The Multistate Bar Exam, also known as the MBE, is the multiple-choice component of the Uniform Bar Exam.  It consists 
of 200 questions, each with four possible answers, and is used to scale the scores of other components of the exam.

#### Data Source
As in prior work, we use only MBE questions designed by the National Conference of Bar Examiners (NCBE).  The NCBE
is the organization responsible for designing the UBE and advising state bars on their exams, and so these are the 
most realistic, official questions available.  MBE exams can be purchased directly from the NCBE or through its 
resellers.

In the current release of this paper, we present only the results for the most-recent MBE released by the NCBE.
This exam was released [by the NCBE in December 2021]((https://www.ncbex.org/news/mbe-complete-practice-exam-release/))
and is currently available for purchase from the NCBE's authorized reseller, [JD Advising](https://jdadvising.com/product/200-mbe-question-exam-2022/).

In prior work, we tested and fine-tuned on different NCBE exams or simulations.  Compiled results for all exams may
be provided in future releases of this paper, and links to those exams will be separately provided at that time.

#### Data Formatting
The MBE questions are provided in a text PDF file.  We extracted the questions and answer key directly from the PDF and
reviewed these for errors.  We then converted each question to a structured record with the following fields:
* Question Number: the sequence number of the question in the exam
* Question Category: the subject area of the question, if provided; otherwise, manually coded by the authors.  This field is used only for analysis of results and not provided to the model.
* Question Prompt: the "body" of the question, up to the multiple choice options
* Choice A: the first multiple choice option
* Choice B: the second multiple choice option
* Choice C: the third multiple choice option
* Choice D: the fourth multiple choice option
* Correct Answer: the correct letter answer to the question, as provided by the NCBE

Both CSV and JSON are supported for replication, but the original MBE results in prior work and this publication were
prepared and reviewed in CSV like this:
```
question_category,question_number,correct_answer,question_prompt,choice_a,choice_b,choice_c,choice_d
Civil Procedure,1,C,"A shareholder of a car [...]", Where the [...],Where the [...],Where the [...],Where the [...].
```
