#! /usr/bin/env python3

"A module for plotting a regression line for petal length vs sepal length of flower species"


import sys
import pandas as pd
import matplotlib
matplotlib.use('Agg')
from scipy import stats
import matplotlib.pyplot as plt

def collect_species(file):
    """
    Reads csv file and returns species represented in file

    Parameters
    ----------
    file: str
        csv file to be read

    Returns
    -------
    species_list: list
        List of species represented in the input csv file
    """

    species_list = []
    dataframe = pd.read_csv(file)
    species_data = dataframe["species"]
    for species in species_data:
        if species not in species_list:
            species_list.append(species)
    return species_list

def create_dataframe(file, species):

    """
    Creates datafram for given species from csv file

    Parameters
    ----------
    file: str
        csv file to be read

    species: str
        Species of flower dataframe is focuesed on

    Returns
    -------
    species_data: dataframe object
        Dataframe of data based on input species (closely related to
        dictionary)
    """

    dataframe = pd.read_csv(file)
    species_data = dataframe[dataframe.species == species]
    return species_data

def filter_x_y(dataframe):

    """
    Filters petal length and sepal length into x and y coordinates for future
    plotting

    Parameters
    ----------
    dataframe: dataframe object
        Dataframe of species' data

    Returns
    -------
    x: Series object
        X coordinates representing petal length of species
    y: Series object
        Y coordinates representing sepal length of species
    """

    x = dataframe["petal_length_cm"]
    y = dataframe["sepal_length_cm"]
    return x, y

def plot_regression(x, y):

    """
    Calculates linear regression line based off X and Y coordinates of data

    Parameters
    ----------
    x: Series object
        X coordinates of data points
    y: Series object
        Y coordinates of data points

    Returns
    -------
    slope: object
        Calculated slope of regression line
    intercept: object
        Caluclated Y-intercept of regression line
    """

    regression = stats.linregress(x, y)
    slope = regression.slope
    intercept = regression.intercept
    return slope, intercept

def plot_graph(species, x, y, slope, intercept):

    """
    Plots scatter plot and linear regression line of flower data

    Parameters
    ----------
    species: str
        Name of species plot is focusing on
    x: object
        X coordinates of data representing petal length of species
    y: object
        Y coordinates of data representing sepal length of species
    slope: object
        Calculated slope of regression line
    intercept: object
        Calculated Y-intercept of regression line

    Returns
    -------
    None
    """

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
        plt.figure()
        dataframe = create_dataframe(iris_file, species)
        x, y = filter_x_y(dataframe)
        slope, intercept = plot_regression(x, y)
        plot_graph(species, x, y, slope, intercept)
        print("Plot successful.")


