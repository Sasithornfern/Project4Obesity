import pandas as pd 
import numpy as np 
#import matplotlib.pyplot as plt
from sklearn import metrics 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold,cross_val_predict,cross_val_score,cross_validate
from sklearn.metrics import classification_report


# load dataset
#df = pd.read_csv('Dataset/hypertension-1.csv',encoding='cp1252') #โรคความดัน
df = pd.read_csv('Dataset/hypertension-2.csv',encoding='cp1252') #โรคความดัน

#ลบค่า NAN & inf
df[df==np.inf]=np.nan
df.fillna(df.mean(), inplace=True)

# คอลัมน์ต่างๆ
x = df.drop("Result",axis=1).values #dropcolum Result ออกไป
#print(x) check x
# คอลัมน์ผลลัพธ์
y = df["Result"].values #ผลเฉลย
#print(y) check y
#model
decisiontree = (DecisionTreeClassifier(criterion="gini",max_depth=35))
#train test train80 test 20
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
#X_train,X_test,y_train,y_test = train_test_split(x,y)
#train model
decisiontree.fit(X_train,y_train)

y_pred = decisiontree.predict(X_test)

#k=7
score = cross_val_score(decisiontree,X_train,y_train, cv=7, scoring="accuracy")#ดูการสอน
score1 = cross_val_score(decisiontree,X_test,y_test, cv=7, scoring="accuracy")#ดูการทดสอบ

score2 = cross_val_predict(decisiontree,X_test,y_test, cv=7)#การทำนาย


print(df.shape)
print("จำนวนของการสอน",X_train.shape)
print("จำนวนของการทดสอบ",X_test.shape)
print("จำนวนของการสอน",y_train.shape)
print("จำนวนของการทดสอบ",y_test.shape)

print("การสอน",score)
print("การทดสอบ",score1)
#print("ทำนาย",score2)

#print("ค่าความถูกต้องของการสอน",metrics.accuracy_score(y_train, y_train))
print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, y_pred)*100)
print(classification_report(y_test,y_pred))
print("ผลการทำนาย",y_pred)

#print("ผลการทำนายของคนที่เป็นจริงๆ ", decisiontree.predict([[1,36,2,121 ,150, 0,0,	0,	0,	3,	0,	3,	2,	3,	1,	4,	1,	1,	1,	1,	2,	4,	2,	0,	3,	3,	1,	1,	3,	3,	3,	1,	1,	4,	1,	1,	1,	1,	3,	3,	1,	3,	1,	2,	2,	0,	0,	3,	3,	4,	2,	3,	1,	4,	4,	2,	1,	1,	1,	1,	3,	2,	2,	0,	1,	4,	0,	0,	0,	2,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	2,	3,	3,	3,	1,	1,	0,	3,	0,	0,	0,	0,	0,	0,	0,	3,	3,	1,	0,	2 , 1,	0,	2,	0,	0,	0,	0,	3,	2,	1,	1,	0]]))
#print("ผลการทำนายของเฟิร์น ", decisiontree.predict([[1,	22,	0,	41,	160,	0,	0,	1,	4,	1,	0,	1,	0,	1,	0,	4,	1,	1,	0,	0,	0,	4,	4,	0,	0	,0	,0,	0,	0,	0,	0	,0	,0	,0,	0,	0,	0,	0,	0,	0	,0,	0	,0,	0,	0,	0	,0	,0,0	,0,	0	,0	,0,	0	,0,	0,	0,	0,	0,	0,	1,	0,	0,	1,	1,	4,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0	,0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0]]))
#print("ผลการทำนาย ", decisiontree.predict([[1,	22,	0	,41	,160,	0,	0,	1,	3,	3,	1,	3,	0,	1,	1,	4,	1,	3,	1,	1,	0	,4,	4,	0,	0,	1,	0,	0,	3,	1,	1,	0,	0,	0,0	,0,	0,	2,	3,	3,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	1,	1,	0,1	,0	,0	,1	,0,	0,	0,2	,0,	1	,1	,3,	3,	1,	0	,0,	0,	0,	0	,0,	0,	0,	0,	0	,0	,0,	0	,0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,0,0	]]))

