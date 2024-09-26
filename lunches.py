import plotly.graph_objects as go

config = {
  'toImageButtonOptions': {
    'format': 'jpeg',
    'filename': 'lunch_planner',
    'scale': 1
  }
}
# Let's plan our lunches!!
# Before proceeding, run this program to see what it looks like.

# The following variables will provide data for a table planner used to create your lunches.

# Pick a fruit for your lunch. First fruit will be for the Monday lunch, second for Tuesday and so on.
fruits = []

# Pick a veggie for your lunch. First veggie will be for the Monday lunch, second for Tuesday and so on.
veggie = []

# Pick a main for your lunch. First main will be for the Monday lunch, second for Tuesday and so on.
main = []

# Pick an optional snack/drink for your lunch.
option = []

fig = go.Figure(data=[go.Table(
    header=dict(values=['Day', 'Fruit', 'Veggie', 'Main', 'Option'],
                line_color='darkslategray',
                fill_color='lightskyblue',
                align='left'),
    cells=dict(values=[['Monday','Tuesday','Wednesday','Thursday','Friday'], # 1st column
                       fruits, veggie, main, option],
               line_color='darkslategray',
               fill_color='lightcyan',
               align='left'))
])

fig.update_layout(width=900, height=700)
fig.show(config = config)

# When you're done creating your lunch planner, you can click a "Download plot" on top right of the chart
# and save the planner as an image. Share the file with me once you are done. We did this before !
# Grab me when you're ready.
