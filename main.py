from preprocess.pre_processing_dataset import pre_processing_dataset
from solvers.greed_algorithm import greed

dataset = pre_processing_dataset('rat195')
greed(dataset)
