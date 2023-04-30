from django.shortcuts import render
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler

from joblib import load
model = load('./savedModels/model_rishav_aich.joblib')

def predictor(request):
    if request.method == 'POST':
        input1 = request.POST['input1']
        input2 = request.POST['input2']
        input3 = request.POST['input3']
        input4 = request.POST['input4']
        input5 = request.POST['input5']
        input6 = request.POST['input6']
        input7 = request.POST['input7']
        input8 = float(input5) - float(input4)
        input8 = str(input8)

        l=[[input1, input2, input3, input4, input5, input6, input7, input8]]

        encoder = OrdinalEncoder()
        encoded_data = encoder.fit_transform(l)

        scaler = StandardScaler()
        df_scaled = scaler.fit_transform(encoded_data)

        y_pred = model.predict(df_scaled)


        print('y_pred:', y_pred)
        if y_pred[0] == 0:
            y_pred = 'Non Fraud'
        else:
            y_pred = 'Fraud'
        return render(request, 'main.html', {'result' : y_pred})
    return render(request, 'main.html')

def index(request):
    return render(request, 'index.html') 
