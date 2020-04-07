import os,sys,requests,json


c = requests.session()
#-*-Cek User-*-#
def cekus():
	q = raw_input("User : ")
	#q = "mrxsz"
	url = "https://id-api.spooncast.net/search/user/?q=" + q
	#headers =  "Android Phone / Chrome 61 [Mobile]: Mozilla/5.0 (Linux; Android 12.5; Marvel Xcore7 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36"
	r = c.get(url) 
	js = json.loads(r.text)
	for a in js["results"]:
		print ("Nickname  : "+a["nickname"])
		print ("Username  : "+a["username"])
		print ("ID : "+str(a["id"]))
		print ("Following : "+str(a["following_count"]))
		print ("Followers : "+str(a["follower_count"]))
		print ("Email  : "+a["email"])
		print ("Link Profil : "+str(a["profile_url"]))







	
	
	
	
	
	
	
	
	
  
