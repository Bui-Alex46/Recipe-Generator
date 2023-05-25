from flask import Flask, render_template, request
import pandas as pd
import random

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

print('python file working')
data = pd.read_csv('/Users/harshuljain/Desktop/dataset')
headers = list(data.columns.values)
print(headers)