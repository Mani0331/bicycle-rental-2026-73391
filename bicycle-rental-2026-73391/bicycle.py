"""
bicycle.py

This module contains the Bicycle class, which represents a single bicycle
in the rental shop. It inherits from the RentalItem abstract base class
and provides functionality for borrowing, returning, pricing, and cost
calculation.

Author: Muhammad Usman Waqar
"""

from rental_item import RentalItem


class Bicycle(RentalItem):
    """
    Represents a bicycle available for rent.

    Attributes:
        bicycle_id (str): Unique identifier for the bicycle.
        model (str): The model name of the bicycle.
        hourly_rate (float): Cost per hour to rent the bicycle.
        is_available (bool): Whether the bicycle is currently available.
        times_borrowed (int): How many times the bicycle has been borrowed.
    """

    # Class-level counter used by the alternative constructor
    _next_id = 1000

    def __init__(self, bicycle_id, model, hourly_rate):
        """
        Initialise a new Bicycle instance.

        Parameters:
            bicycle_id (str): Unique identifier for the bicycle.
            model (str): The model name of the bicycle.
            hourly_rate (float): Cost per hour to rent the bicycle.

        Raises:
            ValueError: If any argument is invalid.
        """
        self.bicycle_id = self._validate_id(bicycle_id)
        self.model = self._validate_model(model)
        self.hourly_rate = self._validate_hourly_rate(hourly_rate)
        self.is_available = True
        self.times_borrowed = 0

    # ------------------------------------------------------------------
    # Validation helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _validate_id(bicycle_id):
        """Ensure the bicycle ID is a non-empty string."""
        if not isinstance(bicycle_id, str) or not bicycle_id.strip():
            raise ValueError("Bicycle ID must be a non-empty string.")
        return bicycle_id.strip()

    @staticmethod
    def _validate_model(model):
        """Ensure the model name is a non-empty string."""
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Model must be a non-empty string.")
        return model.strip()

    @staticmethod
    def _validate_hourly_rate(hourly_rate):
        """Ensure the hourly rate is a positive number."""
        if not isinstance(hourly_rate, (int, float)):
            raise ValueError("Hourly rate must be a number.")
        if hourly_rate <= 0:
            raise ValueError("Hourly rate must be greater than zero.")
        return float(hourly_rate)

    # ------------------------------------------------------------------
    # Core functionality
    # ------------------------------------------------------------------

    def borrow(self):
        """
        Mark the bicycle as borrowed.

        Raises:
            RuntimeError: If the bicycle is already borrowed.
        """
        if not self.is_available:
            raise RuntimeError(
                f"Bicycle {self.bicycle_id} is already borrowed."
            )
        self.is_available = False
        self.times_borrowed += 1

    def return_bicycle(self):
        """
        Mark the bicycle as returned.

        Raises:
            RuntimeError: If the bicycle was not borrowed.
        """
        if self.is_available:
            raise RuntimeError(
                f"Bicycle {self.bicycle_id} is not currently borrowed."
            )
        self.is_available = True

    def update_price(self, new_rate):
        """
        Update the hourly rental rate.

        Parameters:
            new_rate (float): The new hourly rate.

        Raises:
            ValueError: If the new rate is invalid.
        """
        self.hourly_rate = self._validate_hourly_rate(new_rate)

    def calculate_rental_cost(self, hours):
        """
        Calculate the cost of renting this bicycle for a number of hours.

        Parameters:
            hours (float): The number of hours rented.

        Returns:
            float: The total rental cost.

        Raises:
            ValueError: If hours is not a positive number.
        """
        if not isinstance(hours, (int, float)):
            raise ValueError("Hours must be a number.")
        if hours <= 0:
            raise ValueError("Hours must be greater than zero.")
        return round(self.hourly_rate * hours, 2)

    def get_description(self):
        """Return a short description of the bicycle."""
        status = "available" if self.is_available else "borrowed"
        return (
            f"Bicycle {self.bicycle_id} ({self.model}) - "
            f"£{self.hourly_rate:.2f}/hour - currently {status}"
        )

    # ------------------------------------------------------------------
    # Alternative constructors
    # ------------------------------------------------------------------

    @classmethod
    def from_string(cls, data_string):
        """
        Create a Bicycle from a comma-separated string.

        Expected format: "id,model,hourly_rate"

        Example:
            Bicycle.from_string("B001,Mountain Pro,5.50")
        """
        try:
            bicycle_id, model, rate = data_string.split(",")
            return cls(bicycle_id.strip(), model.strip(), float(rate.strip()))
        except ValueError as exc:
            raise ValueError(
                f"Invalid bicycle data string: '{data_string}'. "
                "Expected format: 'id,model,hourly_rate'"
            ) from exc

    @classmethod
    def create_new(cls, model, hourly_rate):
        """
        Create a brand-new Bicycle with an auto-generated ID.

        Example:
            Bicycle.create_new("City Cruiser", 4.00)
        """
        new_id = f"B{cls._next_id}"
        cls._next_id += 1
        return cls(new_id, model, hourly_rate)

    # ------------------------------------------------------------------
    # Dunder methods
    # ------------------------------------------------------------------

    def __str__(self):
        return self.get_description()

    def __repr__(self):
        return (
            f"Bicycle('{self.bicycle_id}', '{self.model}', "
            f"{self.hourly_rate})"
        )
