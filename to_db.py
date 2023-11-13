import sqlite3
import time


def to_db(df):
    con = sqlite3.connect("MNIST_Handwritten_Digit_Recognition-SVM.db")
    cur = con.cursor()

    try:
        cur.execute(
            "CREATE TABLE MNIST_Handwritten_Digit_Recognition(Fname,Predicted)")

    except sqlite3.OperationalError:
        pass

    con.executemany(
        "INSERT INTO MNIST_Handwritten_Digit_Recognition VALUES(?,?)", [df])
    con.commit()

    log_time = '{}, '.format(time.ctime())
    filename = '{}, '.format(df[0])
    predicted = '{}\n'.format(df[1])
    labels = 'time, filename ,predicted\n'

    with open('logs.txt', 'a') as f:
        f.write(labels)
        f.write(log_time)
        f.write(filename)
        f.write(predicted)
