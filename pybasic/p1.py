#%% (구간나누는 기호)
# #%% shift+enter
print('hello world')
# %%

# #%% 나운나운
print("나운")
# %%

# 변수 명명 규칙
#print =1 이라고하면 오류남. 예약어 사용금지

# %%
# 리스트
a= [1, '1', [2,3,'사']]
print(a, '타입:', type(a[0]), type(a[1]))
a[0]=5 # 수정가능하다
print(a)

# %%
# 튜플
a= (1,'1', [2,3,'사'])
print(a, '타입:', type(a[0]), type(a[1]))
a[0]=5 # 수정불가
print(a)

# %%
# 딕셔너리
b={ '한국': '서울', '일본': '도쿄'}
print(b, type(b), b['한국']) # 접근은 키값을 넣어서 접근

# %%
# 집합
c= set([1,1,2,2,3,4,5])
print(c, type(c))

# %%
a=[1,2,3,'4']

# %%
import numpy as np

a=[1,2,3,'4']
ar=np.array(a).astype(int)
print(ar,type(ar))

# %%
# 자유로운 동일한 형변환
a=range(12)
ar=np.array(a)
print(a,type(a),ar,type(ar))
for i in range(10):
    print(i)
# %%
# 형태변환(차원변환)이 자유로움
print(ar,'형태:', ar.shape)
ar34=ar.reshape(3,4)
print(ar34,'차원:', ar34.shape)

# %%
# 슬라이싱
ar34[1]
ar34[1:,1:]
# %%
# 연산
