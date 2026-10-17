"""
test_bicycle.py

Automated unit tests for the Bicycle Rental System.

Run with:  python -m unittest test_bicycle.py -v

Author: [Your Full Name]
Student Number: [Your Student Number]
Date: October 2026
"""

import unittest

from bicycle import Bicycle
from rental_item import RentalItem


class TestBicycleCreation(unittest.TestCase):
    """Tests for creating Bicycle objects."""

    def test_valid_creation(self):
        """A bicycle with valid arguments should be created correctly."""
        bike = Bicycle("B001", "Mountain Pro", 5.50)
        self.assertEqual(bike.bicycle_id, "B001")
        self.assertEqual(bike.model, "Mountain Pro")
        self.assertEqual(bike.hourly_rate, 5.50)
        self.assertTrue(bike.is_available)
        self.assertEqual(bike.times_borrowed, 0)

    def test_invalid_id_raises(self):
        """An empty ID should raise ValueError."""
        with self.assertRaises(ValueError):
            Bicycle("", "Model", 5.00)

    def test_invalid_model_raises(self):
        """An empty model name should raise ValueError."""
        with self.assertRaises(ValueError):
            Bicycle("B001", "   ", 5.00)

    def test_negative_rate_raises(self):
        """A negative hourly rate should raise ValueError."""
        with self.assertRaises(ValueError):
            Bicycle("B001", "Model", -1.00)

    def test_zero_rate_raises(self):
        """A zero hourly rate should raise ValueError."""
        with self.assertRaises(ValueError):
            Bicycle("B001", "Model", 0)

    def test_non_numeric_rate_raises(self):
        """A non-numeric hourly rate should raise ValueError."""
        with self.assertRaises(ValueError):
            Bicycle("B001", "Model", "five")


class TestBorrowAndReturn(unittest.TestCase):
    """Tests for borrowing and returning bicycles."""

    def setUp(self):
        self.bike = Bicycle("B001", "Mountain Pro", 5.00)

    def test_borrow_success(self):
        """Borrowing an available bicycle should work."""
        self.bike.borrow()
        self.assertFalse(self.bike.is_available)
        self.assertEqual(self.bike.times_borrowed, 1)

    def test_borrow_twice_raises(self):
        """Borrowing an already-borrowed bicycle should raise RuntimeError."""
        self.bike.borrow()
        with self.assertRaises(RuntimeError):
            self.bike.borrow()

    def test_return_success(self):
        """Returning a borrowed bicycle should work."""
        self.bike.borrow()
        self.bike.return_bicycle()
        self.assertTrue(self.bike.is_available)

    def test_return_not_borrowed_raises(self):
        """Returning an available bicycle should raise RuntimeError."""
        with self.assertRaises(RuntimeError):
            self.bike.return_bicycle()

    def test_multiple_borrow_cycles(self):
        """The borrow count should increment across cycles."""
        for _ in range(3):
            self.bike.borrow()
            self.bike.return_bicycle()
        self.assertEqual(self.bike.times_borrowed, 3)


class TestPricing(unittest.TestCase):
    """Tests for price management and rental cost calculation."""

    def setUp(self):
        self.bike = Bicycle("B001", "Mountain Pro", 5.00)

    def test_update_price(self):
        """Updating the price should change the hourly rate."""
        self.bike.update_price(6.50)
        self.assertEqual(self.bike.hourly_rate, 6.50)

    def test_update_price_invalid(self):
        """Updating the price with a negative value should raise."""
        with self.assertRaises(ValueError):
            self.bike.update_price(-3.00)

    def test_calculate_cost(self):
        """Rental cost should equal rate * hours."""
        cost = self.bike.calculate_rental_cost(4)
        self.assertEqual(cost, 20.00)

    def test_calculate_cost_fractional_hours(self):
        """Fractional hours should be handled correctly."""
        cost = self.bike.calculate_rental_cost(1.5)
        self.assertEqual(cost, 7.50)

    def test_calculate_cost_invalid_hours(self):
        """Non-positive hours should raise ValueError."""
        with self.assertRaises(ValueError):
            self.bike.calculate_rental_cost(0)
        with self.assertRaises(ValueError):
            self.bike.calculate_rental_cost(-1)


class TestAlternativeConstructors(unittest.TestCase):
    """Tests for the @classmethod alternative constructors."""

    def test_from_string_valid(self):
        """Creating from a valid string should work."""
        bike = Bicycle.from_string("B010, City Cruiser, 4.25")
        self.assertEqual(bike.bicycle_id, "B010")
        self.assertEqual(bike.model, "City Cruiser")
        self.assertEqual(bike.hourly_rate, 4.25)

    def test_from_string_invalid(self):
        """A malformed string should raise ValueError."""
        with self.assertRaises(ValueError):
            Bicycle.from_string("only-one-field")

    def test_create_new_generates_unique_ids(self):
        """Auto-generated IDs should be unique."""
        bike_a = Bicycle.create_new("Model A", 3.00)
        bike_b = Bicycle.create_new("Model B", 4.00)
        self.assertNotEqual(bike_a.bicycle_id, bike_b.bicycle_id)


class TestAbstractBaseClass(unittest.TestCase):
    """Tests confirming RentalItem behaves as an abstract base class."""

    def test_cannot_instantiate_rental_item(self):
        """RentalItem itself should not be instantiable."""
        with self.assertRaises(TypeError):
            RentalItem()

    def test_bicycle_is_subclass(self):
        """Bicycle should be recognised as a subclass of RentalItem."""
        self.assertTrue(issubclass(Bicycle, RentalItem))


if __name__ == "__main__":
    unittest.main(verbosity=2)