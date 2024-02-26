from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from tinymce.models import HTMLField


class Information(models.Model):
    name = models.CharField(_("name"), max_length=100, db_index=True)
    description = HTMLField(_("description"), max_length=10000, null=True, blank=True)
    owner = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE, 
        verbose_name=_("owner"), 
        related_name='information', 
    )
    
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True, db_index=True)
    youtube_video = models.CharField(_('Youtube video'), max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = _("information")
        verbose_name_plural = _("information")
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("information_detail", kwargs={"pk": self.pk})



class InformationLike(models.Model):
    information = models.ForeignKey(
        Information, 
        verbose_name=_("information"), 
        on_delete=models.CASCADE,
        related_name='likes',
    )
    user = models.ForeignKey(
        get_user_model(), 
        verbose_name=_("user"), 
        on_delete=models.CASCADE,
        related_name='information_likes',
    )
    
    class Meta:
        verbose_name = _("information like")
        verbose_name_plural = _("information likes")

    def __str__(self):
        return f"{self.information} {self.user}"

    def get_absolute_url(self):
        return reverse("information_like_detail", kwargs={"pk": self.pk})
