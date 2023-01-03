word = 'Hydrophobic'
print(word[0])

print(word[-1])
print(word[3:7])
word2 = word[3:7]

word3 = word + word2
print(word3)
print(word3 * 2)

if "roph" in word:
    print("Found")

if "Z" not in word:
    print("Well done!")

word4 = (word2[slice(0,4)])

print(word4)


for alpha in range(97,123):
    print(chr(alpha),end="")
