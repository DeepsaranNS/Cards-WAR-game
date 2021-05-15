import random

# will define the global variables ,for suits , ranks and values.
#values are a dictionary, ehich has ranks as key and corresponding integers as values.

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

# the card class contains the attributes suits rank and values.

class Card:

    def __init__(self,suits,ranks):
        self.suits=suits
        self.ranks=ranks
        self.values=values[ranks]
        
    def __str__(self):
        return self.ranks+" of "+self.suits


class Deck:

    def __init__(self):
        self.all_cards=[]
        
        for suit in suits:
            for rank in ranks:
                #this creates a card object for all cards.
                card_object = Card(suit,rank)
                self.all_cards.append(card_object) 

    def shuffle(self):
        #this shuffles the deck of the card.
        random.shuffle(self.all_cards)
        print("cards has been shuffled")

    def deal_a_card(self):
        #this pops out a single card from the deck.
        return self.all_cards.pop()

class Player:
    
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
        
    def remove_card(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        ''' to check whether a single card is going to be added or
        multiple cards i.e (list of new cards) are being added.'''
        
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
            
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"
    
#Game Setup

player_one=Player("one")
player_two=Player("two")

new_deck=Deck()
new_deck.shuffle()

#distributing equal no of cards to the player
for x in range(26):
    player_one.add_cards(new_deck.deal_a_card())
    player_two.add_cards(new_deck.deal_a_card())

    
game_on=True

round_num = 0

while game_on:
    round_num += 1
    print(f"Round - {round_num}")
    
    if len(player_one.all_cards)==0:
        print("player Two has won the game!!!")
        game_on=False
        break
    
    if len(player_two.all_cards)==0:
        print("player One has won the game!!!")
        game_on=False
        break
    
    player_one_cards=[]
    player_one_cards.append(player_one.remove_card())
    
    player_two_cards=[]
    player_two_cards.append(player_two.remove_card())
    
    #checking the cards for equality,which tends to war!!
    at_war=True
    
    while at_war:
        
        if player_one_cards[-1].values > player_two_cards[-1].values:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war=False
        
        elif player_one_cards[-1].values < player_two_cards[-1].values:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war=False
            
        else:
            print("WAR!!")
            
            if len(player_one.all_cards)<5:
                print("player One doesn't have enough cards to fight a war.")
                print("player Two has won")
                game_on=False
                break
            
            elif len(player_two.all_cards)<5:
                print("player Two  doesn't have enough cards to fight a war.")
                print("player One has won")
                game_on=False
                break
            
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())
    



        
    
