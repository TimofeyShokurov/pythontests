import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# One-hot без get_dummies
one_hot_data = data['whoAmI'].str.get_dummies()

print(one_hot_data.head())