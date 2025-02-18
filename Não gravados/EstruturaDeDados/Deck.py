class Card():
    def __init__(self, value, suit):
        self._value = value
        self._suit = suit

    def __str__(self):
        return f"{self._value} de {self._suit}"
    

class Deck():
    def __init__(self):
        suits = ["Espadas", "Copas", "Ouros", "Paus"]
        cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self._cards = []
        self.enabled = False

        for suit in suits:
            for card in cards:
                self._cards.append(Card(card, suit))


    def __getitem__(self, index):
        return self._cards[index]
    
    def __len__(self):
        return len(self._cards)
    
    def __eq__(self, other):
        return len(self) == len(other)

    def __repr__(self):
        return f"Baralho de {len(self)} cartas"
    
    def __add__(self, other):
        cards = self._cards + other._cards
        deck = Deck()
        deck._cards = cards
        return deck
    
    def __mul__(self, scalar):
        cards = self._cards * scalar
        deck = Deck()
        deck._cards = cards
        return deck

    def __bool__(self):
        return self.enabled


    
if __name__ == "__main__":

    baralho = Deck()
    baralho2 = Deck()
    baralho2.enabled = True

    print(len(baralho))
    print(len(baralho2))
    print(baralho, baralho2)
    print(baralho == baralho2)
    print("----------")
    print(baralho + baralho2)
    print(baralho * 3)

    if baralho:
        print("Baralho OK")
    else:
        print("Baralho Desativado")

    if baralho2:
        print("Baralho OK")
    else:
        print("Baralho Desativado")