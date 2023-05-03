def get_table(results):
    table = {}
    for result in results:
        tm_one_name, tm_two_name, scores = map(lambda x: x.strip(), result.split('-'))
        tm_one_scores, tm_two_scores = map(lambda x: int(x.strip()), scores.split(':'))
        if not table.get(tm_one_name):
            table[tm_one_name] = {
                'points': 0,
                'scores': 0,
                'results': {},
                'wins': 0,
                'looses': 0,
                'draws': 0
            }
        if not table.get(tm_two_name):
            table[tm_two_name] = {
                'points': 0,
                'scores': 0,
                'results': {},
                'wins': 0,
                'looses': 0,
                'draws': 0
            }

        table[tm_one_name]['scores'] += tm_one_scores
        table[tm_two_name]['scores'] += tm_two_scores

        if tm_one_scores > tm_two_scores:
            table[tm_one_name]['points'] += 3
            table[tm_one_name]['wins'] += 1

            table[tm_two_name]['looses'] += 1
        elif tm_one_scores < tm_two_scores:
            table[tm_two_name]['points'] += 3
            table[tm_two_name]['wins'] += 1

            table[tm_one_name]['looses'] += 3
        else:
            table[tm_one_name]['points'] += 1
            table[tm_two_name]['scores'] += 1

            table[tm_one_name]['draws'] += 1
            table[tm_two_name]['draws'] += 1

        table[tm_one_name]['results'][tm_two_name] = scores
        table[tm_two_name]['results'][tm_one_name] = scores[::-1]

    return table





print(get_table([
    'Linux - Gentoo - 1:0',
    'Gentoo - Windows - 2:1',
    'Linux - Windows - 0:2',
]))
