word = input('Write one word: ').replace(' ', '')
lower = 0
upper = 0
number = 0
symbols = 0
for i in word:
    if i.islower() == True:
        lower +=1
    elif i.isupper()== True:
        upper +=1
    elif i.isnumeric() == True:
        number +=1
    else:
        symbols +=1

letters = lower + upper

def per_of(word):
    lower_p = [lower*100/letters]
    upper_p = [upper*100/letters]
    print('Lower: %.2f%%',lower_p)
    print('Upper: %.2f%%',upper_p)

per_of(word)
