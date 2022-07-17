# jabber = open('.\\TextFiles\\Jabberwocky.txt', 'r')

# for line in jabber:
#     print(line.strip())
#     # print(len(line))

# jabber.close()

with open('.\\TextFiles\\Jabberwocky.txt', 'r') as jabber:
    # for line in jabber:
    #     print(line.rstrip())
    lines = jabber.readlines() 
print(lines)
print(lines[-1:])

#  lines = jabber.readlines() displays each line break this only works best with small files due to computer memory stuff 

with open('.\\TextFiles\\Jabberwocky.txt', 'r') as jabber2:
    text = jabber2.read()
print(text)

for boob in reversed(text):
    print(boob, end='')

with open('.\\TextFiles\\Jabberwocky.txt', 'r') as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break

print('break break break breeeeeeeeeeaak')

with open('.\\TextFiles\\Jabberwocky.txt', 'r') as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break
