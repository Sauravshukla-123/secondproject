import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt

data={
    'Hours': [1,2,3,4,5,6,7,8],
    'Marks':[100,200,300,400,500,600,700,800]


}
Rd=pd.DataFrame(data)

colors=['red', 'orange', 'yellow', 'brown', 'purple', 'pink', 'black', 'green']


plt.figure(figsize=(6,5))

sns.barplot(x='Hours',y='Marks', data=Rd, palette=colors)

plt.title('Marks Prediction Graph')


plt.show()