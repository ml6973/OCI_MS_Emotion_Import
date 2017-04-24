from OCI_MS_Emotion_Import import importTool

picture = open("pathToFile", "rb")

try:
   importTool.importYouTubeVideoMetaData("nameOfFile", "YouTubeURL")
except ValueError:
   print "nameOfFile already exists in database"

try:
   importTool.importEmotionToDB(picture, "nameOfFile")
except ValueError:
   print "nameOfFile already exists in database"
