nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        break
    print(num)

# break break out of the loop
# continue move on to the next iteration of the loop

for num in nums:
    if num == 3:
        continue
    print(num)

for num in nums:
    for letter in 'abc':
        print(num, letter)

for i in range(1, 11):  # start point
    print(i)

x = 0
while x < 10:
    if x==5:
        break
    print(x)
    x += 1


# control + C to stop infinite loop


x = 0
while True:
    print(x)
    x += 1
