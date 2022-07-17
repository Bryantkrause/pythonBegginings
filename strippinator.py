filename = '.\\Jabberwocky.txt'

with open(filename) as poem:
    first = poem.readline().strip()

print(first)

# strip on works based on characters from ends based on characters provided
chars = "'Twas b"
noApost = first.strip(chars)
print(noApost)

for character in first:
    if character in chars:
        print(f'removing "{character}"')
    else:
        break 
print("thingy thingy thingy")

twas_removed = first.removeprefix("'Twas")
print(twas_removed)
toves_removed = first.removesuffix("toves")
print(toves_removed)


def removeprefix(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]


def removesuffix(string: str, suffix: str) -> str:
    if suffix and string.endswith(suffix):
        return string[len(suffix)]
    else:
        return string[:]


twas_removed = removeprefix(first, "'Twas")
toves_removed = removesuffix(first, "toves")

print(twas_removed)
print(toves_removed)
