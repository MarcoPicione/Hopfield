import numpy as np

global d
d = dict()

# 9 stuff

d['one9'] = np.array([-1, 1, -1, 1, 1, -1, -1, 1, -1])
d['two9'] = np.array([1, 1, -1, 1, 1, -1, 1, 1, -1])
d['four9'] = np.array([1, 1, -1, 1, 1, -1, -1, 1, -1])

# 25 stuff

d['one25'] = np.zeros(25) - 1
for i in range(5): d['one25'][2+5*i] = 1
d['one25'][6] = 1

d['two25'] = np.zeros(25) - 1
for j in range(3):
    for i in range(1,4): d['two25'][j*10+i] = 1
d['two25'][8] = 1
d['two25'][16] = 1

d['three25'] = np.zeros(25) - 1
for j in range(3):
    for i in range(1,4): d['three25'][j*10+i] = 1
d['three25'][8] = 1
d['three25'][18] = 1

d['four25'] = np.zeros(25) - 1
for i in range(5): d['four25'][3+5*i] = 1
for i in range(3): d['four25'][1+5*i] = 1
d['four25'][12] = 1

d['five25'] = np.zeros(25) - 1
for i in range(1,4): d['five25'][i] = 1
for j in range(1,3):
    for i in range(1,3): d['five25'][j*10+i] = 1
d['five25'][6] = 1
d['five25'][18] = 1

d['six25'] = np.zeros(25) - 1
for j in range(3):
    for i in range(1,4): d['six25'][j*10+i] = 1
d['six25'][6] = 1
d['six25'][16] = 1
d['six25'][18] = 1

d['seven25'] = np.zeros(25) - 1
for i in range(1,4): d['seven25'][i] = 1
for i in range(2,5): d['seven25'][i*5+2] = 1
d['seven25'][8] = 1

d['eight25'] = np.zeros(25) - 1
for j in range(3):
    for i in range(1,4): d['eight25'][j*10+i] = 1
d['eight25'][6] = 1
d['eight25'][8] = 1
d['eight25'][16] = 1
d['eight25'][18] = 1

d['nine25'] = np.zeros(25) - 1
for j in range(3):
    for i in range(1,4): d['nine25'][j*10+i] = 1
d['nine25'][8] = 1
d['nine25'][18] = 1
d['nine25'][6] = 1

# 81 stuff

d['one81'] = np.zeros(81) - 1
for i in range(9): d['one81'][4+9*i] = 1
d['one81'][12] = 1
d['one81'][20] = 1

d['two81'] = np.zeros(81) - 1
for j in range(3):
    for i in range(2,7): d['two81'][j*36+i] = 1
for i in range(5): d['two81'][6+i*9] = 1
for i in range(5,9): d['two81'][2+i*9] = 1

d['three81'] = np.zeros(81) - 1
for j in range(3):
    for i in range(2,7): d['three81'][j*36+i] = 1
for i in range(9): d['three81'][6+i*9] = 1

d['four81'] = np.zeros(81) - 1
for i in range(9): d['four81'][6+9*i] = 1
for i in range(38,43): d['four81'][i] = 1
for i in range(4): d['four81'][2+i*9] = 1

d['five81'] = np.zeros(81) - 1
for j in range(3):
    for i in range(2,7): d['five81'][j*36+i] = 1
for i in range(5): d['five81'][2+i*9] = 1
for i in range(5,9): d['five81'][6+i*9] = 1

d['six81'] = np.zeros(81) - 1
for j in range(3):
    for i in range(2,7): d['six81'][j*36+i] = 1
for i in range(9): d['six81'][2+i*9] = 1
for i in range(5,9): d['six81'][6+i*9] = 1

d['seven81'] = np.zeros(81) - 1
for i in range(2,7): d['seven81'][i] = 1
for i in range(4,9): d['seven81'][i*9+3] = 1
d['seven81'][15] = 1
d['seven81'][23] = 1
d['seven81'][31] = 1

d['eight81'] = np.zeros(81) - 1
for j in range(3):
    for i in range(3,6): d['eight81'][j*36+i] = 1
for i in range(1,8): d['eight81'][i*9+2] = 1
for i in range(1,8): d['eight81'][i*9+6] = 1
d['eight81'][38] = -1
d['eight81'][42] = -1

d['nine81'] = np.zeros(81) - 1
for j in range(3):
    for i in range(2,7): d['nine81'][j*36+i] = 1
for i in range(9): d['nine81'][6+i*9] = 1
for i in range(1,4): d['nine81'][2+i*9] = 1