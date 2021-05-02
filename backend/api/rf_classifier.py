"""Importing libraries"""
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

import csv  


def save_json_to_csv(json_payload):     
    
    """This function gets a values from json and saves them into cvs file"""

    first_title = json_payload['FIRST_TITLE']
    second_title = json_payload['SECOND_TITLE']
    third_title = json_payload['THIRD_TITLE']

    fields=['08/03/2021','0',first_title, second_title, third_title]
    with open(r'C:\Users\atuta\Documents\Stock Price Predictions using Machine Learning\backend\api\new_titles.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

def delete_last_row():
    """This function deletes last row from the cvs file."""
    f = open(r'C:\Users\atuta\Documents\Stock Price Predictions using Machine Learning\backend\api\new_titles.csv', "r+", encoding='utf-8')
    lines = f.readlines()
    lines.pop()
    f = open(r'C:\Users\atuta\Documents\Stock Price Predictions using Machine Learning\backend\api\new_titles.csv', "w+")
    f.writelines(lines)



def get_prediction():
    """Read the data"""
    df = pd.read_csv(r'C:\Users\atuta\Documents\Stock Price Predictions using Machine Learning\backend\api\Combined_News_DJIA.csv', encoding = 'ISO-8859-1')
    df_test = pd.read_csv(r'C:\Users\atuta\Documents\Stock Price Predictions using Machine Learning\backend\api\new_titles.csv', encoding = 'utf-8')

    """Divide the data into sets"""

    #divide in training_dataset and test
    # Prepare the groups for tests. 
    training_dataset = df 
    test = df_test 

    """Prepering data"""

    # remove punctuation
    # apart from alphabets we will replace every character with blank
    data = training_dataset.iloc[:, 2:27]
    data.replace("[^a-zA-Z]", " ", regex=True, inplace=True)

    # Renaming the columns
    list1 = [i for i in range(3)]
    new_Index = [str(i) for i in list1]
    data.columns = new_Index


    # converting hadlines to lower case
    for index in new_Index:
        data[index] = data[index].str.lower()


    ' '.join(str(x) for x in data.iloc[1, 0:3])  #Combine all the 3 headlines to a single sentence

    #all the sentences in the form of list

    headlines = []
    for row in range(0, len(data.index)):
        headlines.append(' '.join(str(x) for x in data.iloc[row, 0:3]))

    """ Countvectorizer is used to convert all the sentences into vectors """

    # implememt BAG OF WORDS
    countVector = CountVectorizer(ngram_range=(2,2))
    #ngram(2,2) means it will combine the 2 words together and assign the value

    training_dataset = countVector.fit_transform(headlines)

    """Preparing testing and training_dataset"""

    testTransform =[]
    for row in range(0, len(test.index)):
        testTransform.append(' '.join(str(x) for x in test.iloc[row, 0:3]))
        
    test_dataset = countVector.transform(testTransform)

    """Open pickle"""
    pickle_open = open(r"C:\Users\atuta\Documents\Stock Price Predictions using Machine Learning\backend\api\stocks_news_model.pickle", "rb")

    """Load pickle"""
    randomForestClassifier = pickle.load(pickle_open)

    """Predict"""
    prediction = randomForestClassifier.predict(test_dataset)

    print(prediction)

    return prediction

