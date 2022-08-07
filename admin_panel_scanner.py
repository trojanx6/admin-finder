import requests as req 
target = str(input("Hedef adresi giriniz: "))


def main():
    istek = req.get("https://"+target)
    if istek.status_code != "404":
        istek = req.get('https://'+target)
        with open("wordlist.txt","r+") as f:
              for i in f.readlines():
                  istek_1 = req.get("https://" +target + '/' + i )
                  if istek_1.status_code == "200":
                     print("Send:","https://" +target + '/' + i)
                  else:
                     print("Not Found !")
    else:
        istek = req.get("http://"+target)
        with open("wordlist.txt","r+") as f:
              for i in f.readlines():
                  istek_1 = req.get("http://"+target + '/' + i)
                  if istek_1.status_code == "200":
                     print("Send:","http://" +target + '/' + i)
                  else:
                      print("Not Found !")
               
       
main()
 
        