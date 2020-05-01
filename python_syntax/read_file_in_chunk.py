def read_in_chunks(file_object, chunk_size=100):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

with open('/home/dhanesh/Documents/apache_spark/taxi.csv') as f:
    for piece in read_in_chunks(f):
        # print(len(piece))
        print(piece)


# f = open('/home/dhanesh/Documents/apache_spark/taxi.csv')
# def read1k():
#     return f.read(100)
#
# for piece in iter(read1k, ''):
#     # print(len(piece))
#     print(piece)