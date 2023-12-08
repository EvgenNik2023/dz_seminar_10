import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())
print(data.shape)

human_hot = {'human': '1', 'robot': '0'}
data['human'] = data['whoAmI'].map(human_hot)
robot_hot = {'human': '0', 'robot': '1'}
data['robot'] = data['whoAmI'].map(robot_hot)

print(data.head())
