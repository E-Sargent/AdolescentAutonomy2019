# Adolescent Autonomy and Ability Development README
What should be in this folder:
1. HelperFunctions.py 
-A module containing a few helpful functions used at various different stages in the estimation
2. HelperFrames.py 
-A module containing: 
  a. A variable dataframe with information on all imported variables
  b. A dataframe with information on all imported files
  c. Data mappings for all non-numeric data
 3. Data.py
 -The primary data cleaning module, only needs to be run once after which it stores the cleaned data as mcs.pkl in the local directory
 4. TimeUseDiaries.py
 -Because the time use diaries are painfully large and need to be handled differently from other data they get their own data cleaning module. Only needs to be run once at which point the results will be stored as a tud_weekday.pkl 
 5. Analysis.py 
 -Module containing bulk of statistical analysis, will automatically run Data.py and TimeUseDiaries.py to clean the data if it hasn't already been cleaned. 
6. Graphs.py
 -Module for making graphs, note that the graphs folder will be empty until this is run. 
7. software.pdf 
 -Citations and version informations for all software used in the estimation 
8.README.md
 -This thing
 

Steps for replication:
1. Acquire the MCS data
  -Send me an email at eric.s.sargent@protonmail.ch and I'll send you the .zip file
  -Pick up the files from the UK Data Service https://ukdataservice.ac.uk/
2. Open Analysis.py 
3. Uncomment the print(model_fit.summary()) statements for any regressions you'd like to see the results of
4. Run Analysis.py 
  -This will automatically call Data.py and TimeUseDiaries.py if the data has not already been cleaned. 
  -Requires the following python packages: pandas, numpy, os, and statsmodels. All should be included in any standard python distribution.

NOTE: The first run will take some time as the operations on time use diaries are unweildy due to the dimensions of the data, future runs should be much quicker as the results will be stored locally as a .pkl file. 
I do not include the .pkl files by default as they are potentially insecure. 
