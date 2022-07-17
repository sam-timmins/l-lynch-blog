from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

class Projects(models.Model):
    """ Projects model """

    name = models.CharField(
        max_length=254,
        blank=False,
        null=False,
        unique=True,
    )

    description = RichTextField(
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True
    )

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
