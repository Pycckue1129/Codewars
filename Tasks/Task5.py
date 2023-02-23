def count_sheep(n):
    # your code
    count = ''
    for i in range(n):
        count += str(i + 1) + ' ' + 'sheep...'
    print(count)


count_sheep(10)