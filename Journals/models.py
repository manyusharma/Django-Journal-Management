from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.conf import settings
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType

class Journal(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
							 default=1,
							 on_delete=models.DO_NOTHING)
	title = models.CharField(max_length=50)
	detail = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField(unique=True, max_length=50,
							default="")
	image = models.ImageField(null=True,
							  blank=True)

	publish = models.DateField(default=timezone.now)

	@property 
	def get_content_type(self):
		content_type = ContentType.objects.get_for_model(self.__class__)
		return content_type

	def get_absolute_url_id(self):
		return reverse("Journals:by_id", kwargs={'id': self.id})

	def get_absolute_url(self):
		return reverse("Journals:by_slug", kwargs={'inp_slug': self.slug})

	def __str__(self):
		return "{}".format(self.title)

		
def generate_slug(sender, instance, *args, **kwargs):
	instance.slug = slugify(instance.title)

	return instance.slug 

pre_save.connect(generate_slug, sender=Journal)