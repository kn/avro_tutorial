# Avro Tutorial

## Install Avro

1. Download avro tar ball for python from stable [avro release](http://avro.apache.org/releases.html) (1.7.6 was used with this example)
2. Unzip the the downloaded package.
3. Run: `sudo python setup.py install`

## Defining Schema

Avro schema is defined using JSON. e.g.:

```
{
  "namespace": "blog.avro",
  "type": "record",
  "name": "Blog",
  "fields": [
    { "name": "title", "type": "string" },
    { "name": "content", "type": "string" },
    { "name": "is_published", "type": "boolean", "default": false }
  ]
}
```

## Serializing

```
import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

with open("blog.avsc") as schema_file:
    schema = avro.schema.parse(schema_file.read())

with open("blog.avro", "wb") as out_file:
    writer = DataFileWriter(out_file, DatumWriter(), schema)
    writer.append({
        "title": "Avro is awesome",
        "content": "Let's learn Avro!",
        "is_published": False })
    writer.close()
```

## Deserializing

```
import avro.schema
from avro.datafile import DataFileReader
from avro.io import DatumReader

with open("blog.avsc") as schema_file:
    schema = avro.schema.parse(schema_file.read())

with open("blog.avro") as in_file:
    reader = DataFileReader(in_file, DatumReader())
    for blog in reader:
        print blog
    reader.close()
```

## MapReduce with Avro
