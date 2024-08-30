# Stackoverflow-scraper
This repository searches for profiles in Stackoverflow and extracts some of their information


## Overview

This repository contains a code that aims to extract profiles along with some of their data with a maximum number of 50 profiles per search. The research is based on a keyword of a specific field.
## Getting Started

### Follow these steps to get started with the project:
To begin, you will need to clone this GitHub repository by running this command in the command prompt :
```bash
$ git clone [https://github.com/06sahar06/Stackoverflow-scraper.git]
```
Navigate to the project directory:
```bash 
$ cd Stackoverflow-Scraper
```

## Usage

### To run the project, use the following command:
```bash
$ python Stackoverflow_scraper.py
```


## Using the code with streamlit
### Follow these steps to create an interface:
First, you will need to install streamlit by running the following command in the command prompt :
```bash
$ pip install streamlit
```
Create a virtual environment:

```bash
$ python -m streamlit_env myenv
$ streamlit_env\Scripts\activate
```

you can then run the streamlit app directly:
```bash
$ streamlit run Stackoverflow_scraper.py
```
Streamlit will then launch a local web server and open your app in the default web browser. You can interact with your app through the browser.
To stop the Streamlit server, go back to the command prompt and press Ctrl + C.
