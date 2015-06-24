from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
	user = models.OneToOneField(User)
	avatar = models.CharField(max_length=200)
	rating = models.DecimalField(max_digits=3, decimal_places=0, default=0)
	def __unicode__(self):
		return self.user.username


class Question(models.Model):
	question_title = models.CharField(max_length=200)
	question_text = models.CharField(max_length=400)
	author = models.ForeignKey(User, related_name="author")
	pub_date = models.DateTimeField('date published')
	#likes_number = models.DecimalField(max_digits=3, decimal_places=0, default=0)
	#dislikes_number = models.DecimalField(max_digits=3, decimal_places=0, default=0)
	users_liked = models.ManyToManyField(User, related_name="question_users_liked", blank=True )
	users_disliked = models.ManyToManyField(User, related_name="question_users_disliked", blank=True )
	rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
	comments_number = models.DecimalField(max_digits=3, decimal_places=0, default=0)
	correct_comment = models.ForeignKey('Comment', related_name='correct_comment', null=True)
	def __unicode__(self):
		return self.question_title
	def get_rating(self):
		liked = self.users_liked.count()
		disliked = self.users_disliked.count()
		if((liked + disliked) == 0): return 0
		return int(float((liked - disliked) * 100 /(liked + disliked)))/100.0
	#def get_votes_number(self):
	#	return self.likes_number + self.dislikes_number
	def can_like(self, user):
		if( user in self.users_liked.all() ):
			return True
		else:
			return False
	def can_dislike(self, user):
		if( user in self.users_disliked.all() ):
			return True
		else:
			return False
	def count_comments(self):
		self.comments_number = self.comment_set.count()
	def save(self, *args, **kwargs):
		self.count_comments()
		super(Question, self).save(*args, **kwargs)
		self.rating = self.get_rating()
		super(Question, self).save(*args, **kwargs)
			

class Comment(models.Model):
	question = models.ForeignKey(Question)
	author = models.ForeignKey(User)
	comment_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	is_right = models.NullBooleanField(default=False)
	users_liked = models.ManyToManyField(User, related_name="comment_users_liked", blank=True )
	users_disliked = models.ManyToManyField(User, related_name="comment_users_disliked", blank=True )
	rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
	def __unicode__(self):
		return self.comment_text
	def get_rating(self):
		liked = self.users_liked.count()
		disliked = self.users_disliked.count()
		if((liked + disliked) == 0): return 0
		return int(float((liked - disliked) * 100 /(liked + disliked)))/100.0
	def can_like(self, user):
		if( user in self.users_liked.all() ):
			return True
		else:
			return False
	def can_dislike(self, user):
		if( user in self.users_disliked.all() ):
			return True
		else:
			return False
	def save(self, *args, **kwargs):
		#self.question.count_comments()
		super(Comment, self).save(*args, **kwargs)
		#self.rating = self.get_rating()
		super(Comment, self).save(*args, **kwargs)

class Tag(models.Model):
	questions = models.ManyToManyField(Question)
	tag_text = models.CharField(max_length=200)
	absolute_popularity = models.DecimalField(max_digits=3, decimal_places=0, default=0)
#	absolute_popularity = models.IntegerField(default=0)
#	relative_popularity = models.IntegerField
	def __unicode__(self):
		return self.tag_text + " [" + str(self.absolute_popularity) + "]"
	def save(self, *args, **kwargs):
		#import pdb
		#pdb.set_trace()
		#self.absolute_popularity = self.questions.count()
		super(Tag, self).save(*args, **kwargs)
		self.absolute_popularity = self.questions.count()
		super(Tag, self).save(*args, **kwargs)
#	def update_popularity(self):
#		scale_step=0
#		for tag in Tag.objects.all():
#			scale_step = max(scale_step,tag.questions.all().count())
#		scale_step= scale_step / 5.0
#		for tag in Tag.objects.all():
#			tag.relative_popularity = int(result[tag] / scale_step)
#		return result
		

