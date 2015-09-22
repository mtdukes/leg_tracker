#This script will be periodically run to load in lawmakers to the leg_tracker system.
#Probably need to think through the workflow
#When is this run? Automatically or manually?
#Do we keep lawmakers in the database if they're no longer active?
#maybe with the active boolean?

import json, os, urllib

from billcatcher.models import Lawmaker

url = 'http://www.wral.com/news/state/nccapitol/data_set/14376504/?dsi_id=ncga-eid&version=jsonObj'

def load_lawmakers():
	response = urllib.urlopen(url)
	data = json.loads(response.read())

	for d in data:
		Lawmaker.objects.get_or_create(
			name = d['member'],
			party = d['party'],
			position = d['title'],
			member_id = d['ncleg_id'],
			headshot = d['headshot'],
			district = d['district'],
			county_short = d['county_short'],
			phone = d['phone'],
			email = d['email'],
			county_long = d['county_long'],
			chamber = d['chamber'],
			#need to add a legiscan people_id item here to deal with eid duplication issue
			legiscan_id = d['legiscan_id'],
			eid = d['eid'],
			active = str(1)
			)

if __name__ == '__main__':
	load_lawmakers()
	print "...lawmakers loaded"