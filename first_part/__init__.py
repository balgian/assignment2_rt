# first_part/scripts/__init__.py

"""
This package contains the following modules:\n
- `target_client`: Module for sending the target position and retrieving velocity.
- `last_target_pos`: Module for getting the last target position set by the user.
"""

from .scripts import target_client, last_target_pos

__all__ = ["target_client", "last_target_pos"]