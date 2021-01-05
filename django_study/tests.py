from django.test import TestCase
from django_study.models import Kimetsu

# Create your tests here.



k = Kimetsu(name="なまえ", sex="男", feature="とくちょう")
k.save()
Kimetsu.objects.all()
