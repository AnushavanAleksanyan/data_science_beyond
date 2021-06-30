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


# 1. Կարդալ ֆայլը և վերածել դատաֆրեյմի
file_path = "./other/project-2/Data_Project_2.csv"
df = pd.read_csv(file_path)
print(df)

df["number"] = df["number"].apply(mod_data)  # correcting data
print(df[198:210])


## Հեռացրեք այն տողերը, որտեղ հրդեհների քանակը 0 է։ Նախ 0֊ները սարքեք Nan, հետո հեռացրեք
df["number"].replace(0, np.nan, inplace=True)  # raplace 0 with NaN
df.dropna(inplace=True) #remove NaN

print(df[198:210])


# Խմբավորեք տվյալները ըստ ամիսների։ Արդյունքը լինելու է Series , ընդ որում ամիսները այբբենական կարգով։
by_months = df.groupby(['month'])['number'].mean()
print(by_months)
new_index = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
by_months = by_months.reindex(new_index)
print(by_months)


# 4. Googletrans գրադարանի միջոցով թարգմանել ամիսները
def translate_text(txt):
    translator = googletrans.Translator()
    translated = translator.translate(txt, src='pt', dest="ru")
    return translated.text

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

new_index2 = []
for elem in new_index:
	new_index2.append(translate_text_alt(elem))
	#for sub_str in ["месяц", "Месяц", " "]:
	# print(arm.replace("месяц", "").replace("Месяц", ""))
	# arm1 = arm.replace(" ", "")
	#print(arm)
print(new_index2)

# 5. Վիզուալիզացրեք ստացված տվյալները՝
# ներկայացնելով կապը ամիսների և այդ ամիսների ընթացքում եղած հրդեհների քանակի հետ
by_months = by_months.reindex(new_index2)
by_months.plot(kind="bar", x="month", y="number")
plt.show()