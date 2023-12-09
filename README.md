# housewebsite
# Project Description:
Web APP to get medical information in a sarcastic way like Dr. House would given.
The users will be able to ask questions about health symtomps and diseases to a an AI provided by OPENAI, which will simulate to be Dr. Gregory House a fictional protagonist of the american serie HOUSE and this ones will respond as he usually does in a sarcastic manner.

# Purpose:
The purpose of this application is for entertaniment but include a link where the users can find real medical information.

# Aknowledgements:
1.-You are interacting with an AI system no real person is behind the recommendations deployed, thus this information does not pretend to be a medical advice or any medical suggestions.
2.-For real information related to health symptoms, medical treatments and all related we encourage you to visit a Doctor and this website which may contain relevant information about it: MedlinePlus.gov
3.-Several question options included in the list deployed in a drop down tag were gathered from EverybodyWiki Visit https://en.everybodywiki.com/List_of_diagnoses_from_House_%28TV_series%29.

# Components:
The application consists in:
-Front-end interface builded with traditional HTML,CSS,JAVASCRIPT and Flask Framework
-Back-end interface builded with Python and Flask Framework
-OPENAI API endpoints to interact with GPT 3.5 Turbo
-CSV file that contains a list of prompts to be loaded in the application

# Requirements to install and run the application
## CREATE A PYTHON VIRTUAL ENVIRONMENT AND INSTALL OPENAI PYTHON LIBRARIES
Install Python.
Setup a python virtual environment in your folder project with. 
```bash pip python -m venv "housewebsite" ```
this will create a directory name "housewebsite" inside your project directory.
it is a good practice to create a virtual python environment to install the OpenAI Python library. Virtual environments provide a clean working space for your Python packages to be installed so that you do not have conflicts with other libraries you install for other projects.
3.-Inside you project directory activate the virtual environment with: housewebsite\Scripts\activate
4.-Navigate to housewebsite and install OPENAI Python Library with: pip install --upgrade openai
5.-Setup your API Key with: setx OPENAI_API_KEY "your-api-key-here"





