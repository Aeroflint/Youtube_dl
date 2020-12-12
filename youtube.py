import pafy

url = input("Введите ссылку для скачивания файла: ")
video = pafy.new(url)

streams = video.streams
for i in streams:
    print(i)

best = video.getbest()
best.resolution, best.extension

file = best.download(filepath="D:\\")

input("Нажмите enter")