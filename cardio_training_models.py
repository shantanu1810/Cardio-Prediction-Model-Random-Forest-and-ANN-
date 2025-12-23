import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import joblib
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


dataset=pd.read_csv('cardio_train.csv')

x=dataset.drop(['id','cardio'],axis=1)
y=dataset['cardio']
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=42)

scaler=StandardScaler()

xtrain=scaler.fit_transform(xtrain)
xtest=scaler.transform(xtest)

RF_model=RandomForestClassifier(n_estimators=100,random_state=42)
RF_model.fit(xtrain,ytrain)
ypred=RF_model.predict(xtest)



NN_model=Sequential([
    Dense(64,activation='relu',input_shape=(xtrain.shape[1],)),
    Dense(32,activation='relu'),
    Dense(16,activation='relu'),
    Dense(1,activation='sigmoid')
])

NN_model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

train_nn_model=NN_model.fit(xtrain,ytrain,epochs=40,batch_size=32,validation_split=0.2,verbose=1)

tloss,tacc=NN_model.evaluate(xtest,ytest,verbose=0)
print("NN Acc:",tacc)
print("RF Acc : ",accuracy_score(ytest,ypred))
joblib.dump(RF_model,'Rf_Nodel.sav')
joblib.dump(scaler,'scaler.save')
NN_model.save('NN_Model.keras')