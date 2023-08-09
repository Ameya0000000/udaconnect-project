from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

@dataclass
class Connection:
    location: Dict  # Represent Location data as dict
    person: Dict  # Represent Person data as dict
