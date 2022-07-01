letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1] # reverse string based array from 1-25 || this omits starting character and anything beyond 25
backwards2 = letters[25::-1] # reverse string based 25- to end || this starts from array position 25 and show cases everything from that point
backwards3 = letters[::-1] #reverse whole string || reverses entire string no matter how large
print(backwards)
print(backwards2)
print(backwards3)
challenge1 = letters[16:13:-1] 
print(challenge1)
challenge2 = letters[4::-1] 
print(challenge2)
challenge3 = letters[25:25-8:-1] 
print(challenge3)

pythonIdiom = letters[::-1] # this is for reversing string

print(letters[-1:]) # this is for getting last digit

print(letters[:1]) # this is for getting first digit

print(letters[0]) # this gets first digit however if string is empty will result in error
