import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import googletrans


def mod_data(data)->int:
    if data - int(data) != 0:
        data = str(data).replace(".", "")
        return int(data)
    else:
        return int(data)

def translate_text_alt(txt):
	m = {"Janeiro": "Январь",
	"Fevereiro": "Февраль",
	"Março": "Март",
	"Abril": "Апрель",
	"Maio": "Май",
	"Junho": "Июнь",
	"Julho": "Июль",
	"Agosto":  "Август",
	"Setembro": "Сентябрь",
	"Outubro": "Октябрь",
	"Novembro": "Ноябрь",
	"Dezembro": "Декабрь"}
	return m[txt]


# 1. Կարդալ ֆայլը և վերածել դատաֆրեյմի
file_path = "./other/project-2/Data_Project_2.csv"
df = pd.read_csv(file_path)

df["number"] = df["number"].apply(mod_data)  # correcting data

## Հեռացրեք այն տողերը, որտեղ հրդեհների քանակը 0 է։ Նախ 0 ները սարքեք Nan, հետո հեռացրեք
df["number"].replace(0, np.nan, inplace=True)  # raplace 0 with NaN
df.dropna(inplace=True) #remove NaN
df["month"] = df["month"].apply(translate_text_alt)  # 4. translates month names


# 2. Բաժանեք դատան փոքր մասերի՝
#   * Առաջին բանը, որ կարելի է անել, վիզուալիզացնել հրդեհների քանակը ըստ տարիների, ամիսների
new_index = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
df1 = df.groupby(['year'])['number'].sum()
df2 = df.groupby(['month'])['number'].sum()  # 5. ներկայացնել կապը ամիսների և այդ ամիսների ընթացքում եղած հրդեհների քանակի հետ
df2 = df2.reindex(new_index)  # 3. Փոխեք, ամիսները ըստ ճիշտ հերթականության reindex֊ի միջոցով։
fig = plt.figure(figsize=(15,4))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.plot(df1)
ax2.plot(df2)
ax1.tick_params(axis = "x", labelrotation=45)
ax2.tick_params(axis = "x", labelrotation=45)
plt.show()
