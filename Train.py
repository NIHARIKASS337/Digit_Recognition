from sklearn.preprocessing import scale
import pandas as pd
from sklearn.model_selection import train_test_split


digits = pd.read_csv("train.csv")

# Creating training and test sets
# Splitting the data into train and test
X = digits.iloc[:, 1:]
Y = digits.iloc[:, 0]

# Rescaling the features
X = scale(X)

# train test split with train_size=10% and test size=90%
x_train, x_test, y_train, y_test = train_test_split(
    X, Y, train_size=0.10, random_state=101)


def get_array(n):
    from PIL import Image
    import numpy

    img = Image.open(n)
    np_img = numpy.array(img)
    nx = np_img.reshape(1, 784)
    return nx


def linear_svm(x):
    from sklearn import svm

    n = get_array(x)

    # an initial SVM model with linear kernel
    svm_linear = svm.SVC(kernel='linear')

    # fit
    svm_linear.fit(x_train, y_train)

    # predict
    l_predictions = svm_linear.predict(n)
    print(l_predictions)
    return l_predictions
