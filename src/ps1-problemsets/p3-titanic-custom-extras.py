# -*- coding: utf-8 -*-
import numpy
import pandas
import statsmodels.api as sm

def custom_heuristic(file_path):
    '''
    You are given a list of Titantic passengers and their associated
    information. More information about the data can be seen at the link below:
    http://www.kaggle.com/c/titanic-gettingStarted/data

    For this exercise, you need to write a custom heuristic that will take
    in some combination of the passenger's attributes and predict if the passenger
    survived the Titanic diaster.

    Can your custom heuristic beat 80% accuracy?
    
    The available attributes are:
    Pclass          Passenger Class
                    (1 = 1st; 2 = 2nd; 3 = 3rd)
    Name            Name
    Sex             Sex
    Age             Age
    SibSp           Number of Siblings/Spouses Aboard
    Parch           Number of Parents/Children Aboard
    Ticket          Ticket Number
    Fare            Passenger Fare
    Cabin           Cabin
    Embarked        Port of Embarkation
                    (C = Cherbourg; Q = Queenstown; S = Southampton)
                    
    SPECIAL NOTES:
    Pclass is a proxy for socioeconomic status (SES)
    1st ~ Upper; 2nd ~ Middle; 3rd ~ Lower

    Age is in years; fractional if age less than one
    If the age is estimated, it is in the form xx.5

    With respect to the family relation variables (i.e. SibSp and Parch)
    some relations were ignored. The following are the definitions used
    for SibSp and Parch.

    Sibling:  brother, sister, stepbrother, or stepsister of passenger aboard Titanic
    Spouse:   husband or wife of passenger aboard Titanic (mistresses and fiancees ignored)
    Parent:   mother or father of passenger aboard Titanic
    Child:    son, daughter, stepson, or stepdaughter of passenger aboard Titanic
    
    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associating value should be 1 if the
    passenger survvied or 0 otherwise. 

    For example, if a passenger is predicted to have survived:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 1

    And if a passenger is predicted to have perished in the disaster:
    passenger_id = passenger['PassengerId']
    predictions[passenger_id] = 0
    
    You can also look at the Titantic data that you will be working with
    at the link below:
    https://www.dropbox.com/s/r5f9aos8p9ri9sa/titanic_data.csv
    '''

    predictions = {}
    df = pandas.read_csv(file_path)
    
    
    i = 0
    counter = 0
    correct = 0
    
    for passenger_index, passenger in df.iterrows():
        # 
        # your code here
        #
    
        # to save typing assume dies unless meets lives criteria
        predictions[passenger['PassengerId']] = 0
        
        if passenger['Sex'] == 'female':

            if passenger['Pclass'] < 3:

                predictions[passenger['PassengerId']] = 1

            # hypothesis - lower class females less likely to be saved
            # basic filtering and stats suggests it was ~ 50 - 50
            #
            # so I need to identify another attribute with some kind
            # of bias to decide whether to go 0 or 1
            #
            # my expectation was that those with parents or children or
            # with siblings would be more likely to survive. simple
            # analysis shows the opposite so choose live if travelling
            # alone          
            elif passenger['SibSp'] + passenger['Parch'] == 0:
                            
                predictions[passenger['PassengerId']] = 1
                
        # hypothesis - children in lower classes still more likely than not
        # to survive.  Appears true for 1st and 2nd class                
        elif passenger['Pclass'] < 3 and passenger['Age'] < 18:                
            predictions[passenger['PassengerId']] = 1

        counter = counter + 1
        if passenger['Survived'] == predictions[passenger['PassengerId']]:
            correct = correct + 1
            
    
    
    proportion = float(correct) / float(counter)
    print counter
    print correct    
    print proportion    
    
    
    return predictions

custom_heuristic("./titanic_data.csv")


