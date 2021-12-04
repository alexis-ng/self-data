# Import the required Module
import tabula
#file
filename = "Engineering Self Fellows.pdf"
# Read a PDF File
df = tabula.read_pdf(filename, pages='1')[0]
# convert PDF into CSV
# tabula.convert_into("Engineering Self Fellows.pdf", "alum_assoc_info.csv", output_format="csv", pages='all')
print(df)