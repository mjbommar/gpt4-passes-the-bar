"""
This module defines a base class for all engines to implement based on "normal" interaction with a text completion LLM.
"""

# imports
from abc import ABC, abstractmethod
from typing import Iterator


class BaseEngine(ABC):
    """
    This is the base class for all engines.  All engines must implement the following methods:
    1. A method to return the name of the engine
    2. A method to return the current parameters of the engine
    3. A method to yield a set of valid parameters
    4. A method to return a random, valid parameter set
    5. A method to set the parameters of the engine
    6. A "traditional" text completion method
    """

    @abstractmethod
    def get_name(self) -> str:
        """
        This method returns the name of the engine.
        Returns:
            str: The name of the engine
        """
        pass

    @abstractmethod
    def get_current_parameters(self) -> dict:
        """
        This method returns the current parameters of the engine.
        Returns:
            dict: The current parameters of the engine.
        """
        pass

    @abstractmethod
    def get_valid_parameters(self) -> Iterator[dict]:
        """
        This method returns a set of valid parameters.
        Returns:
            Iterator[dict]: An iterator of valid parameters.
        """
        pass

    @abstractmethod
    def get_random_parameters(self) -> dict:
        """
        This method returns a random, valid parameter set.
        Returns:
            dict: A random, valid parameter set
        """
        pass

    @abstractmethod
    def set_parameters(self, parameters: dict) -> None:
        """
        This method sets the parameters of the engine.
        Args:
            parameters (dict): The parameters to set.
        """
        pass

    @abstractmethod
    def get_completions(self, prompt: str) -> list[str]:
        """
        This method performs a "traditional" text completion based on the prompt provided.
        Args:
            prompt (str): The prompt to complete.
        Returns:
            str: The completion of the prompt.
        """
        pass
