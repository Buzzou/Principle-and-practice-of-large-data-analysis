import numpy as np
array_1 = np.arange(0, 1, 0.01)

array_2 = np.random.normal(size=(1, 100))

score_matrix = np.loadtxt('stu.txt', skiprows=1)
stu_average = np.mean(score_matrix, axis=1)
subject_average = np.mean(score_matrix, axis=0)
