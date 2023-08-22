from django.db import models

class VisualData(models.Model):
    end_year = models.PositiveIntegerField(null=True, blank=True)
    intensity = models.CharField(max_length=100, null=True, blank=True)
    sector = models.CharField(max_length=100, null=True, blank=True)
    topic = models.CharField(max_length=100, null=True, blank=True)
    insight = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    start_year = models.PositiveIntegerField(null=True, blank=True)
    impact = models.CharField(max_length=100,null=True, blank=True)
    added = models.DateTimeField(null=True, blank=True)
    published = models.DateTimeField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    relevance = models.CharField(max_length=100, null=True, blank=True)
    pestle = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    likelihood = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.insight or f"VisualData object {self.pk}"
