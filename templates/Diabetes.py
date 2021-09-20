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
#df = pd.read_csv('Dataset/diabetes-1.csv',encoding='cp1252') #โรคเบาหวาน
df = pd.read_csv('Dataset/diabetes-2.csv',encoding='cp1252') #โรคเบาหวาน

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
decisiontree = (DecisionTreeClassifier(criterion="gini",max_depth=49))

#train test train80 test 20
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
#X_train,X_test,y_train,y_test = train_test_split(x,y)
#train model
decisiontree.fit(X_train,y_train)

#แปลงข้อมูลก่อนใช้งาน
sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)





y_pred = decisiontree.predict(X_test)

#k=8
score = cross_val_score(decisiontree,X_train,y_train, cv=8, scoring="accuracy")#ดูการสอน
score1 = cross_val_score(decisiontree,X_test,y_test, cv=8, scoring="accuracy")#ดูการทดสอบ

score2 = cross_val_predict(decisiontree,X_test,y_test, cv=8)#การทำนาย


print(df.shape)
print("จำนวนของการสอน",X_train.shape)
print("จำนวนของการทดสอบ",X_test.shape)
print("จำนวนของการสอน",y_train.shape)
print("จำนวนของการทดสอบ",y_test.shape)

print("การสอน",score)
print("การทดสอบ",score1)
#print("ทำนาย",score2)S

#print("ค่าความถูกต้องของการสอน",metrics.accuracy_score(y_train, y_train))
print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, y_pred)*100)
print(classification_report(y_test,y_pred))
print("ผลการทำนาย",y_pred)

#print("ผลการทำนายของคนที่เป็นจริงๆ ", decisiontree.predict([[1,	18,	0	,107,	162	,1,	0	,3,	0,	0	,0,	3,	3,	2,	2,	4,	2,	2,	1,	1,	4,	2,	0	,1,	1,	0,	0,	2,	4,	1,	0,	0,	1,	1,	2,	2,	0,	2	,1,	1,	2,	4,	0,	1,	0,	0,	1,	1,	0,	1,	0,	2,	1,	0	,0,	0	,0,	0	,0,	0,	0,	0,	0,	0,	1,	0,	1,	0,	1,	0,	0,	0,	1,	0,	3,	4,	1,	1,	2,	2,	0,	0,	0,	0,	0,	0,	1,	2	,2,	1,	1	,0,	1,	3,	1,	3,	0	,1,	0,	0	,0	,0,	0,	0,	1,	0]]))
#print("ผลการทำนายของเฟิร์น ", decisiontree.predict([[1,	22,	0,	41,	160,	0,	0,	1,	4,	1,	0,	1,	0,	1,	0,	4,	1,	1,	0,	0,	4,	4,	0,	0	,0	,0,	0,	0,	0,	0,	0	,0	,0,0	,0,	0	,0	,0,	0	,0,	0,	0,	0,	0,	0,	1,	0,	0,	1,	1,	4,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0	,0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0]]))
#print("ผลการทำนาย ", decisiontree.predict([[1,	22,	0	,41	,160,	0,	0,	1,	3,	3,	1,	3,	0,	1,	1,	4,	1,	3,	1,	1,	0	,4,	4,	0,	0,	1,	0,	0,	3,	1,	1,	0,	0,	0,0	,0,	0,	2,	3,	3,	1,	1,	1,	0,	0,	0,	0,	0,	0,	0,	1,	1,	0,1	,0	,0	,1	,0,	0,	0,2	,0,	1	,1	,3,	3,	1,	0	,0,	0,	0,	0	,0,	0,	0,	0,	0	,0	,0,	0	,0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,0,0	]]))

