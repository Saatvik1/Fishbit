# Fishbit
A project dedicated to finding out more about myself through data from Fitbit, MyFitnessPal, and self-surveyed data

# To-do List:
## Data Gathering
* ~~Configure Fitbit app and authentication process, get keys and tokens~~
* ~~Decide what data would be good to use~~
* ~~Analyze Fitbit JSON structures for each endpoint~~
* ~~Get all historical data required and save for analysis in JSON files~~
* ~~Get myfitnesspal data~~
* ~~Change Google form data collection questions to include stress and specific sleep details~~
* ~~Get google form data~~
* ~~See if raw JSON collection is fixed in terms of not collecting any more duplicates~~
* Create .py scripts based on notebooks, for general use

## Data Wrangling
* ~~Design a plan to transform data into a structure more suitable for analysis.~~
* ~~Convert to tables~~
* ~~Rid tables of redundant data, and create any necessary changes~~
* ~~Combine sleep data from the two different Fitbit formats/sources.~~
* ~~Convert all data to csv~~
* ~~Complete plan outlined in 4.0 notebook.~~
* ~~Create Excel documentation of pre-storage data transformations and the original raw data format...~~
* Make a script to extract the stress_score file from the takeout folder and perform a basic clean, then export it to the interim data folder.

## Data ETL
* ~~Create SQL schemas~~
* ~~Create dump scripts~~

## Data Analysis / EDA
* ~~Write a basic univariate analysis report.~~
* Formulate a plan, and outline North Star metrics (initial ones, to get a sense of my current situation, then perform stat analysis to select important metrics)
* Formulate a plan for SQL and pandas analysis of data, for recreatability...


# Progress
## 8/1/24
* Added basic files
* Analyzed JSON formats from Fitbit API and added all endpoints that will be used in the initial analysis. This is the planning phase for data gathering.

## 8/6/24
* Designed API calls, creating scripts to gather all historical data
* Acquired all data listed out previously, and completed raw data gathering. Moving onto data wrangling.

## 8/7/24
* Created a list of columns wanted and notes on how tables would look from JSON data.
* Created tables from JSON data

## 8/8/24
* Created a few columns from inner JSON data.

## 8/15/24
* Completed wrangling for activity_df, almost done with sleep_df.
 
## 8/22/24
* Completed sleep_df wrangling, and consolidated date formats between the 2 tables. Converted all DFs to csv's.

## 9/9/24
* Edited project structure. Will implement requirements.txt and others once work resumes.
* Created documents for stakeholder requirements and pipeline
* Edited raw_data json, improving code, made it more general, preparing it for script creation later on...
* Created updated plan for data cleaning immmediately after data collection. This is NOT pre EDA cleaning, this is data storage cleaning...

## 9/10/24
* Downloaded MFP data

## 9/11/24
* Created jupyter NB for SQL dump, made a basic outline

## 9/12/24
* Created a detailed doc on pre-dump cleaning and formatting

## 9/13/24
* Worked on wrangling NB

## 9/15/24
* Completed wrangling NB and fixed raw_json data collection, since it collected duplicates.
* Updated table documentation

## 9/16/24
* Fixed some more issues with wrangling NB, that's all done now (should be lol, this is like the 4th time I've committed saying it's done)
* Completed SQL dump, and created docs for SQL schema

## 11/14/24
* After two months... I am back! I updated the data using the notebooks I made (all I had to do was run them! super easy!)
* Started making a plan for EDA and what I want to explore out of this data

## 11/16/24
* Started EDA on activities, and explored basic correlations between features, got basic descriptive statistics for numeric features.

## 11/25/24 
* Continued EDA on activities
* Developed a technical outline plan for the project (sort of, needs to be fleshed out more)

## 12/26/24
* Finished EDA on activities
* Started on Br, HRV, and tempSkin.

## 01/02/25
* Finished eda on BR, HRV, tempSkin
* started sleep analysis

## 01/05/25
* Finished very basic sleep analysis on the first dataframe

## 01/06/25
* Finished basic univariate analysis on everything.
* Wrote report and summarized things to study in future analysis.

