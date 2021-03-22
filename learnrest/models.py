from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


class Snippet(models.Model):
    LANGUAGE_CHOICES = (
        ('C', 'C'),
        ('C++', 'C++'),
        ('Java', 'Java'),
        ('Python', 'Python'),
    )
    owner = models.ForeignKey('auth.user', related_name='snippets', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    highlight = models.TextField(null=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)


class JobPositions(models.Model):
    position = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    experience_req = models.IntegerField(default='0')

    def __str__(self):
        return self.position


class JobApplication(models.Model):
    name = models.CharField(max_length=100, null=True)
    resume = models.FileField()
    mobile = models.CharField(null=True, max_length=100)
    email = models.EmailField(max_length=100, null=True)
    job_position = models.ForeignKey(JobPositions, on_delete=models.CASCADE, null=True)
    recent_education = models.CharField(max_length=100, null=True)
    last_exp = models.IntegerField(null=True)

    def __str__(self):
        return self.name