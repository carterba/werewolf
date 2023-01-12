from cards.cards import WwCard,WwDeck
from cards.actions import WwActionBook

from copy import copy,deepcopy
from dataclasses import dataclass
from random import choice
from typing import Dict,List
from typing import Optional

class WwCardCountError(Exception):
    ...

@dataclass
class WwPlayer:
    name: str
    acting_card: Optional[WwCard] = None
    visible_card: Optional[WwCard] = None
    knowledge: List[str] = []
    address: Optional[str] = None
    _turn: bool = True

class WwGameManager:
    deck: WwDeck
    vote_length_s: int = 300

    def __init__(self) -> None:
        self.deck = WwDeck()
        self.players: Dict[str,WwPlayer] = {}

    def add_player(self,player: WwPlayer) -> None:
        self.players[player.name] = player

    def remove_player(self,player:WwPlayer) -> None:
        self.players.pop(player.name)

    def add_role(self,role:str) -> None:
        if self.deck.loaded_cards[role].maximum == self.deck.active_cards.count(role) + 1:
            raise WwCardCountError(f"Cannot add more {role} roles")
        while self.deck.loaded_cards[role].minimum < self.deck.active_cards.count(role) + 1:
            self.deck.active_cards.append[role]
        self.deck.active_cards.append[role]

    def remove_role(self,role:str) -> None:
        if self.deck.loaded_cards[role].absolute_minimum == self.deck.active_cards.count(role) - 1:
            raise WwCardCountError(f"Cannot remove more {role} roles")
        while self.deck.loaded_cards[role].minimum > self.deck.active_cards.count(role) and self.deck.active_cards.count(role) > 0:
            self.deck.active_cards.remove[role]
        self.deck.active_cards.remove[role]

    def change_vote_length_s(self,vote_length_s:int) -> None:
        self.vote_length_s = vote_length_s

    def play_round(self):
        manager = WwRoundManager(self.deck,self.players,self.vote_length_s)

class WwRoundManager:
    
    def __init__(self,deck:WwDeck,players:Dict[str,WwPlayer],vote_length_s:int) -> None:
        self.deck=deck
        self.players=deepcopy(players)
        self.vote_length_s=vote_length_s

        self.run_round()

    def run_round(self):
        self.assign_roles()
        self.do_turns()
        self.do_vote()
        self.determine_winner()

    def assign_roles(self):
        active_cards = copy(self.deck.active_cards)
        for i in range(active_cards.count()-len(self.players)):
            self.players[f"_center{i}"] = WwPlayer(name=f"_center{i}",turn=False)
        for player in self.players.values():
            role = choice(active_cards)
            player.visible_card = role
            player.acting_card = role
            active_cards.remove(role)


    def do_turns(self) -> None:
        for player in self.players.values():
            if player._turn:
                funct = getattr(WwActionBook,player.acting_card.action)
                funct(self,player)

    def do_vote(self) -> None:
        pass

    def determine_winner(self) -> None:
        pass    