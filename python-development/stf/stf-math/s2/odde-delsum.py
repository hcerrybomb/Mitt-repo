index = 1
sum1 = 1
sum2 = 1
while sum1 < 3003:
    print(index, sum1, sum2)
    index += 1
    sum1 += index
    sum2 += sum1
print(f"\nsvar: {index} {sum1} {sum2}\n")
    

