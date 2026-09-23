import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    first_vector = np.array([x], dtype=float)
    second_vector = np.array([y], dtype=float)
    sum_vectors = first_vector + second_vector
    vector_multiply = np.multiply(first_vector, second_vector)
    result = np.sum(vector_multiply)
    return float(result)     
    
