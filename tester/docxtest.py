import bs4
from docx import Document

document = Document()

soup = bs4.BeautifulSoup(open('test.html'), "html.parser")
soup1 = soup.find("table").get_text(separator='neko', strip=True)
soup2 = soup.find("table", {'class' : 'table-cetak'})
# soup2_part2 = bs4.BeautifulSoup(soup2, "html.parser")

# maping1 = soup1.replace("\n", "").replace(" ", "").replace("Tanggal:", "Tanggal : ").replace("Nama:", "\nNama : ").replace("Instansi:", "\nInstansi : ")
# maping2 = soup2

maping1 = soup1.split("neko")
# maping2 = soup2.split("neko")
print(soup2)


def merge(list1, list2, list3):    
    merged_list = [(list1[i], list2[i], list3[i]) for i in range(0, len(list1))]
    return merged_list

def maping(mapings):
    l = len(mapings)
    a, b, c = [], [], []
    for i in range(0, l, 3):
        a.append(mapings[i])
    for i in range(1, l, 3):
        b.append(mapings[i])
    for i in range(2, l, 3):
        c.append(mapings[i])

    return merge(a, b, c)

print(maping(maping1))