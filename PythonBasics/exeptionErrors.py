# Handling exception errors: Try-except
new_list = [2,4,6, 'California']

# When it runs into an error, it will run except
for element in new_list:
    try:
        print(element/2)
    except:
        print("The element is not a number")

# While-Break (while loop)
n = 4
while n > 0:
    print(n)
    n = n - 1
    if n==2:
        break

print('Loop ended')