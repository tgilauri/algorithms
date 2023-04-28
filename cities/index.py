def search(city_n, graph):
    search_queue = []
    search_queue[s] = 0

def get_distance(city_from, city_to):
    return abs(city_from[0] - city_to[0]) + abs(city_from[1] - city_to[1])


def find_route(cities, max_distance, start_city_idx, target_city_idx):
    result = None
    connections = get_connections_list(cities)

    for idx in range(start_city_idx - 1, target_city_idx - 1):
        distance = get_distance(cities[idx], cities[idx + 1])
        if distance <= max_distance:
            result = min(result, distance) if result is not None else distance
    return result if result is not None else -1


def get_connections_list(cities):
    result = []
    for i in range(len(cities)):
        result.append([])
        for j in range(len(cities)):
            result[i].append(j)
    return result


def process_routes(input_fd, output_fd):
    input_rows = [line.strip() for line in input_fd]
    max_distance = int(input_rows[-2])
    start_city_idx, target_city_idx = map(lambda i: int(i), input_rows[-1].split(' '))
    cities = list(map(lambda city: list(map(lambda i: int(i), city.split(' '))), input_rows[1:-2]))

    result = find_route(start_city_idx=int(start_city_idx), target_city_idx=int(target_city_idx),
                        max_distance=max_distance, cities=cities)

    output_fd.write(str(result))


input_file = open('./input.txt', 'r')

output_file = open('./output.txt', 'w')

process_routes(input_file, output_file)

output_file.close()
