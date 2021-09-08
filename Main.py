# msg = "Hello World"
# print(msg)

import casparser
import io
import pandas as pd



string ='This is string.'
file = io.StringIO(string)
print(file.read())

csv_str  = casparser.read_cas_pdf("C:/Users/rachana.gandhi/Projects/Python/pyTestProject/pdfFile/CAS_test.pdf", 
"CNXPM5699F", output="csv")


# print(csv_str)
csv_data=io.StringIO(csv_str)
# print(csv_data.read())

df = pd.read_csv(csv_data)
df.to_csv('C:/Users/rachana.gandhi/Projects/Python/pyTestProject/CSV_file/fileTest.csv') 
print("Imported to CSV file")





 
