from model.dataset import Dataset


def greed(dataset: Dataset):
    try:
        solution = [0]
        value = 0.0
        actual_node = 0

        while len(solution) < dataset.dimension:
            min_dist = float('inf')

            for candidate in range(0, len(dataset.dist_matrix[actual_node])):
                if dataset.dist_matrix[actual_node][candidate] < min_dist \
                        and candidate not in solution:
                    next_node = candidate
                    min_dist = dataset.dist_matrix[actual_node][candidate]

            solution.append(next_node)
            value = value + dataset.dist_matrix[actual_node][next_node]

            actual_node = next_node
        solution.append(0)
        value = value + dataset.dist_matrix[actual_node][0]

    except Exception as e:
        print(f'Faield when greed algorithm were running: {e}')

    print(solution, value)
