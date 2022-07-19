# jabber = open('.\\Jabberwocky.txt', 'r')

# for line in jabber:
#     print(line)

# jabber.close()

with open('Jabberwocky.txt', encoding='utf-8') as jabber:
    for line in jabber:
        print(line.rstrip())
