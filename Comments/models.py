from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings

class CommentManager(models.Manager):
	def filter_by_instance(self, instance):
		content_type = ContentType.objects.get_for_model(instance.__class__)
		qs = super().filter(content_type=content_type,
							object_id=instance.id)
		qs = qs.order_by("-timestamp")
		return qs



class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
							 on_delete=models.DO_NOTHING)
	content_type = models.ForeignKey(ContentType,
									 on_delete=models.CASCADE)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type',
									   'object_id')

	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	objects = CommentManager() 

	def __str__(self):
		return self.content


