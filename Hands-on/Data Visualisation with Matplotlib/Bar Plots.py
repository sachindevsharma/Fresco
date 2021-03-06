import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

def test_barplot_of_iris_sepal_length():

    # Write your functionality below
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    species= ['setosa', 'versicolor', 'viriginica']
    index=[0.2, 1.2, 2.2]
    sepal_len = [5.01, 5.94, 6.59]
    ax.bar(index,sepal_len,width = 0.5,color='red',edgecolor='black')
    ax.set(title='Mean Sepal Length of Iris Species',
           xlabel='Species',ylabel='Sepal Length (cm)',
           xlim=(0,3),ylim=(0,7),
           xticks=[0.45,1.45,2.45],
           xticklabels = ['setosa', 'versicolor', 'viriginica'])
    fig.savefig('bar_iris_sepal.png')

def test_barplot_of_iris_measurements():

    # Write your functionality below
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    sepal_len = [5.01, 5.94, 6.59]
    sepal_wd = [3.42, 2.77, 2.97]
    petal_len = [1.46, 4.26, 5.55]
    petal_wd = [0.24, 1.33, 2.03]
    species = ['setosa', 'versicolor', 'viriginica']
    species_index1 = [0.7, 1.7, 2.7]
    species_index2 = [0.9, 1.9, 2.9]
    species_index3 = [1.1, 2.1, 3.1]
    species_index4 = [1.3, 2.3, 3.3]
    ax.bar(species_index1,sepal_len,color='c',edgecolor='black',width=0.2,label='Sepal Length')
    ax.bar(species_index2,sepal_wd,color='m',edgecolor='black',width=0.2,label='Sepal Width')
    ax.bar(species_index3,petal_len,color='y',edgecolor='black',width=0.2,label='Petal Length')
    ax.bar(species_index4,petal_wd,color='orange',edgecolor='black',width=0.2,label='Petal Width')
    ax.set( xlabel='Species',ylabel='Iris Measurements (cm)',
            title = 'Mean Measurements of Iris Species',
            xlim=(0.5,3.7),ylim=(0,10),
            xticks= [1.1,2.1,3.1],
            xticklabels = ['setosa','versicolor','viriginica'])
    ax.legend()
    fig.savefig('bar_iris_measure.png')

def test_hbarplot_of_iris_petal_length():

    # Write your functionality below
    fig = plt.figure(figsize=(12,5))
    ax = fig.add_subplot(111)
    species = ['setosa', 'versicolor', 'viriginica']
    index=[0.2, 1.2, 2.2]
    petal_len = [1.46, 4.26, 5.55]
    ax.barh(index,petal_len,height=0.5,color='c',edgecolor='black')
    ax.set( title='Mean Petal Length of Iris Species',
            xlabel='Petal Length (cm)',ylabel='Species',
            yticks=[0.45,1.45,2.45],
            yticklabels=['setosa', 'versicolor', 'viriginica'])
    fig.savefig('bar_iris_petal.png')
    
    
test_barplot_of_iris_sepal_length()
test_barplot_of_iris_measurements()
test_hbarplot_of_iris_petal_length()
