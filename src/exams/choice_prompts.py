"""
Define multiple choice prompts for the MBE and MPRE.

All methods take as input a dictionary from the questions spreadsheet and return a string.

The dict must contain:
 * question_prompt: the question text
    * choice_a: the text of choice A
    * choice_b: the text of choice B
    * choice_c: the text of choice C
    * choice_d: the text of choice D

TODO: Decide if we want to go deep on further contextual information and zero-shot prompting strats.
"""

def mbe_prompt_001(row: dict) -> str:
    """Generate a prompt from a row of the question spreadsheet."""
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1) :].strip()
    prompt = f"""Act as if you are taking the Bar Exam.\nPlease answer the following question in this rank order format: 
First Choice: <LETTER>

-----
Question: {question_text}
(A) {row["choice_a"].strip()}
(B) {row["choice_b"].strip()}
(C) {row["choice_c"].strip()}
(D) {row["choice_d"].strip()}
-----

Answer: """.strip()

    return prompt


def mbe_prompt_002(row: dict) -> str:
    """Generate a prompt from a row of the question spreadsheet."""
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1) :].strip()
    prompt = f"""Act as if you are taking the Bar Exam.\nPlease answer the following question in this rank order format: 
First Choice: <LETTER>
Second Choice: <LETTER>

-----
Question: {question_text}
(A) {row["choice_a"].strip()}
(B) {row["choice_b"].strip()}
(C) {row["choice_c"].strip()}
(D) {row["choice_d"].strip()}
-----

Answer: """.strip()

    return prompt


def mbe_prompt_003(row: dict) -> str:
    """Generate a prompt from a row of the question spreadsheet."""
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1) :].strip()
    prompt = f"""Act as if you are taking the Bar Exam.\nPlease answer the following question in this rank order format: 
First Choice: <LETTER>
Second Choice: <LETTER>
Third Choice: <LETTER>

-----
Question: {question_text}
(A) {row["choice_a"].strip()}
(B) {row["choice_b"].strip()}
(C) {row["choice_c"].strip()}
(D) {row["choice_d"].strip()}
-----

Answer: """.strip()

    return prompt


def mbe_prompt_004(row: dict) -> str:
    """Generate a prompt from a row of the question spreadsheet."""
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1) :].strip()
    prompt = f"""Act as if you are taking the Bar Exam.\nPlease answer the following question in this rank order format: 
First Choice: <LETTER>
Second Choice: <LETTER>
Third Choice: <LETTER>
Explanation of Choices: <EXPLANATION> 

-----
Question: {question_text}
(A) {row["choice_a"].strip()}
(B) {row["choice_b"].strip()}
(C) {row["choice_c"].strip()}
(D) {row["choice_d"].strip()}
-----

Answer: """.strip()

    return prompt


def mbe_prompt_005(row: dict) -> str:
    """Generate a prompt from a row of the question spreadsheet."""
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1) :].strip()
    prompt = f"""You are well-prepared lawyer taking the MBE.\nPlease answer the following question in this rank order format: 
First Choice: <LETTER>
Second Choice: <LETTER>
Third Choice: <LETTER>

-----
Question: {question_text}
(A) {row["choice_a"].strip()}
(B) {row["choice_b"].strip()}
(C) {row["choice_c"].strip()}
(D) {row["choice_d"].strip()}
-----

Answer: """.strip()

    return prompt

def mbe_prompt_006(row: dict) -> str:
    """Generate a prompt from a row of the question spreadsheet."""
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1) :].strip()
    prompt = f"""Act as if you are taking the Bar Exam.\nPlease answer the following question in this rank order format: 
First Choice: <LETTER>
Second Choice: <LETTER>
Third Choice: <LETTER>
Explanation of Choices: <EXPLANATION>
Authority or Citation for Explanation: 

-----
Question: {question_text}
(A) {row["choice_a"].strip()}
(B) {row["choice_b"].strip()}
(C) {row["choice_c"].strip()}
(D) {row["choice_d"].strip()}
-----

Answer: """.strip()

    return prompt

def mbe_prompt_007(row: dict) -> str:
    """Generate a prompt from a row of the question spreadsheet."""
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1) :].strip()
    prompt = f"""Answer the following Bar Exam question in the following rank order format: 
First Choice: <LETTER>
Second Choice: <LETTER>
Third Choice: <LETTER>

-----
Question: {question_text}
(A) {row["choice_a"].strip()}
(B) {row["choice_b"].strip()}
(C) {row["choice_c"].strip()}
(D) {row["choice_d"].strip()}
-----

Answer: """.strip()

    return prompt


def mpre_prompt_001(row: dict) -> str:
    """Generate a prompt from a row of the question spreadsheet."""
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1) :].strip()
    prompt = f"""Act as if you are taking the Bar Exam.\nPlease answer the following question in this rank order format: 
First Choice: <LETTER>

-----
Question: {question_text}
(A) {row["choice_a"].strip()}
(B) {row["choice_b"].strip()}
(C) {row["choice_c"].strip()}
(D) {row["choice_d"].strip()}
-----

Answer: """.strip()

    return prompt


def mpre_prompt_002(row: dict) -> str:
    """Generate a prompt from a row of the question spreadsheet."""
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1) :].strip()
    prompt = f"""Act as if you are taking the Bar Exam.\nPlease answer the following question in this rank order format: 
First Choice: <LETTER>
Second Choice: <LETTER>

-----
Question: {question_text}
(A) {row["choice_a"].strip()}
(B) {row["choice_b"].strip()}
(C) {row["choice_c"].strip()}
(D) {row["choice_d"].strip()}
-----

Answer: """.strip()

    return prompt


def mpre_prompt_003(row: dict) -> str:
    """Generate a prompt from a row of the question spreadsheet."""
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1) :].strip()
    prompt = f"""Act as if you are taking the Bar Exam.\nPlease answer the following question in this rank order format: 
First Choice: <LETTER>
Second Choice: <LETTER>
Third Choice: <LETTER>

-----
Question: {question_text}
(A) {row["choice_a"].strip()}
(B) {row["choice_b"].strip()}
(C) {row["choice_c"].strip()}
(D) {row["choice_d"].strip()}
-----

Answer: """.strip()

    return prompt


def mpre_prompt_004(row: dict) -> str:
    """Generate a prompt from a row of the question spreadsheet."""
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1) :].strip()
    prompt = f"""Act as if you are taking the Bar Exam.\nPlease answer the following question in this rank order format: 
First Choice: <LETTER>
Second Choice: <LETTER>
Third Choice: <LETTER>
Explanation of Choices: <EXPLANATION> 

-----
Question: {question_text}
(A) {row["choice_a"].strip()}
(B) {row["choice_b"].strip()}
(C) {row["choice_c"].strip()}
(D) {row["choice_d"].strip()}
-----

Answer: """.strip()

    return prompt


def mpre_prompt_005(row: dict) -> str:
    """Generate a prompt from a row of the question spreadsheet."""
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1) :].strip()
    prompt = f"""You are well-prepared lawyer taking the MBE.\nPlease answer the following question in this rank order format: 
First Choice: <LETTER>
Second Choice: <LETTER>
Third Choice: <LETTER>

-----
Question: {question_text}
(A) {row["choice_a"].strip()}
(B) {row["choice_b"].strip()}
(C) {row["choice_c"].strip()}
(D) {row["choice_d"].strip()}
-----

Answer: """.strip()

    return prompt

def mpre_prompt_006(row: dict) -> str:
    """Generate a prompt from a row of the question spreadsheet."""
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1) :].strip()
    prompt = f"""Act as if you are taking the Bar Exam.\nPlease answer the following question in this rank order format: 
First Choice: <LETTER>
Second Choice: <LETTER>
Third Choice: <LETTER>
Explanation of Choices: <EXPLANATION>
Authority or Citation for Explanation: 

-----
Question: {question_text}
(A) {row["choice_a"].strip()}
(B) {row["choice_b"].strip()}
(C) {row["choice_c"].strip()}
(D) {row["choice_d"].strip()}
-----

Answer: """.strip()

    return prompt

def mpre_prompt_007(row: dict) -> str:
    """Generate a prompt from a row of the question spreadsheet."""
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1) :].strip()
    prompt = f"""Answer the following Bar Exam question in the following rank order format: 
First Choice: <LETTER>
Second Choice: <LETTER>
Third Choice: <LETTER>

-----
Question: {question_text}
(A) {row["choice_a"].strip()}
(B) {row["choice_b"].strip()}
(C) {row["choice_c"].strip()}
(D) {row["choice_d"].strip()}
-----

Answer: """.strip()

    return prompt


# consolidate prompts for MBE
MBE_PROMPT_LIST = [
    mbe_prompt_006,
    mbe_prompt_007,
]

# consolidate prompts for MPRE
MPRE_PROMPT_LIST = [
    mpre_prompt_006,
    mpre_prompt_007,
]
