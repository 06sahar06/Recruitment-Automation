# Social Media APIs for Posting, Scheduling, and Analytics

This repository is forked from Ayrshare's official repository for social media posting: https://github.com/ayrshare/social-media-api.git , it's been tested on Linkedin through a new python file: test.py with additional integration of streamlit.
The obtained interface would take as input a text to post alongside with an image if it's desired to be posted.
It then publishes the post on Linkedin (or other social media when needed)

## Getting started
### Follow these steps to get started with the project:
To begin, you will need to clone this GitHub repository by running this command in the command prompt :
```bash
$ git clone [https://github.com/06sahar06/Social-Media-Posting.git]
```
Navigate to the project directory:
```bash 
$ cd Social-Media-Posting
```

## Usage
### Insert your own API Key in the config file: config.js

### To run the project, use the following command:
```bash
$ python test.py
```


## Using the code with streamlit
### Follow these steps to create an interface:
First, you will need to install streamlit by running the following command in the command prompt :
```bash
$ pip install streamlit
```
you can then run the streamlit app directly:
```bash
$ streamlit run app.py
```
Streamlit will then launch a local web server and open your app in the default web browser. You can interact with your app through the browser.
To stop the Streamlit server, go back to the command prompt and press Ctrl + C.
