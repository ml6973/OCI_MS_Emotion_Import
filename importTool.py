import configuration.globalVars as globalVars
import json
import MySQLdb
import os
import requests
import time

def importToDB(data, fileName):
   globalVars.init()
   my_headers = {"Content-Type": 'application/octet-stream', "Ocp-Apim-Subscription-Key": globalVars.subKey}
   r = requests.post(globalVars.url, data=data, headers=my_headers)
   while r.status_code == requests.codes.too_many:
      data.seek(0)
      time.sleep(60)
      r = requests.post(globalVars.url, data=data, headers=my_headers)
   if not r.status_code == requests.codes.ok:
      print "API Request Error"
      print r
      print r.text
      return
   json_results = r.json()
   conn = MySQLdb.connect(host=globalVars.dbIP,
                        user=globalVars.dbUser,
                        passwd=globalVars.dbPass,
                        db="oci_emotions")
   x = conn.cursor()

   try:
      FrameNumber = os.path.splitext(os.path.basename(data.name))[0]
      if not json_results:
         x.execute("""INSERT INTO ImageCatalog (VideoName, FrameNumber, NumFace, SadnessProbability, 
                                                   NeutralProbability, ContemptProbability, 
                                                   DisgustProbability, AngerProbability, 
                                                   SurpriseProbability, FearProbability, 
                                                   HappinessProbability, RectangleLeft,
                                                   RectangleTop, RectangleWidth, RectangleHeight) 
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                     (fileName, FrameNumber, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

      else:
         NumFace = len(json_results)
         for face in json_results:
            x.execute("""INSERT INTO ImageCatalog (VideoName, FrameNumber, NumFace, SadnessProbability, 
                                                   NeutralProbability, ContemptProbability, 
                                                   DisgustProbability, AngerProbability, 
                                                   SurpriseProbability, FearProbability, 
                                                   HappinessProbability, RectangleLeft,
                                                   RectangleTop, RectangleWidth, RectangleHeight) 
                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                     (fileName, FrameNumber, NumFace, face['scores']['sadness'], face['scores']['neutral'], 
                     face['scores']['contempt'], face['scores']['disgust'], 
                     face['scores']['anger'], face['scores']['surprise'], 
                     face['scores']['fear'], face['scores']['happiness'], face['faceRectangle']['left'],
                     face['faceRectangle']['top'], face['faceRectangle']['width'],
                     face['faceRectangle']['height']))
      conn.commit()
   except MySQLdb.Error as e:
      conn.rollback()
      print e

   conn.close()
