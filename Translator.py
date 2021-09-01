# Translator function

def translate(phrase):
    translation = ""
    for i in phrase:
        if i.lower() in "aeiou":
            # if i.isupper():
            # translation = translation +"A"
            translation = translation + '*'
        else:
            translation = translation + i
    return translation


print(translate(input("Enter a phrase :\t")))
