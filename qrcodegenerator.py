import qrcode as qr

img = qr.make("https://github.com/unitiaathiras")
img.save("athira-github.png")