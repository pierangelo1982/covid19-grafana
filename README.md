### monitoring covid19 with Grafana

# crea mysql e phpmyadmin
```
docker run --name covid19-mysql -e MYSQL_ROOT_PASSWORD=password -p 3306:3306 -d mysql:5.7
```

```
docker run --name covid19-phpmyadmin -d --link covid19-mysql:db -p 8081:80 phpmyadmin/phpmyadmin
```

crea grafana:
```
docker run --name covid19-dashboard -d -p 3000:3000 --link covid19-mysql:db grafana/grafana
```


# salva i dati in database mysql
 ottieni i dati dal repository del governo:

 https://github.com/pcm-dpc/COVID-19


 # crea script per importare dati in database
 store_data.py

