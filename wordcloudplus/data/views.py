from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import mining
import simplejson as json
from lxml import html, etree
from lxml.html.clean import clean_html
from data.models import Docs

@csrf_exempt
def index(request):
	site_content_keys = []
	site_content_values = []
	site_content_json = '['
	wordcloud_object_dict = {}
	"""
	if request.method == 'POST':
		#print request.POST		#for testing / error handling
		site_content = mining.get_data_set(request.POST['address'])
		
		for i in site_content:
			site_content_keys.append(i[0])
			site_content_values.append(i[1])
			json_string += (('' + i[0] + ', ') * i[1])
		json_string = json_string[:-2] + ']'
	else:
		site_content = ''
		
	zipped_counter = zip(site_content_keys, site_content_values)
	
	c = {
			'mined_data': site_content,
			'zipped_counter': zipped_counter,
			'json_string': json_string
		}
	
	return render(request, 'data/index.html', c)
	"""
	if request.method == 'POST':
		#print request.POST		#for testing / error handling
		
		# if request.POST['file_upload']:
		# 	file=request.FILES['doc']
		# 	print file
			
		# 	instance = Docs(	file=request.FILES['doc'],
		# 						title = 'temp',
		# 					)
		# 	instance.save()
		
		# else:
			#site_content, site1_percentage, site2_percentage
		
		wordcloud_object_dict = mining.get_data_set(request.POST.getlist('addresses'))
		site_content = wordcloud_object_dict['site_content']

		for i in site_content:
			site_content_keys.append(i[0])
			site_content_values.append(i[1])
			site_content_json += (('' + i[0] + ', ') * i[1])
		site_content_json = site_content_json[:-2] + ']'
	else:
		site_content = ''

	c = {
			'site_content_json':site_content_json,
			'wordcloud_object_dict':wordcloud_object_dict
		}

	return render(request, 'data/index.html', c)