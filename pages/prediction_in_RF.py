import joblib
import pandas as pd
import streamlit as st
from PIL import Image

Page_title="Random Forest Based Model"
icon=Image.open("neuralnetworklogo.jpg")
st.set_page_config(page_title=Page_title,page_icon=icon,layout="wide",initial_sidebar_state="collapsed")
def Random_Forest_Model(age,gender,height,weight,aphi,aplo,cholesterol,gluc,smoke,alco,active,):
    Rf_model=joblib.load('Rf_Nodel.sav')
    scaler=joblib.load('scaler.save')

    data={'age':age,'gender':gender,'height':height,'weight':weight,'ap_hi':aphi,'ap_lo':aplo,'cholesterol':cholesterol,'gluc':gluc,'smoke':smoke,'alco':alco,'active':active}
    df=pd.DataFrame(data,index=[0])
    df=scaler.transform(df)
    ypre=Rf_model.predict(df)
    return ypre

st.markdown(
    """
    <style>
        .st-emotion-cache-pkm19r{
            display:none;
        }
        div.stColumn{
            width:25%;
        }
        div[data-testid="stToolbar"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }
        div[data-testid="stDecoration"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }
        div[data-testid="stStatusWidget"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }
        #MainMenu {
        visibility: hidden;
        height: 0%;
        }
        header {
        visibility: hidden;
        height: 0%;
        }
        footer {
        visibility: hidden;
        height: 0%;
        }
    </style>
    """,
    unsafe_allow_html=True
)

col0,col1=st.columns(2)
with col0:
    st.page_link('index.py',label=':blue-background[Back to main]')
with col1:
    st.page_link('pages/prediction_in_NN.py',label=':green-background[Artificial Neural Network Model]')

st.title("Random Forest Model")
with st.form('Details'):
    name=st.text_input("Name")
    age=st.text_input('Age')
    gender=st.selectbox(
        'Gender',
        ['Male','Female']
    )
    height=st.text_input('Height (in Centimeter)')
    weight=st.text_input('weight (in kilogram)')
    aphi=st.text_input('BP Systolic Pressure(Upper Number)')
    aplo=st.text_input('BP Diastolic Pressure(Lower Number)')
    cholesterol=st.selectbox(
        'Cholestoral',['Normal','Above Normal','High']
    )
    gluc=st.selectbox(
        'Sugar Level',['Normal','Above Normal','High']
    )
    smoke=st.selectbox(
        'Do Smoking',
        ['NO','YES']
    )
    alco=st.selectbox(
        'Drink Alcohol',
        ['NO','YES']
    )
    active=st.selectbox(
        'Do Activity',
        ['NO','YES']
    )

    submitted=st.form_submit_button('Submit')

if(submitted):
    y_n={'YES':1,"NO":0}
    ch_gl={'Normal':1,'Above Normal':2,'High':3}
    gen={'Male':2,'Female':1}
    preval=Random_Forest_Model(float(age)*365.24,gen[gender],float(height),float(weight),float(aphi),float(aplo),ch_gl[cholesterol],ch_gl[gluc],y_n[smoke],y_n[alco],y_n[active])
    if(preval==1):
        g,al=1,1
        ans="Hello, "+name+"\n\n"
        if(smoke=='YES'):
            
            ans=ans+"You do Smoking. You need to avoid smoking as much as possible "
            if(alco=="YES"):
                al=0
                ans=ans+"and also you drink alcohol. Smoking and alcohol is very much injurious to health. It is a suggesstion to stop both.\n"
                if(gluc!="Normal"):
                    g=0
                    ans+="Alcohol as also one of the reason for you sugar level increase. And also maintain a proper diet.\n\n"
                else:
                    ans+="Stop Drinking alcohol our your sugar level may increase.\n\n"
            else:
                ans+=".\n\n"
        if(alco=="YES" and al==1):
            ans=ans+"You drink alcohol. You need to stop drinking alcohol."
            if(gluc!="Normal"):
                g=0
                ans+="Alcohol may be also the reason for you sugar level increase.\n\n"
            else:
                ans+="Stop Drinking alcohol our your sugar level may increase.\n\n"
        if(gluc!='Normal' and g==1):
            ans+="Your Sugar Level rise, So maintain a proper diet and try to avoid high sugar foods and cold drinks.\n\n"
        if(cholesterol!="Normal"):
            ans+="You have "+cholesterol+" cholesterol that is because of you unhealth diet. Try as much to avoid unhealth foods and drinks.\n\n"
        if(int(aphi)>120):
            ans+="You have high Blood Pressure."
            if(alco=="YES"):
                ans+="This is because you drink alcohol"
                if(smoke=="YES"):
                    ans+=" and smoking.\n\n"
                else:
                    ans+=".\n\n"
            elif(smoke=='YES'):
                ans+="This is because you do smoking.\n\n"
        elif(int(aplo)>80 and int(aphi)<=120):
            ans+="Your blood pressure is elevated.\n\n"
        if(float(weight)>=120.0):
            ans+="Your weight is too heavy.\n\n"
        elif(float(weight)>=100.0 and float(height)<165.0):
            ans+="Your Weight is also heavy with respect with your height.\n\n"
        
        if(active=="YES"):
            ans+="***It is a good thing that you do activities but with that you can also start doing cardio***.\n\n"
        elif(int(aphi)<90):
            ans+="***You Blood pressure is low although you need cardio to do but before consult with your doctor before starting***.\n\n"
        else:
            ans+="***Considering the all the things you need to do cardio and exercise daily for better health***.\n\n"
        st.warning(ans)
    else:
        g,al=1,1
        c=0
        ans="Hello, "+name+"\n\n"
        if(smoke=='YES'):
            ans=ans+"You do Smoking. It is a suggession to Stop smoking it may effect you health in future."
            c+=3
            if(alco=="YES"):
                c+=3
                al=0
                ans=ans+"And also you drink alcohol. Smoking and alcohol is very much injurious to health. It is a suggesstion to stop both.\n\n"
                if(gluc!="Normal"):
                    g=0
                    ans+="Alcohol as also one of the reason for you sugar level increase.\n\n"
                else:
                    ans+="Stop Drinking alcohol our your sugar level may increase.\n\n"
            else:
                ans+="."
        if(alco=="YES" and al==1):
            ans=ans+"You drink alcohol. You need to stop drinking alcohol.\n\n"
            if(gluc!="Normal"):
                g=0
                ans+="Alcohol is also one of the reason for you sugar level increase.\n\n"
            else:
                ans+="Stop Drinking alcohol our your sugar level may increase.\n\n"
        if(gluc!='Normal' and g==1):
            ans+="Your Sugar Level rise, So maintain a proper diet and try to avoid high sugar foods and cold drinks.\n\n"
        c+=ch_gl[gluc]-2
        if(cholesterol!="Normal"):
            ans+="You have "+cholesterol+" cholesterol that is because of you unhealth diet. Try as much to avoid unhealth foods and drinks.\n\n"
        c+=ch_gl[cholesterol]-2
        if(int(aphi)>120):
            ans+="You have high Blood Pressure."
            if(alco=="YES"):
                ans+="This is because you drink alcohol"
                if(smoke=="YES"):
                    ans+=" and smoking.\n\n"
                else:
                    ans+=".\n\n"
            elif(smoke=='YES'):
                ans+="This is because you do smoking.\n\n"
        elif(int(aplo)>80 and int(aphi)<=120):
            ans+="Your blood pressure is elevated.\n\n"
        if(float(weight)>=100.0 and float(height)<165.0):
            ans+="Your Weight is also heavy with respect with your height.\n\n"
        elif(float(weight)>120.0):
            ans+="Your weight is too heavy.\n\n"
            if(active=="NO"):
                ans+="Exercise can help you to reduce weight.\n\n"
        
        if(active=="YES"):
            ans+="***You do exercise so you don't need to do cardio for now***.\n\n"
        elif(int(aphi)<90 and c>=6):
            ans+="***You Blood pressure is low although you need cardio to do but before consult with your doctor before starting***.\n\n"
        elif(c>=6):
            ans+="***Although your health suggested preety good but you are suggested to do cardio few times***.\n\n"
        else:
            ans+="***For Now you are fit you don't need to do cardio***.\n\n"
        st.success(ans)