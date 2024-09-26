import plotly.graph_objects as go

config = {
  'toImageButtonOptions': {
    'format': 'jpeg',
    'filename': 'birthday_picker',
    'scale': 1
  }
}

# Complete this bar chart program
# For reference, here are bar chart examples at Plotly documentation: https://plotly.com/python/bar-charts/

# Let's create a Bar chart, which will show your favorite choices for a Birthday present!
# You will need to create 2 lists. Remember, we created lists in the previous lunches.py program

# first list will have the name(s) of the item(s) you would like. Use and appropriate type here.
# Remember, you can have strings, booleans, integers and so on.


# second list will have the price of the item. Do not use the dollar $ sign. Same as above, use an appropriate
# datatype suitable for defining money


# Line below is incomplete.
# Below, the X axis will show your prsent items and the Y axis will show your prices
# Please define your lists above and then assign them to the X and Y axis below
# Remember, to assign something to a variable, we use an equals sign. Fill out the missing parts below
fig = go.Figure([go.Bar(x = , y = )])


fig.show(config = config)

# When you're done creating your birthday present list, you can click a "Generate as PNG button"
# and save the image. Share the file with me once you are done. We did this before !
# Grab me when you're ready.
