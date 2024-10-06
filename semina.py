import requests
from bs4 import BeautifulSoup 
import pandas

URI="http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey="
SERVICE_KEY="CFb1DxFt6DFD4EJMROIAF17sd8oShhYeI%2BpVNTTRC2RgxfHgkDEqjjYSfqXSP5VxND%2BdKSOdYCLS8HW%2Fs50%2FuA%3D%3D"
items="&numOfRows=25"
PageNum="&pageNo=1"
SidoName="&sidoName=서울"
searchCondition="&searchCondition=HOUR"
URI=URI+SERVICE_KEY+items+PageNum+SidoName+searchCondition
response=requests.get(URI) #REQUST로 데이터 요청하기
soup = BeautifulSoup(response.text, 'lxml-xml')
ItemList = soup.findAll('item')

datetimeList=[]
citynameList=[]
so2valueList=[]
covalueList=[]
o3valueList=[]
no2valueList=[]
pm10valueList=[]


for item in ItemList:
    datetime=item.find('dataTime').text
    cityname=item.find('stationName').text
    so2value=item.find('so2Value').text
    covalue=item.find('coValue').text
    o3value=item.find('o3Value').text
    no2value=item.find('no2Value').text
    pm10value=item.find('pm10Value').text

    
    datetimeList.append(datetime)
    citynameList.append(cityname)
    so2valueList.append(so2value)
    covalueList.append(covalue)
    o3valueList.append(o3value)
    no2valueList.append(no2value)
    pm10valueList.append(pm10value)

DATA = pandas.concat([pandas.DataFrame(datetimeList),
pandas.DataFrame(citynameList),
pandas.DataFrame(so2valueList),
pandas.DataFrame(covalueList),
pandas.DataFrame(o3valueList),
pandas.DataFrame(no2valueList),
pandas.DataFrame(pm10valueList)]
,axis=1) 

DATA.to_csv("서울시_미세먼지데이터.csv",index=False)