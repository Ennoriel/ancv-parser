from json import loads
import urllib.request
import xml.etree.ElementTree as ET
import re


class AncvItem:
	
	def __init__(self, o):
		self.nid = o["nid"]
		self.longitude = o["longitude"]
		self.latitude = o["latitude"]
		self.picto_activite_marqueur = o["picto_activite_marqueur"]

	def parse(self):
		with urllib.request.urlopen("https://guide.ancv.com/ancv_arcgis/popup/" + str(self.nid)) as url:

			content = url.read().decode()
			content = re.sub(r'<img[^>]*>', ' ', content)
			content = re.sub(r'<\/a><\/span>', '</a>', content)

			self.raw_data = ET.fromstring(content)

			self.nom = self.sstrip(self.raw_data[0][0][1].text)
			self.details = self.sstrip(self.raw_data[0][1][0].text)
			self.adresse = self.sstrip(self.raw_data[0][1][1].text)
			self.ville = self.sstrip(self.raw_data[0][1][3].text)
			self.tel = self.sstrip(self.raw_data[0][1][4].text)

	@staticmethod
	def sstrip(s):
		return " ".join(s.split())


with open('ancv.json', 'r') as f:
	ancv_data = f.read()

ancv_data = loads(ancv_data)

with open('ancv_out.csv', 'w') as f:
	f.write("nom;details;adresse;ville;longitude;latitude")
	for ancv_data_item in ancv_data:
		try:
			item = AncvItem(ancv_data_item)
			item.parse()
			f.write("%s;%s;%s;%s;%s;%s\n"%(item.nom, item.details, item.adresse, item.ville, item.longitude, item.latitude))
		except:
			print(item.nid)
