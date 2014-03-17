import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

with open("blog.avsc") as schema_file:
    schema = avro.schema.parse(schema_file.read())

with open("blog.avro", "wb") as out_file:
    writer = DataFileWriter(out_file, DatumWriter(), schema)
    writer.append({
        "title": "Avro is awesome",
        "content": "Let's learn Avro!",
        "is_published": False })
    writer.close()

with open("blog.avro") as in_file:
    reader = DataFileReader(in_file, DatumReader())
    for blog in reader:
        print blog
    reader.close()
