import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Your Title",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded",

)
# Updated data dictionary with specified order and modified subkey
data = {
    'Purpose': {
        'score': 93,
        'agreement': 62,
        'mixed opinions': 74
    },
    'Performance': {
        'score': 80,
        'agreement': 91,
        'mixed opinions': 73
    },
    'Sustainability': {
        'score': 85,
        'agreement': 71,
        'mixed opinions': 46
    },
    'Conformance': {
        'score': 79,
        'agreement': 75,
        'mixed opinions': 43
    },
    'Board Composition': {
        'score': 89,
        'agreement': 79,
        'mixed opinions': 100
    }
}

# Create a DataFrame from the updated data dictionary
df = pd.DataFrame.from_dict(data)

# Transpose the DataFrame to group by the main keys of the JSON
df = df[['Purpose', 'Performance', 'Sustainability', 'Conformance', 'Board Composition']]
df = df.T.reset_index().rename(columns={'index': 'Categories'})
df = df.melt(id_vars='Categories', var_name='Subcategories', value_name='Values')

# Plot the grouped bar chart based on main keys and subkeys
fig, ax = plt.subplots()
df.pivot(index='Categories', columns='Subcategories', values='Values').plot(kind='bar', ax=ax)

# Customize the plot
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Scores, Agreement, and Mixed Opinions')
ax.legend(title='Subkeys', bbox_to_anchor=(1.05, 1), loc='upper left')

st.header('Scoring and Level of Agreement ')

# Show the plot in Streamlit
st.pyplot(fig)


# Function to determine labels based on conditions
def label_condition(value):
    try:
        value = float(value)
        if value >= 90:
            return 'HIGHEST'
        elif value >= 80:
            return 'MODERATE'
        elif value >= 70:
            return 'LOWEST'
        else:
            return 'LOW'
    except ValueError:
        return value

# Apply conditions to the data
for key, sub_dict in data.items():
    for sub_key, value in sub_dict.items():
        data[key][sub_key] = label_condition(value)

# Create a DataFrame from the data
df = pd.DataFrame(data).T  # Transpose to have main keys as rows

st.header('Graph Summary')

table_style = {
    'selector': 'th, td, table',
    'props': [
        ('color', 'black'),
        ('border-collapse', 'collapse'),
        ('border', '1px solid black'),
    ]
}

# table_style = {
#     'selector': 'table',
#     'props': [
#         ('border-collapse', 'collapse'),
#         ('border', '1px solid black'),
#     ]
# }

# Display the styled table using Streamlit
st.table(df.style.set_table_styles([table_style]))










