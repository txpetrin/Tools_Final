# ChatGPT Powered Text Summarizer
This application is used to summarize text or ideas using the OpenAI ChatGPT LLM as a back end. 

## Steps to build application:
These instructions are in Powershell for Windows:
Note that the user must have an OpenAI API Key to run this application. 
+ User must set environnmet variable for OPEN_AI_KEY:
```bash
$env:OPENAI_API_KEY = "UNIQUE_OPENAI_API_KEY" 
```
+ Change directory to summarizer:
```bash
cd summarizer
```
 + Run the application using python:
 ```bash
 python app.py
 ```
 + Open the application in web interface:
 Navigate to link: 
 [localhost](http://127.0.0.1:5000/) 

## Solution Approach:
### Merit of Use Case:
To increase workers' productivity, this document summarization tool will save time when they are asked to distill information, and time for executives such that they do not need to read a bloated document. This tool is designed to instantaneously distill a document or public domain concept and distill it into 6-8 bullet points. 

### Why AI is the best case to solve the problem: 
ChatGPT will summarize a document or concept virtually instantaneously, eliminating the need for an individual to take the time to pull out the most important parts of a document. If there was a portion that ChatGPT missed, as it tends to miss statistics, the rules it uses can be altered or a human can manually re-add the missed information. 

 ## Implementation details:
 ### Flask
Most of the implementation is done on the server port 'home' page with no additional extension on the hyperlink. The home page will be listening to the database for any kind of update to the database. Flask upon the initialization of the application will create the SQLite database with the help of the flask_sqlalchemy package, which will be elaborated upon in the SQL section. 

 One of the main benefits to this approach is the simple python run command that lets the application handle the local database setup while Postgres or another database is not ready yet. 

### HTML
HTML will render the home page of the application. Within the head of the application is simply the title, with the body containing a text input field, submit button, and table. 

The text input field is intended to accept the question asked by the user for summarization using the ChatGPT API, which is cleared upon hitting the 'submit' button, which uses the submitPrompt() function. The function will POST the data to the application, which will use the python file to query the OpenAI API. The response is received by the HTML file and then converted into JSON where it is input into the results table. 

There is an additional page, /all_entries, which displays every row in the database. 

### SQL
The SQL table, Response, is implemented as an SQLite database which renders when the application is built. The table carries the primary key, ID, which is assigned in the order which the prompts are submitted followed by a Prompt text field containing the user input, followed by the Response text field containing the ChatGPT response. 

### Python
The main functionality is to piece everything together, allowing the HTML to communicate with the database via Flask and look for their summary using the ChatGPT API. 

The main page has both the GET and POST handlers to be able to query the API as well as receive and display the API's response. It takes in the user input from the HTML document, formats the response, then pushes it to the API where it then receives a response and updates the Response DB table. 

The python file is also responsible for creating the instance of the GPT API where the rule set for the bot was changed to inherently give an executive summary as opposed to the typical 'systematic helper' default behavior. 