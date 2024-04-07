# Google Maps Scraper

This project is a web scraping tool developed with Selenium to extract data from Google Maps. It was created as part of my undergraduate studies for my final year project.

## Overview

The scraper enables you to gather information such as business names, addresses, ratings, reviews, and more from Google Maps based on specified search queries.

## Prerequisites

- **Chrome Driver**: Install the latest Chromium driver compatible with your Chrome browser version. Place the driver executable in the `build` directory of this project.
  
- **Python Environment**: Set up a virtual environment (venv) for managing dependencies.

## Installation

1. Clone the repository:

 
   git clone https://github.com/omkarcloud/google-maps-scraper.git
   cd google-maps-scraper
2. Set up the Python environment:    
    python -m venv venv
source venv/bin/activate  # Activate virtual environment
3.Install required Python libraries:
  pip install -r requirements.txt
   FOR-
Generate Queries
Prepare a list of search queries and add them to the config.py file under the keywords field. Each query will be used to search for relevant results on Google Maps.
4.Run the Scraper
Execute the scraper script:
python main.py
Avoid running more than 5 scrapers simultaneously if your system has limited resources (RAM < 8GB, i5 processor).

Data Extraction and Filtering
Allow the scraper to complete its task. The extracted data will be saved to seprated csv and json all in one name with all.csv/json.

Use the provided filter script (data_filteration) to process the raw output into a formatted CSV file suitable for data analysis.

   
