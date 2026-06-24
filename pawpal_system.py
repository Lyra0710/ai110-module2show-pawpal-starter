from __future__ import annotations

from dataclasses import dataclass, field
from datetime import time
from typing import Optional


# ---------------------------------------------------------------------------
# Task — a single pet care activity
# ---------------------------------------------------------------------------

@dataclass
class Task:
    title: str
    duration_minutes: int
    priority: str                          # "low" | "medium" | "high"
    preferred_time: Optional[time] = None
    recurring: bool = False

    def priority_score(self) -> int:
        """Return a numeric score for sorting (higher = more urgent)."""
        pass

    def __repr__(self) -> str:
        pass


# ---------------------------------------------------------------------------
# Pet — the animal the tasks belong to
# ---------------------------------------------------------------------------

@dataclass
class Pet:
    name: str
    species: str                           # "dog" | "cat" | "other"
    breed: str = ""
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task: Task) -> None:
        pass

    def list_tasks(self) -> list[Task]:
        pass


# ---------------------------------------------------------------------------
# Owner — the person whose time budget constrains the schedule
# ---------------------------------------------------------------------------

class Owner:
    def __init__(
        self,
        name: str,
        available_minutes: int = 480,      # default: 8-hour day
        preferences: Optional[dict] = None,
    ) -> None:
        self.name = name
        self.pets: list[Pet] = []
        self.available_minutes = available_minutes
        self.preferences: dict = preferences or {}

    def add_pet(self, pet: Pet) -> None:
        pass

    def add_task(self, pet: Pet, task: Task) -> None:
        pass

    def set_available_time(self, minutes: int) -> None:
        pass


# ---------------------------------------------------------------------------
# Scheduler — builds a prioritised, time-bounded daily plan
# ---------------------------------------------------------------------------

class Scheduler:
    def __init__(
        self,
        tasks: list[Task],
        available_minutes: int,
        start_time: time = time(8, 0),
    ) -> None:
        self.tasks = tasks
        self.available_minutes = available_minutes
        self.start_time = start_time

    def sort_tasks(self) -> list[Task]:
        """Return tasks ordered by priority score (descending)."""
        pass

    def filter_tasks(self) -> list[Task]:
        """Drop tasks that would exceed the available time budget."""
        pass

    def resolve_conflicts(self) -> None:
        """Adjust start times so no two tasks overlap."""
        pass

    def build_schedule(self) -> list[dict]:
        """Return a list of {task, start_time, end_time} dicts."""
        pass

    def explain(self) -> str:
        """Return a human-readable explanation of why each task was chosen."""
        pass
