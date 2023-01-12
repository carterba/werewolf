from manager import WwPlayer,WwRoundManager

class WwActionBook:

    @staticmethod
    def villager_action(rm: WwRoundManager, pl: WwPlayer):
        print(pl.acting_card.prompt)

    @staticmethod
    def doppelganger_action(rm: WwRoundManager, pl: WwPlayer):
        choice=input(pl.acting_card.prompt)
        pl.acting_card = rm.players[choice].visible_card

    @staticmethod
    def seer_action(rm: WwRoundManager, pl: WwPlayer):
        choice=input(pl.acting_card.prompt)
        pl.knowledge.append(f"{choice} has the {rm.players[choice].visible_card.name} role")

    @staticmethod
    def robber_action(rm: WwRoundManager, pl: WwPlayer):
        choice=input(pl.acting_card.prompt)
        pl.visible_card = rm.players[choice].visible_card
        rm.players[choice].visible_card = rm.deck["robber"]
        pl.knowledge.append(f"You have the {pl.visible_card.name} role from {choice}")

    @staticmethod
    def troublemaker_action(rm: WwRoundManager, pl: WwPlayer):
        choice1=input(pl.acting_card.prompt)
        choice2=input(pl.acting_card.prompt)
        _temp= rm.players[choice1].visible_card
        rm.players[choice1].visible_card = rm.players[choice2].visible_card
        rm.players[choice2].visible_card = _temp

    @staticmethod
    def drunk_action(rm: WwRoundManager, pl: WwPlayer):
        choice=input(pl.acting_card.prompt)
        