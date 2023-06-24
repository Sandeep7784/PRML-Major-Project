# from django.shortcuts import render
# from sklearn.preprocessing import OrdinalEncoder
# from sklearn.preprocessing import StandardScaler

# from joblib import load
# model = load('./savedModels/model_major.joblib')

# def predictor(request):
#     if request.method == 'POST':
#         input1 = request.POST['input1']
#         input2 = request.POST['input2']
#         input3 = request.POST['input3']
#         input4 = request.POST['input4']
#         input5 = request.POST['input5']
#         input6 = request.POST['input6']
#         input7 = request.POST['input7']
#         input8 = float(input5) - float(input4)
#         input8 = str(input8)

#         l=[[input1, input2, input3, input4, input5, input6, input7, input8]]

#         encoder = OrdinalEncoder()
#         encoded_data = encoder.fit_transform(l)

#         scaler = StandardScaler()
#         df_scaled = scaler.fit_transform(encoded_data)

#         y_pred = model.predict(df_scaled)


#         print('y_pred:', y_pred)
#         if y_pred[0] == 0:
#             y_pred = 'Non Fraud'
#         else:
#             y_pred = 'Fraud'
#         return render(request, 'main.html', {'result' : y_pred})
#     return render(request, 'main.html')

# def index(request):
#     return render(request, 'index.html') 
from django.shortcuts import render
import librosa
import soundfile
import os, glob, pickle
import numpy as np
import librosa.display

from joblib import load
model = load('./savedModels/model_major.joblib')

def predictor(request):
    # pass
    if request.method == 'POST':

        # print(request.FILES.get('file-upload'))
        file =  request.FILES.get('file-upload')
        l_mfccs=[]
        l_chroma=[]
        l_mel=[]
        y=[]
        n_plots=0
        l_file=[]
        print(model)
        # Load audio file
        signal, sr = librosa.load(file)
        # signal, sr = librosa.load(file)
        
        # print(sr)
        l_file.append(file)

        # Extract MFCC features
        mfccs = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=20)
        mfccs = np.mean(mfccs, axis=1) # Take the mean of each MFCC coefficient
        l_mfccs.append(mfccs)

            # extract chroma feature
        chroma = librosa.feature.chroma_stft(y=signal, sr=sr)
        chroma_mean = np.mean(chroma, axis=1)
        l_chroma.append(chroma_mean)
        
        # extract mel feature
        mel = librosa.feature.melspectrogram(y=signal, sr=sr)
        mel_mean = np.mean(mel, axis=1)
        l_mel.append(mel_mean)
        
        l_file=np.array(l_file)
        l_mfccs=np.array(l_mfccs)
        l_chroma=np.array(l_chroma)
        l_mel=np.array(l_mel)
        
        X_test=np.hstack((l_mfccs,l_chroma,l_mel))
        
        y_pred=model.predict(X_test)

        print('y_pred:', y_pred)
        # if y_pred[0] == 0:
        #     y_pred = 'Non Fraud'
        # else:
        #     y_pred = 'Fraud'
        return render(request, 'form.html', {'result' : y_pred})
    return render(request, 'form.html')

def index(request):
    return render(request, 'index.html') 
