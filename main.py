# import requests
# import streamlit as st
# url = "https://online-movie-database.p.rapidapi.com/auto-complete"
# querystring = {"q":"game of thrones"}
# headers = {
# 	"X-RapidAPI-Key": "3219a68b92msh29b6e8a5f3ac678p1f555fjsnd1399975bbb0",
# 	"X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
# }
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)
# moviename = response.json()
# name = moviename["d"][0]["i"]["imageUrl"]
# print(name)
# st.info(name)



# import requests
# import streamlit as st
# st.title("Netflix Data")
# inputUN = st.text_input("Enter name of movie or season:")
# clickbutton = st.button("Check")
# if clickbutton:
# 	url = "https://netflix54.p.rapidapi.com/search/"
#
# 	querystring = {"query":inputUN,"offset":"0","limit_titles":"10","limit_suggestions":"2","lang":"en"}
#
# 	headers = {
# 		"X-RapidAPI-Key": "3219a68b92msh29b6e8a5f3ac678p1f555fjsnd1399975bbb0",
# 		"X-RapidAPI-Host": "netflix54.p.rapidapi.com"
# 	}
#
# 	response = requests.request("GET", url, headers=headers, params=querystring)
#
# 	print(response.text)
# 	output = response.json()
# 	st.info(output)

# import requests
# import streamlit as st
# st.title("Movie Data")
# inputUN = st.text_input("Enter name of movie or season:")
# clickbutton = st.button("Check")
# if clickbutton:
# 	url = "https://mdblist.p.rapidapi.com/"
#
# 	querystring = {"s":inputUN}
#
# 	headers = {
# 		"X-RapidAPI-Key": "3219a68b92msh29b6e8a5f3ac678p1f555fjsnd1399975bbb0",
# 		"X-RapidAPI-Host": "mdblist.p.rapidapi.com"
# 	}
#
# 	response = requests.request("GET", url, headers=headers, params=querystring)
#
# 	print(response.text)
# 	movie = response.json()
# 	# final = movie ["search"][0]["id"]
# 	# st.info(final)
# 	st.info(movie)

import requests
import streamlit as st

input_no = st.text_input("Enter Phone No")
clickbutton = st.button("Verify")
if clickbutton:
	url = "https://veriphone.p.rapidapi.com/verify"

	querystring = {"phone":input_no}

	headers = {
		"X-RapidAPI-Key": "3219a68b92msh29b6e8a5f3ac678p1f555fjsnd1399975bbb0",
		"X-RapidAPI-Host": "veriphone.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	print(response.text)
	var1 = response.json()
	final = var1["status"]
	final2 = var1["country"]
	final3 = var1["carrier"]
	# ["local_number"]
	# ["carrier"]["country"]
	print(final)
	print(final2)
	print(final3)

	st.info(final)
	st.info(final2)
	st.info(final3)