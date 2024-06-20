from flask import Flask, render_template, redirect
import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.random.rand(100, 1), columns=[i for i in range(1)] )
def highlight_errors(val):
    color = 'red' if val > 0.5 else 'green'
    return f"background-color: {color}"

style = df.style.apply(lambda x: x.map(highlight_errors))
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", table=style.to_html(escape=False))

@app.route("/displaySingle/<col>")
def display(col):
    print("col: ", col, flush=True)
    if col == '\xa0':
        return redirect("/", code=302)

    table = pd.DataFrame(df.T[int(col)]).T
    table_style = table.style.apply(lambda x: x.map(highlight_errors))
    return render_template("single.html", table=table_style.to_html(escape=False), id=col)
