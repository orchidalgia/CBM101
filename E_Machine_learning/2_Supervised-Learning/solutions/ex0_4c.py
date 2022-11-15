
#simple solution
def get_indeces(N, p):
    idxs = np.arange(N) # array of numbers 0-N

    c = int(pcnt(N, p)) # get index where to slice

    train = idxs[:c]
    test = idxs[c:]

    return train, test


# random selection
def get_indeces(N, p):
    idxs = np.arange(N)
    n_train = int(N * p)
    
    np.random.shuffle(idxs)
    
    train_idxs = idxs[:n_train]
    test_idxs = idxs[n_train:]
    
    return train_idxs, test_idxs
