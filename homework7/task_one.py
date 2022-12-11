def get_winners(results):
    result = []
    sorted_winners = sorted(results, reverse=True)
    for points in range(3):
        result.append((results.index(sorted_winners[points])) + 1)
    return result


result = get_winners([550, 352, 600, 310, 500])
print(result)
