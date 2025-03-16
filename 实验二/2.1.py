import numpy as np

array_1 = np.arange(0, 1, 0.01)
another_array_1 = np.linspace(0, 1, 100)

array_2 = np.random.normal(size=(1, 100))

score_matrix = np.loadtxt('stu.txt', skiprows=1)
stu_average = np.mean(score_matrix, axis=1)
subject_max = np.max(score_matrix, axis=0)
subject_min = np.min(score_matrix, axis=0)
