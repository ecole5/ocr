from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import re
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

#OCR handwritten form
print(pytesseract.image_to_string(Image.open('Samples/HealthForm.png')))


#typed form extraction--------------


#Convert pdf to image first
# Path to the PDF file
pdf_path = "Samples/employment2.pdf"

# Convert PDF to images
images = convert_from_path(pdf_path, dpi=600)

# Save each page as an image
for i, image in enumerate(images):
    image.save(f"page_{i+1}.png", "PNG")
    
    
#OCR from image
text = pytesseract.image_to_string(Image.open('page_1.png'))
print(text)

# Regular expressions to extract relevant information
name_pattern = re.search(r"First Name:\s*([A-Za-z]+)\s*Last Name:\s*([A-Za-z]+)", text)
address_pattern = re.search(r"Address:\s*([^\n]+)", text)  # Captures only the address line
activities_section = re.search(r"What civic or athletic activities are you involved in\?\n(.*?)(?:\n\n|$)", text, re.DOTALL)

activities = []
if activities_section:
    activities = [activity.strip() for activity in activities_section.group(1).split("\n") if activity.strip()]
    
    
first_name = name_pattern.group(1) if name_pattern else None
last_name = name_pattern.group(2) if name_pattern else None
address = address_pattern.group(1).strip() if address_pattern else None
activities_str = ", ".join(activities) if activities else None

# Define schema for Iceberg table
schema = StructType([
    StructField("first_name", StringType(), True),
    StructField("last_name", StringType(), True),
    StructField("address", StringType(), True),
    StructField("athletic_activities", StringType(), True)
])


###--------Use your own connection snippet
# create spark connection
import cml.data_v1 as cmldata

CONNECTION_NAME = "ecoleocr-aw-dl"
conn = cmldata.get_connection(CONNECTION_NAME)
spark = conn.get_spark_session()
####----------

# Sample usage to run query through spark
EXAMPLE_SQL_QUERY = "show tables"
spark.sql(EXAMPLE_SQL_QUERY).show()

# Create DataFrame with extracted data
data = [(first_name, last_name, address,  activities_str)]
df = spark.createDataFrame(data, schema=schema)

# Define Iceberg table name
iceberg_table = "default.test1"

# Append data to the Iceberg table if it exists or create a new one if it does not
try:
    df.write.format("iceberg").mode("append").save(iceberg_table)
    print(f"Data successfully appended to Iceberg table: {iceberg_table}")
except Exception as e:
  spark.sql(f"""
    CREATE TABLE IF NOT EXISTS {iceberg_table} (
            first_name STRING,
            last_name STRING,
            address STRING,
            athletic_activities STRING
        ) USING iceberg
    """)
  df.write.format("iceberg").mode("append").save(iceberg_table)
  print("Created new table because it didn't exist")