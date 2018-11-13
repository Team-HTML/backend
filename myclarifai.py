from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import cv2 
import os
import json


def prediction(fimg, key):
	app = ClarifaiApp(api_key=key)
	model = app.models.get('cs110.1')
	model.model_version = '2dfc0f65c21a45e0a1978c3d45726307'


	response = model.predict_by_filename(fimg)
	#with open('response.json','w') as outfile: 
		#json.dump(response[data][concepts], outfile)
	#print(response[concepts])
	maxValue, maxId = parseJSON(response)
	return maxValue, maxId 

def parseJSON(data):
	#the part where has the concepts 

	d = (data['outputs'])[0]['data']

	maxValue = d['concepts'][0]['value']
	maxId = d['concepts'][0]['id']
	for i in d['concepts']: 
		if i['value'] > maxValue: 
			maxValue = i['value']
			maxId = i['id']
	return maxValue, maxId
