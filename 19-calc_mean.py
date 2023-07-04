def calculate_mean(list):
    sum=0
    for i in list:
        sum+=i
    l = len(list)
    mean = sum/l
    return mean

l = [1,2,3,4,5,6,7,8,9]
mean_value = calculate_mean(l)
print("Mean:", mean_value)