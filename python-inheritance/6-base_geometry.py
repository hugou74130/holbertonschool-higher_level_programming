#!/usr/bin/python3
"""Module defining a base geometry class."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Indicates that the area method is not implemented.
        """
        # Méthode volontairement non implémentée pour être surchargée
        raise Exception("area() is not implemented")
