# Appends golden globe and critics choice data to existing csv

fd = open("alex_data.csv")
new_fd = open("new_alex_data.csv", 'w')

critics_choice_nominees = ['the-big-sick', 'call-me-by-your-name', 'darkest-hour', 'dunkirk', 'the-florida-project', 'get-out', 'lady-bird',
                           'the-papers', 'three-billboards-outside-ebbing-missouri','the-shape-of-water']
critic_winner = 'the-shape-of-water'
golden_nominees = ['call-me-by-your-name', 'three-billboards-outside-ebbing-missouri', 'dunkirk',
                    'the-papers', 'the-shape-of-water', 'lady-bird', 'the-disaster-artist', 'get-out', 'i-tonya']
# Note greatest showman was below our over 65 movie cutoff
golden_winners = ['lady-bird', 'three-billboards-outside-ebbing-missouri']

for line in fd:
    line = line.strip()
    lineArray = line.split(",")
    critic = -1
    globe = -1
    if lineArray[0] in critics_choice_nominees:
        critic = 5
    elif lineArray[0] == critic_winner:
        critic = 10

    if lineArray[0] in golden_nominees:
        globe = 5
    elif lineArray[0] in golden_winners:
        globe = 10

    line = line + ",{},{}\n".format(critic, globe)
    new_fd.write(line)
