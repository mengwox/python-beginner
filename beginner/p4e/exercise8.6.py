array = []
while True:
    try:
        num_str = input('Enter a number:')
        if num_str == 'done':
            break
        array.append(float(num_str))
    except ValueError:
        print('input is not a legal number')

print('Maximum:', max(array))
print('Minimum:', min(array))
