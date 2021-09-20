from django.shortcuts import render
from django.http import HttpRequest
from django.db.models import Q,query

from .models import NameHospital
from .models import Dobesity
from .models import diabetes
from .models import hypertention
from .models import dyslipidemia
from .models import Question
from .models import EatQuestion
from .models import exerciseQuestion

import pandas as pd 
import numpy as np 
#import matplotlib.pyplot as plt
from sklearn import metrics 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold,cross_val_predict,cross_val_score,cross_validate
from sklearn.metrics import classification_report

# Create your views here.
def home(request):
    return render(request,'index.html')


def assessment(request):
    typename1 = Question.objects.all()
    typename2 = EatQuestion.objects.all()
    typename3 = exerciseQuestion.objects.all()
    return render(request,'Assessment.html',{"Question":typename1,"EatQuestion":typename2,"exerciseQuestion":typename3})


def assessment(request):
    typename1 = Question.objects.all()
    typename2 = EatQuestion.objects.all()
    typename3 = exerciseQuestion.objects.all()
    return render(request,'Assessment.html',{"Question":typename1,"EatQuestion":typename2,"exerciseQuestion":typename3})

def search(request):
    search_post = request.GET.get('search')
    if search_post:
        posts = NameHospital.objects.filter(Q(name__contains = search_post) | Q(provinces__contains = search_post))
              
    else:
        posts = NameHospital.objects.all()    
    return render(request,'Search.html',{'NameHospitals':posts})

def suggestion(request):
    return render(request,'Suggestion.html')

def Obesity(request): #ดึงข้อมูลออกมาแสดง
    d1 = Dobesity.objects.all()
    return render(request,'obesity.html',{'obesity':d1})

def result(request):
    return render(request,'Result.html')

def diabete(request):#ดึงข้อมูลออกมาแสดง
    data1 = diabetes.objects.all()
    return render(request,'diabetes.html',{'diabetest':data1})

def hypertension(request):
    #Query Data From Model ดึงข้อมูลจากโมเดลมาแสดง
    data2 = hypertention.objects.all()
    return render(request,'hypertension.html',{'hypertentions1':data2})

def diseaseofhyperlipidemia(request):
    #Query Data From Model ดึงข้อมูลจากโมเดลมาแสดง
    data2 = dyslipidemia.objects.all()
    return render(request,'diseaseofhyperlipidemia.html',{'dyslipidemias':data2})


#ฟังก์ชันที่ตัดช้อย4โรค
def TestTree(request): 
    def obesity():
        # load dataset
        df = pd.read_csv('Dataset/dataobesity-2.csv',encoding='cp1252') #โรคอ้วน
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
        X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
        decisiontree.fit(X_train,y_train)

        #แปลงข้อมูลก่อนใช้งาน
        sc = StandardScaler()
        sc.fit(X_train)
        X_train = sc.transform(X_train)
        X_test = sc.transform(X_test)

        gender          = (request.POST["gender"])
        age             = (request.POST["age"])
        status          = (request.POST["status"])
        weights         = (request.POST["weights"])
        heights         = (request.POST["heights"])
        DHD             = (request.POST["DHD"])
        DPHD            = (request.POST["DPHD"])
        onemeal         = (request.POST["onemeal"])
        twomeals        = (request.POST["twomeals"])
        threemeals      = (request.POST["threemeals"])
        fourorfivemeal  = (request.POST["fourorfivemeal"])
        Eat_spicy       = (request.POST["Eat_spicy"])
        Eat_salty       = (request.POST["Eat_salty"] )
        Eat_sweet       = (request.POST["Eat_sweet"] )
        Eat_tasteless   = (request.POST["Eat_tasteless"] ) 
        Eat_rice        = (request.POST["Eat_rice"])
        Eat_stickyrice  = (request.POST["Eat_stickyrice"])
        Eat_noodles     = (request.POST["Eat_noodles"] )
        Eat_ricenoodles = (request.POST["Eat_ricenoodles"] )    
        Eat_bread       = (request.POST["Eat_bread"])
        ERM             = (request.POST["ERM"])
        EPM             = (request.POST["EPM"] )
        EWM             = (request.POST["EWM"]  )  
        EFM             = (request.POST["EFM"])
        ESM             = (request.POST["ESM"] ) 
        EAM             = (request.POST["EAM"])
        EVI	            = (request.POST["EVI"])
        Eat_egg         = (request.POST["Eat_egg"])
        Tastelessmilk       = (request.POST["Tastelessmilk"])
        Sweetenedcondensedmilk  = (request.POST["Sweetenedcondensedmilk"])
        Sourmilk                = (request.POST["Sourmilk"])
        Yogurt                  = (request.POST["Yogurt"])
        Soymilk                 = (request.POST["Soymilk"])
        Morningglory            = (request.POST["Morningglory"])
        Kale                    = (request.POST["Kale"])
        Pumpkin                 = (request.POST["Pumpkin"])
        Cucumber                = (request.POST["Cucumber"])
        Greenbeans_longbeans    = (request.POST["Greenbeans_longbeans"])
        Papaya                  = (request.POST["Papaya"])
        Banana                  = (request.POST["Banana"])
        Orange                  = (request.POST["Orange"])
        Pineapple               = (request.POST["Pineapple"])
        Mango                   = (request.POST["Mango"])
        Crisp                   = (request.POST["Crisp"])
        Icecream                = (request.POST["Icecream"])
        Sparkingwater           = (request.POST["Sparkingwater"])
        Sweetwater              = (request.POST["Sweetwater"])
        Tea                     = (request.POST["Tea"])
        Coffee                  = (request.POST["Coffee"])
        Liquor_beer_wine        = (request.POST["Liquor_beer_wine"])
        Energy_drink            = (request.POST["Energy_drink"])
        MTS                     = (request.POST["MTS"])
        Antidepressants         = (request.POST["Antidepressants"])
        Antiepilepticdrug       = (request.POST["Antiepilepticdrug"])
        Diabetesmedication      = (request.POST["Diabetesmedication"])
        Birthcontrolpills       = (request.POST["Birthcontrolpills"])
        Antiinflammatorydrug         = (request.POST["Antiinflammatorydrug"])
        Antiviraldrug                = (request.POST["Antiviraldrug"])
        Varioussupplements           = (request.POST["Varioussupplements"])
        Smoke                        = (request.POST["Smoke"])
        Run                          = (request.POST["Run"])
        Cycling                      = (request.POST["Cycling"])
        Swim                         = (request.POST["Swim"])
        Basketball                   = (request.POST["Basketball"])
        Football                     = (request.POST["Football"])
        Yoga                         = (request.POST["Yoga"])
        Aerobic                      = (request.POST["Aerobic"])
        Weightlifting                = (request.POST["Weightlifting"])
        NGS                          = (request.POST["NGS"])
        SHS                          = (request.POST["SHS"])
        SDD                          = (request.POST["SDD"])
        WEBFS                        = (request.POST["WEBFS"])
        Difficultybreathing	         = (request.POST["Difficultybreathing"])
        WBLFTC	                     = (request.POST["WBLFTC"])
        SWH	                         = (request.POST["SWH"])
        Itchyskin                    = (request.POST["Itchyskin"])
        TSY                          = (request.POST["TSY"])
        Yellowskin                   = (request.POST["Yellowskin"])
        YSP                          = (request.POST["YSP"])
        CRS                          = (request.POST["CRS"])
        AirAllergic                  = (request.POST["AirAllergic"])
        Blurredvision                = (request.POST["Blurredvision"])
        Badbreath                    = (request.POST["Badbreath"])
        HFN                          = (request.POST["HFN"])
        Urinaryincontinence          = (request.POST["Urinaryincontinence"])
        Foamyurine                   = (request.POST["Foamyurine"])
        WLC                          = (request.POST["WLC"])
        Havestress                   = (request.POST["Havestress"])
        Dizziness	                 = (request.POST["Dizziness"])
        SHQ                          = (request.POST["SHQ"])
        NHF                          = (request.POST["NHF"])
        SHF                          = (request.POST["SHF"])
        Coldhandandfeet              = (request.POST["Coldhandandfeet"])
        Nauseaandvomiting	         = (request.POST["Nauseaandvomiting"])
        Stomachcolic                 = (request.POST["Stomachcolic"])
        AMS	                         = (request.POST["AMS"])
        Agony                        = (request.POST["Agony"])
        PIH	                         = (request.POST["PIH"])
        DAT	                         = (request.POST["DAT"])
        Cannotliedown                = (request.POST["Cannotliedown"])  

        #ทำนาย
        y_pred = decisiontree.predict([[gender, age, status, weights ,heights ,DHD,DPHD,onemeal,twomeals,threemeals,fourorfivemeal,
                Eat_spicy,Eat_salty,Eat_sweet,Eat_tasteless,Eat_rice,Eat_stickyrice,Eat_noodles,Eat_ricenoodles,Eat_bread,ERM,EPM,EWM,EFM,ESM,EAM,EVI,Eat_egg,
                Tastelessmilk,Sweetenedcondensedmilk,Sourmilk,Yogurt,Soymilk,Morningglory,
                Kale,Pumpkin,Cucumber,Greenbeans_longbeans,Papaya,Banana,Orange,Pineapple,Mango,Crisp,Icecream,Sparkingwater,
                Sweetwater,Tea,Coffee,Liquor_beer_wine,Energy_drink,MTS,Antidepressants,Antiepilepticdrug,Diabetesmedication,Birthcontrolpills,
                Antiinflammatorydrug,Antiviraldrug,Varioussupplements,Smoke,Run,Cycling,Swim,Basketball,Football,
                Yoga,Aerobic,Weightlifting,NGS,SHS,SDD,WEBFS,Difficultybreathing,WBLFTC,SWH,Itchyskin,TSY,Yellowskin,YSP,CRS,AirAllergic,
                Blurredvision,Badbreath,HFN,Urinaryincontinence,Foamyurine,WLC,Havestress,Dizziness,SHQ,NHF,SHF,Coldhandandfeet,Nauseaandvomiting,Stomachcolic,
                AMS,Agony,PIH,DAT,Cannotliedown]])

        result1 = ""+""
        if y_pred == [1]:
            result1 = "ท่านมีความเสี่ยงเป็นโรคอ้วน"
        if y_pred == [0]:
            result1 = "ท่านไม่มีความเสี่ยงเป็นโรคอ้วน"
            

        print("Hello")
        print(df.shape)
        print(y_pred.shape)
        print("ผลการทำนายโรคอ้วน",y_pred)
        #print("การสอน",score)
        #print("การทดสอบ",score1)
        #print("ทำนาย",score2)
        #print(X_train.shape)
        #print(X_test.shape)
        #print(y_train.shape)
        #print(y_test.shape)

        #print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, y_pred)*100)

        #print("ค่าความถูกต้องของการสอน",metrics.accuracy_score(y_train, y_train))
        #print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, y_pred))
        #print(classification_report(y_test,y_pred))
        return result1
        #return render(request,'Result.html',{"result2":result2,"accuracyscoretest":accuracyscoretest})
        #return ({"result1":result1})
    
    def diabetes():
        # load dataset
        df = pd.read_csv('Dataset/diabetes-2.csv',encoding='cp1252') #โรคอ้วน
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
        X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
        decisiontree.fit(X_train,y_train)

        #แปลงข้อมูลก่อนใช้งาน
        sc = StandardScaler()
        sc.fit(X_train)
        X_train = sc.transform(X_train)
        X_test = sc.transform(X_test)

        gender          = (request.POST["gender"])
        age             = (request.POST["age"])
        status          = (request.POST["status"])
        weights         = (request.POST["weights"])
        heights         = (request.POST["heights"])
        DHD             = (request.POST["DHD"])
        DPHD            = (request.POST["DPHD"])
        onemeal         = (request.POST["onemeal"])
        twomeals        = (request.POST["twomeals"])
        threemeals      = (request.POST["threemeals"])
        fourorfivemeal  = (request.POST["fourorfivemeal"])
        Eat_spicy       = (request.POST["Eat_spicy"])
        Eat_salty       = (request.POST["Eat_salty"] )
        Eat_sweet       = (request.POST["Eat_sweet"] )
        Eat_tasteless   = (request.POST["Eat_tasteless"] ) 
        Eat_rice        = (request.POST["Eat_rice"])
        Eat_stickyrice  = (request.POST["Eat_stickyrice"])
        Eat_noodles     = (request.POST["Eat_noodles"] )
        Eat_ricenoodles = (request.POST["Eat_ricenoodles"] )    
        Eat_bread       = (request.POST["Eat_bread"])
        ERM             = (request.POST["ERM"])
        EPM             = (request.POST["EPM"] )
        EWM             = (request.POST["EWM"]  )  
        EFM             = (request.POST["EFM"])
        ESM             = (request.POST["ESM"] ) 
        EAM             = (request.POST["EAM"])
        EVI	            = (request.POST["EVI"])
        Eat_egg         = (request.POST["Eat_egg"])
        Tastelessmilk       = (request.POST["Tastelessmilk"])
        Sweetenedcondensedmilk  = (request.POST["Sweetenedcondensedmilk"])
        Sourmilk                = (request.POST["Sourmilk"])
        Yogurt                  = (request.POST["Yogurt"])
        Soymilk                 = (request.POST["Soymilk"])
        Morningglory            = (request.POST["Morningglory"])
        Kale                    = (request.POST["Kale"])
        Pumpkin                 = (request.POST["Pumpkin"])
        Cucumber                = (request.POST["Cucumber"])
        Greenbeans_longbeans    = (request.POST["Greenbeans_longbeans"])
        Papaya                  = (request.POST["Papaya"])
        Banana                  = (request.POST["Banana"])
        Orange                  = (request.POST["Orange"])
        Pineapple               = (request.POST["Pineapple"])
        Mango                   = (request.POST["Mango"])
        Crisp                   = (request.POST["Crisp"])
        Icecream                = (request.POST["Icecream"])
        Sparkingwater           = (request.POST["Sparkingwater"])
        Sweetwater              = (request.POST["Sweetwater"])
        Tea                     = (request.POST["Tea"])
        Coffee                  = (request.POST["Coffee"])
        Liquor_beer_wine        = (request.POST["Liquor_beer_wine"])
        Energy_drink            = (request.POST["Energy_drink"])
        MTS                     = (request.POST["MTS"])
        Antidepressants         = (request.POST["Antidepressants"])
        Antiepilepticdrug       = (request.POST["Antiepilepticdrug"])
        Diabetesmedication      = (request.POST["Diabetesmedication"])
        Birthcontrolpills       = (request.POST["Birthcontrolpills"])
        Antiinflammatorydrug         = (request.POST["Antiinflammatorydrug"])
        Antiviraldrug                = (request.POST["Antiviraldrug"])
        Varioussupplements           = (request.POST["Varioussupplements"])
        Smoke                        = (request.POST["Smoke"])
        Run                          = (request.POST["Run"])
        Cycling                      = (request.POST["Cycling"])
        Swim                         = (request.POST["Swim"])
        Basketball                   = (request.POST["Basketball"])
        Football                     = (request.POST["Football"])
        Yoga                         = (request.POST["Yoga"])
        Aerobic                      = (request.POST["Aerobic"])
        Weightlifting                = (request.POST["Weightlifting"])
        NGS                          = (request.POST["NGS"])
        SHS                          = (request.POST["SHS"])
        SDD                          = (request.POST["SDD"])
        WEBFS                        = (request.POST["WEBFS"])
        Difficultybreathing	         = (request.POST["Difficultybreathing"])
        WBLFTC	                     = (request.POST["WBLFTC"])
        SWH	                         = (request.POST["SWH"])
        Itchyskin                    = (request.POST["Itchyskin"])
        TSY                          = (request.POST["TSY"])
        Yellowskin                   = (request.POST["Yellowskin"])
        YSP                          = (request.POST["YSP"])
        CRS                          = (request.POST["CRS"])
        AirAllergic                  = (request.POST["AirAllergic"])
        Blurredvision                = (request.POST["Blurredvision"])
        Badbreath                    = (request.POST["Badbreath"])
        HFN                          = (request.POST["HFN"])
        Urinaryincontinence          = (request.POST["Urinaryincontinence"])
        Foamyurine                   = (request.POST["Foamyurine"])
        WLC                          = (request.POST["WLC"])
        Havestress                   = (request.POST["Havestress"])
        Dizziness	                 = (request.POST["Dizziness"])
        SHQ                          = (request.POST["SHQ"])
        NHF                          = (request.POST["NHF"])
        SHF                          = (request.POST["SHF"])
        Coldhandandfeet              = (request.POST["Coldhandandfeet"])
        Nauseaandvomiting	         = (request.POST["Nauseaandvomiting"])
        Stomachcolic                 = (request.POST["Stomachcolic"])
        AMS	                         = (request.POST["AMS"])
        Agony                        = (request.POST["Agony"])
        PIH	                         = (request.POST["PIH"])
        DAT	                         = (request.POST["DAT"])
        Cannotliedown                = (request.POST["Cannotliedown"])  

        #ทำนาย
        y_pred = decisiontree.predict([[gender, age, status, weights ,heights ,DHD,DPHD,onemeal,twomeals,threemeals,fourorfivemeal,
                Eat_spicy,Eat_salty,Eat_sweet,Eat_tasteless,Eat_rice,Eat_stickyrice,Eat_noodles,Eat_ricenoodles,Eat_bread,ERM,EPM,EWM,EFM,ESM,EAM,EVI,Eat_egg,
                Tastelessmilk,Sweetenedcondensedmilk,Sourmilk,Yogurt,Soymilk,Morningglory,
                Kale,Pumpkin,Cucumber,Greenbeans_longbeans,Papaya,Banana,Orange,Pineapple,Mango,Crisp,Icecream,Sparkingwater,
                Sweetwater,Tea,Coffee,Liquor_beer_wine,Energy_drink,MTS,Antidepressants,Antiepilepticdrug,Diabetesmedication,Birthcontrolpills,
                Antiinflammatorydrug,Antiviraldrug,Varioussupplements,Smoke,Run,Cycling,Swim,Basketball,Football,
                Yoga,Aerobic,Weightlifting,NGS,SHS,SDD,WEBFS,Difficultybreathing,WBLFTC,SWH,Itchyskin,TSY,Yellowskin,YSP,CRS,AirAllergic,
                Blurredvision,Badbreath,HFN,Urinaryincontinence,Foamyurine,WLC,Havestress,Dizziness,SHQ,NHF,SHF,Coldhandandfeet,Nauseaandvomiting,Stomachcolic,
                AMS,Agony,PIH,DAT,Cannotliedown]])

        result2 = ""+""
        if y_pred == [2]:
            result2 = "ท่านมีความเสี่ยงเป็นโรคเบาหวาน"
        if y_pred == [0]:
            result2 = "ท่านไม่มีความเสี่ยงเป็นโรคเบาหวาน"
            

        print("Hello")
        print(df.shape)
        print(y_pred.shape)
        print("ผลการทำนายโรคเบาหวาน",y_pred)
        #print("การสอน",score)
        #print("การทดสอบ",score1)
        #print("ทำนาย",score2)
        #print(X_train.shape)
        #print(X_test.shape)
        #print(y_train.shape)
        #print(y_test.shape)

        #print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, y_pred)*100)

        #print("ค่าความถูกต้องของการสอน",metrics.accuracy_score(y_train, y_train))
        #print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, y_pred))
        #print(classification_report(y_test,y_pred))
        return result2
        #return render(request,'Result.html',{"result2":result2,"accuracyscoretest":accuracyscoretest})
        #return ({"result2":result2})
    
    def hypertension():
        # load dataset
        df = pd.read_csv('Dataset/hypertension-2.csv',encoding='cp1252') #โรคอ้วน
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
        #train test train70 test 30
        X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
        decisiontree.fit(X_train,y_train)

        #แปลงข้อมูลก่อนใช้งาน
        sc = StandardScaler()
        sc.fit(X_train)
        X_train = sc.transform(X_train)
        X_test = sc.transform(X_test)

        gender          = (request.POST["gender"])
        age             = (request.POST["age"])
        status          = (request.POST["status"])
        weights         = (request.POST["weights"])
        heights         = (request.POST["heights"])
        DHD             = (request.POST["DHD"])
        DPHD            = (request.POST["DPHD"])
        onemeal         = (request.POST["onemeal"])
        twomeals        = (request.POST["twomeals"])
        threemeals      = (request.POST["threemeals"])
        fourorfivemeal  = (request.POST["fourorfivemeal"])
        Eat_spicy       = (request.POST["Eat_spicy"])
        Eat_salty       = (request.POST["Eat_salty"] )
        Eat_sweet       = (request.POST["Eat_sweet"] )
        Eat_tasteless   = (request.POST["Eat_tasteless"] ) 
        Eat_rice        = (request.POST["Eat_rice"])
        Eat_stickyrice  = (request.POST["Eat_stickyrice"])
        Eat_noodles     = (request.POST["Eat_noodles"] )
        Eat_ricenoodles = (request.POST["Eat_ricenoodles"] )    
        Eat_bread       = (request.POST["Eat_bread"])
        ERM             = (request.POST["ERM"])
        EPM             = (request.POST["EPM"] )
        EWM             = (request.POST["EWM"]  )  
        EFM             = (request.POST["EFM"])
        ESM             = (request.POST["ESM"] ) 
        EAM             = (request.POST["EAM"])
        EVI	            = (request.POST["EVI"])
        Eat_egg         = (request.POST["Eat_egg"])
        Tastelessmilk       = (request.POST["Tastelessmilk"])
        Sweetenedcondensedmilk  = (request.POST["Sweetenedcondensedmilk"])
        Sourmilk                = (request.POST["Sourmilk"])
        Yogurt                  = (request.POST["Yogurt"])
        Soymilk                 = (request.POST["Soymilk"])
        Morningglory            = (request.POST["Morningglory"])
        Kale                    = (request.POST["Kale"])
        Pumpkin                 = (request.POST["Pumpkin"])
        Cucumber                = (request.POST["Cucumber"])
        Greenbeans_longbeans    = (request.POST["Greenbeans_longbeans"])
        Papaya                  = (request.POST["Papaya"])
        Banana                  = (request.POST["Banana"])
        Orange                  = (request.POST["Orange"])
        Pineapple               = (request.POST["Pineapple"])
        Mango                   = (request.POST["Mango"])
        Crisp                   = (request.POST["Crisp"])
        Icecream                = (request.POST["Icecream"])
        Sparkingwater           = (request.POST["Sparkingwater"])
        Sweetwater              = (request.POST["Sweetwater"])
        Tea                     = (request.POST["Tea"])
        Coffee                  = (request.POST["Coffee"])
        Liquor_beer_wine        = (request.POST["Liquor_beer_wine"])
        Energy_drink            = (request.POST["Energy_drink"])
        MTS                     = (request.POST["MTS"])
        Antidepressants         = (request.POST["Antidepressants"])
        Antiepilepticdrug       = (request.POST["Antiepilepticdrug"])
        Diabetesmedication      = (request.POST["Diabetesmedication"])
        Birthcontrolpills       = (request.POST["Birthcontrolpills"])
        Antiinflammatorydrug         = (request.POST["Antiinflammatorydrug"])
        Antiviraldrug                = (request.POST["Antiviraldrug"])
        Varioussupplements           = (request.POST["Varioussupplements"])
        Smoke                        = (request.POST["Smoke"])
        Run                          = (request.POST["Run"])
        Cycling                      = (request.POST["Cycling"])
        Swim                         = (request.POST["Swim"])
        Basketball                   = (request.POST["Basketball"])
        Football                     = (request.POST["Football"])
        Yoga                         = (request.POST["Yoga"])
        Aerobic                      = (request.POST["Aerobic"])
        Weightlifting                = (request.POST["Weightlifting"])
        NGS                          = (request.POST["NGS"])
        SHS                          = (request.POST["SHS"])
        SDD                          = (request.POST["SDD"])
        WEBFS                        = (request.POST["WEBFS"])
        Difficultybreathing	         = (request.POST["Difficultybreathing"])
        WBLFTC	                     = (request.POST["WBLFTC"])
        SWH	                         = (request.POST["SWH"])
        Itchyskin                    = (request.POST["Itchyskin"])
        TSY                          = (request.POST["TSY"])
        Yellowskin                   = (request.POST["Yellowskin"])
        YSP                          = (request.POST["YSP"])
        CRS                          = (request.POST["CRS"])
        AirAllergic                  = (request.POST["AirAllergic"])
        Blurredvision                = (request.POST["Blurredvision"])
        Badbreath                    = (request.POST["Badbreath"])
        HFN                          = (request.POST["HFN"])
        Urinaryincontinence          = (request.POST["Urinaryincontinence"])
        Foamyurine                   = (request.POST["Foamyurine"])
        WLC                          = (request.POST["WLC"])
        Havestress                   = (request.POST["Havestress"])
        Dizziness	                 = (request.POST["Dizziness"])
        SHQ                          = (request.POST["SHQ"])
        NHF                          = (request.POST["NHF"])
        SHF                          = (request.POST["SHF"])
        Coldhandandfeet              = (request.POST["Coldhandandfeet"])
        Nauseaandvomiting	         = (request.POST["Nauseaandvomiting"])
        Stomachcolic                 = (request.POST["Stomachcolic"])
        AMS	                         = (request.POST["AMS"])
        Agony                        = (request.POST["Agony"])
        PIH	                         = (request.POST["PIH"])
        DAT	                         = (request.POST["DAT"])
        Cannotliedown                = (request.POST["Cannotliedown"])  

        #ทำนาย
        y_pred = decisiontree.predict([[gender, age, status, weights ,heights ,DHD,DPHD,onemeal,twomeals,threemeals,fourorfivemeal,
                Eat_spicy,Eat_salty,Eat_sweet,Eat_tasteless,Eat_rice,Eat_stickyrice,Eat_noodles,Eat_ricenoodles,Eat_bread,ERM,EPM,EWM,EFM,ESM,EAM,EVI,Eat_egg,
                Tastelessmilk,Sweetenedcondensedmilk,Sourmilk,Yogurt,Soymilk,Morningglory,
                Kale,Pumpkin,Cucumber,Greenbeans_longbeans,Papaya,Banana,Orange,Pineapple,Mango,Crisp,Icecream,Sparkingwater,
                Sweetwater,Tea,Coffee,Liquor_beer_wine,Energy_drink,MTS,Antidepressants,Antiepilepticdrug,Diabetesmedication,Birthcontrolpills,
                Antiinflammatorydrug,Antiviraldrug,Varioussupplements,Smoke,Run,Cycling,Swim,Basketball,Football,
                Yoga,Aerobic,Weightlifting,NGS,SHS,SDD,WEBFS,Difficultybreathing,WBLFTC,SWH,Itchyskin,TSY,Yellowskin,YSP,CRS,AirAllergic,
                Blurredvision,Badbreath,HFN,Urinaryincontinence,Foamyurine,WLC,Havestress,Dizziness,SHQ,NHF,SHF,Coldhandandfeet,Nauseaandvomiting,Stomachcolic,
                AMS,Agony,PIH,DAT,Cannotliedown]])

        result3 = ""+""
        if y_pred == [3]:
            result3 = "ท่านมีความเสี่ยงเป็นโรคความดัน"
        if y_pred == [0]:
            result3 = "ท่านไม่มีความเสี่ยงเป็นโรคความดัน"
            

        print("Hello")
        print(df.shape)
        print(y_pred.shape)
        print("ผลการทำนายโรคความดัน",y_pred)
        #print("การสอน",score)
        #print("การทดสอบ",score1)
        #print("ทำนาย",score2)
        #print(X_train.shape)
        #print(X_test.shape)
        #print(y_train.shape)
        #print(y_test.shape)

        #print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, y_pred)*100)

        #print("ค่าความถูกต้องของการสอน",metrics.accuracy_score(y_train, y_train))
        #print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, y_pred))
        #print(classification_report(y_test,y_pred))
        return result3
        #return render(request,'Result.html',{"result2":result2,"accuracyscoretest":accuracyscoretest})
        #return ({"result3":result3})
    
    def dieseaseofhyprtlipidemia():
        # load dataset
        df = pd.read_csv('Dataset/diesease-of-hyprtlipidemia.1.csv',encoding='cp1252') #โรคอ้วน
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
        #train test train60 test 40
        X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.4,random_state=0)
        decisiontree.fit(X_train,y_train)

        #แปลงข้อมูลก่อนใช้งาน
        sc = StandardScaler()
        sc.fit(X_train)
        X_train = sc.transform(X_train)
        X_test = sc.transform(X_test)

        gender          = (request.POST["gender"])
        age             = (request.POST["age"])
        status          = (request.POST["status"])
        weights         = (request.POST["weights"])
        heights         = (request.POST["heights"])
        DHD             = (request.POST["DHD"])
        DPHD            = (request.POST["DPHD"])
        onemeal         = (request.POST["onemeal"])
        twomeals        = (request.POST["twomeals"])
        threemeals      = (request.POST["threemeals"])
        fourorfivemeal  = (request.POST["fourorfivemeal"])
        Eat_spicy       = (request.POST["Eat_spicy"])
        Eat_salty       = (request.POST["Eat_salty"] )
        Eat_sweet       = (request.POST["Eat_sweet"] )
        Eat_tasteless   = (request.POST["Eat_tasteless"] ) 
        Eat_rice        = (request.POST["Eat_rice"])
        Eat_stickyrice  = (request.POST["Eat_stickyrice"])
        Eat_noodles     = (request.POST["Eat_noodles"] )
        Eat_ricenoodles = (request.POST["Eat_ricenoodles"] )    
        Eat_bread       = (request.POST["Eat_bread"])
        ERM             = (request.POST["ERM"])
        EPM             = (request.POST["EPM"] )
        EWM             = (request.POST["EWM"]  )  
        EFM             = (request.POST["EFM"])
        ESM             = (request.POST["ESM"] ) 
        EAM             = (request.POST["EAM"])
        EVI	            = (request.POST["EVI"])
        Eat_egg         = (request.POST["Eat_egg"])
        Tastelessmilk       = (request.POST["Tastelessmilk"])
        Sweetenedcondensedmilk  = (request.POST["Sweetenedcondensedmilk"])
        Sourmilk                = (request.POST["Sourmilk"])
        Yogurt                  = (request.POST["Yogurt"])
        Soymilk                 = (request.POST["Soymilk"])
        Morningglory            = (request.POST["Morningglory"])
        Kale                    = (request.POST["Kale"])
        Pumpkin                 = (request.POST["Pumpkin"])
        Cucumber                = (request.POST["Cucumber"])
        Greenbeans_longbeans    = (request.POST["Greenbeans_longbeans"])
        Papaya                  = (request.POST["Papaya"])
        Banana                  = (request.POST["Banana"])
        Orange                  = (request.POST["Orange"])
        Pineapple               = (request.POST["Pineapple"])
        Mango                   = (request.POST["Mango"])
        Crisp                   = (request.POST["Crisp"])
        Icecream                = (request.POST["Icecream"])
        Sparkingwater           = (request.POST["Sparkingwater"])
        Sweetwater              = (request.POST["Sweetwater"])
        Tea                     = (request.POST["Tea"])
        Coffee                  = (request.POST["Coffee"])
        Liquor_beer_wine        = (request.POST["Liquor_beer_wine"])
        Energy_drink            = (request.POST["Energy_drink"])
        MTS                     = (request.POST["MTS"])
        Antidepressants         = (request.POST["Antidepressants"])
        Antiepilepticdrug       = (request.POST["Antiepilepticdrug"])
        Diabetesmedication      = (request.POST["Diabetesmedication"])
        Birthcontrolpills       = (request.POST["Birthcontrolpills"])
        Antiinflammatorydrug         = (request.POST["Antiinflammatorydrug"])
        Antiviraldrug                = (request.POST["Antiviraldrug"])
        Varioussupplements           = (request.POST["Varioussupplements"])
        Smoke                        = (request.POST["Smoke"])
        Run                          = (request.POST["Run"])
        Cycling                      = (request.POST["Cycling"])
        Swim                         = (request.POST["Swim"])
        Basketball                   = (request.POST["Basketball"])
        Football                     = (request.POST["Football"])
        Yoga                         = (request.POST["Yoga"])
        Aerobic                      = (request.POST["Aerobic"])
        Weightlifting                = (request.POST["Weightlifting"])
        NGS                          = (request.POST["NGS"])
        SHS                          = (request.POST["SHS"])
        SDD                          = (request.POST["SDD"])
        WEBFS                        = (request.POST["WEBFS"])
        Difficultybreathing	         = (request.POST["Difficultybreathing"])
        WBLFTC	                     = (request.POST["WBLFTC"])
        SWH	                         = (request.POST["SWH"])
        Itchyskin                    = (request.POST["Itchyskin"])
        TSY                          = (request.POST["TSY"])
        Yellowskin                   = (request.POST["Yellowskin"])
        YSP                          = (request.POST["YSP"])
        CRS                          = (request.POST["CRS"])
        AirAllergic                  = (request.POST["AirAllergic"])
        Blurredvision                = (request.POST["Blurredvision"])
        Badbreath                    = (request.POST["Badbreath"])
        HFN                          = (request.POST["HFN"])
        Urinaryincontinence          = (request.POST["Urinaryincontinence"])
        Foamyurine                   = (request.POST["Foamyurine"])
        WLC                          = (request.POST["WLC"])
        Havestress                   = (request.POST["Havestress"])
        Dizziness	                 = (request.POST["Dizziness"])
        SHQ                          = (request.POST["SHQ"])
        NHF                          = (request.POST["NHF"])
        SHF                          = (request.POST["SHF"])
        Coldhandandfeet              = (request.POST["Coldhandandfeet"])
        Nauseaandvomiting	         = (request.POST["Nauseaandvomiting"])
        Stomachcolic                 = (request.POST["Stomachcolic"])
        AMS	                         = (request.POST["AMS"])
        Agony                        = (request.POST["Agony"])
        PIH	                         = (request.POST["PIH"])
        DAT	                         = (request.POST["DAT"])
        Cannotliedown                = (request.POST["Cannotliedown"])  

        #ทำนาย
        y_pred = decisiontree.predict([[gender, age, status, weights ,heights ,DHD,DPHD,onemeal,twomeals,threemeals,fourorfivemeal,
                Eat_spicy,Eat_salty,Eat_sweet,Eat_tasteless,Eat_rice,Eat_stickyrice,Eat_noodles,Eat_ricenoodles,Eat_bread,ERM,EPM,EWM,EFM,ESM,EAM,EVI,Eat_egg,
                Tastelessmilk,Sweetenedcondensedmilk,Sourmilk,Yogurt,Soymilk,Morningglory,
                Kale,Pumpkin,Cucumber,Greenbeans_longbeans,Papaya,Banana,Orange,Pineapple,Mango,Crisp,Icecream,Sparkingwater,
                Sweetwater,Tea,Coffee,Liquor_beer_wine,Energy_drink,MTS,Antidepressants,Antiepilepticdrug,Diabetesmedication,Birthcontrolpills,
                Antiinflammatorydrug,Antiviraldrug,Varioussupplements,Smoke,Run,Cycling,Swim,Basketball,Football,
                Yoga,Aerobic,Weightlifting,NGS,SHS,SDD,WEBFS,Difficultybreathing,WBLFTC,SWH,Itchyskin,TSY,Yellowskin,YSP,CRS,AirAllergic,
                Blurredvision,Badbreath,HFN,Urinaryincontinence,Foamyurine,WLC,Havestress,Dizziness,SHQ,NHF,SHF,Coldhandandfeet,Nauseaandvomiting,Stomachcolic,
                AMS,Agony,PIH,DAT,Cannotliedown]])

        result4 = ""+""
        if y_pred == [4]:
            result4 = "ท่านมีความเสี่ยงเป็นโรคไขมันในเลือดสูง"
        if y_pred == [0]:
            result4 = "ท่านไม่มีความเสี่ยงเป็นโรคไขมันในเลือดสูง"
            

        print("Hello")
        print(df.shape)
        print(y_pred.shape)
        print("ผลการทำนายโรคไขมันในเลือดสูง",y_pred)
        #print("การสอน",score)
        #print("การทดสอบ",score1)
        #print("ทำนาย",score2)
        #print(X_train.shape)
        #print(X_test.shape)
        #print(y_train.shape)
        #print(y_test.shape)

        #print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, y_pred)*100)

        #print("ค่าความถูกต้องของการสอน",metrics.accuracy_score(y_train, y_train))
        #print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, y_pred))
        #print(classification_report(y_test,y_pred))
        return result4
        #return render(request,'Result.html',{"result2":result2,"accuracyscoretest":accuracyscoretest})
        #return ({"result4":result4})

    print("Hello1")
    result1 = obesity()
    result2 = diabetes()
    result3 = hypertension()
    result4 = dieseaseofhyprtlipidemia()

    return render(request,'Result.html',{"result1": result1,"result2": result2,"result3": result3,"result4": result4})
   

#ฟังก์ชันที่มี3โรคไม่ตัดช้อย  
def TestTree2(request): 
    def obesity():
        # load dataset
        df = pd.read_csv('Dataset/dataobesity-1.csv',encoding='cp1252') #โรคอ้วน
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
        decisiontree = (DecisionTreeClassifier(criterion="entropy",max_depth=35))
        #train test train70 test 30
        X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
        decisiontree.fit(X_train,y_train)

        #แปลงข้อมูลก่อนใช้งาน
        sc = StandardScaler()
        sc.fit(X_train)
        X_train = sc.transform(X_train)
        X_test = sc.transform(X_test)

        gender          = (request.POST["gender"])
        age             = (request.POST["age"])
        status          = (request.POST["status"])
        weights         = (request.POST["weights"])
        heights         = (request.POST["heights"])
        DHD             = (request.POST["DHD"])
        DPHD            = (request.POST["DPHD"])
        onemeal         = (request.POST["onemeal"])
        twomeals        = (request.POST["twomeals"])
        threemeals      = (request.POST["threemeals"])
        fourorfivemeal  = (request.POST["fourorfivemeal"])
        Eat_spicy       = (request.POST["Eat_spicy"])
        Eat_salty       = (request.POST["Eat_salty"] )
        Eat_sweet       = (request.POST["Eat_sweet"] )
        Eat_tasteless   = (request.POST["Eat_tasteless"] ) 
        Eat_rice        = (request.POST["Eat_rice"])
        Eat_stickyrice  = (request.POST["Eat_stickyrice"])
        Eat_noodles     = (request.POST["Eat_noodles"] )
        Eat_ricenoodles = (request.POST["Eat_ricenoodles"] )
        Eat_bread       = (request.POST["Eat_bread"])
        Eat_sugar       = (request.POST["Eat_sugar"] )
        ERM             = (request.POST["ERM"])
        EPM             = (request.POST["EPM"] )
        EWM             = (request.POST["EWM"]  )  
        EFM             = (request.POST["EFM"])
        ESM             = (request.POST["ESM"] ) 
        EAM             = (request.POST["EAM"])
        EVI	            = (request.POST["EVI"])
        Eat_egg= (request.POST["Eat_egg"])
        Eat_nuts        = (request.POST["Eat_nuts"])
        Eat_tofu        = (request.POST["Eat_tofu"])
        Lord            = (request.POST["Lord"])
        Coconut_oil     = (request.POST["Coconut_oil"])
        Palm_oil        = (request.POST["Palm_oil"])
        Mixed_oil       = (request.POST["Mixed_oil"])
        Butterormargarine   = (request.POST["Butterormargarine"])
        Cookwithsteaming    = (request.POST["Cookwithsteaming"])
        Cookbyboiling       = (request.POST["Cookbyboiling"])
        Cookwithstirfry     = (request.POST["Cookwithstirfry"])
        Cookwithfries       = (request.POST["Cookwithfries"])
        Cookwithstew        = (request.POST["Cookwithstew"])
        Cookwithgrill       = (request.POST["Cookwithgrill"])
        Cookwithbaking      = (request.POST["Cookwithbaking"])
        Tastelessmilk       = (request.POST["Tastelessmilk"])
        Sweetmilk           = (request.POST["Sweetmilk"])
        Powdermilk          = (request.POST["Powdermilk"])
        Sweetenedcondensedmilk  = (request.POST["Sweetenedcondensedmilk"])
        Sourmilk                = (request.POST["Sourmilk"])
        Yogurt                  = (request.POST["Yogurt"])
        Soymilk                 = (request.POST["Soymilk"])
        Morningglory            = (request.POST["Morningglory"])
        Kale                    = (request.POST["Kale"])
        Pumpkin                 = (request.POST["Pumpkin"])
        Cucumber                = (request.POST["Cucumber"])
        Greenbeans_longbeans    = (request.POST["Greenbeans_longbeans"])
        Papaya                  = (request.POST["Papaya"])
        Banana                  = (request.POST["Banana"])
        Orange                  = (request.POST["Orange"])
        Pineapple               = (request.POST["Pineapple"])
        Mango                   = (request.POST["Mango"])
        Crisp                   = (request.POST["Crisp"])
        Thaidessert             = (request.POST["Thaidessert"])
        Cookie	                = (request.POST["Cookie"])
        Candy                   = (request.POST["Candy"])
        Icecream                = (request.POST["Icecream"])
        Sparkingwater           = (request.POST["Sparkingwater"])
        Sweetwater              = (request.POST["Sweetwater"])
        Tea                     = (request.POST["Tea"])
        Coffee                  = (request.POST["Coffee"])
        Liquor_beer_wine        = (request.POST["Liquor_beer_wine"])
        Energy_drink            = (request.POST["Energy_drink"])
        MTS                     = (request.POST["MTS"])
        Antidepressants         = (request.POST["Antidepressants"])
        Antiepilepticdrug       = (request.POST["Antiepilepticdrug"])
        Diabetesmedication      = (request.POST["Diabetesmedication"])
        Birthcontrolpills       = (request.POST["Birthcontrolpills"])
        Diffrentdrugforendometriosis = (request.POST["Diffrentdrugforendometriosis"])
        Antiinflammatorydrug         = (request.POST["Antiinflammatorydrug"])
        Antiviraldrug                = (request.POST["Antiviraldrug"])
        Varioussupplements           = (request.POST["Varioussupplements"])
        Smoke                        = (request.POST["Smoke"])
        Run                          = (request.POST["Run"])
        Cycling                      = (request.POST["Cycling"])
        Swim                         = (request.POST["Swim"])
        Basketball                   = (request.POST["Basketball"])
        Football                     = (request.POST["Football"])
        Yoga                         = (request.POST["Yoga"])
        Aerobic                      = (request.POST["Aerobic"])
        Weightlifting                = (request.POST["Weightlifting"])
        NGS                          = (request.POST["NGS"])
        SHS                          = (request.POST["SHS"])
        SDD                          = (request.POST["SDD"])
        WEBFS                        = (request.POST["WEBFS"])
        Difficultybreathing	         = (request.POST["Difficultybreathing"])
        WBLFTC	                     = (request.POST["WBLFTC"])
        SWH	                         = (request.POST["SWH"])
        Itchyskin                    = (request.POST["Itchyskin"])
        TSY                          = (request.POST["TSY"])
        Yellowskin                   = (request.POST["Yellowskin"])
        YSP                          = (request.POST["YSP"])
        CRS                          = (request.POST["CRS"])
        AirAllergic                  = (request.POST["AirAllergic"])
        Blurredvision                = (request.POST["Blurredvision"])
        Badbreath                    = (request.POST["Badbreath"])
        HFN                          = (request.POST["HFN"])
        Urinaryincontinence          = (request.POST["Urinaryincontinence"])
        Foamyurine                   = (request.POST["Foamyurine"])
        WLC                          = (request.POST["WLC"])
        Havestress                   = (request.POST["Havestress"])
        Dizziness	                 = (request.POST["Dizziness"])
        SHQ                          = (request.POST["SHQ"])
        NHF                          = (request.POST["NHF"])
        SHF                          = (request.POST["SHF"])
        Coldhandandfeet              = (request.POST["Coldhandandfeet"])
        Nauseaandvomiting	         = (request.POST["Nauseaandvomiting"])
        Stomachcolic                 = (request.POST["Stomachcolic"])
        AMS	                         = (request.POST["AMS"])
        Agony                        = (request.POST["Agony"])
        PIH	                         = (request.POST["PIH"])
        DAT	                         = (request.POST["DAT"])
        Cannotliedown                = (request.POST["Cannotliedown"])  

        #ทำนาย
        y_pred = decisiontree.predict([[gender, age, status, weights ,heights ,DHD,DPHD,onemeal,twomeals,threemeals,fourorfivemeal,
                    Eat_spicy,Eat_salty,Eat_sweet,Eat_tasteless,Eat_rice,Eat_stickyrice,Eat_noodles,Eat_ricenoodles,Eat_bread,Eat_sugar,ERM,EPM,EWM,EFM,ESM,EAM,EVI,Eat_egg,
                    Eat_nuts, Eat_tofu,Lord,Coconut_oil,Palm_oil,Mixed_oil,Butterormargarine,Cookwithsteaming,Cookbyboiling,Cookwithstirfry,Cookwithfries,
                    Cookwithstew,Cookwithgrill,Cookwithbaking,Tastelessmilk,Sweetmilk,Powdermilk,Sweetenedcondensedmilk,Sourmilk,Yogurt,Soymilk,Morningglory,
                    Kale,Pumpkin,Cucumber,Greenbeans_longbeans,Papaya,Banana,Orange,Pineapple,Mango,Crisp,Thaidessert,Cookie,Candy,Icecream,Sparkingwater,
                    Sweetwater,Tea,Coffee,Liquor_beer_wine,Energy_drink,MTS,Antidepressants,Antiepilepticdrug,Diabetesmedication,Birthcontrolpills,
                    Diffrentdrugforendometriosis,Antiinflammatorydrug,Antiviraldrug,Varioussupplements,Smoke,Run,Cycling,Swim,Basketball,Football,
                    Yoga,Aerobic,Weightlifting,NGS,SHS,SDD,WEBFS,Difficultybreathing,WBLFTC,SWH,Itchyskin,TSY,Yellowskin,YSP,CRS,AirAllergic,
                    Blurredvision,Badbreath,HFN,Urinaryincontinence,Foamyurine,WLC,Havestress,Dizziness,SHQ,NHF,SHF,Coldhandandfeet,Nauseaandvomiting,Stomachcolic,
                    AMS,Agony,PIH,DAT,Cannotliedown]])


        result1 = ""+""
        if y_pred == [1]:
            result1 = "ท่านเสี่ยงเป็นโรคอ้วน"
        if y_pred == [0]:
            result1 = "ท่านไม่เสี่ยงเป็นโรคอ้วน"
            return result1

        print("Hello")
        print(df.shape)
        print(y_pred.shape)
        print("ผลการทำนายโรคอ้วน",y_pred)
            #print("การสอน",score)
            #print("การทดสอบ",score1)
            #print("ทำนาย",score2)
            #print(X_train.shape)
            #print(X_test.shape)
            #print(y_train.shape)
            #print(y_test.shape)

            #print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, y_pred)*100)

            #print("ค่าความถูกต้องของการสอน",metrics.accuracy_score(y_train, y_train))
            #print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, y_pred))
            #print(classification_report(y_test,y_pred))
        
            #return render(request,'Result.html',{"result2":result2,"accuracyscoretest":accuracyscoretest})
        return (obesity,{"result1":result1})

    def diabetes():
        # load dataset
        df = pd.read_csv('Dataset/diabetes-1.csv',encoding='cp1252')# เบาหวาน
        
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
        decisiontree = (DecisionTreeClassifier(criterion="entropy",max_depth=35))
        #train test train80 test 20

        X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
        decisiontree.fit(X_train,y_train)   

        #แปลงข้อมูลก่อนใช้งาน
        sc = StandardScaler()
        sc.fit(X_train)
        X_train = sc.transform(X_train)
        X_test = sc.transform(X_test)      

        gender          = (request.POST["gender"])
        age             = (request.POST["age"])
        status          = (request.POST["status"])
        weights         = (request.POST["weights"])
        heights         = (request.POST["heights"])
        DHD             = (request.POST["DHD"])
        DPHD            = (request.POST["DPHD"])
        onemeal         = (request.POST["onemeal"])
        twomeals        = (request.POST["twomeals"])
        threemeals      = (request.POST["threemeals"])
        fourorfivemeal  = (request.POST["fourorfivemeal"])
        Eat_spicy       = (request.POST["Eat_spicy"])
        Eat_salty       = (request.POST["Eat_salty"] )
        Eat_sweet       = (request.POST["Eat_sweet"] )
        Eat_tasteless   = (request.POST["Eat_tasteless"] ) 
        Eat_rice        = (request.POST["Eat_rice"])
        Eat_stickyrice  = (request.POST["Eat_stickyrice"])
        Eat_noodles     = (request.POST["Eat_noodles"] )
        Eat_ricenoodles = (request.POST["Eat_ricenoodles"] )
        Eat_bread       = (request.POST["Eat_bread"])
        Eat_sugar       = (request.POST["Eat_sugar"] )
        ERM             = (request.POST["ERM"])
        EPM             = (request.POST["EPM"] )
        EWM             = (request.POST["EWM"]  )  
        EFM             = (request.POST["EFM"])
        ESM             = (request.POST["ESM"] ) 
        EAM             = (request.POST["EAM"])
        EVI	            = (request.POST["EVI"])
        Eat_egg= (request.POST["Eat_egg"])
        Eat_nuts        = (request.POST["Eat_nuts"])
        Eat_tofu        = (request.POST["Eat_tofu"])
        Lord            = (request.POST["Lord"])
        Coconut_oil     = (request.POST["Coconut_oil"])
        Palm_oil        = (request.POST["Palm_oil"])
        Mixed_oil       = (request.POST["Mixed_oil"])
        Butterormargarine   = (request.POST["Butterormargarine"])
        Cookwithsteaming    = (request.POST["Cookwithsteaming"])
        Cookbyboiling       = (request.POST["Cookbyboiling"])
        Cookwithstirfry     = (request.POST["Cookwithstirfry"])
        Cookwithfries       = (request.POST["Cookwithfries"])
        Cookwithstew        = (request.POST["Cookwithstew"])
        Cookwithgrill       = (request.POST["Cookwithgrill"])
        Cookwithbaking      = (request.POST["Cookwithbaking"])
        Tastelessmilk       = (request.POST["Tastelessmilk"])
        Sweetmilk           = (request.POST["Sweetmilk"])
        Powdermilk          = (request.POST["Powdermilk"])
        Sweetenedcondensedmilk  = (request.POST["Sweetenedcondensedmilk"])
        Sourmilk                = (request.POST["Sourmilk"])
        Yogurt                  = (request.POST["Yogurt"])
        Soymilk                 = (request.POST["Soymilk"])
        Morningglory            = (request.POST["Morningglory"])
        Kale                    = (request.POST["Kale"])
        Pumpkin                 = (request.POST["Pumpkin"])
        Cucumber                = (request.POST["Cucumber"])
        Greenbeans_longbeans    = (request.POST["Greenbeans_longbeans"])
        Papaya                  = (request.POST["Papaya"])
        Banana                  = (request.POST["Banana"])
        Orange                  = (request.POST["Orange"])
        Pineapple               = (request.POST["Pineapple"])
        Mango                   = (request.POST["Mango"])
        Crisp                   = (request.POST["Crisp"])
        Thaidessert             = (request.POST["Thaidessert"])
        Cookie	                = (request.POST["Cookie"])
        Candy                   = (request.POST["Candy"])
        Icecream                = (request.POST["Icecream"])
        Sparkingwater           = (request.POST["Sparkingwater"])
        Sweetwater              = (request.POST["Sweetwater"])
        Tea                     = (request.POST["Tea"])
        Coffee                  = (request.POST["Coffee"])
        Liquor_beer_wine        = (request.POST["Liquor_beer_wine"])
        Energy_drink            = (request.POST["Energy_drink"])
        MTS                     = (request.POST["MTS"])
        Antidepressants         = (request.POST["Antidepressants"])
        Antiepilepticdrug       = (request.POST["Antiepilepticdrug"])
        Diabetesmedication      = (request.POST["Diabetesmedication"])
        Birthcontrolpills       = (request.POST["Birthcontrolpills"])
        Diffrentdrugforendometriosis = (request.POST["Diffrentdrugforendometriosis"])
        Antiinflammatorydrug         = (request.POST["Antiinflammatorydrug"])
        Antiviraldrug                = (request.POST["Antiviraldrug"])
        Varioussupplements           = (request.POST["Varioussupplements"])
        Smoke                        = (request.POST["Smoke"])
        Run                          = (request.POST["Run"])
        Cycling                      = (request.POST["Cycling"])
        Swim                         = (request.POST["Swim"])
        Basketball                   = (request.POST["Basketball"])
        Football                     = (request.POST["Football"])
        Yoga                         = (request.POST["Yoga"])
        Aerobic                      = (request.POST["Aerobic"])
        Weightlifting                = (request.POST["Weightlifting"])
        NGS                          = (request.POST["NGS"])
        SHS                          = (request.POST["SHS"])
        SDD                          = (request.POST["SDD"])
        WEBFS                        = (request.POST["WEBFS"])
        Difficultybreathing	         = (request.POST["Difficultybreathing"])
        WBLFTC	                     = (request.POST["WBLFTC"])
        SWH	                         = (request.POST["SWH"])
        Itchyskin                    = (request.POST["Itchyskin"])
        TSY                          = (request.POST["TSY"])
        Yellowskin                   = (request.POST["Yellowskin"])
        YSP                          = (request.POST["YSP"])
        CRS                          = (request.POST["CRS"])
        AirAllergic                  = (request.POST["AirAllergic"])
        Blurredvision                = (request.POST["Blurredvision"])
        Badbreath                    = (request.POST["Badbreath"])
        HFN                          = (request.POST["HFN"])
        Urinaryincontinence          = (request.POST["Urinaryincontinence"])
        Foamyurine                   = (request.POST["Foamyurine"])
        WLC                          = (request.POST["WLC"])
        Havestress                   = (request.POST["Havestress"])
        Dizziness	                 = (request.POST["Dizziness"])
        SHQ                          = (request.POST["SHQ"])
        NHF                          = (request.POST["NHF"])
        SHF                          = (request.POST["SHF"])
        Coldhandandfeet              = (request.POST["Coldhandandfeet"])
        Nauseaandvomiting	         = (request.POST["Nauseaandvomiting"])
        Stomachcolic                 = (request.POST["Stomachcolic"])
        AMS	                         = (request.POST["AMS"])
        Agony                        = (request.POST["Agony"])
        PIH	                         = (request.POST["PIH"])
        DAT	                         = (request.POST["DAT"])
        Cannotliedown                = (request.POST["Cannotliedown"])  

        #ทำนาย
        y_pred = decisiontree.predict([[gender, age, status, weights ,heights ,DHD,DPHD,onemeal,twomeals,threemeals,fourorfivemeal,
                    Eat_spicy,Eat_salty,Eat_sweet,Eat_tasteless,Eat_rice,Eat_stickyrice,Eat_noodles,Eat_ricenoodles,Eat_bread,Eat_sugar,ERM,EPM,EWM,EFM,ESM,EAM,EVI,Eat_egg,
                    Eat_nuts, Eat_tofu,Lord,Coconut_oil,Palm_oil,Mixed_oil,Butterormargarine,Cookwithsteaming,Cookbyboiling,Cookwithstirfry,Cookwithfries,
                    Cookwithstew,Cookwithgrill,Cookwithbaking,Tastelessmilk,Sweetmilk,Powdermilk,Sweetenedcondensedmilk,Sourmilk,Yogurt,Soymilk,Morningglory,
                    Kale,Pumpkin,Cucumber,Greenbeans_longbeans,Papaya,Banana,Orange,Pineapple,Mango,Crisp,Thaidessert,Cookie,Candy,Icecream,Sparkingwater,
                    Sweetwater,Tea,Coffee,Liquor_beer_wine,Energy_drink,MTS,Antidepressants,Antiepilepticdrug,Diabetesmedication,Birthcontrolpills,
                    Diffrentdrugforendometriosis,Antiinflammatorydrug,Antiviraldrug,Varioussupplements,Smoke,Run,Cycling,Swim,Basketball,Football,
                    Yoga,Aerobic,Weightlifting,NGS,SHS,SDD,WEBFS,Difficultybreathing,WBLFTC,SWH,Itchyskin,TSY,Yellowskin,YSP,CRS,AirAllergic,
                    Blurredvision,Badbreath,HFN,Urinaryincontinence,Foamyurine,WLC,Havestress,Dizziness,SHQ,NHF,SHF,Coldhandandfeet,Nauseaandvomiting,Stomachcolic,
                    AMS,Agony,PIH,DAT,Cannotliedown]])


        result2= ""+""
        if y_pred == [2]:
            result2 = "ท่านเสี่ยงเป็นโรคเบาหวาน"
        if y_pred == [0]:
            result2 = "ท่านไม่เสี่ยงเป็นโรคเบาหวาน"
            return result2

        print("Hello")
        print(df.shape)
        print(y_pred.shape)
        print("ผลการทำนายโรคเบาหวาน",y_pred)
        #print("การสอน",score)
        #print("การทดสอบ",score1)
        #print("ทำนาย",score2)
        #print(X_train.shape)
        #print(X_test.shape)
        #print(y_train.shape)
        #print(y_test.shape)

        #print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, y_pred)*100)

        #print("ค่าความถูกต้องของการสอน",metrics.accuracy_score(y_train, y_train))
        #print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, y_pred))
        #print(classification_report(y_test,y_pred))
        
        #return render(request,'Result.html',{"result2":result2,"accuracyscoretest":accuracyscoretest})
        return {"result2":result2}

    def hypertension():
            # load dataset
            df = pd.read_csv('Dataset/hypertension-1.csv',encoding='cp1252')
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
            decisiontree = (DecisionTreeClassifier(criterion="entropy",max_depth=35))
            #train test train80 test 20
            X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
            #X_train,X_test,y_train,y_test = train_test_split(x,y)
            decisiontree.fit(X_train,y_train)

            #แปลงข้อมูลก่อนใช้งาน
            sc = StandardScaler()
            sc.fit(X_train)
            X_train = sc.transform(X_train)
            X_test = sc.transform(X_test)
               
            gender          = (request.POST["gender"])
            age             = (request.POST["age"])
            status          = (request.POST["status"])
            weights         = (request.POST["weights"])
            heights         = (request.POST["heights"])
            DHD             = (request.POST["DHD"])
            DPHD            = (request.POST["DPHD"])
            onemeal         = (request.POST["onemeal"])
            twomeals        = (request.POST["twomeals"])
            threemeals      = (request.POST["threemeals"])
            fourorfivemeal  = (request.POST["fourorfivemeal"])
            Eat_spicy       = (request.POST["Eat_spicy"])
            Eat_salty       = (request.POST["Eat_salty"] )
            Eat_sweet       = (request.POST["Eat_sweet"] )
            Eat_tasteless   = (request.POST["Eat_tasteless"] ) 
            Eat_rice        = (request.POST["Eat_rice"])
            Eat_stickyrice  = (request.POST["Eat_stickyrice"])
            Eat_noodles     = (request.POST["Eat_noodles"] )
            Eat_ricenoodles = (request.POST["Eat_ricenoodles"] )
            Eat_bread       = (request.POST["Eat_bread"])
            Eat_sugar       = (request.POST["Eat_sugar"] )
            ERM             = (request.POST["ERM"])
            EPM             = (request.POST["EPM"] )
            EWM             = (request.POST["EWM"]  )  
            EFM             = (request.POST["EFM"])
            ESM             = (request.POST["ESM"] ) 
            EAM             = (request.POST["EAM"])
            EVI	            = (request.POST["EVI"])
            Eat_egg= (request.POST["Eat_egg"])
            Eat_nuts        = (request.POST["Eat_nuts"])
            Eat_tofu        = (request.POST["Eat_tofu"])
            Lord            = (request.POST["Lord"])
            Coconut_oil     = (request.POST["Coconut_oil"])
            Palm_oil        = (request.POST["Palm_oil"])
            Mixed_oil       = (request.POST["Mixed_oil"])
            Butterormargarine   = (request.POST["Butterormargarine"])
            Cookwithsteaming    = (request.POST["Cookwithsteaming"])
            Cookbyboiling       = (request.POST["Cookbyboiling"])
            Cookwithstirfry     = (request.POST["Cookwithstirfry"])
            Cookwithfries       = (request.POST["Cookwithfries"])
            Cookwithstew        = (request.POST["Cookwithstew"])
            Cookwithgrill       = (request.POST["Cookwithgrill"])
            Cookwithbaking      = (request.POST["Cookwithbaking"])
            Tastelessmilk       = (request.POST["Tastelessmilk"])
            Sweetmilk           = (request.POST["Sweetmilk"])
            Powdermilk          = (request.POST["Powdermilk"])
            Sweetenedcondensedmilk  = (request.POST["Sweetenedcondensedmilk"])
            Sourmilk                = (request.POST["Sourmilk"])
            Yogurt                  = (request.POST["Yogurt"])
            Soymilk                 = (request.POST["Soymilk"])
            Morningglory            = (request.POST["Morningglory"])
            Kale                    = (request.POST["Kale"])
            Pumpkin                 = (request.POST["Pumpkin"])
            Cucumber                = (request.POST["Cucumber"])
            Greenbeans_longbeans    = (request.POST["Greenbeans_longbeans"])
            Papaya                  = (request.POST["Papaya"])
            Banana                  = (request.POST["Banana"])
            Orange                  = (request.POST["Orange"])
            Pineapple               = (request.POST["Pineapple"])
            Mango                   = (request.POST["Mango"])
            Crisp                   = (request.POST["Crisp"])
            Thaidessert             = (request.POST["Thaidessert"])
            Cookie	                = (request.POST["Cookie"])
            Candy                   = (request.POST["Candy"])
            Icecream                = (request.POST["Icecream"])
            Sparkingwater           = (request.POST["Sparkingwater"])
            Sweetwater              = (request.POST["Sweetwater"])
            Tea                     = (request.POST["Tea"])
            Coffee                  = (request.POST["Coffee"])
            Liquor_beer_wine        = (request.POST["Liquor_beer_wine"])
            Energy_drink            = (request.POST["Energy_drink"])
            MTS                     = (request.POST["MTS"])
            Antidepressants         = (request.POST["Antidepressants"])
            Antiepilepticdrug       = (request.POST["Antiepilepticdrug"])
            Diabetesmedication      = (request.POST["Diabetesmedication"])
            Birthcontrolpills       = (request.POST["Birthcontrolpills"])
            Diffrentdrugforendometriosis = (request.POST["Diffrentdrugforendometriosis"])
            Antiinflammatorydrug         = (request.POST["Antiinflammatorydrug"])
            Antiviraldrug                = (request.POST["Antiviraldrug"])
            Varioussupplements           = (request.POST["Varioussupplements"])
            Smoke                        = (request.POST["Smoke"])
            Run                          = (request.POST["Run"])
            Cycling                      = (request.POST["Cycling"])
            Swim                         = (request.POST["Swim"])
            Basketball                   = (request.POST["Basketball"])
            Football                     = (request.POST["Football"])
            Yoga                         = (request.POST["Yoga"])
            Aerobic                      = (request.POST["Aerobic"])
            Weightlifting                = (request.POST["Weightlifting"])
            NGS                          = (request.POST["NGS"])
            SHS                          = (request.POST["SHS"])
            SDD                          = (request.POST["SDD"])
            WEBFS                        = (request.POST["WEBFS"])
            Difficultybreathing	         = (request.POST["Difficultybreathing"])
            WBLFTC	                     = (request.POST["WBLFTC"])
            SWH	                         = (request.POST["SWH"])
            Itchyskin                    = (request.POST["Itchyskin"])
            TSY                          = (request.POST["TSY"])
            Yellowskin                   = (request.POST["Yellowskin"])
            YSP                          = (request.POST["YSP"])
            CRS                          = (request.POST["CRS"])
            AirAllergic                  = (request.POST["AirAllergic"])
            Blurredvision                = (request.POST["Blurredvision"])
            Badbreath                    = (request.POST["Badbreath"])
            HFN                          = (request.POST["HFN"])
            Urinaryincontinence          = (request.POST["Urinaryincontinence"])
            Foamyurine                   = (request.POST["Foamyurine"])
            WLC                          = (request.POST["WLC"])
            Havestress                   = (request.POST["Havestress"])
            Dizziness	                 = (request.POST["Dizziness"])
            SHQ                          = (request.POST["SHQ"])
            NHF                          = (request.POST["NHF"])
            SHF                          = (request.POST["SHF"])
            Coldhandandfeet              = (request.POST["Coldhandandfeet"])
            Nauseaandvomiting	         = (request.POST["Nauseaandvomiting"])
            Stomachcolic                 = (request.POST["Stomachcolic"])
            AMS	                         = (request.POST["AMS"])
            Agony                        = (request.POST["Agony"])
            PIH	                         = (request.POST["PIH"])
            DAT	                         = (request.POST["DAT"])
            Cannotliedown                = (request.POST["Cannotliedown"])  

            #ทำนาย
            y_pred = decisiontree.predict([[gender, age, status, weights ,heights ,DHD,DPHD,onemeal,twomeals,threemeals,fourorfivemeal,
                        Eat_spicy,Eat_salty,Eat_sweet,Eat_tasteless,Eat_rice,Eat_stickyrice,Eat_noodles,Eat_ricenoodles,Eat_bread,Eat_sugar,ERM,EPM,EWM,EFM,ESM,EAM,EVI,Eat_egg,
                        Eat_nuts, Eat_tofu,Lord,Coconut_oil,Palm_oil,Mixed_oil,Butterormargarine,Cookwithsteaming,Cookbyboiling,Cookwithstirfry,Cookwithfries,
                        Cookwithstew,Cookwithgrill,Cookwithbaking,Tastelessmilk,Sweetmilk,Powdermilk,Sweetenedcondensedmilk,Sourmilk,Yogurt,Soymilk,Morningglory,
                        Kale,Pumpkin,Cucumber,Greenbeans_longbeans,Papaya,Banana,Orange,Pineapple,Mango,Crisp,Thaidessert,Cookie,Candy,Icecream,Sparkingwater,
                        Sweetwater,Tea,Coffee,Liquor_beer_wine,Energy_drink,MTS,Antidepressants,Antiepilepticdrug,Diabetesmedication,Birthcontrolpills,
                        Diffrentdrugforendometriosis,Antiinflammatorydrug,Antiviraldrug,Varioussupplements,Smoke,Run,Cycling,Swim,Basketball,Football,
                        Yoga,Aerobic,Weightlifting,NGS,SHS,SDD,WEBFS,Difficultybreathing,WBLFTC,SWH,Itchyskin,TSY,Yellowskin,YSP,CRS,AirAllergic,
                        Blurredvision,Badbreath,HFN,Urinaryincontinence,Foamyurine,WLC,Havestress,Dizziness,SHQ,NHF,SHF,Coldhandandfeet,Nauseaandvomiting,Stomachcolic,
                        AMS,Agony,PIH,DAT,Cannotliedown]])
           
            result3 = ""+""
            if y_pred == [3]:
                result3 = "ท่านเสี่ยงเป็นโรคความดัน"
            if y_pred == [0]:
                result3 = "ท่านไม่เสี่ยงเป็นโรคความดัน"
                return result3
               
            print("Hello")
            print(df.shape)
            print(y_pred.shape)
            print("ผลการทำนายโรคความดัน",y_pred)
                #print("การสอน",score)
                #print("การทดสอบ",score1)
                #print("ทำนาย",score2)
                #print(X_train.shape)
                #print(X_test.shape)
                #print(y_train.shape)
                #print(y_test.shape)

                #print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, y_pred)*100)

                #print("ค่าความถูกต้องของการสอน",metrics.accuracy_score(y_train, y_train))
                #print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, y_pred))
                #print(classification_report(y_test,y_pred))
            
            #return render(request,'Result.html',{"result2":result2,"accuracyscoretest":accuracyscoretest})
            return {"result3":result3}
    print("Hello1")
    result1 = obesity()
    result2 = diabetes()
    result3 = hypertension()

    return render(request,'Result.html',{"result1": result1,"result2": result2,"result3": result3})


#ฟังก์ชันที่มีแค่โรคเดียว
def TestTree1(request): 
    # load dataset
    df = pd.read_csv('Dataset/dataobesity-2.csv',encoding='cp1252') #โรคอ้วน
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
    decisiontree = (DecisionTreeClassifier(criterion="entropy",max_depth=35))
    #train test train70 test 30
    X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
    decisiontree.fit(X_train,y_train)

    #แปลงข้อมูลก่อนใช้งาน
    sc = StandardScaler()
    sc.fit(X_train)
    X_train = sc.transform(X_train)
    X_test = sc.transform(X_test)

    gender          = (request.POST["gender"])
    age             = (request.POST["age"])
    status          = (request.POST["status"])
    weights         = (request.POST["weights"])
    heights         = (request.POST["heights"])
    DHD             = (request.POST["DHD"])
    DPHD            = (request.POST["DPHD"])
    onemeal         = (request.POST["onemeal"])
    twomeals        = (request.POST["twomeals"])
    threemeals      = (request.POST["threemeals"])
    fourorfivemeal  = (request.POST["fourorfivemeal"])
    Eat_spicy       = (request.POST["Eat_spicy"])
    Eat_salty       = (request.POST["Eat_salty"] )
    Eat_sweet       = (request.POST["Eat_sweet"] )
    Eat_tasteless   = (request.POST["Eat_tasteless"] ) 
    Eat_rice        = (request.POST["Eat_rice"])
    Eat_stickyrice  = (request.POST["Eat_stickyrice"])
    Eat_noodles     = (request.POST["Eat_noodles"] )
    Eat_ricenoodles = (request.POST["Eat_ricenoodles"] )    
    Eat_bread       = (request.POST["Eat_bread"])
    ERM             = (request.POST["ERM"])
    EPM             = (request.POST["EPM"] )
    EWM             = (request.POST["EWM"]  )  
    EFM             = (request.POST["EFM"])
    ESM             = (request.POST["ESM"] ) 
    EAM             = (request.POST["EAM"])
    EVI	            = (request.POST["EVI"])
    Eat_egg         = (request.POST["Eat_egg"])
    Tastelessmilk       = (request.POST["Tastelessmilk"])
    Sweetenedcondensedmilk  = (request.POST["Sweetenedcondensedmilk"])
    Sourmilk                = (request.POST["Sourmilk"])
    Yogurt                  = (request.POST["Yogurt"])
    Soymilk                 = (request.POST["Soymilk"])
    Morningglory            = (request.POST["Morningglory"])
    Kale                    = (request.POST["Kale"])
    Pumpkin                 = (request.POST["Pumpkin"])
    Cucumber                = (request.POST["Cucumber"])
    Greenbeans_longbeans    = (request.POST["Greenbeans_longbeans"])
    Papaya                  = (request.POST["Papaya"])
    Banana                  = (request.POST["Banana"])
    Orange                  = (request.POST["Orange"])
    Pineapple               = (request.POST["Pineapple"])
    Mango                   = (request.POST["Mango"])
    Crisp                   = (request.POST["Crisp"])
    Icecream                = (request.POST["Icecream"])
    Sparkingwater           = (request.POST["Sparkingwater"])
    Sweetwater              = (request.POST["Sweetwater"])
    Tea                     = (request.POST["Tea"])
    Coffee                  = (request.POST["Coffee"])
    Liquor_beer_wine        = (request.POST["Liquor_beer_wine"])
    Energy_drink            = (request.POST["Energy_drink"])
    MTS                     = (request.POST["MTS"])
    Antidepressants         = (request.POST["Antidepressants"])
    Antiepilepticdrug       = (request.POST["Antiepilepticdrug"])
    Diabetesmedication      = (request.POST["Diabetesmedication"])
    Birthcontrolpills       = (request.POST["Birthcontrolpills"])
    Antiinflammatorydrug         = (request.POST["Antiinflammatorydrug"])
    Antiviraldrug                = (request.POST["Antiviraldrug"])
    Varioussupplements           = (request.POST["Varioussupplements"])
    Smoke                        = (request.POST["Smoke"])
    Run                          = (request.POST["Run"])
    Cycling                      = (request.POST["Cycling"])
    Swim                         = (request.POST["Swim"])
    Basketball                   = (request.POST["Basketball"])
    Football                     = (request.POST["Football"])
    Yoga                         = (request.POST["Yoga"])
    Aerobic                      = (request.POST["Aerobic"])
    Weightlifting                = (request.POST["Weightlifting"])
    NGS                          = (request.POST["NGS"])
    SHS                          = (request.POST["SHS"])
    SDD                          = (request.POST["SDD"])
    WEBFS                        = (request.POST["WEBFS"])
    Difficultybreathing	         = (request.POST["Difficultybreathing"])
    WBLFTC	                     = (request.POST["WBLFTC"])
    SWH	                         = (request.POST["SWH"])
    Itchyskin                    = (request.POST["Itchyskin"])
    TSY                          = (request.POST["TSY"])
    Yellowskin                   = (request.POST["Yellowskin"])
    YSP                          = (request.POST["YSP"])
    CRS                          = (request.POST["CRS"])
    AirAllergic                  = (request.POST["AirAllergic"])
    Blurredvision                = (request.POST["Blurredvision"])
    Badbreath                    = (request.POST["Badbreath"])
    HFN                          = (request.POST["HFN"])
    Urinaryincontinence          = (request.POST["Urinaryincontinence"])
    Foamyurine                   = (request.POST["Foamyurine"])
    WLC                          = (request.POST["WLC"])
    Havestress                   = (request.POST["Havestress"])
    Dizziness	                 = (request.POST["Dizziness"])
    SHQ                          = (request.POST["SHQ"])
    NHF                          = (request.POST["NHF"])
    SHF                          = (request.POST["SHF"])
    Coldhandandfeet              = (request.POST["Coldhandandfeet"])
    Nauseaandvomiting	         = (request.POST["Nauseaandvomiting"])
    Stomachcolic                 = (request.POST["Stomachcolic"])
    AMS	                         = (request.POST["AMS"])
    Agony                        = (request.POST["Agony"])
    PIH	                         = (request.POST["PIH"])
    DAT	                         = (request.POST["DAT"])
    Cannotliedown                = (request.POST["Cannotliedown"])  

    #ทำนาย
    y_pred = decisiontree.predict([[gender, age, status, weights ,heights ,DHD,DPHD,onemeal,twomeals,threemeals,fourorfivemeal,
                Eat_spicy,Eat_salty,Eat_sweet,Eat_tasteless,Eat_rice,Eat_stickyrice,Eat_noodles,Eat_ricenoodles,Eat_bread,ERM,EPM,EWM,EFM,ESM,EAM,EVI,Eat_egg,
                Tastelessmilk,Sweetenedcondensedmilk,Sourmilk,Yogurt,Soymilk,Morningglory,
                Kale,Pumpkin,Cucumber,Greenbeans_longbeans,Papaya,Banana,Orange,Pineapple,Mango,Crisp,Icecream,Sparkingwater,
                Sweetwater,Tea,Coffee,Liquor_beer_wine,Energy_drink,MTS,Antidepressants,Antiepilepticdrug,Diabetesmedication,Birthcontrolpills,
                Antiinflammatorydrug,Antiviraldrug,Varioussupplements,Smoke,Run,Cycling,Swim,Basketball,Football,
                Yoga,Aerobic,Weightlifting,NGS,SHS,SDD,WEBFS,Difficultybreathing,WBLFTC,SWH,Itchyskin,TSY,Yellowskin,YSP,CRS,AirAllergic,
                Blurredvision,Badbreath,HFN,Urinaryincontinence,Foamyurine,WLC,Havestress,Dizziness,SHQ,NHF,SHF,Coldhandandfeet,Nauseaandvomiting,Stomachcolic,
                AMS,Agony,PIH,DAT,Cannotliedown]])    

    result2 = ""+""
    if y_pred == [1]:
        result2 = "ท่านเสี่ยงเป็นโรคอ้วน"
    if y_pred == [2]:
        result2 = "ท่านเสี่ยงเป็นโรคเบาหวาน"
    if y_pred == [3]:
        result2 = "ท่านเสี่ยงเป็นโรคความดัน"
    if y_pred == [0]:
        result2 = "ท่านไม่เสี่ยงเป็นโรค"

    #score = cross_val_score(decisiontree,X_train,y_train, cv=6, scoring="accuracy")#ดูการสอน
    #score1 = cross_val_score(decisiontree,X_test,y_test, cv=6, scoring="accuracy")#ดูการทดสอบ
    #score2 = cross_val_predict(decisiontree,X_test,y_test, cv=6)#การทำนาย   
    #accuracyscoretest = metrics.accuracy_score(y_test, y_pred)*100

    print("Hello")
    print(df.shape)
    print(y_pred.shape)
    #print("การสอน",score)
    #print("การทดสอบ",score1)
    #print("ทำนาย",score2)
    #print(X_train.shape)
    #print(X_test.shape)
    #print(y_train.shape)
    #print(y_test.shape)

    #print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, y_pred)*100)

    #print("ค่าความถูกต้องของการสอน",metrics.accuracy_score(y_train, y_train))
    #print("ค่าความถูกต้องของการทดสอบ",metrics.accuracy_score(y_test, y_pred))
    #print(classification_report(y_test,y_pred))
    print("ผลการทำนาย",y_pred)
    #return render(request,'Result.html',{"result2":result2,"accuracyscoretest":accuracyscoretest})
    return render(request,'Result.html',{"result2":result2})