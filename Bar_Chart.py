import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie','Richard'],
    'Age': [24, 30, 35,15]
})

print(df)

# Visualization
df.plot(kind='bar', x='Name', y='Age', color='red')
plt.title('Age of People')
plt.xlabel('Name')
plt.ylabel('Age')
plt.show()
