from math import sqrt
from model.dataset import Dataset


def pre_processing_dataset(dataset_name: str):
    try:
        with open(f'datasets/{dataset_name}.tsp') as file:
            dataset_raw = file.readlines()

        dataset_dimension = int(dataset_raw[3].split(': ')[1])

        distance_matrix = [
            [0 for col in range(dataset_dimension)]
            for row in range(dataset_dimension)
        ]

        for index_node1 in range(6, len(dataset_raw) - 1):
            node1_splited = dataset_raw[index_node1].split(' ')

            for index_node2 in range(6, len(dataset_raw) - 1):
                node2_splited = dataset_raw[index_node2].split(' ')

                if index_node1 == index_node2:
                    distance_matrix[index_node1 -
                                    6][index_node2 - 6] = float('inf')
                else:
                    distance_matrix[index_node1 - 6][index_node2 - 6] = sqrt(
                        (float(node1_splited[1]) -
                         float(node2_splited[1])) ** 2
                        +
                        (float(node1_splited[2]) -
                         float(node2_splited[2])) ** 2
                    )

        return Dataset(
            dataset_name, dataset_dimension, distance_matrix
        )

    except Exception as e:
        print(f'Faield to open dataset {e}')
        return None
