http://api.nytimes.com/svc/search/v2/articlesearch.response-format?[q=crime&fq=glocations:(New York City)]&api-key=8e87327b1c250edd19f69b7d92bf4df2:13:69417116

## NREL data
Solar Irradiance:-

https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json?api_key=&location=Denver+CO

curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://developer.nrel.gov/api/alt-fuel-stations/v1.json?api_key=fd0KdiUlVaibcZProOaccHgZJ2iYehiNJtl6Sgee

curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://developer.nrel.gov/solar/solar_resource/v1.json?api_key=fd0KdiUlVaibcZProOaccHgZJ2iYehiNJtl6Sgee&lat=40&lon=-105


r=  requests.get('http://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key=fd0KdiUlVaibcZProOaccHgZJ2iYehiNJtl6Sgee&lat=34&lon=118')


### Code

# fetch OPenDAP
from pydap.client import open_url
dataset =  open_url('http://mynasadata.larc.nasa.gov/thredds/dodsC/las/monthly_SSE/data_usr_local_fer_data_data_SSE_glob_rad.nc.jnl')

## Convert data to dict for US (lat and long are adjusted accordingly)
data =collections.defaultdict(list)
i=0
for month in range(2,12):
  for lat in range(113,140):
    for lon in range(50,118):
      if i%10 == 0:
        print "Progress @ lat = ", lat, "long = ", long
      i+=1
      if len(data[lat,lon]) != 3:
          data[lat,lon].append([dataset['GLOB_RADIATION']['GLOB_RADIATION'].data[month][0][lat][lon]])



## Writing dict to csv
import csv
file  = open('data.csv','w')
a =  csv.writer(file)
a = [['lat', 'long', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'july', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']]
for i in data.keys():
  a.append()[i[0],i[1]] + data[i]

with open('data.csv','w') as fp:
    a = csv.writer(fp, delimiter=',')
    data_csv = [['lat', 'long', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'july', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']]
    for i in data.keys():
        data_csv.append([i[0]-90,i[1]-180] + [x[0] for x in data[i]]) ## adjust for lat lon, they were taken in the form of index
    a.writerows(data_csv)
