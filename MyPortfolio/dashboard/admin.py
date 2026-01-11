from django.contrib import admin
from dashboard.models import Hero
from dashboard.models import About_Me
from dashboard.models import Services
from dashboard.models import Education
from dashboard.models import lenguage
from dashboard.models import project
from dashboard.models import testimonial
from dashboard.models import touch
class hero(admin.ModelAdmin):
    list_display = ['smHead','Head','Head_img','Head_Desc','Head_link1','Head_link2','Head_link3','Head_link4','Head_link5','Mail']
    
class Abt(admin.ModelAdmin):
    list_display=['about_head','about_text','about_img']

class Serv(admin.ModelAdmin):
    list_display=['Card_img','Card_hd']

class Educ(admin.ModelAdmin):
    list_display=['Course','Department','Year']

class leng(admin.ModelAdmin):
    list_display=['language_img']

class proj(admin.ModelAdmin):
    list_display=['pro_img','pro_detail','pro_link']

class testim(admin.ModelAdmin):
    list_display=['test_img','test_text']

class tch(admin.ModelAdmin):
    list_display=['t_email','t_cnt','t_loc']


# Register your models here.
admin.site.register(Hero,hero)
admin.site.register(About_Me,Abt)
admin.site.register(Services,Serv)
admin.site.register(Education,Educ)
admin.site.register(lenguage,leng)
admin.site.register(project,proj)
admin.site.register(testimonial,testim)
admin.site.register(touch,tch)