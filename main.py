# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#Part 1

#1
scorer_1 = 'Ruud Gullit '
scorer_2 = 'Marco van Basten '

#2
goal_0 = 32
goal_1 = 54

#3
scorers = scorer_1 +''+ str(goal_0) + ', ' + scorer_2 + '' + str(goal_1)
print(scorers)

#4
report = f'{scorer_1}scored in the {goal_0}nd minute' '\n' f'{scorer_2}scored in the {goal_1}th minute' 
print(report)

#part 2

#1
player = 'Erwin Koeman'

#2
first_name = player[:5]
print(first_name)

#3
last_name_len = len(player[6:])
print(last_name_len)

#4
name_short = player[:1] + '. ' + player[6:]
print(name_short)

#5
chant = (first_name + '!' + ' ') * 4 + (first_name + '!')
print(chant)

#6
good_chant = chant[-1:] != ''
print(good_chant)
