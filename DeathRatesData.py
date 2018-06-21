import PyPDF2
import csv

########################################################################
#
#  Code for scrapping the data from 'PRmort2.pdf'. The data extraction
#  is not perfect regarding the name of the columns, because of the 
#  format, and the non-ascii characters (characters from Spanish).
#
########################################################################



# Opening the file PRmort2.pdf and extracting data from each page
file = open("PRmort2.pdf", 'rb')
pdfreader = PyPDF2.PdfFileReader(file)
text0 = pdfreader.getPage(0).extractText() # Monthly death per gender
text1 = pdfreader.getPage(1).extractText() # Monthly death per ages
text2 = pdfreader.getPage(2).extractText() # Monthly death per places
text3 = pdfreader.getPage(3).extractText() # Monthly death by cause (part 1)
text4 = pdfreader.getPage(4).extractText() # Monthly death by cause (part 2)
text5 = pdfreader.getPage(5).extractText() # Monthly death by cause (part 3)


# Scrapping Gender death count table (Page 1) 
newFile = open("data.txt", 'w')
newFile.write(text0.encode('ascii', 'ignore'))
newFile.close()

lines = []
with open('data.txt', 'r') as in_file:
    ctr = 0
    chunks = []
    for w in in_file:
        ctr = ctr+1
        line = w.strip('\n')
        if (line == "Fuente:  Registro Demogrfico y Estadsticas Vitales, Departamento de Salud"):
            break
        line = line.replace(',', '')
        chunks.append(line)
        if (ctr==4):
            lines.append(chunks)
            chunks = []
            ctr = 0

with open('GenderDeathCount.csv', 'w') as out_file:
    writer = csv.writer(out_file)
    writer.writerows(lines)



# Scrapping Ages Death Count Table (Page 2) 
newFile = open("data.txt", 'w')
newFile.write(text1.encode('ascii', 'ignore'))
newFile.close()

lines  = []
with open('data.txt', 'r') as in_file:
    ctr = 0
    chunks = []
    for w in in_file:
        ctr = ctr+1
        line = w.strip('\n')
        if (line == "Fuente:  Registro Demogrfico y Estadsticas Vitales, Departamento de Salud"):
            break
        if(line == "ms "):
            ctr = ctr-1
            continue
        line = line.replace(',', '')
        chunks.append(line)
        if (ctr==11):
            lines.append(chunks)
            chunks = []
            ctr = 0

with open('AgesDeathCount.csv', 'w') as out_file:
    writer = csv.writer(out_file)
    writer.writerows(lines)



# Scrapping Places Death Count Table (Page 3) 
newFile = open("data.txt", 'w')
newFile.write(text2.encode('ascii', 'ignore'))
newFile.close()

with open('data.txt', 'r') as in_file:
    ctr = 0
    stop_ctr = 0
    chunks = []
    lines = []
    for w in in_file:
        if (stop_ctr < 13): # Ignoring the column names. They screw up the format!
            stop_ctr += 1
            continue
        ctr = ctr+1
        line = w.strip('\n')
        if (line == "Fuente:  Registro Demogrfico y Estadsticas Vitales, Departamento de Salud"):
            break
        line = line.replace(',', '')
        chunks.append(line)
        if (ctr==8): # number of columns
            lines.append(chunks)
            chunks = []
            ctr = 0

with open('PlacesDeathCount.csv', 'w') as out_file:
    writer = csv.writer(out_file)
    writer.writerows(lines)



# Scrapping Monthly Death Causes Count Table (Page 4-6)
lines = []

# Page 4
newFile = open("data.txt", 'w')
newFile.write(text3.encode('ascii', 'ignore'))
newFile.close()

with open('data.txt', 'r') as in_file:
    ctr = 0
    chunks = []
    s = ""
    for w in in_file:
        if (w[len(w)-2] == ' '):
            s += w.strip('\n')
            continue
        if (s != ""):
            w = s+w
            s = ""
        ctr = ctr+1
        line = w.strip('\n')
        if (line == "Fuente:  Registro Demogrfico y Estadsticas Vitales, Departamento de Salud"):
            break
        line = line.replace(',', '')
        chunks.append(line)
        if (ctr==14): # number of columns
            lines.append(chunks)
            chunks = []
            ctr = 0

# Page 5
newFile = open("data.txt", 'w')
newFile.write(text4.encode('ascii', 'ignore'))
newFile.close()

with open('data.txt', 'r') as in_file:
    ctr = 0
    stop_ctr = 0
    chunks = []
    for w in in_file:
        if (stop_ctr < 16): # Ignoring the column names (we already have them)
            stop_ctr += 1
            continue
        if (w[len(w)-2] == ' ' or w[len(w)-2] == '-'):
            s += w.strip('\n')
            continue
        if (s != ""):
            w = s+w
            s = ""
        ctr = ctr+1
        line = w.strip('\n')
        if (line == "Fuente:  Registro Demogrfico y Estadsticas Vitales, Departamento de Salud"):
            break
        line = line.replace(',', '')
        chunks.append(line)
        if (ctr==14): # number of columns
            lines.append(chunks)
            chunks = []
            ctr = 0

# Page 6
newFile = open("data.txt", 'w')
newFile.write(text5.encode('ascii', 'ignore'))
newFile.close()

with open('data.txt', 'r') as in_file:
    ctr = 0
    stop_ctr = 0
    chunks = []
    for w in in_file:
        if (stop_ctr < 16): # Ignoring the column names (we already have them)
            stop_ctr += 1
            continue
        if (w[len(w)-2] == ' ' or w[len(w)-2] == '-'):
            s += w.strip('\n')
            continue
        if (s != ""):
            w = s+w
            s = ""
        ctr = ctr+1
        line = w.strip('\n')
        if (line == "Fuente:  Registro Demogrfico y Estadsticas Vitales, Departamento de Salud"):
            break
        line = line.replace(',', '')
        chunks.append(line)
        if (ctr==14): # number of columns
            lines.append(chunks)
            chunks = []
            ctr = 0


with open('CausesDeathCount.csv', 'w') as out_file:
    writer = csv.writer(out_file)
    writer.writerows(lines)

file.close()

