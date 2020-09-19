from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=False, null=False)
    location = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['-id']
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def get_author_location(self):
        return f"Location is {self.location}"


class Post(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="post_author")
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"


class Language(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    paradigm = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
