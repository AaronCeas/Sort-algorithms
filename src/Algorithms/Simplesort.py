import random
from typing import List, Any

class EquiprobableRaffle:
    def __init__(self, participants: List[Any]):
        if not participants:
            raise ValueError("La lista de participantes no puede estar vacía.")
        self.participants = participants
        self.n = len(participants)

    def get_probability(self) -> float:
        return 1 / self.n

    def select_winner(self) -> Any:
        return random.choice(self.participants)

if __name__ == "__main__":
    players = ["Alice", "Bob", "Charlie", "David"]
    raffle = EquiprobableRaffle(players)
    
    print(f"Probabilidad por participante P(X=e_i): {raffle.get_probability():.4f}")
    print(f"Ganador del sorteo: {raffle.select_winner()}")
