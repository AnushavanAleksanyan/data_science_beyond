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
print(df)

df["number"] = df["number"].apply(mod_data)  # correcting data
print(df[198:210])


## Հեռացրեք այն տողերը, որտեղ հրդեհների քանակը 0 է։ Նախ 0 ները սարքեք Nan, հետո հեռացրեք
df["number"].replace(0, np.nan, inplace=True)  # raplace 0 with NaN
df.dropna(inplace=True) #remove NaN

print(df[198:210])


# 3. Խմբավորեք տվյալները ըստ ամիսների։ Արդյունքը լինելու է Series , ընդ որում ամիսները
# այբբենական կարգով։ Փոխեք, ամիսները ըստ ճիշտ հերթականության reindex֊ի միջոցով։
by_months = df.groupby(['month'])['number'].mean()
new_index = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
by_months = by_months.reindex(new_index)
print(by_months)


# 4. Googletrans գրադարանի միջոցով թարգմանել ամիսները
def translate_text(txt):
    translator = googletrans.Translator()
    translated = translator.translate(txt, src='pt', dest="ru")
    return translated.text

print("task 4")
df["month"] = df["month"].apply(translate_text_alt)  # translates month names
print(df[198:510])


# 5. Վիզուալիզացրեք ստացված տվյալները՝
# ներկայացնելով կապը ամիսների և այդ ամիսների ընթացքում եղած հրդեհների քանակի հետ
print(by_months)
by_months.plot(kind="bar", x="month", y="number")
plt.show()