from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField()
    
    def get_absolute_url(self):
        return reverse('organizer_tag_detail',kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('organizer_tag_update', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('organizer_tag_delete', kwargs={'slug' : self.slug})

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.title()

class Startup(models.Model):
    name = models.CharField(max_length=31, unique=True, db_index=True)
    slug = models.SlugField(max_length=31, unique=True, help_text='A label for URL config.')
    description = models.TextField()
    founded_date = models.DateField('date founded')
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag, blank=True)

    def get_absolute_url(self):
        return reverse('organizer_startup_detail',kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('organizer_startup_update', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('organizer_startup_delete', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'
    
    def __str__(self):
        return self.name


class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    pub_date = models.DateField('date published')
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(Startup)
    slug = models.SlugField(max_length = 63)

    def get_absolute_url(self):
        return self.startup.get_absolute_url()

    def get_update_url(self):
        return reverse('organizer_newslink_update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('organizer_newslink_delete', kwargs={'pk':self.pk})

    def __str__(self):
        return "{}:{}".format(self.startup, self.title)

    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'
        unique_together = (('slug', 'startup'),)
