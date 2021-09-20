from sklearn import tree
import numpy as np 
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import metrics
import csv 
import pandas as pd 
from c.model_selection import KFold,cross_val_predict,cross_val_score,cross_validate
from sklearn.metrics import classification_report

df = pd.read_csv('Dataset/dataobesity-2.csv',encoding='cp1252') 
#df = pd.read_csv('D:\ปี 4 projectจบ\Dataset/diabetes-1.csv',encoding='cp1252') #โรคเบาหวาน
#df = pd.read_csv('D:\ปี 4 projectจบ\Dataset/hypertension-1.csv',encoding='cp1252') #โรคความดัน
#df = pd.read_csv('D:\ปี 4 projectจบ\Dataset/Total1.csv',encoding='cp1252') #รวมทุกโรค

#ลบค่า NAN & inf
df[df==np.inf]=np.nan
df.fillna(df.mean(), inplace=True)

# คอลัมน์ต่างๆ
x = df.drop("Result",axis=1).values #dropcolum Result ออกไป
#print(x) check x
# คอลัมน์ผลลัพธ์
y = df["Result"].values #ผลเฉลย 
#print(y) check y

classifier = tree.DecisionTreeClassifier(criterion="entropy",max_depth=35)
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
classifier.fit(X_train,y_train)

predict = classifier.predict(X_test)
#print(predict)
print(df.shape)
print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, predict)*100)

#print("ผลการทำนายของคนที่เป็นโรคอ้วนจริงๆ ", classifier.predict([[1,36,2,121 ,150, 0,0,	0,	0,	3,	0,	3,	2,	3,	1,	4,	1,	1,	1,	1,	2,	4,	2,	0,	3,	3,	1,	1,	3,	3,	3,	1,	1,	4,	1,	1,	1,	1,	3,	3,	1,	3,	1,	2,	2,	0,	0,	3,	3,	4,	2,	3,	1,	4,	4,	2,	1,	1,	1,	1,	3,	2,	2,	0,	1,	4,	0,	0,	0,	2,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,	3,	3,	3,	1,	1,	0,	3,	0,	0,	0,	0,	0,	0,	0,	3,	3,	1,	0,	2 , 1,	0,	2,	0,	0,	0,	0,	3,	2,	1,	1,	0]]))
#print("ผลการทำนายของคนที่เป็นโรคเบาหวานจริงๆ ",classifier.predict([[1,	62	,2,	89,	156,	1	,1	,0,	1,	4,	0,	4,	4,	1,4	,4,	4,	2,	1,	0,	3	,3	,3,	0,	1,	1,	0	,1,	2,	2,	0,	0,	0,	0	,4,	0	,1,	1,	3,	3,	0,	2	,3	,0,	0,	0,	0	,1,	0,	3,	1,	1,	2,	2	,1,	1,	1,	0	,0,	1	,1	,0,	0	,0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	4,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0	,2,	4,	0,	2,	0,	0,	4,	0,	3,	0,	0,	0,	0,	4,	0,	4	,0	,0,	0,	1,	0	,0,	3,	0,	0,	0,	0,	0,	0,	0,	4,	0]]))
#print("ผลการทำนายของคนที่เป็นโรคความดันจริงๆ ",)
#print("ผลการทำนายของเฟิร์น ", classifier.predict([[1,	22,	0,	41,	160,	0,	0,	1,	4,	1,	0,	1,	0,	1,	0,	4,	1,	1,	0,	0,	0,	4,	4,	0,	0	,0	,0,	0,	0,	0,	0	,0	,0	,0,	0,	0,	0,	0,	0,	0	,0,	0	,0,	0,	0,	0	,0	,0,0	,0,	0	,0	,0,	0	,0,	0,	0,	0,	0,	0,	1,	0,	0,	1,	1,	4,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0	,0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0]]))
#print("ผลการทำนาย ", classifier.predict([[1,	22,	0	,41	,160,	0,	0,	1,	3,	3,	1,	3,	0,	1,	1,	4,	1,	3,	1,	1,	0	,4,	4,	0,	0,	1,	0,	0,	3,	1,	1,	0,	0,	0,0	,0,	0,	2,	3,	3,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	1,	1,	0,1	,0	,0	,1	,0,	0,	0,2	,0,	1	,1	,3,	3,	1,	0	,0,	0,	0,	0	,0,	0,	0,	0,	0	,0	,0,	0	,0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,0,0	]]))