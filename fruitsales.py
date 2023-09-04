#import os
import pandas as pd
#import pytest

fruit = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])
fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                index=['2017 Sales', '2018 Sales'])
fruit.to_csv("c:/fruit.csv")
