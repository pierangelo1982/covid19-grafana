import csv
import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="0.0.0.0",
  port=3306,
  user="root",
  passwd="password",
  database="covid19"
)


mycursor = mydb.cursor()

sql = "INSERT INTO regioni (data, stato, codice_regione, denominazione_regione, lat, lon, ricoverati_con_sintomi, terapia_intensiva, totale_ospedalizzati, isolamento_domiciliare, totale_attualmente_positivi, nuovi_attualmente_positivi, dimessi_guariti, deceduti, totale_casi, tamponi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


try:
    last_cursor = mydb.cursor()
    last_sql = "SELECT * FROM corona ORDER BY id DESC LIMIT 1"
    last_cursor.execute(last_sql)
    last_record = last_cursor.fetchall()
    print("ultimo record: " + str(last_record[0][1]))
    last_data = last_record[0][1]
except:
    last_data = datetime.datetime.strptime("1900-01-01", "%Y-%m-%d %H:%M:%S").date()
    pass

with open('dati-regioni/dpc-covid19-ita-regioni-20200301.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if line_count > 0:
                
                data = datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S").date()
                stato = row[1]
                codice_regione = int(row[2])
                denominazione_regione = str(row[3])
                lat = float(row[4])
                lon = float(row[5])
                ricoverati_con_sintomi = int(row[6])
                terapia_intensiva = int(row[7])
                totale_ospedalizzati = int(row[8])
                isolamento_domiciliare = int(row[9])
                totale_attualmente_positivi = int(row[10])
                nuovi_attualmente_positivi = int(row[11])
                dimessi_guariti = int(row[12])
                deceduti = int(row[13])
                totale_casi = int(row[14])
                tamponi = int(row[15])

                val = (data, stato, codice_regione, denominazione_regione, lat,lon, ricoverati_con_sintomi, terapia_intensiva, totale_ospedalizzati, isolamento_domiciliare, totale_attualmente_positivi, nuovi_attualmente_positivi, dimessi_guariti, deceduti, totale_casi, tamponi)

                print (val)
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount, "record inserted.")





