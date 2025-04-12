import requests,re
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[1;32m' #اخضر

user = input(X+'Enter Your username : ')
pasw = input(X+'Enter Your password : ')

api_getCookies = requests.post(url = 'https://www.instagram.com/accounts/login/ajax/',headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "385",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "csrftoken=Lk9Lfwj0Hp0T3zCBYwjoeGBUBjU1sVXC; mid=YSuaiwAEAAEzvEB8maY7IzJ6MDzJ; ig_did=07753880-8B96-4C09-93E9-BA39B801DD08",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/accounts/login/",
        "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "x-asbd-id": "437806",
        "x-csrftoken": "Lk9Lfwj0Hp0T3zCBYwjoeGBUBjU1sVXC",
        "x-ig-app-id": "936619743392459",
        "x-ig-www-claim": "0",
        "x-instagram-ajax": "56f3c2d2a823",
        "x-requested-with": "XMLHttpRequest"},data = {"username": f"{user}","enc_password": f"#PWD_INSTAGRAM_BROWSER:0:1613414957:{pasw}","queryParams": "{}","optIntoOneTap": "false"})

if '"authenticated":true' in api_getCookies.text:
	print(f'{F}Login Good ✅\n')
	see = f"{api_getCookies.cookies.get_dict()['sessionid']}"
	cs = f"{api_getCookies.cookies.get_dict()['csrftoken']}"
	
	print(f'{F}Session title : {see}\ncsrf : {cs}')
	cookies = {
    'mid': 'ZlyrzwABAAFceK0Phqdmd7088OEr',
    'ig_did': '6963C9E9-04AB-49B9-93C8-1AE038DB5FF2',
    'ig_nrcb': '1',
    'datr': 'yqtcZms2N_zjc62L8miVe-ce',
    'ps_n': '1',
    'ps_l': '1',
    'igd_ls': '%7B%2217847471666042092%22%3A%7B%22c%22%3A%7B%221%22%3A%22HCwAABaqdBautpPQBxMFFtjT2IzKi7Q_AA%22%2C%222%22%3A%22GRwVQBxMAAAWARbw6OblDBYAFvDo5uUMABYoAA%22%7D%2C%22d%22%3A%228c7977ef-991b-4c43-a676-20cdb9ff030d%22%2C%22s%22%3A%220%22%2C%22u%22%3A%22mx58co%22%7D%2C%2217845730126851040%22%3A%7B%22c%22%3A%7B%221%22%3A%22HDwWARYBAAAWARYBEwUWwK-_z5qmsz8A%22%2C%222%22%3A%22GRwVQBxMAAAWARa-3vXlDBYAFr7e9eUMABYoAA%22%7D%2C%22d%22%3A%22138ff0b5-0154-4e31-8343-c3a8b8de36d6%22%2C%22s%22%3A%220%22%2C%22u%22%3A%220zh4yo%22%7D%7D',
    'csrftoken': cs,
    'ds_user_id': '30782426491',
    'dpr': '3.2983407974243164',
    'shbid': '"9983\\05430782426491\\0541756407145:01f7346a701861734f9461b0ed510f409b55c77d7085dc82f80e694d4aefcbd10a61e115"',
    'shbts': '"1724871145\\05430782426491\\0541756407145:01f74fcf2be45fa99a8c7ce948851df5965d80682e6caa7e617bc7b243e675caea643bcb"',
    'sessionid': see,
    'wd': '891x1627',
    'rur': '"NCG\\05430782426491\\0541756407225:01f7a13f8c6c4536e64d74f566ca33f4fab4b1ed84d433de57ffdd65aaea94ed01829729"',
}
	headers = {
	    'authority': 'www.instagram.com',
	    'accept': '*/*',
	    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://www.instagram.com',
	    'referer': 'https://www.instagram.com/stories/cahitkayaoglu_/',
	    'sec-ch-prefers-color-scheme': 'dark',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-model': '""',
	    'sec-ch-ua-platform': '"Linux"',
	    'sec-ch-ua-platform-version': '""',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
	    'x-asbd-id': '129477',
	    'x-csrftoken': cs,
	    'x-ig-app-id': '936619743392459',
	    'x-ig-www-claim': 'hmac.AR0KNgKDGG_TzcQiTWOl0cNhBWBR05x38V3TeNps_D35FywY',
	    'x-instagram-ajax': '1016035497',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	st = input(f'{X}Enter the story link : ')
	match = re.search(r'/stories/.+?/(\d+)', st)
	if match:
		ii = match.group(1)
		print(f"{F}\nStory ID: {ii}")
		cod = input(X+'Enter Your code Report : ')
		
		data = {
    'container_module': 'StoriesPage',
    'entry_point': '1',
    'location': '4',
    'object_id': ii,
    'object_type': '1',
    'context': '{"tags":[],"ixt_context_from_www":"QVRNR2pINWcyeDdsbjhzeEZLRWdsQ0Jsa0lQVU5vd3o4eDBQTTVZNlVxUkw4TmRNbEdBdjFxRlp2TlMwY21iaEpnRmx4UzZCeG5SWnlTajJsR2lmdjF4eWNuTFZXTzM5bVVQMzc2eHk2TmVpbVFDalFRNkNlWG9hQ0xCWm9CYXhjVWhIZGZidU5PTzhnTmtUNUtqNlNKME9JdEg0VnNqR1dER0FPdnZ6TzVMWXY1bjBwQUh2SFo0SDlfODJlXzJlYXR6Q1htUFpiNFVPczNVbzU2d0xya2FlTEd2eWQzeXQzRjBPYjh1VkdtaHF1NkpGX2xuQXdxYWNYbDN6Wm81aTYzbHhfejVzdlJ5TmlYVl9ueEtXYWN3dkp4ZmtYTkhPazV3T3RVdFppX0JBRnhSR2dkRl9kWGh1X3lRRjE1OC16eGdELXloS0VoVHR1VUdBYjBJZlI0SkxONGJfVWpRZTRLZE5paXlHNmZRZXVXNnNHU0JCRHR6NkdJc1RkQ1dZWjEyZDRMV19zT1FzM0tCcWJaQXNJU3lpOENvVlNnUWl2emM5MzBRbHJkQUJxdE8yNWNqMDFlTlBZREZ5di11U3B3MkdLb09NdHEwMTlBQkROYkk5VEdJX3BOT3hVajlnMWNJLXREYzFXdnJZTkRaUW9iMGc5REg3TWk0THp0VlFJRkNldDJ2LUQ3dVJqMXZTczExaGhYRFZydGpBN0xYNUpBajI2bnYzaDM5WXlZbXZyWGJnNUtxbndIYzR5MlFrMEt0NDhKS1QyMDA4N2l4RlRzeFR0QTI5ZV9tRUxQbFVpUmNudTh6dzBsOXhMLTJiVmNJLWt6OVBiY0dWT1Y3TmRkbEx0M3NxNUJDOTRMcWZtQXBGU20xbzNyS3B6V29xa1pjYWVXRWE1RHc3U0FqaTZDX0RsNW16cGJSV2RmSkEwdlVUcUdPNm45cVFmenAtbjV1SHB1SGtNeE9NTExNaFhqaVNfeERPSDRqMHBDWTBfYnMzLW51ZmNtUmRlQUhRempyeWpraUtRc0J2cWtiNUFnZGtRRDV4T2lzNGJDclFoMTlQaDFDZGczbXhRamtHcXdTZ3NDNnBsNnlUd0NjZmNQdHlkSVBWWGRiUlBiRWkzRWhhOUtlQnRvSUFmUVZUT3ljTkt5QTh4QUZDNU14UENoZXBubXA2NjlwUFJuQ29saktDOEM1WXV4TkNNWlJtc1pyX2lQdUtydzN5ZERPVGRDOFJ0OFZueWNjSllTdVhzRlVMS09qejEyVE5ucFVEdlU2c3Bmb0tiNkM1U1ZvaW9fODc4N3dWRWo4V1BTR3RsNVUybE1TaVl3UFZzQVVkNWtpd0l5VmI5NHUxZEhrRjFrU3JHdUFpNDVHYk1fTnd0a2dTbzJSWW1yMHFnSEk3WnFLNUV3MG1rMmNWekU5S2otWFkyelZSRWZETnFEQnRrdHA3RnpvQ3ozRDBHODBFWUhHQ3ctYkVYTWEyczFRYk8yTE1uSlo5UWl0UlVremFDRndMMVM0b29iWlpWS01GVWpoNXhJSGY4blVFWnIzbzdqLVB2Vm9GZzVFVHMtQTlfeS1OVEJOQU1iUDBfS0xhcHYteHdpRXZRaHBoV21jMUZyNS05SmpNMWlSUUxEeUV6emROLUlOLXpxWmdiYlRzamVOaUZ2ZTJCSEpjckpDUVYydEV3NUVHYWVVOGxYMGNXMzlHeWxja0VudXJDaklQaDdhLTkwcEhHYlNKb3ZscUI1MU9VQ3NoUVh0eTdrVXlwRHo1cDREQkhyVndmaVhDeUgxSUpveWs1RDNPWVdGTVMzQnl6ZXlyQWlnWU5VamhRcTVJcDVFSXBRNGEtY2dBNnpaNzNQTFdNVW9sZ3J1VjFUWlZEVkh4V0tlOVhoV3R5VDA2Y3I5djA3V3MwblhOeUpxcEo5d09SMFZvUTktQW9QYXQ2cjNSa2h0QTBfcnVyM1Q5LVpMWGhrSVprUnBWcy1aV1d2VVlJNDN5X1E3TkRQNDBDZGZlSDlXTm9YZThRaXJjeGJLcTFYODJfUnVjVFF1ZW53eTd2SzZWVFFucGRocVhaS3V3ZDdMb29nZDdvUWpVZjZDV1c0NzUxSkFGSVNCbi1ZeTNLdi1kcVdpZTRKV3NkM2lSNktqcXVZWXRVM1pBdnR2VTN4LUhUN1FpQThGdEQ4OHFnZUNzRnFlUTFOZGFOZXoxaE9pRW1EeEk0bFFmYzkwYVZmNjIteURnajdwazVIVmh0RkFfcURfTmpkcmZfOEZVbjhNWWNfUk55MEZHODdoNVZXQ1BCdmZPTzloVVhKTWYwajFjdXowUUtfMU1oUlFJYUhBSDctMzNnak9WQVNIaXJRT05QeFlGcFhRMW5ZRF8xSGMxU29uTlhoUGl5amV5dDVwaFhJeGNyWU5faWJCZkVBZFRacmpHWHlIQllZODQ1UUxvcXUzaEhuN21Eb0d5eDNzREJVM2ZBMS1OV0dWMWJaUDMwSzhncDdqZnoyVUw0eVh6SGxmVUFNV2pmQ2x4QUU0N0k0N2p4ZlQ0clhNTVpybkpLVElWVnNDQTJHQl9JQUVuRVR1Szh0NHpHWjVnRzRtcmVQMlZEa2V1aDhuRU5uMjhZM1RUYVhuZ3RTUEJJWTY2VEtYTVZiTGhjX1N3OEtrZGhURnhjdmV0ZnJFc1d6WFVBeGFUN1lNeHRXZk5Hc2V0Q1ZLR2g1RklmQ3lZMGNGVnpSd1g3c3FKSVBZa2VCdk16Q19GVXFqZWNxWm1qWmc0akFiR2lsWV9pRTFnd01ERFVlY01KcVcweHpHc1lhRkR1MHZocm1vQVkyUmpCaXZTbkNMUW5td1dVTEphd0NVTE5kOUVJWW13ajVCbS12YTFKcldYUzhrYmJacHN3dHB0d1kxUWxIVzltclBtb2l3WjBZbmdXekVKU0tWU0RLV1BwWGhEV19DTkdJb1NNZ2VKRERKWjhjR1Baei10RjhjSEZTSnVTNlBhbXF5QS1COXpBVDh3UkZRdklFOHh6NG1Pb19TenRLbmVNRGFDOGd1eEdSMU05NTBsTGVvS1NiUGlyclgycjhiREdDMXhNSnhiMEYyQllFeTVVT2ZOU3ZMTkEwNk1YWVNTZ2ZuM1paMmVxQnNKd0VxSnEtdU5qdlNQamZENTVER18xdHBucHc4dVVucG1Hd2pxNzVsRzkxa2xHQ0poYy1mNW1OTFkwM1BhYU9IN05TbVhjdDh6RkJIWnZxY3ZkMURqVmRWT0NxLUh3MXZLanFsQnZpS3lyejF6SjJyYmRaekp3MkpjU0ZaR0d1TTduOTg3XzEyMEVaaDhyWGFFdVJZMXI2MS1IYUxoSXI5VkJXbGtWTkJfSFhmRzRrZndWUWlOZmZBNm4zc2hTMnB3LVAzTEI4bVFkTXB2SzhmQ21CRk8tRS1LTlBuZjRkTG9zblQ5MmQ1TFVkU3cyd1hBdktUc29qbUIySlJzRUw5V0JqUS1Wd1BJTHhPd2loOFc1M1g1UERpZnNRZ1k5TXNBbngyQUlaUVo1WXJjTFhlUHIydDRvd0oxQWpBSnVxLVdBZnp4bXYyLU1ZeVRrbW5VVVgzUW42ZE51bVhGaWJFWGdjRXU4MzNiYzdGZ2Y4dm9yMXdsWXc1dXMtWklFdWZhODNwWW1GMW1NQjdkcmU3a2RFUkdvV1VoODNSQXhieE9POHdkb0FIX0d1Q2t3bl9ZRm1MU3dDNHdfa3pjaHNVWmljbUptaXRLXy15YWM2ZXRwWldUWnZDaW5tYnRzTi1GTGFuX0wtek83Yi1IOGVQSlBRekVpYjBQRDQyTzA3bjAyYXZyVTNMTFhKaW1yNjNydDY3cHo2a0NwbTdXd1BSRGY3UjVqZDNJR0dzSHNnaC1USWtrdUlMNkcyLUNqQVJwc0pXd0J4SkUzVFc4OXN4cXRsX0hQYUxyYVJJV2lmby1ueEpXc2ZZOW5vWVNVMl9uaklsME13","frx_context_from_www":"{\\"location\\":\\"ig_story\\",\\"entry_point\\":\\"chevron_button\\",\\"session_id\\":\\"52adec1b-2df0-4f24-896a-06c844f7d32c\\",\\"tags\\":[],\\"object\\":\\"{\\\\\\"media_id\\\\\\":\\\\\\"3444470701165612904\\\\\\"}\\",\\"reporter_id\\":17841430794737803,\\"responsible_id\\":17841400763277384,\\"locale\\":\\"ar_AR\\",\\"app_platform\\":4,\\"extra_data\\":{\\"container_module\\":\\"StoriesPage\\",\\"app_version\\":\\"None\\",\\"is_dark_mode\\":null,\\"app_id\\":936619743392459,\\"sentry_feature_map\\":\\"Jva1tKzlARgONDUuMTUzLjExOS4xOTIYZU1vemlsbGEvNS4wIChYMTE7IExpbnV4IHg4Nl82NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjAuMCBTYWZhcmkvNTM3LjM2GAVhcl9BUhwYIGY3YjdmZWJmMjc2NGE5ZTZmMDdmZjEzOGI4NGNmZjRiGAAYIDFlMDUwNmU4MWFmM2Y0M2ZkYjEzNjBiZWM3MDRkMDNhGCRxdWljNzFiMDdhODBiOTBmOTY0Y2YzOTE3ODliNDhkNjU1Y2MViKMHKCBhYjE2MmI3ZWM1ZGNlZDZiZDU3MTJiYWI3MDhjOGU0YQA8LBgcWmx5cnp3QUJBQUZjZUswUGhxZG1kNzA4OE9Fchawgvmf+2MAHBUIKwGIAm9zA1gxMQAiPDkVABkVADkVAAAYIDNjMjk2MDcyNzU1MjQyNDU4YWQ3NmIwMmJiNzliZjBiFQIREhgPOTM2NjE5NzQzMzkyNDU5HBbCj4bxz\\\\\\/e7PxhAYzEwYmYzMjE4OTZmYjAwNDJmZTA0NWU2YzY4ZDI2NjYzYjdiZTg0NmZlMjllMjYxYmFhODc5MjNiZWQ3NDEyYQAcFQQAEigxaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS9zdG9yaWVzL2NhaGl0a2F5YW9nbHVfLxgOWE1MSHR0cFJlcXVlc3QAFpbi8Iz6q7E\\\\\\/KCMvYXBpL3YxL3dlYi9yZXBvcnRzL2dldF9mcnhfcHJvbXB0LxYQFoa85+sMAA==\\",\\"shopping_session_id\\":null,\\"logging_extra\\":null,\\"is_in_holdout\\":null,\\"preloading_enabled\\":null},\\"frx_feedback_submitted\\":false,\\"ufo_key\\":\\"ufo-83dc0813-1459-4cdf-b28f-367373d17aaf\\",\\"additional_data\\":{\\"is_ixt_session\\":true,\\"frx_validation_ent\\":\\"IITASEntMedia\\"},\\"profile_search\\":false,\\"screen_type\\":\\"frx_tag_selection_screen\\",\\"ent_has_music\\":false}"}',
    'selected_tag_types': f'["{cod}"]',
    'frx_prompt_request_type': '2',
}
		n=0
		while True:
			re = requests.post('https://www.instagram.com/api/v1/web/reports/get_frx_prompt/',cookies=cookies,headers=headers,data=data).text
			if '"status":"ok"' in re:
				n+=1
				print(f'{F}It has been reported Spam [ {n} ] ')
			else:
				print(Z+'An unexpected error occurred')
	
	else:
		print(Z+'Error in the story')


else:
    exit(Z+'False in Login | خطا في التسجيل')
