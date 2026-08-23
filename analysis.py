import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
sns.set_style("whitegrid")
df= pd.read_csv(r"basics/german_credit_data.csv")
df.head()