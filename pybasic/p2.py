#%%
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# %%
from sklearn.datasets import load_iris
iris=load_iris()
print(type(iris),iris)
# %%
iris.keys()
# %%
print(iris['data'].shape)
# %%
df=pd.DataFrame(iris['data'])
df
# %%
print(iris['feature_names'])
# %%
cols=['sl','sw','pl','pw']
df=pd.DataFrame(iris['data'],columns=cols)
df
# %%
cap={'한국':'서울','일본':'도쿄'}
print(type(cap),cap.keys(),cap.values())
# %%
print(iris['target'].shape)
# %%
print(iris['target_names'])
# %%
iris.keys()
print(iris['DESCR'])

# %%
# 대표값을 통한 EDA
df.describe()
# %%
# csv로 출력
df.to_csv('data/iris.csv')
# %%
plt.plot(df)
# %%
df.plot(kind="line")
# %%
df.plot(kind="kde")
# %%
# 산점도
df.plot(kind="scatter", x='sl',y='sw')
# %%
df.plot(kind="box", x='sl',y='sw')
# %%
df.plot(kind="box")
df.plot(kind="box",vert=False)

# %%
import seaborn as sns
sns.boxplot(df)
# %%
df['label']=iris['target']
df
# %%
sns.pairplot(df,hue='label')
# %%
# 형태보기
df.shape
# %%
df.describe()
# %%
df.dtypes

# %%
# 데이터 편향 - 라벨이 편향되어있어 머신러닝 경우 셔플 필요함
df.head()
df.tail()
# %%
df.duplicated(keep=False)
# %%
df[df.duplicated(keep=False)]
# %%
df=df.drop_duplicates()
df.shape
# %%
df.isna().sum()
# 빈값 없음
# %%
# 시각화
df['sl'].plot(kind="hist",bins=30)
# 크게 정규성이 없어보인다
# %%
df.plot(kind="scatter",x='sl',y='sw')

#%%
sns.pairplot(df,hue='label')
#시각적으로 어느정도 분리될것으로 보여지나
#겹치는부분이 많아서 통계적 분리는 어려울 것으로 보여진다
#우상향하는 그래프로 볼 때 상관성분석이 필요할것으로 보임

#%%
df.iloc[:,0:4]
# %%
sns.heatmap(df.iloc[:,0:4].corr(),annot= True)
# %%
