from sklearn import datasets
from sklearn import svm
from sklearn import metrics


digits = datasets.load_digits()

n_train = len(digits.data) * 2 // 3
X_train = digits.data[:n_train]
y_train = digits.target[:n_train]
X_test = digits.data[n_train:]
y_test = digits.target[n_train:]

clf = svm.SVC(gamma=0.001)
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
predicted = clf.predict(X_test)
print(predicted)

print(metrics.classification_report(y_test, predicted))
print(metrics.confusion_matrix(y_test, predicted))
