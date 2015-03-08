//Rips images from Google maps

import urllib, os ,time

os.chdir('/Users/mac/Desktop/projects/dshack/SolarataHack/')

shifter=.0058
x_init=34.15-shifter
y_init=-118.297+shifter
x_final=33.83
y_final=-118.1

while x_init> x_final:
	while y_init< y_final:
		time.sleep(10)
		name_schema='LA_top_left_'+str(x_init+.003)+'N_'+str(y_init-.003)+'E_and_bottom_left_'+str(x_init-.003)+'N_'+str(y_init+.003)+'E.png'
		map_query="http://maps.googleapis.com/maps/api/staticmap?center="+str(x_init)+","+str(y_init)+"&size=1000x1000&zoom=18&sensor=false&maptype=satellite"
		new_name = name_schema.replace('.png','.tif')
		urllib.urlretrieve(map_query,new_name)
		
		y_init+=shifter
	x_init-=shifter
	y_init=-118.5+shifter