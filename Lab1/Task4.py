num_list = []

while(True):
    a = float(input('Введіть число:'))
    if a == 0:
        break

    num_list.append(a)
    print('Кількість чисел: ', len(num_list))
    print('Сума чисел: ', sum(num_list))
    print('Максимальне число: ', max(num_list))
    print('Мінімальне число: ', min(num_list))
    print('Середнє арифметичне: ', sum(num_list)/len(num_list))
    num_pos_count = 0
    num_neg_count = 0
    for num in num_list:
        if(num > 0):
            num_pos_count += 1
        else:
            num_neg_count += 1

    print('Кількість додатніх чисел: ', num_pos_count)
    print('Кількість від\'ємних чисел: ', num_neg_count)


