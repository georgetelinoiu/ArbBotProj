class Match:
    def __init__(self, player1, player2, odd1, odd2):
        self.player1 = player1
        self.player2 = player2
        self.odd1 = odd1
        self.odd2 = odd2
        self.probabilitate = (1 / float(odd1) + 1 / float(odd2)) * 100

    def __str__(self):
        return "Match " + self.player1 + " with odd " + self.odd1 + " vs " + self.player2 + " odd " + self.odd2 + " total probability: " + str(self.probabilitate)

    def compare(self, match):
        if(self.player1 == match.player1 and self.player2 == match.player2):
            return True