# stalker

## overview  
a streamlit app that allows you to upload portfolio return data and analyze performance metrics including sharpe ratio, total return, and win rate.

## dependencies  
- python  
- streamlit  
- pandas  
- matplotlib  

## pre-requisites  

### 1. setup python environment  
```bash
pip install streamlit pandas matplotlib
```
### 2. prepare your data  
- import a csv file with a date column and a daily returns column  
- ensure the date format matches `YYYY-MM-DD`

## installation
clone this repo and navigate to the folder

```bash
git clone https://github.com/yourusername/stalker.git
cd stalker
```

## usage
run the app
  1. ```bash
    streamlit run main.py
    ```
  2. upload your csv file
  3. select date and return columns
  4. choose a time period to analyze
  5. view calculated metrics and win/loss pie chart

## example
```csv
Date,Returns
2024-01-01,0.002
2024-01-02,-0.001
```
## outputs include
  - total return
  - annualized return
  - sharpe ratio
  - win rate
  - pie chart of win/loss frequency

## contributing
pull requests are welcome. for major changes, please open an issue first
to discuss what you would like to change.

please make sure to update tests as appropriate.

## license
[MIT](https://mit-license.org/)
