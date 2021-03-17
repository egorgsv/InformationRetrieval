# InformationRetrieval
##Prequirements
* Python >= 3.8
* pip
* git
##Installing
```shell
git clone https://github.com/egorgsv/InformationRetrieval
pip install -r requirements.txt
```

##Usage
```shell
cd InformationRetrieval
python3 main.py "head AND conservative"
```
###
There are three operations that are able to use: AND, OR and NOT.
Also we realized brackets construction
```shell
python3 main.py "head AND (conservative OR faction)"
```