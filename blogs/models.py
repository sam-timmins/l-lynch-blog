from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

from projects.models import Projects

class Blogs(models.Model):
    """ Blogs model """

    title = models.CharField(
        max_length=254,
        blank=False,
        null=False,
        unique=True,
    )

    date = models.DateTimeField(
        auto_now_add=True
        )

    project = models.ManyToManyField(
        'projects.Projects',
        blank=True,
    )

    content = RichTextField(
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True
    )

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
