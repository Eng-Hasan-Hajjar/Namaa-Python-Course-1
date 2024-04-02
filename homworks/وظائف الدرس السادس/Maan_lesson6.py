
st = {'ismail': 0,"sedra":0,"maan":0,"jaber":0,"manaf":0,"abd alfatah":0,"hussam":0}
lesson= int(5)
def stars():
    st['ismail'] += 1
    st['sedra'] += 2
    st['maan'] += 4
    st['jaber'] += 1
    st['manaf'] += 3
    st['abd alfatah'] += 4
    st['hussam'] += 0
    print("Total",st)
def total():
    st['ismail'] += st['ismail']
    st['sedra'] += st['sedra']
    st['maan'] += st['maan']
    st['jaber'] += st['jaber']
    st['manaf'] += st['manaf']
    st['abd alfatah'] += st['abd alfatah']
    st['hussam'] += st['hussam']
if lesson > 0 :
    stars()
    total()



          
