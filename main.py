import requests
import time
import threading
#from app import keep_alive

#keep_alive()

h = {"Host": "diamond-wala.onrender.com","accept": "application/json, text/plain, */*","token": "","content-type": "application/json","accept-encoding": "gzip", "user-agent": "okhttp/4.10.0"}
url = "https://diamond-wala.onrender.com/diamond-wala/userGameData/addTokenCoin"

url2 = "https://diamond-wala.onrender.com/diamond-wala/userGameData/onAdView"

ur2Data = {"adType":"Interstitial"}
data = {"data":{"tokenSource":"Game","gameProvider":"Gamezop","gameName":"Battle Fish","tokenAmount":10}}

with open("./newGamesT.txt","r")as r:
  list = r.read().split("\n")




h2 = {"Host": "diamond-wala.onrender.com",
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.10.0"}
    
urlLogin = "https://diamond-wala.onrender.com/diamond-wala/user/auth/signup-login"




log1= {"email":"gyankumar7282@gmail.com","imgUrl":"https://lh3.googleusercontent.com/a/ACg8ocIRQyw4jtCOccvBKnWJDxmcQpuSUzIbuyMxVD0-R4hq=s96-c","deviceId":"5586a964f4185d05"}
log2 =  {"email":"birihirok@gmail.com","imgUrl":"https://lh3.googleusercontent.com/a/ACg8ocIRQyw4jtCOccvBKnWJDxmcQpuSUzIbuyMxVD0-R4hq=s96-c","deviceId":"55m6a664f4185d"}


def add(Name):
  for i in range(2):
      data ={"data":{"tokenSource":"Game","gameProvider":"Gamezop","gameName":Name,"tokenAmount":10}}
      h["token"] = "Bearer "+requests.post(urlLogin,headers=h2,json=log1).json()["accessToken"]
      print("     ",Name,requests.post(url,headers=h,json=data).text)
      print(requests.post(url2,headers=h,json=ur2Data).text)
      h["token"] = "Bearer "+requests.post(urlLogin,headers=h2,json=log2).json()["accessToken"]
      print("     ",Name,requests.post(url,headers=h,json=data).text)
      print(requests.post(url2,headers=h,json=ur2Data).text)
      time.sleep(240)

def run():
    while(True):
    	 for i in range(5,len(list)):
    	 	add(list[i])
  #time.sleep(140)
  




  
