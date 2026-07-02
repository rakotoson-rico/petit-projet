mot = ["radar"]
mots_inverse = []
r= 0
for i in mot:
    mots_inverse.insert(0,i)
if mots_inverse==mot:
    print(True)
print(mots_inverse)

def palindrome(mots):
    mots_inverse = []
    for mot in mots:
        mots_inverse.insert(0,mot)
    return mots_inverse

def verification():
    if mots_inverse == mot:
        return True

# def appelation():
#     palindrome()
#     verification()

mot = ["radar"]
palindrome(mot)
appelation(mot)
