import numpy as np
from l2_distance import l2_distance
from utils import *

def run_knn(k, train_data, train_labels, valid_data):
    """Uses the supplied training inputs and labels to make
    predictions for validation data using the K-nearest neighbours
    algorithm.

    Note: N_TRAIN is the number of training examples,
          N_VALID is the number of validation examples, 
          and M is the number of features per example.

    Inputs:
        k:            The number of neighbours to use for classification 
                      of a validation example.
        train_data:   The N_TRAIN x M array of training
                      data.
        train_labels: The N_TRAIN x 1 vector of training labels
                      corresponding to the examples in train_data 
                      (must be binary).
        valid_data:   The N_VALID x M array of data to
                      predict classes for.

    Outputs:
        valid_labels: The N_VALID x 1 vector of predicted labels 
                      for the validation data.
    """

    dist = l2_distance(valid_data.T, train_data.T)
    nearest = np.argsort(dist, axis=1)[:,:k]

    train_labels = train_labels.reshape(-1)
    valid_labels = train_labels[nearest]

    # note this only works for binary labels
    valid_labels = (np.mean(valid_labels, axis=1) >= 0.5).astype(np.int)
    valid_labels = valid_labels.reshape(-1,1)

    return valid_labels

if __name__ == '__main__':
    """
    Script that runs kNN for different values of k and plots the clasification rate on the validation set.   
    """
    train_input, train_target = load_train()
    valid_input, valid_target = load_valid()
    test_input, test_target = load_test()
    
    for k in [1,3,5,7,9]:
        pred_val = run_knn(k, train_input, train_target, valid_input)
        val_rate = np.mean(pred_val == valid_target)
        pred_test = run_knn(k, valid_input, valid_target, test_input)
        test_rate = np.mean(pred_test == test_target)
        print "k =", k, ", classification rate on set set =", test_rate
        
    
    
