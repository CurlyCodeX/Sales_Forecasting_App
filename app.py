import pandas as pd
import random
months=['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
units_sold=[random.randint(100,500)for _ in months]
df=pd.DataFrame({
    'months':months,
    'units_sold':units_sold
    })
print(df)
