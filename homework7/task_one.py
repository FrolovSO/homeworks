def number_of_winner(results):
    sorted_results = list(reversed(sorted(results)))
    winer_number = []

    for i in sorted_results[0:3]:
        winer_number.append(results.index(i)+1)

    print(winer_number)


results = number_of_winner([115, 352, 660, 5, 500])
