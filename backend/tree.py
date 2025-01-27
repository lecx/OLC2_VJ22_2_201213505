
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier, plot_tree
import pandas as pd
import numpy as np
from PIL import Image, ImageFont, ImageDraw 
le = preprocessing.LabelEncoder()
#df = pd.read_excel('ent.xlsx')
df = pd.read_csv('pred.csv')

#header = ['A','I']
header = ['A','B','C','D','E']

sizeH = len(header)-1

print("lenCol",sizeH)

lines = []

for i in range(sizeH):    
    print(np.asarray(df[header[i]]))
    lines.append(np.asarray(df[header[i]]))

print(np.asarray(df[header[sizeH]]))
play = np.asarray(df[header[sizeH]])

valS = '5,500,200,False'.split(',')


val = le.fit_transform(valS)

valorPred = val
#valorPred = [int(i, base=16) for i in val]
print(valorPred)

features = list(zip(*lines))
print(features)
clf = DecisionTreeClassifier(max_depth=4,random_state=0).fit(features, play);

predicted = clf.predict([valorPred])
print(predicted)

#plt.title('Arbol de Desición \n' + "PRED = {}".format(prediction))
plt.figure()        
plot_tree(clf, filled=True,fontsize=10)
plt.show();

img = Image.new('RGB', (700, 500), color = 'white')
d = ImageDraw.Draw(img)
myFont = ImageFont.truetype('arial.ttf', 30)

str1 = "Clasificador Arbol de Desición\n\n"
for i in lines:
    str1 += str(i) + '\n'

str1 += "\nValor de Prediccion: " + str(valorPred) + "\n"
str1 += "\n\tPrediccion: " + str(predicted)
d.text((10,10), str1, font=myFont,fill='black')
img.save('arbol.png')
