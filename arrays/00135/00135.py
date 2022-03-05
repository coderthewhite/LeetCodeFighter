
def candy(ratings):
    left = [1] * len(ratings)
    right = [1] * len(ratings)
    for index in range(1, len(ratings)):
        if ratings[index] > ratings[index - 1]:
            left[index] = left[index - 1] + 1
    
    for index in range(len(ratings) - 2, -1, -1):
        if ratings[index] > ratings[index + 1]:
            right[index] = right[index + 1] + 1
            
    total = 0
    for index in range(len(left)):
        total += max(left[index], right[index])
    return total