import pandas as pd
import numpy as np


values= [['Rohan',455],['Elvish',250],['Deepak',495],
         ['Soni',400],['Radhika',350],['Vansh',450]]

df = pd.DataFrame(values,columns=['Name','Total_Marks'])

df = df.assign(Percentage = lambda x: (x['Total_Marks'] /500*100))

print(df)

values_list = [[15, 2.5, 100], [20, 4.5, 50], [25, 5.2, 80],
               [45, 5.8, 48], [40, 6.3, 70], [41, 6.4, 90],
               [51, 2.3, 111]]
df2 = pd.DataFrame(values_list, columns=['Field1', 'Field2', 'Field3'])

df2 = df2.assign(productOfNumbers = lambda x: (x['Field1']+x['Field1']))

print(df2)

df3 = df2.assign(pro = lambda x: (x['Field1']*x['Field2']*x['Field3']))

print(df3)

values_listed = [[15, 2.5, 100], [20, 4.5, 50], [25, 5.2, 80],
               [45, 5.8, 48], [40, 6.3, 70], [41, 6.4, 90],
               [51, 2.3, 111]]
df4 = pd.DataFrame(values_listed, columns=['Field_x', 'Field_y', 'Field_z'],
                  index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(df4)
df5 = df4.apply(lambda x: np.square(x) if x.name == 'd' else x, axis=1)

print(df5)