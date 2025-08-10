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
        self._enabled = False
        
        for suit in suits:
            for card in cards:
                self._cards.append(Card(card, suit))

    def __len__(self):
        return len(self._cards)
    
    # def __str__(self):
    #     return f"Baralho de {len(self)} cartas"
    
    def __repr__(self):
        return f"Baralho de {len(self)} cartas"
    
    def __getitem__(self, index):
        return self._cards[index]

    def __eq__(self, other):
        return len(self) == len(other)
    
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
        return self._enabled
    
    def activate(self):
        print("O baralho foi ativado")
        self._enabled = True

if __name__ == "__main__":
    card = Card("As", "Espadas")
    deck = Deck()
    deck2 = Deck()
    deck3 = deck + deck2
    # deck2._cards.pop()

    print(deck)
    print(deck == deck2)
    print(deck3)
    print(deck3 * 2)


    if deck:
        print("O baralho Esta Ativo")
    else:
        print("O baralho Nao Esta Ativo")


    deck.activate()

    if deck:
        print("O baralho Esta Ativo")
    else:
        print("O baralho Nao Esta Ativo")