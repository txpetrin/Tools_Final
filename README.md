# ChatGPT Powered Text Summarizer
This application is used to summarize text or ideas using the OpenAI ChatGPT LLM as a back end. 

## Steps to build application:
These instructions are in Powershell for Windows:
Note that the user must have an OpenAI API Key to run this application. 
+ User must set environmnet variable for OPEN_AI_KEY:
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

 ## Implementation details:
 ### Flask
 The majority of the implementation is done on the server port 'home' page with no additional extention on the hyperlink. The home page will be listening to the database for any kind of update to the database. Flask upon the initialization of the application will create the SQLite database with the help of the flask_sqlalchemy package, which will be elaborated upon in the SQL section. 

 One of the main benefits to this approach is the simple python run command that lets the application handle the local database setup while Postgres or another database is not ready yet. 

### HTML
The HTML will render the home page of the application. Within the head of the application is simply the title, with the body containing a text input field, submit button, and table. 

The text input field is intended to accept the question asked by the user for summarization using the ChatGPT API, which is cleared upon hitting the 'submit' buttion, which uses the submitPrompt() function. The function will POST the data to application, which will use the python file to query the OpenAI API. The response is received by the HTML file and then converted into JSON where it is input into the results table. 

There is an additional page, /all_entries, which displays every row in the database. 

### SQL
The SQL table, Response, is implemented as an SQLite database which renders when the application is built. The table carries the primary key, ID, which is assigned in the order which the prompts are submitted followed by a Prompt text field containing the user input, followed by the Response text field containing the ChatGPT response. 

### Python
The main functionality is to piece everything together, allowing the HTML to communicate with the database via Flask and look for their summary using the ChatGPT API. 

The main page has both the GET and POST handlers to be able to query the API as well as receive and display the API's response. 