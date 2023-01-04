import datetime

from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
#from django.utils.translation import ugettext_lazy as _

class RenewBookForm(forms.Form):
  renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

  def clean_renewal_date(self):
    data = self.cleaned_data['renewal_date']

    # Vérifier que la date ne se situe pas dans le passé.
    if data < datetime.date.today():
      raise ValidationError(_('Invalid date - renewal in past'))

      # Vérifier que la date tombe dans le bon intervalle (entre maintenant et dans 4 semaines).
    if data > datetime.date.today() + datetime.timedelta(weeks=4):
      raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

    # N'oubliez pas de toujours renvoyer les données nettoyées.
    return data
