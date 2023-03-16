"""
This module provides standardized methods for handling experiment/result data across all exam types.
"""

# imports
from pathlib import Path


def get_next_session_path(exam_type: str, exam_id: str, experiment_id: int) -> Path:
    """Get the next session path.

    Args:
        exam_type (str): The exam type, e..g, mbe.
        exam_id (str): The exam id, e.g., ncbe-pdf-001
        experiment_id (int): The experiment id, e.g., 1.

    Returns:
        Path: The next session path.
    """

    # start from 1 for humans
    session_number = 1

    # get base result path from exam type, exam id, experiment ID
    exam_type_path = (
        Path(__file__).parent.parent.parent  # src/exams/  # src/  # project root
        / "results"
        / exam_type
    )
    exam_type_path.mkdir(exist_ok=True)

    # next, get the exam id path
    exam_id_path = exam_type_path / exam_id
    exam_id_path.mkdir(exist_ok=True)

    # next, get the experiment id path
    experiment_id_path = exam_id_path / f"experiment-{experiment_id:03d}"
    experiment_id_path.mkdir(exist_ok=True)

    while True:
        session_id = f"session-{session_number:03d}"
        session_path = experiment_id_path / session_id

        # skip if exists
        if session_path.exists():
            session_number += 1
            continue

        # otherwise continue
        session_path.mkdir(exist_ok=True)
        return session_path


def get_experiment_session_list(
    exam_type: str, exam_id: str, experiment_id: int
) -> list[Path]:
    """Get a list of all experiment session files from the experiment directory.

    Args:
        exam_type (str): The exam type, e..g, mbe.
        exam_id (str): The exam id, e.g., ncbe-pdf-001
        experiment_id (int): The experiment id, e.g., 1.

    Returns:
        list[Path]: A list of all session paths.
    """

    # start from 1 for humans
    session_number = 1

    # get base result path from exam type, exam id, experiment ID
    exam_type_path = (
        Path(__file__).parent.parent.parent  # src/exams/  # src/  # project root
        / "results"
        / exam_type
    )
    if not exam_type_path.exists():
        return []

    # next, get the exam id path
    exam_id_path = exam_type_path / exam_id
    if not exam_id_path.exists():
        return []

    # next, get the experiment id path
    experiment_id_path = exam_id_path / f"experiment-{experiment_id:03d}"
    if not experiment_id_path.exists():
        return []

    session_path = experiment_id_path
    session_list = []
    for session_id in session_path.iterdir():
        if (session_id / "session.json").exists():
            session_list.append(session_id)
    return sorted(session_list)
