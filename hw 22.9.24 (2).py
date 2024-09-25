# START

player_num = 0
highest_player = None
smallest_player = None
players_higher_2 = 0
player_height_sum = 0
players_above_avg = 0

x: float = float(input("Enter a player height(to stop the program enter -999): "))
player_list: list[float] = []

while x != -999:
    x: float = float(input("Enter a player height(to stop the program enter -999): "))
    if x < 1.6 or x > 3:
        continue
    player_list.append(x)
    player_num += 1
    player_height_sum += x
    if highest_player is None or x > highest_player:
        highest_player = x
    if smallest_player is None or x < smallest_player:
        smallest_player = x
    if x > 2.0:
        players_higher_2 += 1
else:
    avg_height = player_height_sum / player_num
    print(f"{player_num} players were registered!")
    print(f"The tallest player is {highest_player}!")
    print(f"Smallest player is {smallest_player}!")
    print(f"The average height is {avg_height}!")
    print(f"{players_higher_2} player higher then 2.0!")
    for i in range(0, len(player_list)):
        if player_list[i] > avg_height:
            players_above_avg += 1
    print(f"player above average is {players_above_avg}")




# END