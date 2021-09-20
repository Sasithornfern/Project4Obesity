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
df = pd.read_csv('D:\ปี 4 projectจบ\Dataset/hypertension-1.csv',encoding='cp1252') 

#ลบค่า NAN & inf
df[df==np.inf]=np.nan
df.fillna(df.mean(), inplace=True)

# คอลัมน์ต่างๆ
x = df.drop("Result",axis=1).values #dropcolum Result ออกไป
#print(x) check x
# คอลัมน์ผลลัพธ์
y = df["Result"].values #ผลเฉลย
#print(y) check y

#train test train70 test 30
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)

#แปลงข้อมูลก่อนใช้งาน
sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)


#model
decisiontree = (DecisionTreeClassifier(criterion="entropy",max_depth=30))
#train model
decisiontree.fit(X_train,y_train)

y_pred = decisiontree.predict(X_test)


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



