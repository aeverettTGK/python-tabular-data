#! /usr/bin/env python3

import sys
import pandas as pd
import matplotlib
matplotlib.use('Agg')
from scipy import stats
import matplotlib.pyplot as plt

def collect_species(file):
    species_list = []
    dataframe = pd.read_csv(file)
    species_data = dataframe["species"]
    for species in species_data:
        if species not in species_list:
            species_list.append(species)
    return species_list

def create_dataframe(file, species):
    dataframe = pd.read_csv(file)
    species_data = dataframe[dataframe.species == species]
    return species_data

def filter_x_y(dataframe):
    x = dataframe["petal_length_cm"]
    y = dataframe["sepal_length_cm"]
    return x, y

def plot_regression(x, y):
    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    return slope, intercept

def plot_graph(species, x, y, slope, intercept):
    plt.scatter(x, y, label = species)
    plt.plot(x, slope * x + intercept, color = "red", label = "Regression Line")
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Sepal Length (cm)")
    plt.legend()
    filename = species + ".png"
    plt.savefig(filename)

if __name__=="__main__":
    if len(sys.argv) != 2:
        sys.exit(sys.argv[0] + ": Expecting one command line argument of a csv file")
    iris_file = sys.argv[1]
    species_names = collect_species(iris_file)
    for species in species_names:
        dataframe = create_dataframe(iris_file, species)
        x, y = filter_x_y(dataframe)
        slope, intercept = plot_regression(x, y)
        plot_graph(species, x, y, slope, intercept)
        print("Plot successful.")


