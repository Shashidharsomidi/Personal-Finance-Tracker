
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_expenses(data):
    df = pd.DataFrame(data, columns=['Date', 'Category', 'Description', 'Amount'])
    if df.empty:
        return None
    category_summary = df.groupby(['Category','Description'])['Amount'].sum().unstack().fillna(0)

    labels = category_summary.index.tolist()
    categories = category_summary.columns.tolist()
    x = np.arange(len(labels))
    width = 0.45 if len(categories) == 2 else 0.25

    fig, ax = plt.subplots(figsize=(10,6))

    for i, cat in enumerate(categories):
        ax.bar(x + i * width, category_summary[cat], width, label=cat) 
        
    ax.set_title('Expenses by Category and Description')
    ax.set_ylabel('Amount')
    ax.set_xlabel('Description')
    ax.legend(title='Category')
    ax.set_xticks(x + width * (len(categories)-1) / 2)
    ax.set_xticklabels(labels, rotation=45, ha='right')
    plt.tight_layout()

    return fig
