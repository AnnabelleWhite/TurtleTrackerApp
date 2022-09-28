# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 13:44:05 2022

@author: arw87
"""
# OBJECTIVE
# Read and parse each line
# a. Skip comment lines
# b. Skip records below a quality threshold (qc <> 1, 2, or 3)
# c. Add observation date to a date dictionary, keyed by the observation UID
# d. Add observation lat./long. to a location dictionary, keyed by the observation UID
# Allow user to specify date
# a. Inform if date is invalid
# Identify keys in date dictionary matching user supplied date
# Identify values in location dictionary with keys found above
# Print information to screen

# OUTLINE
#1. Parse a single line of tracking data into variables
#2. Read a single line of tracking data from file into Python, parse into variables
#3. Read in all lines of tracking data from file into Python, parse into variables
#4, While reading in all lines, add variables into dictionaries of values
#5. Add conditional statements so only valid values added to dictionaries
#6. From dictionaries, extract data for a selected date
#7. Allow user to specify date used to select data from dictionary
#8. Add code to handle if user enters improper date