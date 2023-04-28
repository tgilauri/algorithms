def bfs(s, adj):
    # Тут храним стоимость прохода до вершины
    cost = [-1] * len(adj)
    # print('cost =', cost)
    # Стоимость пути s -> s = 0
    cost[s] = 0
    # print('cost =', cost)
    queue = [s]
    # print('queue =', queue)
    while queue:
        v = queue.pop(0)
        # запускаем обход из вершины v
        for key, value in adj[v].items():
            # проверка на посещенность
            if cost[key] == -1:
                # добавление вершины в очередь
                queue.append(key)
                # print('queue =', queue)
                # подсчитываем стоимость пути до вершины
                cost[key] = cost[v] + value
                # print('cost =', cost)
    return cost

def process_routes(input_fd, output_fd):
    input_rows = [line.strip() for line in input_fd]
    amount = int(input_rows[0])
    max_distance = int(input_rows[-2])
    start_city_idx, target_city_idx = map(lambda i: int(i), input_rows[-1].split(' '))
    cities = list(map(lambda city: list(map(lambda i: int(i), city.split(' '))), input_rows[1:-2]))

    adj = dict(dict())
    result = -1
    for i in range(len(cities)):
        for j in range(i):
            dist = abs(cities[i][0] - cities[j][0]) + abs(cities[i][1] - cities[j][1])
            if dist <= max_distance:
                if i in adj:
                    adj[i][j] = 1  # dist
                else:
                    adj[i] = {j: 1}  # dist
                if j in adj:
                    adj[j][i] = 1  # dist
                else:
                    adj[j] = {i: 1}  # dist
    # Выведем 'стоимость' пути из вершины city_from в city_to
    # Если cost[u] = -1, значит, вершина u недостижима из стартовой вершины
    if start_city_idx - 1 in adj and target_city_idx - 1 in adj:
        cost = bfs(start_city_idx - 1, adj)
        result = cost[target_city_idx - 1]

    output_fd.write(str(result))


input_file = open('./input.txt', 'r')

output_file = open('./output.txt', 'w')

process_routes(input_file, output_file)

output_file.close()
