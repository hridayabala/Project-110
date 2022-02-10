import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random
import csv

df = pd.read_csv('data.csv')

data = df['readingtime'].tolist()

print('Population mean is : ', statistics.mean(data))

def randomSetofMean(counter):
    dataSet = []

    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value = data[random_index]

        dataSet.append(value)

    mean = statistics.mean(dataSet)
    return mean

def showGraph(mean_list):
    df = mean_list
    mean = statistics.mean(df)

    graph = ff.create_distplot([data], ['readingtime'], show_hist = False)
    graph.show()

def setup():
    mean_list = []

    for i in range(0, 100):
        setOfMean = randomSetofMean(10)

        mean_list.append(setOfMean)
    
    showGraph(mean_list)

    print('Sampling Mean : ', statistics.mean(mean_list))

setup()