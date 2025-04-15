# MattBot-3 Server
A data extraction based integratable chatbot using FastAPI
## Installation
* Create a virtual environment
* Install dependencies from requirements.txt

## Installing NLTK
Natural Language Tool Kit installation, run the following commands in the python terminal.

<code>
import nltk
<br>
nltk.download()
</code>

## Corpora
You can add the custom corpora or the data for the chatbot to refer to as a text content in the filepath <b><i>resources/source.txt</i></b>.
It is advisable to keep the contents in the corpora to be robust enough so that it could answer based on the appropriate commonly used key words.

## Running the Chatbot Server
Run the <i>main.py</i> in the terminal.
The server will be deployed in 127.0.0.1:8000.