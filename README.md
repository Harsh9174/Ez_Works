# Translation Memory Data Pipeline

### This data pipeline extracts, transforms, and loads data from a Translation Memory eXchange (TMX) file containing parallel translations between English and Arabic. The cleaned and structured data is then loaded into a relational database.

### Table of Contents
- Requirements
- Prerequisites
- Installation
- Usage
- Pipeline Steps
- Database

### Requirements
#### Before running the data pipeline, ensure you have the following:-
- Python 3
- MySQL
- The TMX file to process

### Prerequisites
#### Install Python packages using pip:-
- xml.etree.ElementTree,
- pandas
- mysql.connector
pip install xml.etree.ElementTree pandas mysql-connector-python

### Installation
1. Download this repository to your local machine
2. Navigate to the project directory on your system using "cd"
3. Download the TMX file and save it in the project directory

### Usage
#### To run the data pipeline, follow these steps:-
- Open a terminal and navigate to the project directory
- run the main script "python Ez_Coading Assignment.py"
##### The script will perform the following tasks:
- Parse and structure the TMX data
- Clean the data by removing unwanted characters and whitespace
- Removing Duplicates
- Load the cleaned data into the database usig SQL

### Pipeline Steps

- Parsing and Structuring: The TMX file is parsed using the ElementTree library to extract translation pairs between English and Arabic.

- Data Cleaning: Unwanted characters and leading/trailing whitespace are removed from the English and Arabic sentences.

- Database Loading: The cleaned data is loaded into a MySQL database. You can modify the database connection settings in the code if needed.

### Database
#### The cleaned data is stored in a MySQL database named 'Language'. You can access the data by running SQL queries against this database






