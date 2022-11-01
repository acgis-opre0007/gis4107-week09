#-------------------------------------------------------------------------------
# Name:        world_pop_explorer.py
#
# Purpose:     Provide some functions to analyze the data in
#              world_pop_by_country.py
#
# Author:      David Viljoen
#
# Created:     24/11/2017
# Last update: 31/10/2022
#-------------------------------------------------------------------------------

from world_pop_by_country import data as country_pop

# Key = country name and 
# Value = population as a number (i.e. not text containing commas)
#
country_to_pop = dict()


def get_country_count():
    """Return the number of countries in country_pop.  
    NOTE:  Assume data (country_pop) will always have a header"""
    countries = country_pop.split('\n') #every country on a line
    count = len(countries)
    return count - 1
    

def conv_num_with_commas(number_text):
    """Convert a number with commas (str) to a number.
       e.g. '1,000' would be converted to 1000"""
    number = number_text.replace("," ,'')
    return int(number)

def get_top_five_countries():
    """Return a list of names of the top five countries in terms of population"""
    countries = country_pop.split('\n') 
    top_five = countries[1:6]
    top = []
    for country in top_five:
        country_attributes = country.split('\t')
        name = country_attributes[1]
        top.append(name)
    return top
    # d = dict.fromkeys


def set_country_to_pop():
    """Sets the global country_to_pop dictionary where key is country name
         and value is a tuple containing two elements:
            1. A numeric version of the comma separated number in the
               Pop 01Jul2017 column
            2. The % decrease as a number
    """


def get_population(country_name):
    """Given the name of the country, return the population as of 01Jul2017
       from country_to_pop.  If the country_to_pop is
       empty (i.e. no keys or values), then run set_country_to_pop
       to initialize it."""


def get_continents():
    """Return the list of continents"""


def get_continent_populations():
    """Returns a dict where the key is the name of the continent and
       the value is the total population of all countries on that continent"""

