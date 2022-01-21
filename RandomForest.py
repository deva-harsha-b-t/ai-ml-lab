from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score 
from sklearn import datasets

iris=datasets.load_iris() 
iris_data=iris.data 
iris_labels=iris.target 
#print(iris_data) 
#print(iris_labels)

x_train, x_test, y_train, y_test=train_test_split(iris_data,iris_labels,test_size=0.30) 
classifier=RandomForestClassifier(n_estimators=100) 
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)


print('confusion matrix is as follows') 
print(confusion_matrix(y_test,y_pred)) 
print('Accuracy metrics')
 
print(classification_report(y_test,y_pred)) 
print("Accuracy:\n",accuracy_score(y_test, y_pred))
