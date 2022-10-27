# recursion is a function that calls itself
#    recursion is a function that calls itself
#       recursion is a function that calls itself
#            recursion is a function that calls itself

def iterative_factor(n):
    fact = 1
    for i in range (2, n + 1):
        fact *= i
        print(fact)
    return fact
print(iterative_factor(5))


def function2(n):
    if n == 1: return n
    else: return n * function2(n-1)

print(function2(5))

# permutation using recurrsion display each combination of a string
def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)

print(permute("ABCD", ""))
