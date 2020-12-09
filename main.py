# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# / Title: Roster Generator (Orignial Title- Flex Optimizer)                                                                                             /
# / Author: Adam Noor                                                                                                 /
# / Date Created: December 7, 2018                                                                                   /
# / Date Updated: December 9, 2020                                                                                                                  /
# / Description: This program takes in a players.csv file containing fantasy football players, prices,                /
# / positions,  and creates a rosters.csv file with every viable roster                                              /
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# Libraries
import time
import csv
from itertools import combinations
from datetime import datetime



# Player Object
class Player:
	def __init__(self, name, price, position, id):
		self.name = name
		self.price = price
		self.position = position
		self.id = id

class Group:
	def __init__(self, price, players):
		self.price = price,
		self.players = players

# Global Variables
all_players = []
flex_players = []
quarter_backs = []
running_backs = []
wide_receivers = []
tight_ends = []
defenses = []
rb_combos = []
wr_combos = []
rb_wr_combos = []
rb_wr_te_combos = []
flex_groups = []
final_rosters = []
created_rosters = []
qb_df_groups = []
qb_df_combos = []
all_but_flex = []
players_csv = 'players.csv'     # This variable holds the name of the file that is exported
rosters_csv = 'rosters.csv'     # This variable holds the name of the file that is exported
filtered_csv = 'filtered.csv'
budget = 50000  # This variable sets the total budget for the roster
money_left_on_table = 1000
iterations = 10000     # This variable sets how often progress is shown in the console as the program runs
start_time = datetime.now()



def start_program():
        user_choice = 3
        user_choice = int(input("Select an option:\nCreate new rosters(Press 1)\nFilter current rosters(Press 2)\nQuit (Press 0)\n"))
        if user_choice == 1:
                run_main()
        elif user_choice == 2:
                run_filter()
        else:
                print("Program Exited")


def read_players():
	with open(players_csv, 'r') as csv_file:
		csv_reader = csv.reader(csv_file)

		next(csv_reader)  # this functions avoids the header being the first object of the list
		count = 0
		for line in csv_reader:

		    player: Player = Player(line[0], int(line[1]), line[2], count)
		    count+=1

		    if not all_players:
			    all_players.insert(0, player)
		    else:
			    all_players.append(player)

def user_input():
	global budget
	budget = int(input("What is the budget? "))
	global money_left_on_table
	money_left_on_table = int(input("What is the maximum amount allowed to leave unused? "))




def create_player_arrays():
	for player in all_players:
		if player.position == "QB":
		    if not quarter_backs:
			    quarter_backs.insert(0, player)
		    else:
			    quarter_backs.append(player)
		elif player.position == "RB":
			if not running_backs:
				running_backs.insert(0, player)
			else:
				running_backs.append(player)
			if not flex_players:
				flex_players.insert(0, player)
			else:
				flex_players.append(player)
		elif player.position == "WR":
			if not wide_receivers:
				wide_receivers.insert(0, player)
			else:
				wide_receivers.append(player)
				
			if not flex_players:
				flex_players.insert(0, player)
			else:
				flex_players.append(player)
		elif player.position == "TE":
			if not tight_ends:
				tight_ends.insert(0, player)
			else:
				tight_ends.append(player)
				
			if not flex_players:
				flex_players.insert(0, player)
			else:
				flex_players.append(player)
		elif player.position == "DF":
			if not defenses:
				defenses.insert(0, player)
			else:
				defenses.append(player)


def set_running_backs():
	combo = combinations(running_backs, 2)
	for p in list(combo):

		if not rb_combos:
			rb_combos.insert(0, p)
		else:
			rb_combos.append(p)


def set_wide_receivers():
	combo = combinations(wide_receivers, 3)
	for p in list(combo):
		if not wr_combos:
			wr_combos.insert(0, p)
		else:
			wr_combos.append(p)
	print("Done 1 of 6.  The number of players is " + str(len(all_players)))


def combine_wr_rb():
	p = -1
	while p < len(rb_combos) - 1:
		p += 1
		q = 0
		while q < len(wr_combos):
			current_array = [rb_combos[p][0], rb_combos[p][1], wr_combos[q][0], wr_combos[q][1], wr_combos[q][2]]
			if not rb_wr_combos:
				rb_wr_combos.insert(0, current_array)
			else:
				rb_wr_combos.append(current_array)
			q += 1
	print("Done 2 of 6.  The number of RB/WR combos is " + str(len(rb_wr_combos)))


def combine_wr_rb_te():
	p = -1
	while p < len(tight_ends) - 1:
		p += 1
		q = 0
		while q < len(rb_wr_combos):
			current_array = [tight_ends[p], rb_wr_combos[q][0], rb_wr_combos[q][1], rb_wr_combos[q][2],
					 rb_wr_combos[q][3], rb_wr_combos[q][4]]
			if not rb_wr_te_combos:
				rb_wr_te_combos.insert(0, current_array)
			else:
				rb_wr_te_combos.append(current_array)
			q += 1
	print("Done 3 of 6.  The number of RB/WR/TE combos is " + str(len(rb_wr_te_combos)))



def set_qb_df_group():
	count = 0
	for qb in quarter_backs:
		for df in defenses:
			group: Group = Group(qb.price + df.price, [qb, df])
			if not qb_df_groups:
				qb_df_groups.insert(0, group)
			else:
				qb_df_groups.append(group)
	print("Done 4 of 6.  The number of QB/DF combos is " + str(len(qb_df_groups)))
			
		

def old_set_flex_group():
	lcl_array = []
	print('Setting the flex groupings, this may take some time.\nIf it last longer than 4 minutes, consider reducing the number of players.')
	p = -1
	while p < len(flex_players) - 1:
		p += 1
		q = 0
		while q < len(rb_wr_te_combos):
			if flex_players[p] in rb_wr_te_combos[q]:
				pass
			else:
				current_array = [rb_wr_te_combos[q][0], rb_wr_te_combos[q][1], rb_wr_te_combos[q][2],
						 rb_wr_te_combos[q][3], rb_wr_te_combos[q][4], rb_wr_te_combos[q][5],
						 flex_players[p]]

				price = rb_wr_te_combos[q][0].price + rb_wr_te_combos[q][1].price + rb_wr_te_combos[q][2].price + rb_wr_te_combos[q][3].price + rb_wr_te_combos[q][4].price + rb_wr_te_combos[q][5].price + flex_players[p].price
				if (price >= budget):
					pass
				else:
					group: Group = Group(price, current_array)
					
					if not flex_groups:
						flex_groups.insert(0, group)
					else:
						flex_groups.append(group)
			q += 1
	

def set_flex_group():
        timestamp = datetime.now()
        potential_flex_groups = str(len(rb_wr_te_combos) * (len(flex_players) - 1))
        estimated_fast = round((int(potential_flex_groups) / 1000000) * 3, 2)
        estimated_slow = round((int(potential_flex_groups) / 1000000) * 6, 2)

        count = 0
        lcl_array = []
        print("Setting the flex groupings, this may take some time.\nThere are " + potential_flex_groups + " potential flex groups.")
        print("The estimated time to complete flex groupings is between\n" + str(estimated_fast) + " seconds and " + str(estimated_slow) + " seconds")
        p = -1
        while p < len(rb_wr_te_combos) - 1:
                p += 1
                q = 0
                while q < len(flex_players):
                        if flex_players[q] in rb_wr_te_combos[p]:
                                count += 1
                                #pass
                        else:
                                price = rb_wr_te_combos[p][0].price + rb_wr_te_combos[p][1].price + rb_wr_te_combos[p][2].price + rb_wr_te_combos[p][3].price + rb_wr_te_combos[p][4].price + rb_wr_te_combos[p][5].price + flex_players[q].price
                                if (price >= budget):
                                        q = len(flex_players)
                                        count += 1
                                        # pass
                                else:
                                        current_array = [rb_wr_te_combos[p][0], rb_wr_te_combos[p][1], rb_wr_te_combos[p][2],
                                                         rb_wr_te_combos[p][3],rb_wr_te_combos[p][4], rb_wr_te_combos[p][5],
                                                         flex_players[q]]
                                        group: Group = Group(price, current_array)
                                        count += 1
                                        if not flex_groups:
                                                flex_groups.insert(0, group)
                                        else:
                                                flex_groups.append(group)
                        q += 1
                        if count % 1000000 == 0:
                                print(str(len(flex_groups)) + ' flex groups have been created in ' + str((datetime.now() - timestamp).seconds) + ' seconds')
       
        print('Done 5 of 6.\n' + str(len(flex_groups)) + ' valid flex groups were created\nof a possible ' + potential_flex_groups + ' flex groups in ' + str((datetime.now() - timestamp).seconds) + ' seconds')

def create_rosters():

        print("There are " + str((len(flex_groups) * len(qb_df_groups))) + " potential rosters when not considering price")
        global iterations
        iterations = 0
        sorted_qb_df = sorted(qb_df_groups, key=lambda x: x.price[0])
        sorted_flex = sorted(flex_groups, key=lambda x: x.price[0])
        for qb_df in sorted_qb_df:
                count = 0
                while count < len(sorted_flex):
                        iterations += 1
                        if iterations % 5000000 == 0:
                                print(str(iterations) +' iterations and '+ str(len(final_rosters)) + ' rosters have been created')
                        price = qb_df.price[0] + sorted_flex[count].price[0]
                        money_on_table = budget - price
                        if price > budget:
                                count = len(sorted_flex)
                        elif price < budget - money_left_on_table:
                                count += 1
                        else:                   
                                if not final_rosters:
                                        final_rosters.insert(0, [qb_df, sorted_flex[count], money_on_table])
                                else:
                                        final_rosters.append([qb_df, sorted_flex[count], money_on_table])
                                count += 1
        


	
def write_rosters():
	print("Through iterating " + str(iterations) + " times it has been determined there are " + str(len(final_rosters)) + " valid rosters")

	count = 0
	
	with open(rosters_csv, 'w') as f:
		the_writer = csv.writer(f)
		the_writer.writerow(['QB', 'RB1', 'RB2', 'WR1', 'WR2', 'WR3', 'TE', 'DF', 'FX', '$ Unused'])
		lcl_roster_array = []
		for player in final_rosters:
			qb = player[0].players[0].name
			rb1 = player[1].players[1].name
			rb2 = player[1].players[2].name
			wr1 = player[1].players[3].name
			wr2 = player[1].players[4].name
			wr3 = player[1].players[5].name
			te = player[1].players[0].name
			df = player[0].players[1].name
			fx = player[1].players[6].name
			amt = player[2]
			lcl_roster = [qb, rb1, rb2, wr1, wr2, wr3, te, df, fx, amt]
			the_writer.writerow(lcl_roster)

			if not lcl_roster_array:
				lcl_roster_array.insert(0, lcl_roster)
			else:
				lcl_roster_array.append(lcl_roster)
			count += 1
			if count % 100000 == 0:
				print(str(count) + ' rosters created')

	created_rosters = lcl_roster_array		
	print("Done 6 of 6.  " + str(len(created_rosters)) + " rosters were created in " + str((datetime.now() - start_time).seconds) + " seconds")


def read_rosters():
        print("Reading rosters.csv file...")
        with open(rosters_csv, 'r') as csv_file:
                csv_reader = csv.reader(csv_file)

                next(csv_reader)  # this functions avoids the header being the first object of the list
                count = 0
                for line in csv_reader:
                        lcl_roster = [line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9]]
                        count += 1
                        if not created_rosters:
                                created_rosters.insert(0, lcl_roster)
                        else:
                                created_rosters.append(lcl_roster)
                        if count % 100000 == 0:
                                print(str(count) + " rosters have been read")
        print(str(len(created_rosters)) + " rosters have been read")

def user_filter():
        filtered_array = []
        filtered_rosters_array = []
        trigger = 'y'
        
        while trigger == 'y':
                filtered_array.append(str(input("Enter a player to filter? ")))
                print("Players that must be in the roster: " + str(filtered_array))
                trigger = str(input("\nPress y to filter another player,\npress r to run filter\n"))

        print("Filtering Rosters...")

        for roster in created_rosters:
                if all(i in roster for i in filtered_array):
                        filtered_rosters_array.append(roster)
        print("There are " + str(len(filtered_rosters_array)) + " rosters that include " + str(filtered_array))
        trigger = str(input("Press y to write rosters\nPress any other key to start the filter process again "))
        if trigger == 'y':
                count = 0

                with open('filtered' + str(datetime.now()) + '.csv', 'w') as f:
                        the_writer = csv.writer(f)
                        the_writer.writerow(['QB', 'RB1', 'RB2', 'WR1', 'WR2', 'WR3', 'TE', 'DF', 'FX', '$ Unused'])
                        lcl_roster_array = []
                        for player in filtered_rosters_array:
                                qb = player[0]
                                rb1 = player[1]
                                rb2 = player[2]
                                wr1 = player[3]
                                wr2 = player[4]
                                wr3 = player[5]
                                te = player[6]
                                df = player[7]
                                fx = player[8]
                                amt = player[9]
                                lcl_roster = [qb, rb1, rb2, wr1, wr2, wr3, te, df, fx, amt]
                                the_writer.writerow(lcl_roster)

                                if not lcl_roster_array:
                                        lcl_roster_array.insert(0, lcl_roster)
                                else:
                                        lcl_roster_array.append(lcl_roster)
                                count += 1
                                if count % 100000 == 0:
                                        print(str(count) + ' rosters created')
        else:
                user_filter()

        print(str(len(lcl_roster_array)) + " rosters have been created.")

                #filtered_rosters = lcl_roster_array
                                        
                      
        

def run_main():
	read_players()
	create_player_arrays()
	user_input()
	set_running_backs()
	set_wide_receivers()
	combine_wr_rb()
	combine_wr_rb_te()
	set_qb_df_group()
	set_flex_group()
	create_rosters()
	write_rosters()
	
def run_filter():
        read_rosters()
        user_filter()
        

start_program()





