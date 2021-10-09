import qrcode
from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

from dordoy.settings import ALLOWED_HOSTS


class QRcode(models.Model):
    name = models.CharField(default='http://localhost:8000/' + '/watch-video/', max_length=90)
    qr_code = models.ImageField(upload_to='qrcodes', blank=True)

    def __str__(self):
        return str(self.qr_code.url)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.name)
        canvas = Image.new('RGB', (350, 350), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
