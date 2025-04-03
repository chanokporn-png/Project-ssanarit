# from django.urls import path
# from myapp import views

# urlpatterns = [
#     path('', views.index),  # หน้าหลัก
#     path('about/', views.about, name='about'),  # หน้าประวัติ
#     path('form', views.form),  # หน้าฟอร์ม
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index')  # กำหนด URL ที่หน้าแรก
# ]

# ข้างบนใช้ไม่ได้

from django.urls import path
from myapp import views  # นำเข้า views จากแอป myapp

urlpatterns = [
    path('planets/', views.planets),  # หน้าดาวเคราะห์
    path('', views.satellite),
    path('index/', views.index),  # หน้าhome
    path('about/', views.about),  # หน้าประวัติ
    path('form/', views.form),  # หน้าฟอร์ม
    path('index/edit/<person_id>/',views.edit),
    path('index/delete/<person_id>/',views.delete),
    path('leo/', views.leo),  # หน้า fitfile
    path('meo/', views.meo),  # หน้า fitfile
    path('geo/', views.geo),  # หน้า fitfile

    path('leo/leo21/', views.leo21, name='leo21'),  # หน้า fitfile
    path('leo/leo22/', views.leo22, name='leo22'),  # หน้า fitfile

    path('leo/leo21/cosmos21/', views.cosmos21, name='cosmos21'),  # หน้าแสดงผลหลังจากเลือก
    path('leo/leo21/iridium128/', views.iridium128, name='iridium128'),  # หน้าแสดงผลหลังจากเลือก
    path('leo/leo22/cosmos22/', views.cosmos22, name='cosmos22'),  # หน้าแสดงผลหลังจากเลือก
    path('leo/leo21/o3b/', views.o3b, name='o3b'),  # หน้าแสดงผลหลังจากเลือก
    # path('leo/leo21/IRIDIUM/', views.IRIDIUM, name='IRIDIUM')
    path('meo/oneweb/', views.oneweb, name='oneweb'),  # หน้าแสดงผลหลังจากเลือก
    path('geo/opt/', views.opt, name='opt'),  # หน้าแสดงผลหลังจากเลือก
    path('satdata/', views.sat_data),  
    path('tests/', views.tests),  # หน้าลอง tests
    path('tests2/', views.tests2),  # หน้าลอง tests2

    # path('fitfile/', views.fitfile)

]
