#%%
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# %%
from sklearn.datasets import load_breast_cancer
# %%
breast_cancer=load_breast_cancer()
breast_cancer
# %%
print(type(breast_cancer))
print(breast_cancer.keys())
# %%
df = pd.DataFrame(breast_cancer['data'],columns=breast_cancer['feature_names'])
df 
#%%
breast_cancer['target']
# %%
df[df.duplicated(keep=False)]
# %%
df.shape
# %%
breast_cancer['feature_names'].shape
# %%
df
# %%
df['label'] = breast_cancer['target']
# %%
breast_cancer['target'].shape
# %%
df
# %%
df.plot(kind="kde")
# %%
df.plot(kind="scatter",x='worst radius',y='worst texture')
# %%
df
# %%
sns.pairplot(df)
# %%
df.keys()
# %%
