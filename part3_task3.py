num = input('Input numbers: ')
step = int(input('Input step: '))
num_1 = num.split()
def f(step,num_1):
    return num_1[-step:] + num_1[:-step]
print(f(step,num_1))


