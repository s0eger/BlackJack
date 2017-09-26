from blackjack_deck import Deck
from blackjack_player import Player, Dealer

class Blackjack(object):
    def __init__(self,starting_cash=10000, bet=2000):
        self.starting_cash = starting_cash
        self.bet = bet
        self.player = Player(starting_cash)
        self.dealer = Dealer()

    def deal(self):
        print ("Player - ${}".format(self.player.money))
        self.deck = Deck()
        self.deck.shuffle()
        self.player.clear()
        self.dealer.clear()
        self.player.receive_card(self.deck.draw_card())
        self.dealer.receive_card(self.deck.draw_card())
        self.player.receive_card(self.deck.draw_card())
        self.dealer.receive_card(self.deck.draw_card())

        self.player_choice()


    def show_player(self):
        print(self.player.hand_text() + " ({})".format(self.player.hand_total))

    def hide_dealer (self):
        print("Dealer: " + str(self.dealer.hand[0]) + "    ?")

    def show_dealer(self):
        print(self.dealer.hand_text() + " ({})".format(self.dealer.hand_total))

    def player_choice (self):
        self.show_player()
        self.hide_dealer()
        print("Options: Hit   Stay  Quit ")
        p_choice  = input('>>> ')
        p_choice.lower()
        if p_choice == 'hit':
            self.player_hit()
        elif p_choice == 'stay':
            self.player_stay()
        elif p_choice == 'quit':
            self.player.money -= self.bet
            self.end_game()
        else:
            print("Not an option")
            self.player_choice()

    def player_hit (self):
        self.player.receive_card(self.deck.draw_card())
        if self.player.hand_total > 21:
            self.show_player()
            self.show_dealer()
            self.dealer_win()
        elif self.player.hand_total == 21:
            self.show_player()
            self.dealer_choice()
        else:
            self.player_choice()

    def player_stay (self):
        self.dealer_choice()

    def end_game (self):
        print("Player leaves with ${}".format(self.player.money))

    def dealer_choice (self):
        self.show_dealer()
        while self.dealer.hand_total < 17:
            self.dealer.receive_card(self.deck.draw_card())
            self.show_dealer()
        if self.dealer.hand_total > 21 or self.dealer.hand_total < self.player.hand_total:
            self.player_win()
        else:
            self.dealer_win()

    def play_again (self):
        again = input('>>> ')
        again.lower()
        if again == 'y':
            self.deal()
        elif again == 'n':
            self.end_game()
        else:
            print("?")
            self.play_again()

    def player_win (self):
        self.player.money += self.bet/2
        print("You win ${} (${}). Play again? Y/N".format(self.bet, self.player.money))
        self.play_again()

    def dealer_win(self):
        print('You lose ${}'.format(self.bet))
        self.player.money -= self.bet
        if self.player.money < self.bet:
            print("Dealer wins. Out of money.")
        else:
            print("Dealer wins. You have $({}). Play again? Y/N".format(self.player.money))
            self.play_again()

if __name__ == '__main__':
    game = Blackjack()
    game.deal()
