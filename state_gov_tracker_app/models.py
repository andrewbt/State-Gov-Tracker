# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Officials(models.Model):
    legid = models.TextField(primary_key=True, blank=True) # This field type is a guess.
    fullname = models.TextField(blank=True) # This field type is a guess.
    firstname = models.TextField(blank=True) # This field type is a guess.
    middlename = models.TextField(blank=True) # This field type is a guess.
    lastname = models.TextField(blank=True) # This field type is a guess.
    suffixes = models.TextField(blank=True) # This field type is a guess.
    nickname = models.TextField(blank=True) # This field type is a guess.
    active = models.TextField(blank=True) # This field type is a guess.
    state = models.TextField(blank=True) # This field type is a guess.
    chamber = models.TextField(blank=True) # This field type is a guess.
    district = models.IntegerField(null=True, blank=True)
    party = models.TextField(blank=True) # This field type is a guess.
    transparencydataid = models.TextField(blank=True) # This field type is a guess.
    photourl = models.TextField(blank=True) # This field type is a guess.
    createdat = models.TextField(blank=True) # This field type is a guess.
    updatedat = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'officials'

class FbData(models.Model):
    legid = models.ForeignKey(Officials, primary_key=True, blank=True) # This field type is a guess.
    twitter = models.TextField(blank=True) # This field type is a guess.
    timestamp = models.TextField(blank=True) # This field type is a guess.
    post = models.TextField(blank=True) # This field type is a guess.
    text = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'fb_data'

class LegsSocialmedia(models.Model):
    legid = models.ForeignKey(Officials, primary_key=True, blank=True) # This field type is a guess.
    twitter = models.TextField(blank=True) # This field type is a guess.
    facebook = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'legs_socialmedia'

class OfficialTweets(models.Model):
    legid = models.ForeignKey(Officials, blank=True) # This field type is a guess.
    tweet = models.TextField(blank=True) # This field type is a guess.
    timestamp = models.TextField(blank=True) # This field type is a guess.
    tweet_key = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'official_tweets'


class PaBills(models.Model):
    state = models.TextField(blank=True) # This field type is a guess.
    session = models.TextField(blank=True) # This field type is a guess.
    chamber = models.TextField(blank=True) # This field type is a guess.
    bill_id = models.TextField(primary_key=True, blank=True) # This field type is a guess.
    title = models.TextField(blank=True) # This field type is a guess.
    created_at = models.TextField(blank=True) # This field type is a guess.
    updated_at = models.TextField(blank=True) # This field type is a guess.
    type = models.TextField(blank=True) # This field type is a guess.
    subjects = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'pa_bills'

class PaLegisNews(models.Model):
    legid = models.ForeignKey(Officials, blank=True) # This field type is a guess.
    title = models.TextField(blank=True) # This field type is a guess.
    link = models.TextField(blank=True) # This field type is a guess.
    summary = models.TextField(blank=True) # This field type is a guess.
    date = models.TextField(blank=True) # This field type is a guess.
    relevant = models.TextField(blank=True) # This field type is a guess.
    yeas = models.TextField(blank=True) # This field type is a guess.
    nays = models.TextField(blank=True) # This field type is a guess.
    news_key = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'pa_legis_news'

class PaLegisSponsors(models.Model):
    legid = models.ForeignKey(Officials, blank=True) # This field type is a guess.
    bill_id = models.ForeignKey(PaBills, blank=True) # This field type is a guess.
    type = models.TextField(blank=True) # This field type is a guess.
    yeas = models.TextField(blank=True) # This field type is a guess.
    nays = models.TextField(blank=True) # This field type is a guess.
    sponsor_key = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'pa_legis_sponsors'

class PaLegisVotes(models.Model):
    legid = models.ForeignKey(PaBills, blank=True) # This field type is a guess.
    bill_id = models.TextField(blank=True) # This field type is a guess.
    vote = models.IntegerField(null=True, blank=True)
    date = models.TextField(blank=True) # This field type is a guess.
    yeas = models.TextField(blank=True) # This field type is a guess.
    nays = models.TextField(blank=True) # This field type is a guess.
    vote_key = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'pa_legis_votes'

