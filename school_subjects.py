import plotly.graph_objects as go

# Let's learn about graphing, defining variables and other cool things.
# First new thing we will cover are: python lists.
# Let's watch this video and come back when you're done: https://www.youtube.com/watch?v=zEyEC34MY1A

# Okay, on with the show

# Notice the import statement above. It's called Plotly. As in - to plot a graph
# See more about this library here: https://plotly.com/python/plotly-fundamentals/

# Let's create a pie chart, which shows the subjects you're taking in school
# along with your sentiment of each subject.

# These are your subjects
# There are 4 subjects so far. Fill in this list to match the subjects you are taking this semester.
labels = ['Gym','Tech','Math','French']

# You can assign a value to each subject above, according to how much you like the subject.
# For example, each subject is now equally 'good' :). They're all at 25%
# Feel free to change these values, where a higher number shows the subject is more fun and lower number
# means the opposite. You are free to change the list above and the numbers below.
values = [25, 25, 25, 25]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()


# When you're done manipulating this pie chart, please move on to the second program: lunches.py
