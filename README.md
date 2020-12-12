# roster_generator

Try the new main_with_ui.py version of roster_generator!  The UI makes it easier to use!

This program takes in a list of players, prices and positions, the budget price as well as the acceptable amount of money to be unused to generate all the possible standard fantasy football rosters consisting of one qb, two rbs, three wrs, one te, one def and one flex (either an rb, wr or te).

The players.csv, as well as the main.py file must be present to run the program.

After running the first menu option of the program, a rosters.csv file is generated.  This is required to exist in order to run the second menu option of filtering rosters.

A sample players.csv file is provided.  The schema of Player, Price, Position must be followed and the minimum amount of players for at least one roster must exist to run this program.

To try this program start by running the main.py file.

Next select "1" to run the create new rosters program.

Next enter a budget of 50000 (standard for draft kings).

Next enter 200 (this is telling the program to return only rosters that have a budget of 50000, 49000 and 48000)

The program will begin to calculate how many rosters are valid and after it is complete you should generate a rosters.csv file that contains 1,276,030 unique rosters from the players.csv file that fit the parameters of a budget of 50000 and only not using up to 200 of that budget.

Now that you have a rosters.csv file you can run the main.py file again only this time select 2 to filter rosters.

The program will read into memory the rosters.csv file you just created.

Next you will be asked to enter a players name.  Enter Aaron Rogers (a name from the players.csv file).

Next you'll be asked if you'd like to enter another name or run the filter. For this demo select y.

You are now prompted to enter a name.  Enter Mike Davis (another name from the players.csv file).

Now when prompted if you'd like to filter another name press r (this runs the filter).

You should generate 28,049 unique rosters that have both Aaron Rogers and Mike Davis on them.  The file generated is filter<Timestamp>.csv which allows for you to generate multiple filtered rosters and since they are pulled from your orignial rosters.csv file you know they have a budget of either 50000, 49000, 48000.




