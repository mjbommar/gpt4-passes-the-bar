"""
Define essay prompts for the MEE and MPT.
"""


def mee_prompt_001(row: dict) -> str:
    """Generate a prompt from a essay SGML."""
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1) :].strip()
    prompt = f"""Act as if you are taking the Bar Exam.  Please read the following question and answer it in essay form.
--------
Question: {question_text}
--------
Answer:""".strip()

    return prompt


def mee_prompt_002(row: dict) -> str:
    """Generate a prompt from a essay SGML."""
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1) :].strip()
    prompt = f"""Act as if you are taking the MEE section of the Bar Exam.  Please read the following question and answer it in essay form.
--------
Question: {question_text}
--------
Answer:""".strip()

    return prompt

def mee_prompt_003(row: dict) -> str:
    """Generate a prompt from a essay SGML."""
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1) :].strip()
    prompt = f"""Act as if you are taking the MEE section of the Bar Exam.  Please read the following question and answer it in essay form
    using the IRAC method to address the Issue, Rule, Application, and Conclusion.
--------
Question: {question_text}
--------
Answer:""".strip()

    return prompt


def mee_chat_prompt_001(row: dict) -> tuple[str, str]:
    """Generate a prompt from a essay SGML.

    Returns a tuple of system_prompt, question_prompt

    """
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1) :].strip()
    system_prompt = f"""Act as if you are taking the Bar Exam."""
    question_prompt = f"""Please read the following question and answer it in essay form.
--------
Question: {question_text}
--------
Answer:""".strip()

    return system_prompt, question_prompt


def mee_chat_prompt_002(row: dict) -> tuple[str, str]:
    """Generate a prompt from a essay SGML.

    Returns a tuple of system_prompt, question_prompt

    """
    question_text = row["question_prompt"]
    question_text = question_text[(question_text.find(". ") + 1):].strip()
    system_prompt = f"""Act as if you are taking the Bar Exam."""
    question_prompt = f"""Please read the following question and answer it in essay form using the IRAC method to 
address the Issue, Rule, Application, and Conclusion.
    --------
    Question: {question_text}
    --------
    Answer:""".strip()

    return system_prompt, question_prompt


# consolidate prompts for MBE
MEE_PROMPT_LIST = [
    mee_prompt_001,
    mee_prompt_002,
    mee_prompt_003,
]

MEE_CHAT_PROMPT_LIST = [
    mee_chat_prompt_001,
    mee_chat_prompt_002,
]