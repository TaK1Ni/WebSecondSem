def compute_average_scores(score):
    avg_sum = [0] * len(score[0]) 
    for i in range(len(score)):
        for j in range(len(score[i])):
            avg_sum[j]+=score[i][j]

    for i in range(len(avg_sum)): avg_sum[i]/=len(score)
    return avg_sum


