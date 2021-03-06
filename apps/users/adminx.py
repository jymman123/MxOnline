import xadmin

from xadmin  import views
from .models import EmailVerifyRecord,Banner

class BaseSetting(object):
    enable_themes= True
    use_bootswatch=True

class GlobalSettings(object):
    site_title ='后台管理界面'
    site_footer = '江永明'
    menu_style = 'accordion'

class EmailVerifuRecordAdmin(object):
    list_display=['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter=['code','email','send_type','send_time']

class BannerAdmin(object):
    list_display = ['title','image','url','index','add_time']
    search_fields = ['title','image','url','index']
    list_filter = ['title','image','url','index','add_time']

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(EmailVerifyRecord,EmailVerifuRecordAdmin)
xadmin.site.register(views.CommAdminView,GlobalSettings)