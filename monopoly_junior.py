import sys
import argparse

from itertools import cycle
from collections import deque
from multiprocessing.pool import Pool
from random import randint, shuffle

class BoardSpot:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.roll_again = kwargs.get('roll_again', False)

    def __repr__(self):
        return self.name


class BoardProperty(BoardSpot):
    def __init__(self, **kwargs):
        self.price = kwargs['price']
        self.color = kwargs['color']
        self.owner = None
        self.partner_spot = None
        super().__init__(**kwargs)


class PenaltySpot(BoardSpot):
    def __init__(self, **kwargs):
        self.fee = kwargs['fee']
        self.destination = kwargs.get('destination', None)
        super().__init__(**kwargs)


class ChanceCard:
    def __init__(self, name, destination=None,
                 free_ticket_booth=False, free_ticket_booth_options=()):

        self.name = name
        self.free_ticket_booth = free_ticket_booth
        self.free_ticket_booth_options = free_ticket_booth_options
        self.destination = destination

    def __repr__(self):
        return self.name

class OutOfCashError(Exception):
    pass

class Player:
    def __init__(self, name, ticket_booths=12, game=None, verbose=False):
        self.name = name
        self.game = game
        self.verbose = verbose
        self.cash = 31
        self.ticket_booths = ticket_booths
        self.board_spot_index = 0

    def __repr__(self):
        return self.name

    def pay(self, amount, payee=None):
        if self.cash < amount:
            amount = self.cash
            if self.verbose:
                print(f'{self} can only pay ${amount}, because they are out of cash!')
        self.cash -= amount
        if payee:
            payee.cash += amount

        if not self.cash:
            if self.game.monopoly_rules:
                # If player went bankrupt to another player, 
                # the current payee gets all of the bankrupt player's property.
                # If payee is none, the properties go to the bank. 
                # Process the properties starting 
                # with the most expensive until the least expensive.
                spots = self.game.get_properties_by_player(self)
                spots.reverse()
                for spot in spots:
                    if payee:
                        # if the payee doesn't have any ticket booths, 
                        # set the payee to None to give the rest of the properties to the bank
                        if not payee.ticket_booths:
                            payee = None
                        else:
                            # decrement the payee's ticket booth amount
                            payee.ticket_booths -= 1

                    spot.owner = payee
            
            # raise out of cash error
            # and pass this instance of Player to the exception handler
            raise OutOfCashError(self)

    def check_if_collect_go_money(self, old_board_spot_index):
        if old_board_spot_index > self.board_spot_index:
            self.cash += 2
            if self.verbose:
                print(f'{self} passed Go. {self} will collect $2')

    def roll(self):
        roll_value = randint(1, 6)

        old_board_spot_index = self.board_spot_index
        self.board_spot_index = (old_board_spot_index + roll_value) % 32

        if self.verbose:
            roll_status = f'{self} rolled a {roll_value}. ' \
                        f'{self} is now at board spot {self.board_spot_index}'
            print(roll_status)
            
        self.check_if_collect_go_money(old_board_spot_index)

def make_board_and_chance_card_deck():
    board =  list()
    chance_card_deck = deque()
    
    go_spot = BoardSpot(name='Go')
    go_cc = ChanceCard(name='Go to Go - Collect $2 allowance as you pass',
                       destination=go_spot)
    
    board.append(go_spot)
    chance_card_deck.append(go_cc)

    chance_spot = BoardSpot(name='Chance')
    board.append(chance_spot)

    penny_arcade_spot = BoardProperty(name='Penny Arcade', 
                                      price=1, color='Purple')
    
    board.append(penny_arcade_spot)

    sweet_treats_spot = BoardProperty(name='Sweet Treats Snack Shack', 
                                      price=1, color='Purple')

    board.append(sweet_treats_spot)

    penny_arcade_spot.partner_spot = sweet_treats_spot
    sweet_treats_spot.partner_spot = penny_arcade_spot

    ftb_purple_cc = ChanceCard(name='Free Ticket Booth',
                               free_ticket_booth=True,
                               free_ticket_booth_options=(penny_arcade_spot, sweet_treats_spot))

    chance_card_deck.append(ftb_purple_cc)

    board.append(chance_spot)

    yellow_rr_spot = BoardSpot(name='Yellow Line Railroad', roll_again=True)
    board.append(yellow_rr_spot)

    safari_cruise_spot = BoardProperty(name='Safari Cruise', 
                                       price=2, color='Light Blue')
    board.append(safari_cruise_spot)

    cartoon_village_spot = BoardProperty(name='Cartoon Village', 
                                         price=2, color='Light Blue')
    board.append(cartoon_village_spot)

    safari_cruise_spot.partner_spot = cartoon_village_spot
    cartoon_village_spot.partner_spot = safari_cruise_spot

    ftb_light_blue_cc = ChanceCard(name='Free Ticket Booth',
                                   free_ticket_booth=True,
                                   free_ticket_booth_options=(safari_cruise_spot, cartoon_village_spot))

    ftb_light_blue_cc2 = ChanceCard(name='Free Ticket Booth',
                                    free_ticket_booth=True,
                                    free_ticket_booth_options=(safari_cruise_spot, cartoon_village_spot))

    chance_card_deck.append(ftb_light_blue_cc)
    chance_card_deck.append(ftb_light_blue_cc2)

    fireworks_spot = PenaltySpot(name='Pay $2 to see the Fireworks', fee=2)
    board.append(fireworks_spot)

    fireworks_cc = ChanceCard(name='Go to the Fireworks and PAY $2', destination=fireworks_spot)
    chance_card_deck.append(fireworks_cc)

    board.append(chance_spot)

    lunch_spot = BoardSpot(name='Lunch')
    board.append(lunch_spot)

    lunch_cc = ChanceCard(name='Pay $3 and go to Lunch', destination=lunch_spot)
    chance_card_deck.append(lunch_cc)

    palace_of_mirrors_spot = BoardProperty(name='Palace Of Mirrors Carousel', 
                                           price=2, color='Pink')
    board.append(palace_of_mirrors_spot)

    clown_around_funhouse_spot = BoardProperty(name='Clown Around Fun House', 
                                               price=2, color='Pink')
    board.append(clown_around_funhouse_spot)

    palace_of_mirrors_spot.partner_spot = clown_around_funhouse_spot
    clown_around_funhouse_spot.partner_spot = palace_of_mirrors_spot

    ftb_pink_cc = ChanceCard(name='Free Ticket Booth',
                             free_ticket_booth=True,
                             free_ticket_booth_options=(palace_of_mirrors_spot, clown_around_funhouse_spot))
    chance_card_deck.append(ftb_pink_cc)

    palace_of_mirrors_cc = ChanceCard(name='Go to the Palace of Mirrors Carousel', 
                                      destination=palace_of_mirrors_spot)
    chance_card_deck.append(palace_of_mirrors_cc)

    green_rr_spot = BoardSpot(name='Green Line Railroad', roll_again=True)
    board.append(green_rr_spot)

    green_rr_cc = ChanceCard(name='Take a Ride on the Green Line Railroad', 
                             destination=green_rr_spot)
    chance_card_deck.append(green_rr_cc)

    longview_ferris_wheel_spot = BoardProperty(name='Longview Ferris Wheel', 
                                               price=3, color='Orange')
    board.append(longview_ferris_wheel_spot)

    bumper_cars_spot = BoardProperty(name="Bend 'Em Bumper Cars", 
                                     price=3, color='Orange')
    board.append(bumper_cars_spot)

    longview_ferris_wheel_spot.partner_spot = bumper_cars_spot
    bumper_cars_spot.partner_spot = longview_ferris_wheel_spot

    ftb_orange_cc = ChanceCard(name='Free Ticket Booth',
                               free_ticket_booth=True,
                               free_ticket_booth_options=(longview_ferris_wheel_spot, bumper_cars_spot))

    ftb_orange_cc2 = ChanceCard(name='Free Ticket Booth',
                                free_ticket_booth=True,
                                free_ticket_booth_options=(longview_ferris_wheel_spot, bumper_cars_spot))

    chance_card_deck.append(ftb_orange_cc)
    chance_card_deck.append(ftb_orange_cc2)

    longview_ferris_wheel_cc = ChanceCard(name='Go to the Longview Ferris Wheel', 
                                          destination=longview_ferris_wheel_spot)
    chance_card_deck.append(longview_ferris_wheel_cc)

    free_time_spot = BoardSpot(name='Free Time')
    board.append(free_time_spot)

    board.append(chance_spot)

    mystery_mansion_spot = BoardProperty(name='Mystery Mansion', 
                                         price=3, color='Red')
    board.append(mystery_mansion_spot)

    nitro_speed_track_spot = BoardProperty(name='Nitro Speed Track', 
                                           price=3, color='Red')
    board.append(nitro_speed_track_spot)

    mystery_mansion_spot.partner_spot = nitro_speed_track_spot
    nitro_speed_track_spot.partner_spot = mystery_mansion_spot

    ftb_red_cc = ChanceCard(name='Free Ticket Booth',
                            free_ticket_booth=True,
                            free_ticket_booth_options=(mystery_mansion_spot, nitro_speed_track_spot))

    ftb_red_cc2 = ChanceCard(name='Free Ticket Booth',
                             free_ticket_booth=True,
                             free_ticket_booth_options=(mystery_mansion_spot, nitro_speed_track_spot))

    chance_card_deck.append(ftb_red_cc)
    chance_card_deck.append(ftb_red_cc2)

    board.append(chance_spot)

    blue_rr_spot = BoardSpot(name='Blue Line Railroad', roll_again=True)
    board.append(blue_rr_spot)

    blue_rr_cc = ChanceCard(name='Take a Ride on the Blue Line Railroad', 
                            destination=blue_rr_spot)
    chance_card_deck.append(blue_rr_cc)

    fun_food_picnic_grove_spot = BoardProperty(name='Fun Food Picnic Grove', 
                                               price=4, color='Yellow')
    board.append(fun_food_picnic_grove_spot)

    ultimate_idol_grandstand_spot = BoardProperty(name='Ultimate Idol Grandstand', 
                                                  price=4, color='Yellow')
    board.append(ultimate_idol_grandstand_spot)

    fun_food_picnic_grove_spot.partner_spot = ultimate_idol_grandstand_spot
    ultimate_idol_grandstand_spot.partner_spot = fun_food_picnic_grove_spot

    ftb_yellow_cc = ChanceCard(name='Free Ticket Booth',
                            free_ticket_booth=True,
                            free_ticket_booth_options=(fun_food_picnic_grove_spot, ultimate_idol_grandstand_spot))
    
    chance_card_deck.append(ftb_yellow_cc)

    ultimate_idol_grandstand_cc = ChanceCard(name='Go to the Ultimate Idol Grandstand', 
                                                  destination=ultimate_idol_grandstand_spot)
    chance_card_deck.append(ultimate_idol_grandstand_cc)

    water_show_spot = PenaltySpot(name='Pay $2 For the Water Show', fee=2)
    board.append(water_show_spot)

    water_show_cc = ChanceCard(name='Go to the Water Show and PAY $2', destination=water_show_spot)
    chance_card_deck.append(water_show_cc)

    board.append(chance_spot)

    go_to_lunch_spot = PenaltySpot(name='Go To Lunch - Pay $3', fee=3, destination=lunch_spot)
    board.append(go_to_lunch_spot)

    free_zone_drop_spot = BoardProperty(name='Free Zone Drop', 
                                        price=4, color='Green')
    board.append(free_zone_drop_spot)

    whirlwind_water_slide_spot = BoardProperty(name='Whirlwind Water Slide', 
                                               price=4, color='Green')
    board.append(whirlwind_water_slide_spot)

    free_zone_drop_spot.partner_spot = whirlwind_water_slide_spot
    whirlwind_water_slide_spot.partner_spot = free_zone_drop_spot

    ftb_green_cc = ChanceCard(name='Free Ticket Booth',
                            free_ticket_booth=True,
                            free_ticket_booth_options=(free_zone_drop_spot, whirlwind_water_slide_spot))
    
    chance_card_deck.append(ftb_green_cc)

    whirlwind_water_slide_cc = ChanceCard(name='Go to the Whirlwind Water Slide', 
                                          destination=whirlwind_water_slide_spot)
    chance_card_deck.append(whirlwind_water_slide_cc)

    red_rr_spot = BoardSpot(name='Red Line Railroad', roll_again=True)
    board.append(red_rr_spot)

    red_rr_cc = ChanceCard(name='Take a Ride on the Red Line Railroad', 
                            destination=red_rr_spot)
    chance_card_deck.append(red_rr_cc)

    supersonic_space_flight_spot = BoardProperty(name='Supersonic Space Flight', 
                                                 price=5, color='Blue')
    board.append(supersonic_space_flight_spot)

    echo_canyon_coaster_spot = BoardProperty(name='Echo Canyon Coaster', 
                                             price=5, color='Blue')
    board.append(echo_canyon_coaster_spot)

    supersonic_space_flight_spot.partner_spot = echo_canyon_coaster_spot
    echo_canyon_coaster_spot.partner_spot = supersonic_space_flight_spot

    ftb_bluee_cc = ChanceCard(name='Free Ticket Booth',
                              free_ticket_booth=True,
                              free_ticket_booth_options=(supersonic_space_flight_spot, echo_canyon_coaster_spot))

    ftb_bluee_cc2 = ChanceCard(name='Free Ticket Booth',
                               free_ticket_booth=True,
                               free_ticket_booth_options=(supersonic_space_flight_spot, echo_canyon_coaster_spot))

    chance_card_deck.append(ftb_bluee_cc)
    chance_card_deck.append(ftb_bluee_cc2)

    echo_canyon_coaster_cc = ChanceCard(name='Go to the Echo Canyon Coaster', 
                                        destination=echo_canyon_coaster_spot)
    chance_card_deck.append(echo_canyon_coaster_cc)

    shuffle(chance_card_deck)

    return board, chance_card_deck


class MonopolyJuniorGame:
    def __init__(self, player_names=(), monopoly_rules=False, verbose=False):
        # give each player 10 ticket booths,
        # unless there are only 2 players, 
        # then give 12 ticket booths
        ticket_booths = 10
        if len(player_names) == 2:
            ticket_booths = 12

        self.monopoly_rules = monopoly_rules
        self.verbose = verbose

        self.players = deque()
        for player_name in player_names:
            self.players.append(Player(player_name, ticket_booths, game=self, verbose=verbose))

        self.board, self.chance_card_deck = make_board_and_chance_card_deck()

        self.determine_player_order()

    def print_if_verbose(self, msg):
        if self.verbose:
            print(msg)

    def determine_player_order(self):
        # each player rolls the die, values get added to a list
        roll_value_list = []
        for i in self.players:
            roll_value_list.append(randint(1, 6))

        # if only one player has the highest value, determine that player's list index,
        # otherwise if more than one player has the highest value,
        # those players will proceed to roll again, until only one player has the highest value
        if roll_value_list.count(max(roll_value_list)) == 1:
            highest_roll_index = roll_value_list.index(max(roll_value_list))
        else:
            # determine which list indices are the highest value, and add them to a dictionary
            roll_value_by_index = dict()
            for i, roll_value in enumerate(roll_value_list):
                if roll_value == max(roll_value_list):
                    roll_value_by_index[i] = roll_value
            
            # keep rolling until only one player has the highest value
            while list(roll_value_by_index.values()).count(max(roll_value_by_index.values())) != 1:
                for i in roll_value_by_index.keys():
                    roll_value_by_index[i] = randint(1, 6)
            
            # find the highest value and return the original list index of that player
            for i, roll_value in roll_value_by_index.items():
                if roll_value == max(roll_value_by_index.values()):
                    highest_roll_index = i

        # Adjust player list so that the player with the highest roll goes first, 
        # while preserving the order, by using the collections.deque().rotate method
        self.players.rotate(-(highest_roll_index))

    def get_properties_by_player(self, player):
        # return a list of properties owned by player
        props = []
        for spot in self.board:
            try:
                if spot.owner == player:
                    props.append(spot)
            except AttributeError:
                pass
        return props
    

    def handle_chance_card(self, player):
        # get card from the "top" of the deck
        chance_card = self.chance_card_deck.pop()
        # place it at the "bottom" of the deck
        self.chance_card_deck.appendleft(chance_card)

        self.print_if_verbose(f'{player} drew the {chance_card} Chance card')


        if chance_card.free_ticket_booth:
            if not player.ticket_booths:
                self.print_if_verbose(f'{player} does not have any more ticket booths')
                return
                
            spot_options = chance_card.free_ticket_booth_options

            self.print_if_verbose(f'The {chance_card} Chance card is for the {spot_options[0].color} properties: {spot_options}')

            # condition for both properties being owned by the same player
            if spot_options[0].owner == spot_options[1].owner and spot_options[0].owner is not None:
                self.print_if_verbose(f'{spot_options[0].owner} already owns both {spot_options[0].color} properties.  ' \
                                      f'{player} will draw another Chance card')
                self.handle_chance_card(player)
                return

            # condition to check if either spot does not have an owner,
            # assign the first spot that doesn't have an owner to the current player
            for spot_option in spot_options:
                if not spot_option.owner:
                    self.print_if_verbose(f'{player} is getting a free ticket booth on {spot_option}')
                    spot_option.owner = player
                    player.ticket_booths -= 1
                    return
            
            # condition for both spots being owned by different players,
            # which are not the current player.
            #   i.e. player1 draws "free ticket booth" card, player2 owns one spot and player3 owns the other.
            # assign the spot owned by the player with more cash
            if player not in (spot_options[0].owner, spot_options[1].owner):
                if spot_options[0].owner.cash > spot_options[1].owner.cash:
                    spot_to_take = spot_options[0]
                else:
                    spot_to_take = spot_options[1]

                self.print_if_verbose(f'{player} is getting a free ticket booth on {spot_option}')
                self.print_if_verbose(f'{spot_option.owner} owned {spot_option} before {player} took it')

                spot_to_take.owner.ticket_booths += 1
                # switch owner to current player
                spot_to_take.owner = player
                player.ticket_booths -= 1
                return
            else:
                for spot_option in spot_options:
                    if spot_option.owner != player:
                        # TODO print a log statement that player is taking a free ticket booth on spot_option spot from the previous owner
                        spot_option.owner.ticket_booths += 1
                        spot_option.owner = player
                        player.ticket_booths -= 1
                        return

        elif chance_card.destination:
            if self.verbose:
                print(f'{player} is going to the spot "{chance_card.destination}"')
            old_board_spot_index = player.board_spot_index
            board_spot_index = self.board.index(chance_card.destination)
            player.board_spot_index = board_spot_index
            if 'Lunch' in chance_card.destination.name:
                player.pay(3)
            else:
                player.check_if_collect_go_money(old_board_spot_index)

            self.land_on_spot(player, chance_card.destination)

    def land_on_spot(self, player, board_spot):
        if self.verbose:
            print(f'{player} has landed on {board_spot}')

        spot_type = type(board_spot).__name__
        if spot_type == 'BoardProperty':
            if board_spot.owner == player:
                if self.verbose:
                    print(f'{player} already owns {board_spot}')
                return
            if not board_spot.owner:
                # if the player has enough cash and at least one ticket booth, 
                # they will buy the spot
                if (player.cash > board_spot.price) and player.ticket_booths:
                    if self.verbose:
                        print(f'{player} bought {board_spot} for ${board_spot.price}')
                    # player pays bank for the property
                    player.pay(board_spot.price)
                    # decrement player's ticket booth number
                    player.ticket_booths -= 1
                    board_spot.owner = player
                else:
                    no_buy_reason = 'cash'
                    if not player.ticket_booths:
                        no_buy_reason = 'ticket booths'
                    if self.verbose:
                        print(f'{player} does not have enough {no_buy_reason} to buy {board_spot}')
            else:
                if board_spot.owner == board_spot.partner_spot.owner:
                    fee = board_spot.price * 2
                    own_msg = f'both {board_spot.color} properties'
                else:
                    fee = board_spot.price
                    own_msg = board_spot.name
                
                if self.verbose:
                    print(f'{player} must pay {board_spot.owner} ${fee} because {board_spot.owner} owns {own_msg}')
                player.pay(fee, board_spot.owner)
                    
        elif spot_type == 'PenaltySpot':
            if self.verbose:
                print(f'{player} must {board_spot.name}')
            player.pay(board_spot.fee)
            if board_spot.destination:
                if self.verbose:
                    print(f'{player} does not collect $2')
                player.board_spot_index = self.board.index(board_spot.destination)
        elif board_spot.roll_again:
            if self.verbose:
                print(f'{player} is rolling again...')
            self.player_turn(player)
        elif board_spot.name == 'Chance':
            self.handle_chance_card(player)


    def player_turn(self, player):
        owned_spots = self.get_properties_by_player(player)
        self.print_if_verbose(f'#' * 10 + f'{player} has ${player.cash} and properties {owned_spots}')

        player.roll()

        board_spot = self.board[player.board_spot_index]

        self.land_on_spot(player, board_spot)
        

    def start(self):
        for player in cycle(self.players):
            self.player_turn(player)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--players', nargs='+', help='2-4 players')
    parser.add_argument('-m', '--monopoly-rules', action='store_true', 
                        help='This will enable regular Monopoly rules (not "Monopoly Junior")')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument("-g", "--games", type=int, default=1,
                        help="The number of games to simulate")

    return parser.parse_args()


def run_game(player_names=(), monopoly_rules=False, verbose=False):

    game = MonopolyJuniorGame(player_names=player_names, 
                              monopoly_rules=monopoly_rules, 
                              verbose=verbose)

    out_players = []
    while len(game.players) > 1:
        try:
            game.start()
        except OutOfCashError as err:
            out_player = err.args[0]
            if game.verbose:
                hashmarks = '#' * 50
                print(f'{hashmarks} {out_player} is out of the game! {hashmarks}')

            # if not playing monopoly_rules, 
            # end the game after the first player goes bankrupt
            if not game.monopoly_rules:
                break
            
            # add out_player to the list of out players
            out_players.append(out_player)

            # determine which position in the list out_player was
            out_player_index = game.players.index(out_player)

            # remove out of cash player from the game
            game.players.remove(out_player)

            # rotate the player list so that the player who was supposed to 
            # roll next is the first in the list when the game starts again
            game.players.rotate(-(out_player_index))

    if verbose:
        print('The game is over.  Results:')
        for player in list(game.players) + out_players:
            owned_spots = game.get_properties_by_player(player)
            print(f'{player} finished with ${player.cash}')
            print(f'{player} owns spots: {owned_spots}')

    game_result = dict()

    winner = None
    for player in list(game.players) + out_players:
        game_result[player.name] = {'cash': player.cash, 'winner': 0}

        if winner:
            if winner.cash < player.cash:
                winner = player
        else:
            winner = player

    game_result[winner.name]['winner'] = 1

    return game_result


def analyze_game_results(game_results):
    player_stats = dict()

    for game_result in game_results:
        for player, game_stats in game_result.items():
            try:
                player_stats[player]['cash'] += game_stats['cash']
                player_stats[player]['winner'] += game_stats['winner']
            except KeyError:
                player_stats[player] = {'cash': game_stats['cash'], 'winner': game_stats['winner']}

    sorted_stats_list = sorted(player_stats.items(), key=lambda item: item[1]['winner'], reverse=True)
    sorted_stats = dict(sorted_stats_list)
    for player, stats in sorted_stats.items():
        msg = f'### {player}\n' \
              f'    Cash:  ${stats["cash"]:,}\n' \
              f'    Wins:  {stats["winner"]:,}\n'
        print(msg)

def run_games(how_many_games, **kwargs):
    game_results = []
    def log_result(result):
        game_results.append(result)

    with Pool() as pool:
        pool_results = []
        for x in range(how_many_games):
            result = pool.apply_async(run_game, kwds=kwargs, callback=log_result)
            pool_results.append(result)

        pool.close()

        for pool_result in pool_results:
            pool_result.wait()

    return game_results

if __name__ == '__main__':
    args =  parse_args()

    if len(args.players) not in (2, 3, 4):
        raise Exception('You must have between 2 and 4 players')
    
    if args.games > 1 and args.verbose:
        print(f'Ignoring -v/--verbose when more than one game is being played')
        args.verbose = False
    
    # start games
    game_results = run_games(args.games, 
                             player_names=args.players, 
                             monopoly_rules=args.monopoly_rules,
                             verbose=args.verbose)

    # analyze games
    analyze_game_results(game_results)