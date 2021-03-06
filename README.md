# NearestStateFinder
## Execuating requirements
* python 3.6 or higher
* linux x86-64
* compatiable with node-15.4.0
* internet connection
## How to install

* compile only:
```make all```

* compile and run:
```make run```

## Recalculating GeoHash library
- The first step to run this project will be to unzip the ```NationalFile.tar``` and get the information file of the provinces and states. 
``` 
cd pyscript
python3 textReader.py NationalFile_StateProvinceDecimalLatLong.txt
```

- To run this project, first check if there is a folder called  ```dics``` inside your project file. If not, please run the ```textReader.py``` first to get it. This folder will contains all the hierarchy dictionaries this project will use to do the state:country search. If you run this function, it will take a while so please give it some patience.
- If you want to test if the ```textReader.py``` is totally functional, try to change the text file it reads from ```NationalFile_StateProvinceDecimalLatLong.txt``` to ```partial.txt```.


## Search
### via Terminal
```
cd pyscript
python3 codeHandler.py
```
- After you run the code, you will see
```
Use Please input Latitude and press Enter:
Please input Longitude and press Enter:
Please input how many provinces you want to find near this point:
Do you want to remove the repolicated points in same provinces in the results? (1-yes, 0-no)
```

- Note: In this version, the user interface is ```python3 codeHandler 36.4611122 -109.4784394 6 1```
- Here's an example input and output:
```
The Geohash precision in this project is 6
Please input Latitude and press Enter: 36.4611122
Please input Longitude and press Enter: -109.4784394
Please input how many provinces you want to find near this point: 6
Do you want to remove the repolicated points in same provinces in the results? (1-yes, 0-no) 1
36.4611122 -109.4784394
GeoHash Code: 9w6pkv
The nearest reference point would be in NM San Juan with approximately 64.56301138550664 km distance
The nearest reference point would be in NM McKinley with approximately 136.6712929858626 km distance
This results has removed the replicated points.
```
- You can see the result in ```results.json```

### via Gui
![video](./readme_resources/screenshot.gif)

## Technologies
* Vue.js
* Typescript
* Electron
* python3
## TroubleShoot
1. Unable to show the google map.

running the gui program on scc. (google map key limitiation)
