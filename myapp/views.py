from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages
import logging
#แปลงไฟล์ fit ให้เป็นรูปภาพ
from fitparse import FitFile
import matplotlib.pyplot as plt
from astropy.io import fits
import io
import os


# Create your views here.

# def index(request):
#     name = "Noonziee"
#     age = 23
#     return render(request, "index.html" ,{"fname": name,"age":age})

def index(request):
    # all_person = Person.objects.filter(age=23) #fitter ได้ว่าต้องการให้แสดงผลแบบไหน
    all_person = Person.objects.all()
    return render(request, "index.html",{"all_person": all_person}) #โยนค่าเข้าไปเป็น dictionary

def satellite(request):
    return render(request, "satellite.html")


def planets(request):
    return render(request, "planets.html")

def about(request):
    return render(request, "about.html")


def form(request):
    if request.method == "POST":
        # รับข้อมูล
        name = request.POST["name"]
        age = request.POST["age"]
        # บันทึกข้อมูล
        person = Person.objects.create(
            name = name,
            age = age
        )
        #เปลี่ยนเส้นทาง
        person.save()
        messages.success(request,"saved successfully!")
        # print(name, age)
        # บันทึกข้อมูล
        return redirect("/index/")
    else :
        return render(request, "form.html")
    
def edit(request,person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()
        messages.success(request, "Update successfully!")
        return redirect("/index/")

    else:
        #ดึงข้อมูลประชากรที่ต้องการแก้ไข
        person = Person.objects.get(id=person_id)
        return render(request,"edit.html",{"person":person})

def delete(request,person_id):
    person=Person.objects.get(id=person_id)
    person.delete()
    messages.success(request,"deleted success")
    return redirect("/index/")


def leo(request):
    options = [
        {'name': '21/01/2025', 'url': 'leo21/'},  # ลิงก์สำหรับ 21/02/68
        {'name': '22/01/2025', 'url': 'leo22/'}  # ลิงก์สำหรับ 22/02/68
    ]

    selected_option = request.GET.get('option', None)  # รับค่าที่เลือก

    return render(request, 'leo.html', {'options': options, 'selected_option': selected_option})


def leo21(request):
    options = [
        {'name': 'COSMOS', 'url': 'cosmos21/'},
        {'name': 'IRIDIUM128', 'url': 'iridium128/'},
        {'name': 'LUMELITE-4', 'url': 'o3b/'},
        {'name': 'O3B', 'url': 'o3b/'},
        {'name': 'POPACS3', 'url': 'o3b/'},
        {'name': 'PROX_1', 'url': 'o3b/'}
    ]

    selected_option = request.GET.get('option', None)  # รับค่าที่เลือก

    return render(request, 'leo21.html', {'options': options, 'selected_option': selected_option})

def leo22(request):
    options = [
        {'name': 'COSMOS', 'url': 'cosmos22/'},  
        {'name': 'O3B', 'url': 'o3b/'}
        # {'name': 'IRIDIUM', 'url': 'IRIDIUM/'}  
    ]

    selected_option = request.GET.get('option', None)  # รับค่าที่เลือก

    return render(request, 'leo22.html', {'options': options, 'selected_option': selected_option})


def meo(request):
    options = ['Option 1', 'Option 2', 'Option 3']
    selected_option = request.GET.get('option')  # ใช้ GET ใน views.py
    return render(request, 'meo.html', {'options': options, 'selected_option': selected_option})


def geo(request):
    options = ['Option 1', 'Option 2', 'Option 3']
    selected_option = request.GET.get('option')  # ใช้ GET ใน views.py
    return render(request, 'geo.html', {'options': options, 'selected_option': selected_option})


def cosmos21(request):
    selected_option = request.GET.get('option', 'ไม่ได้เลือก')  # ดึงค่าจาก URL
    return render(request, 'cosmos21.html', {'selected_option': selected_option})


def cosmos22(request):
    selected_option = request.GET.get('option', 'ไม่ได้เลือก')  # ดึงค่าจาก URL
    return render(request, 'cosmos22.html', {'selected_option': selected_option})



def o3b(request):
    selected_option = request.GET.get('option', 'ไม่ได้เลือก')  # ดึงค่าจาก URL
    return render(request, 'o3b.html', {'selected_option': selected_option})


def iridium128(request):
    selected_option = request.GET.get('option', 'ไม่ได้เลือก')  # ดึงค่าจาก URL
    return render(request, 'iridium128.html', {'selected_option': selected_option})


def lumelite4(request):
    selected_option = request.GET.get('option', 'ไม่ได้เลือก')  # ดึงค่าจาก URL
    return render(request, 'lumelite4.html', {'selected_option': selected_option})


def oneweb(request):
    selected_option = request.GET.get('option', 'ไม่ได้เลือก')  # ดึงค่าจาก URL
    return render(request, 'oneweb.html', {'selected_option': selected_option})

def opt(request):
    selected_option = request.GET.get('option', 'ไม่ได้เลือก')  # ดึงค่าจาก URL
    return render(request, 'opt.html', {'selected_option': selected_option})


from django.shortcuts import render # type: ignore
from .models import sat_data
from django.db import connection # type: ignore

def sat_data(request):
    # เขียน SQL Query
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM sat_data")  # SQL Query ของคุณ
        rows = cursor.fetchall()  # ดึงข้อมูลทั้งหมดที่ได้จาก query

    # ส่งข้อมูลไปยัง template
    return render(request, 'satdata.html', {'sat_data': rows})



def tests(request):
    # เขียน SQL Query
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM sat_data")  # SQL Query ของคุณ
        rows = cursor.fetchall()  # ดึงข้อมูลทั้งหมดที่ได้จาก query

    # ส่งข้อมูลไปยัง template
    return render(request, 'tests.html', {'sat_data': rows})



def tests2(request):
    # เขียน SQL Query
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM sat_data")  # SQL Query ของคุณ
        rows = cursor.fetchall()  # ดึงข้อมูลทั้งหมดที่ได้จาก query

    # ส่งข้อมูลไปยัง template
    return render(request, 'tests2.html', {'sat_data': rows})


# import io
# import tempfile

# import healpy
# import ligo.skymap.bayestar as ligo_bayestar
# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
# import pysedm
# from astropy.io import fits
# from astropy.table import Table
# from astropy.visualization import ImageNormalize, ZScaleInterval
# from astropy.visualization.stretch import SinhStretch

# np.seterr(all="ignore")  # ignore numpy warnings from astropy normalization

# SKYMAP_ORDER = healpy.nside2order(512)



#fits display.py
# def get_fits_preview(
#     image_name,
#     image_data,
#     figsize=None,
#     output_format="png",
# ):
#     """
#     Return an image of fits data

#     Parameters
#     ----------
#     image_data : bytes
#         Bytes representation of the fits images
#     figsize : tuple, optional
#         Matplotlib figsize of the png created
#     output_format : str, optional
#         "pdf" or "png" -- determines the format of the returned plot
#     Returns
#     -------
#     data
#         Byte representation of the data for display

#     """

#     # first, get the file_type (fits or fits.fz)
#     file_type = image_name.split(".")[-1]
#     if file_type == "fz":
#         file_type = ".fits.fz"
#     else:
#         file_type = ".fits"

#     matplotlib.use("Agg")

#     # try reading the data as a sedm cube
#     try:
#         fig = plt.figure(
#             figsize=figsize if figsize else (8, 8), constrained_layout=False
#         )
#         with tempfile.NamedTemporaryFile(suffix=file_type, mode="wb", delete=True) as f:
#             f.write(image_data)
#             f.flush()
#             cube = pysedm.sedm.load_sedmcube(f.name)

#             with tempfile.NamedTemporaryFile(
#                 suffix=f".{output_format}", mode="wb", delete=True
#             ) as h:
#                 cube.show(savefile=h.name)
#                 h.flush()
#                 with open(h.name, mode="rb") as g:
#                     data = g.read()
#             return data
#     except Exception:
#         pass

#     # try reading the data as a fits image
#     try:
#         fig = plt.figure(
#             figsize=figsize if figsize else (8, 8), constrained_layout=False
#         )
#         with tempfile.NamedTemporaryFile(suffix=file_type, mode="wb", delete=True) as f:
#             f.write(image_data)
#             f.flush()
#             hdul = fits.open(f.name)
#             hdul_index = -1
#             for i, hdu in enumerate(hdul):
#                 if hdu.data is not None:
#                     hdul_index = i
#                     break
#             if hdul_index == -1:
#                 raise IndexError("No image data found in fits file")
#             image = hdul[hdul_index].data.astype(np.float32)

#             norm = ImageNormalize(
#                 image, interval=ZScaleInterval(), stretch=SinhStretch()
#             )
#             plt.imshow(image, cmap="gray", norm=norm, origin="lower")
#             plt.colorbar(fraction=0.046, pad=0.04)

#             buf = io.BytesIO()
#             fig.savefig(buf, format=output_format)
#             plt.close(fig)
#             buf.seek(0)
#             return buf.read()
#     except Exception:
#         pass

#     # try reading the data as a fits localization skymap
#     try:
#         fig = plt.figure(
#             figsize=figsize if figsize else (14, 8), constrained_layout=False
#         )
#         with tempfile.NamedTemporaryFile(suffix=file_type, mode="wb", delete=True) as f:
#             f.write(image_data)
#             f.flush()
#             hdul = fits.open(f.name)
#             # read the content of the skymap
#             skymap = hdul[1].data

#             # the skymap should contain at least 2 columns: UNIQ and PROBDENSITY
#             if not set(skymap.columns.names).issuperset({"UNIQ", "PROBDENSITY"}):
#                 raise ValueError("Invalid skymap format")

#             table_2d = Table(
#                 [
#                     np.asarray(skymap["UNIQ"], dtype=np.int64),
#                     np.asarray(skymap["PROBDENSITY"], dtype=np.float64),
#                 ],
#                 names=["UNIQ", "PROBDENSITY"],
#             )

#             prob = ligo_bayestar.rasterize(table_2d, SKYMAP_ORDER)["PROB"]
#             prob = healpy.reorder(prob, "NESTED", "RING")

#             ax = plt.axes([0.05, 0.05, 0.9, 0.9], projection="astro hours mollweide")

#             ax.grid()
#             ax.imshow_hpx(prob, cmap="cylon")

#             buf = io.BytesIO()
#             fig.savefig(buf, format=output_format)
#             plt.close(fig)
#             buf.seek(0)
#             return buf.read()
#     except Exception:
#         pass

#     raise ValueError("Could not read image data")










# import psycopg2
# from io import BytesIO
# import matplotlib.pyplot as plt
# from astropy.io import fits

# def fetch_fits_from_db(image_name):
#     # เชื่อมต่อกับฐานข้อมูล PostgreSQL
#     conn = psycopg2.connect(dbname="postgres", user="postgres", password="0527", host="localhost", port="5432")
#     cursor = conn.cursor()

#     # ดึงข้อมูลไฟล์ FITS จากฐานข้อมูล
#     cursor.execute("""
#         SELECT data FROM images WHERE name = %s
#     """, (image_name,))
#     image_data = cursor.fetchone()  # ดึงข้อมูลทีละแถว

#     if image_data is None:
#         print("ไม่พบข้อมูลภาพที่ต้องการ")
#         cursor.close()
#         conn.close()
#         return

#     # แปลงข้อมูลไบต์กลับเป็นไฟล์ FITS
#     image_data = image_data[0]  # เพราะ fetchone() จะคืนค่า tuple

#     # ใช้ astropy เพื่อเปิดไฟล์ FITS จากข้อมูลไบต์
#     hdul = fits.open(BytesIO(image_data))
    
#     # แสดงข้อมูลเกี่ยวกับ HDU (Header Data Unit)
#     hdul.info()

#     # แสดงภาพ
#     plt.imshow(hdul[0].data, cmap="gray", origin="lower")
#     plt.colorbar()
#     plt.show()

#     # ปิดการเชื่อมต่อ
#     cursor.close()
#     conn.close()

# # เรียกฟังก์ชันเพื่อดึงภาพ FITS จากฐานข้อมูลและแสดงผล
# fetch_fits_from_db("One_Web-0001_5s.fit")




# import psycopg2
# from io import BytesIO
# import matplotlib.pyplot as plt
# from astropy.io import fits
# from django.shortcuts import render
# from django.http import HttpResponse
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# def fetch_fits_from_db(image_name):
#     # เชื่อมต่อกับฐานข้อมูล PostgreSQL
#     conn = psycopg2.connect(dbname="postgres", user="postgres", password="0527", host="localhost", port="5432")
#     cursor = conn.cursor()

#     # ดึงข้อมูลไฟล์ FITS จากฐานข้อมูล
#     cursor.execute("""
#         SELECT data FROM images WHERE name = %s
#     """, (image_name,))
#     image_data = cursor.fetchone()  # ดึงข้อมูลทีละแถว

#     if image_data is None:
#         print("ไม่พบข้อมูลภาพที่ต้องการ")
#         cursor.close()
#         conn.close()
#         return None

#     # แปลงข้อมูลไบต์กลับเป็นไฟล์ FITS
#     image_data = image_data[0]  # เพราะ fetchone() จะคืนค่า tuple

#     # ใช้ astropy เพื่อเปิดไฟล์ FITS จากข้อมูลไบต์
#     hdul = fits.open(BytesIO(image_data))

#     # สร้างกราฟจากข้อมูล FITS
#     fig, ax = plt.subplots()
#     ax.imshow(hdul[0].data, cmap="gray", origin="lower")
#     ax.set_title(f"FITS Image: {image_name}")
#     fig.colorbar(ax.imshow(hdul[0].data))




# from flask import Flask, request, send_file
# import io
# from your_module import get_fits_preview  # สมมุติว่าฟังก์ชันของคุณอยู่ในไฟล์ชื่อ your_module.py

# app = Flask(__name__)

# @app.route('/get_fits_preview', methods=['POST'])
# def get_fits_preview_api():
#     # รับไฟล์ FITS จากการอัปโหลด
#     file = request.files['image']
#     image_data = file.read()  # อ่านข้อมูลจากไฟล์ FITS

#     try:
#         # เรียกฟังก์ชัน get_fits_preview
#         result_image = get_fits_preview("image.fits", image_data, output_format="png")

#         # ส่งข้อมูลภาพกลับไป
#         return send_file(io.BytesIO(result_image), mimetype='image/png')

#     except ValueError as e:
#         return str(e), 400

# if __name__ == '__main__':
#     app.run(debug=True)

