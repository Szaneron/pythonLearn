def podwoj(x):
    return x * 2

def funkcja_dla_przefiltruj(x):
    if (x % 2) == 0:
        return x

print(podwoj(4))


my_list = [2, 14, 22, 7, 6, 4, 5, 17]

my_list_filtered = list(filter(lambda x: x % 2 == 0, my_list))
my_list_filtered2 = [x for x in my_list if(x % 2) == 0]

print(my_list_filtered)
print(my_list_filtered2)

