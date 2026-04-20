# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.1",
#     "pandas>=3.0.2",
# ]
# ///

import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exploring
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Imports
    """)
    return


@app.cell
def _():
    import pandas as pd




    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Importing data
    """)
    return


@app.cell
def _(pd):
    df = pd.read_stata("data/HCMST Couples Meet 2017-2022 v2.2.dta", convert_categoricals=True)
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Getting an idea of the data
    """)
    return


@app.cell
def _(df):
    df.info()
    #df.describe()
    df_types = df.dtypes
    df_types.info()
    #df_types.groupby("value")
    df.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Counting things:
    - 3.510 rows
    - 725 columns. wow.
    - data types : category(586), datetime64[s](8), float32(46), float64(81), int16(1), int32(1), int8(2)
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
