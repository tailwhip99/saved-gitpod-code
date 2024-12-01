import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    matrix =np.array(input_list).reshape(3,3)

    calculations = {
        'mean' : [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean().item(),

        ],
        'variance' : [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().item(),

        ],
        'standard deviaton' : [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().item(),

        ],
      
        'max' : [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().item(),

        ],
        'min' : [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().item(),

        ],
        'sum' : [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().item(),

        ],
    }
    return calculations
 

  

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = calculate(input_list)

print(result)


    