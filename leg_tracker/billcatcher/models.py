from django.db import models

class Lawmaker(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name
	party = models.CharField(max_length=1)
	position = models.CharField(max_length=20)
	member_id = models.IntegerField(default=0)
	headshot = models.URLField()
	district = models.IntegerField(default=0)
	county_short = models.CharField(max_length=20)
	phone = models.CharField(max_length=15)
	email = models.EmailField()
	county_long = models.CharField(max_length=100)
	chamber = models.CharField(max_length=10)
	eid = models.IntegerField(default=0)
	legiscan_id = models.IntegerField(default=0, primary_key=True)
	active = models.BooleanField()


class Bill(models.Model):
	sponsors = models.ManyToManyField(Lawmaker)
	title = models.CharField(max_length=140)
	def __str__(self):
		return self.title
	bill_id = models.IntegerField(default=0)
	state_link = models.URLField(default=0)
	bill_summaries = models.URLField(default=0)
	bill_number = models.CharField(max_length=5)
	description = models.CharField(max_length=200)
	file_date = models.DateField('date filed')
	#added this
	updated = models.DateTimeField(auto_now=True)
	last_action = models.CharField(max_length=200)
	last_action_date = models.DateField('last action date')
	###
	watch = models.BooleanField(default=False)
