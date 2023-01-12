from typing import Callable, Dict, List
from typing import Optional
from enum import Enum

import yaml

class WwTeam(Enum):
    VILLAGE = "village"
    WEREWOLF = "werewolf"
    TANNER = "tanner"

class WwCard:
    name: str
    role: str
    prompt: Optional[str]
    action: Callable
    _team: str
    maximum: int = 1
    minimum: int = 1
    absolute_minimum: int = 0
    count: int = 0

    @property
    def team(self) -> WwTeam:
        return WwTeam(self._team)

class WwDeck:
    loaded_cards: Dict[str,WwCard]
    active_cards: List[str]

    def __init__(self) -> None:
        with open('cards.yaml', 'r') as file:
            self.loaded_cards = yaml.safe_load(file)