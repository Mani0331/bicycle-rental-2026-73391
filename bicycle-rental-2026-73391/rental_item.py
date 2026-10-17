"""
rental_item.py

This module defines the abstract base class RentalItem, which serves as a
blueprint for all items that can be rented out in the shop. Any class that
inherits from this must implement the calculate_rental_cost method.

Author: [Your Full Name]
Student Number: [Your Student Number]
Date: October 2026
"""

from abc import ABC, abstractmethod


class RentalItem(ABC):
    """
    Abstract base class representing a generic rental item.

    This class cannot be instantiated on its own. It exists purely to
    enforce a common interface for all rentable objects in the system.
    """

    @abstractmethod
    def calculate_rental_cost(self, hours):
        """
        Calculate the total rental cost for a given number of hours.

        Parameters:
            hours (float): The number of hours the item was rented for.

        Returns:
            float: The total cost of the rental.

        Raises:
            NotImplementedError: If a subclass does not override this method.
        """
        raise NotImplementedError(
            "Subclasses of RentalItem must implement calculate_rental_cost()"
        )

    @abstractmethod
    def get_description(self):
        """
        Return a short human-readable description of the rental item.

        Returns:
            str: A description of the item.
        """
        raise NotImplementedError(
            "Subclasses of RentalItem must implement get_description()"
        )