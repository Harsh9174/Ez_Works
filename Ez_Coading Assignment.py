# importing necessary Library to read and load the TMX file
import xml.etree.ElementTree as ET
import pandas as pd

# Define a function to parse and structure TMX data
def parse_tmx_file(tmx_file):
    # Create an ElementTree object from the TMX file
    tree = ET.parse("C:/Users/Mi/Downloads/ar-en.tmx/ar-en.tmx")
    root = tree.getroot()

    # Initialize lists to store English and Arabic sentences
    english_sentences = []
    arabic_sentences = []

    # Iterate through the TMX file to extract translation pairs
    for tu in root.findall(".//tu"):
        english = None
        arabic = None

        for tuv in tu.findall(".//tuv"):
            lang = tuv.get("{http://www.w3.org/XML/1998/namespace}lang")

            if lang == "en":
                english = tuv.find(".//seg").text
            elif lang == "ar":
                arabic = tuv.find(".//seg").text

        # Add the translation pair to the respective lists
        if english and arabic:
            english_sentences.append(english)
            arabic_sentences.append(arabic)

    return english_sentences, arabic_sentences

# Specify the path to your TMX file
tmx_file_path = "C:/Users/Mi/Downloads/ar-en.tmx/ar-en.tmx"

# Call the function to parse and structure the data
english_sentences, arabic_sentences = parse_tmx_file(tmx_file_path)

# we have now the cleaned and structured data in the two lists
# below are the transformation steps



# Creating a DataFrame
df = pd.DataFrame({'english_sentences':english_sentences,
                   'arabic_sentences':arabic_sentences})



df["english_sentences"] = df["english_sentences"].str.strip()  # Remove leading/trailing whitespace
df["arabic_sentences"] = df["arabic_sentences"].str.strip()    # Remove leading/trailing whitespace




# code to transform the text and to remove unwanted characters from text
def text(text):
    L = []
    for i in text:
        if i.isalpha() or i.isspace():
            L.append(i)
    return "".join(L)
for i in df.columns:
    df[i] = df[i].apply(text)



# Cheching the Duplicates
df.duplicated().sum()



# Droping the Duplicates from the DataFrame
df.drop_duplicates(inplace=True)



# installing the Library to connect Sql 
pip install mysql-connector-python



# Importing SQL library to connect with python
import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(host='localhost', user='root', password='Harsh@9174', database='Language')

if conn.is_connected():
    cursor = conn.cursor()
    cursor.execute(f"create database if not exists {'Language'}")
    cursor.execute('use Language')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Eng_Arab_Lang (
                  english_sentences TEXT,
                  arabic_sentences TEXT
                )''')
    
    
    # Iterate through the DataFrame rows and insert data into the table
    for index, row in df.iterrows():
        english_sentence = row['english_sentences']
        arabic_sentence = row['arabic_sentences']
        
        # Define the SQL INSERT statement
        insert_query = f"INSERT INTO Eng_Arab_Lang (english_sentences, arabic_sentences) VALUES ('{english_sentence}', '{arabic_sentence}')"
        
        # Execute the INSERT statement
        cursor.execute(insert_query)
    
    # Execute the SELECT statement to retrieve data
    cursor.execute('SELECT * FROM Eng_Arab_Lang')
    
    # Fetch all the rows from the result set
    rows = cursor.fetchall()
    
    # Print the retrieved data
    for row in rows:
        english_sentence, arabic_sentence = row
        print(f'English: {english_sentence}, Arabic: {arabic_sentence}')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()





