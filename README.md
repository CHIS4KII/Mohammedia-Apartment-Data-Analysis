# Mohammedia Apartment Rental Prices Scraper and Analysis
This repository contains a Python script and a Jupyter Notebook for scraping, cleaning, analyzing, and visualizing apartment rental data from a real estate website for the city of Mohammedia, Morocco. The project leverages the BeautifulSoup library for data extraction and Pandas for data manipulation, with Matplotlib and Seaborn used for data visualization.
## Features :
- **Web Scraping:** The script collects data from the first six pages of the targeted real estate listing site.
- **Data Cleaning:** The Jupyter Notebook includes steps to clean the data, such as standardizing price formats and removing redundant information from location names.
- **Data Analysis:** The Notebook provides insights into the rental market in Mohammedia, including average rental prices, price distribution, and correlations between location and price.
- **Data Visualization:** Various plots and charts are generated to visualize the rental prices, the number of bedrooms, and the distribution of listings across different locations within Mohammedia.
- **CSV Export:** The cleaned and processed dataset is exported to rent_price_Mohammedia.csv, ready for further analysis or use in other projects.

## DataSet :
The resulting CSV file, `rent_price_Mohammedia.csv`, contains the following columns:

- **cost:** The rental price of the apartment.
- **location:** The location of the apartment within Mohammedia.
- **bedrooms:** The number of bedrooms in the apartment.

## Requirements :
- Python 3.x
- BeautifulSoup4
- Requests
- Pandas
- Matplotlib
- Seaborn
