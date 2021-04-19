import django_filters
from django.forms.widgets import TextInput
from django_filters import CharFilter, ChoiceFilter
from search.models import Announcement


MODE = (
        ('kunlik ijara', "kunlik ijara"),
        ('oylik ijara', "oylik ijara"),
        ('yillik ijara', "yillik ijara"),
    )
KIMLAR = (
        ("erkak", "erkak"),
        ("ayol", "ayol"),
        ("oila", "oila"),
    )


# */****************************************
KISHI_SONI = (
        ('1 kishilik', "1 kishilik"),
        ('2 kishilik', "2 kishilik"),
        ('3 kishilik', "3 kishilik"),
        ('4 kishilik', "4 kishilik"),
        ('5 kishilik', "5 kishilik"),
        ('6 kishilik', "6 kishilik"),
        ('7 kishilik', "7 kishilik"),
        ('oilalilar', "oilalilar"),
    )
TOPSHIRILGAN = (
        ("uy bo'sh", "uy bo'sh"),
        ("uy band", "uy band"),
    )

MONEYC = (
        ('USD', "USD"),
        ('RUB', "RUB"),
        ("UZS", "UZS"),
    )

SOVUQ_SUV = (
        ('sovuq suv bor KT.bilan', "sovuq suv bor KT.bilan"),
        ('sovuq suv bor KT.tashqari', "sovuq suv bor KT.tashqari"),
        ('sovuq suv yoq', "sovuq suv yoq"),
    )
ISSIQ_SUV = (
        ('issiq suv bor KT.bilan', "issiq suv bor KT.bilan"),
        ('issiq suv bor KT.tashqari', "issiq suv bor KT.tashqari"),
        ('issiq suv yoq', "issiq suv yoq"),
    )
SVET = (
        ('svet bor KT.bilan', "svet bor KT.bilan"),
        ('svet bor KT.tashqari', "svet bor KT.tashqari"),
        ('svet yoq', "svet yoq"),
    )
GAZ = (
        ('gaz bor KT.bilan', "gaz bor KT.bilan"),
        ('gaz bor KT.tashqari', "gaz bor KT.tashqari"),
        ('gaz yoq', "gaz yoq"),
    )
WIFI = (
        ('wifi bor KT.bilan', "wifi bor KT.bilan"),
        ('wifi bor KT.tashqari', "wifi bor KT.tashqari"),
        ('wifi yoq', "wifi yoq"),
    )
SOVUTGICH = (
        ('sovutgich bor KT.bilan', "sovutgich bor KT.bilan"),
        ('sovutgich bor KT.tashqari', "sovutgich bor KT.tashqari"),
        ('sovutgich yoq', "sovutgich yoq"),
    )
KONDISIONER = (
        ('kondisioner bor KT.bilan', "kondisioner bor KT.bilan"),
        ('kondisioner bor KT.tashqari', "kondisioner bor KT.tashqari"),
        ('kondisioner yoq', "kondisioner yoq"),
    )
HAMMOM = (
        ('hammom bor KT.bilan', "hammom bor KT.bilan"),
        ("hammom bor KT.tashqari", "hammom bor KT.tashqari"),
        ("hammom yo'q", "hammom yo'q"),
    )
XAVSIZ = (
        ('xavsizlik E.tizimi bor', "xavsizlik E.tizimi bor"),
        ("xavsizlik E.tizimi yo'q", "xavsizlik E.tizimi yo'q"),
    )

REGIONN = (
        ("Samarqand shahri", "Samarqand shahri"),
        ("Samarqand tumani", "Samarqand tumani"),
        ("Toyloq tumani", "Toyloq tumani"),        
        ("Bulungʻur tumani", "Bulungʻur tumani"),
        ("Jomboy tumani", "Jomboy tumani"),
        ("Urgut tumani", "Urgut tumani"),        
        ("Pastdargʻom tumani", "Pastdargʻom tuman"),
        ("Payariq tumani", "Payariq tumani"),
        ("Oqdaryo tumani", "Oqdaryo tumani"),        
        ("Ishtixon tumani", "Ishtixon tumani"),
        ("Qoʻshrabot tumani", "Qoʻshrabot tumani"),
        ("Kattaqoʻrgʻon tumani", "Kattaqoʻrgʻon tumani"),        
        ("Nurobod tumani", "Nurobod tumani"),
        ("Narpay tumani", "Narpay tumani"),
        ("Paxtachi tumani", "Paxtachi tumani"),
    )

class AnnouncementFilter(django_filters.FilterSet):
    region = ChoiceFilter(choices=REGIONN)
    address = CharFilter(field_name='address', lookup_expr='icontains', widget=TextInput(attrs={'placeholder': "Mahalla, yoki Ko'cha manzilini kiriting"}))
    mode = ChoiceFilter(choices=MODE)
    kimlar = ChoiceFilter(choices=KIMLAR)
    # ****************************************
    kishilar = ChoiceFilter(choices=KISHI_SONI)
    topshirilgan = ChoiceFilter(choices=TOPSHIRILGAN)
    moneyc = ChoiceFilter(choices=MONEYC)
    money = CharFilter(field_name='money', lookup_expr='icontains')
    sovuq_suv = ChoiceFilter(choices=SOVUQ_SUV)
    issiq_suv = ChoiceFilter(choices=ISSIQ_SUV)
    svet = ChoiceFilter(choices=SVET)
    gaz = ChoiceFilter(choices=GAZ)
    wifi = ChoiceFilter(choices=WIFI)
    sovutgich = ChoiceFilter(choices=SOVUTGICH)
    kondisioner = ChoiceFilter(choices=KONDISIONER)
    hammom = ChoiceFilter(choices=HAMMOM)
    xafsiz = ChoiceFilter(choices=XAVSIZ)



    class Meta:
        model = Announcement
        fields = ['region','address','mode','kimlar', 

		'kishilar', 'topshirilgan', 'moneyc', 
		'money', 'sovuq_suv', 'issiq_suv', 'svet',
		'gaz','wifi','sovutgich','kondisioner',
		'hammom','xafsiz']
























