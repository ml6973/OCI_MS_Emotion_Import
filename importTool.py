import configuration.globalVars as globalVars
import json
import MySQLdb
import os
import requests

def importToDB(data, fileName):
   globalVars.init()
   my_headers = {"Content-Type": 'application/octet-stream', "Ocp-Apim-Subscription-Key": globalVars.subKey}
   r = requests.post(globalVars.url, data=data, headers=my_headers)
   json_results = r.json()
   conn = MySQLdb.connect(host=globalVars.dbIP,
                        user=globalVars.dbUser,
                        passwd=globalVars.dbPass,
                        db="oci_emotions")
   x = conn.cursor()

   try:
      if not json_results:
         x.execute("""INSERT INTO ImageCatalog (frameNumber, numFace, sadness, neutral, 
                                                contempt, disgust, anger, 
                                                surprise, fear, happiness) 
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                  (fileName, 0, 0, 0, 0, 0, 0, 0, 0, 0)) 

      else:
         x.execute("""INSERT INTO ImageCatalog (frameNumber, numFace, sadness, neutral, 
                                                contempt, disgust, anger, 
                                                surprise, fear, happiness) 
                      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                  (fileName, "1", json_results[0]['scores']['sadness'], json_results[0]['scores']['neutral'], 
                  json_results[0]['scores']['contempt'], json_results[0]['scores']['disgust'], 
                  json_results[0]['scores']['anger'], json_results[0]['scores']['surprise'], 
                  json_results[0]['scores']['fear'], json_results[0]['scores']['happiness']))
      conn.commit()
   except MySQLdb.Error as e:
      conn.rollback()
      print e

   conn.close()
