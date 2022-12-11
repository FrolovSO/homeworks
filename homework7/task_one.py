def number_of_winner(results):
    length = len(results)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if results[j] > results[j + 1]:
                temp = results[j]
                results[j] = results[j + 1]
                results[j + 1] = temp
    winners_results = results[::-1]
    print(winners_results[0:3])


results = number_of_winner([115, 352, 0, 600, 500])
