from app.reader import read_file


dataset = read_file("../../resource/history.data")
print("sharp = {}".format(dataset.shape))
print(dataset.head(50))


