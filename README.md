
# Stock Sentiment Analysis and Correlation with Stock Returns

## Project Overview
This project aims to analyze the correlation between daily news sentiment scores and stock daily returns. The analysis includes sentiment analysis on news headlines, calculation of daily stock returns, and correlation analysis.

## Data Sources
- **Stock Data**: Historical stock prices.
- **News Data**: Daily news articles and headlines.

## Steps Involved
1. **Data Collection and Preparation**:
    - Load and merge stock and news data.
    - Clean and normalize data for analysis.
    
2. **Sentiment Analysis**:
    - Perform sentiment analysis on news headlines using TextBlob.
    - Aggregate daily sentiment scores for days with multiple articles.
    
3. **Daily Stock Returns Calculation**:
    - Calculate daily stock returns based on closing prices.
    - Visualize the stock returns.

4. **Correlation Analysis**:
    - Determine the Pearson correlation coefficient between average daily sentiment scores and stock daily returns.
    - Visualize the correlation.

## How to Run the Analysis
1. **Requirements**:
    - Python 3.x
    - Jupyter Notebook
    - pandas
    - numpy
    - nltk
    - textblob
    - matplotlib
    - seaborn

2. **Setup**:
    - Install necessary libraries using `pip install pandas numpy nltk textblob matplotlib seaborn`.
    - Download necessary NLTK data using `nltk.download('punkt')`.

3. **Run the Analysis**:
    - Open the provided Jupyter Notebook file.
    - Follow the cells sequentially to load data, perform analysis, and visualize results.

## Results
- The correlation analysis provides insights into how daily news sentiment scores relate to stock daily returns for Amazon.
- The visualizations help understand the data trends and correlations effectively.

## Conclusion
This project demonstrates the potential impact of news sentiment on stock market performance. The findings can be used for further financial analysis and decision-making.


# News Analysis Project

This project provides comprehensive data analysis on a dataset containing news headlines and related information. The analysis is divided into four parts: Descriptive Statistics, Text Analysis, Time Series Analysis, and Publisher Analysis.

## Packages and Libraries Used

The analysis is built using the following packages and libraries:

- Python 3.10.12
- numpy 1.23.5
- matplotlib 3.9.4
- pandas 1.3.5
- plotly 5.24.1
- ta-lib 0.5.1

## Installing TA-Lib

To install the TA-Lib C library, follow these steps:

1. Download the source code:
   ```bash
   wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz

tar -xvf ta-lib-0.4.0-src.tar.gz
cd ta-lib

./configure --prefix=/usr
make
sudo make install
sudo apt upgrade

pip install ta-lib


Analyses Performed
1. Descriptive Statistics
This analysis includes obtaining basic statistics for textual lengths (like headline length), counting the number of articles per publisher, and analyzing publication dates to identify trends over time.

How to Run:
Load the dataset and convert the date column to datetime format.

Calculate the length of each headline.

Count the number of articles per publisher.

Analyze and plot the publication dates to identify trends.

2. Text Analysis
This analysis performs sentiment analysis on headlines to gauge the sentiment (positive, negative, neutral) associated with the news. It also identifies common keywords or phrases.

How to Run:
Use TextBlob for sentiment analysis on headlines.

Categorize headlines based on keywords using CountVectorizer.

Plot the sentiment distribution and top keywords.

3. Time Series Analysis
This analysis explores how publication frequency varies over time and identifies any specific time-related patterns or spikes related to market events.

How to Run:
Convert the date column to datetime format and set it as the index.

Resample the data by day to get the count of articles per day and plot the frequency.

Identify dates with spikes in publication frequency.

Analyze publication times and plot the distribution of articles by hour.

4. Publisher Analysis
This analysis identifies which publishers contribute most to the news feed, examines the type of news they report, and identifies unique domains if email addresses are used as publisher names.

How to Run:
Count the number of articles per publisher and plot the top publishers.

Categorize headlines into different types based on keywords and analyze the type of news reported by top publishers.

Identify unique domains from email addresses and plot the top domains.

Usage
To run the analyses, load the dataset into your Jupyter Notebook or Python environment and follow the code cells provided for each analysis. Ensure you have installed the required packages and libraries before running the code.