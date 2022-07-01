letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1] # reverse string based array from 1-25 || this omits starting character and anything beyond 25
backwards2 = letters[25::-1] # reverse string based 25- to end || this starts from array position 25 and show cases everything from that point
backwards3 = letters[::-1] #reverse whole string || reverses entire string no matter how large
print(backwards)
print(backwards2)
print(backwards3)