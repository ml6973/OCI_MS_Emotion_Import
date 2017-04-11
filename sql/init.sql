DROP DATABASE if EXISTS oci_emotions;
CREATE DATABASE oci_emotions;
USE oci_emotions;

CREATE TABLE ImageCatalog (
  ImageId                      int(11) NOT NULL AUTO_INCREMENT UNIQUE,
  VideoName                    varchar(255) COLLATE utf8_unicode_ci,
  FrameNumber                  int(11),
  NumFace                      int(4),
  SadnessProbability           DECIMAL(65, 30),
  NeutralProbability           DECIMAL(65, 30),
  ContemptProbability          DECIMAL(65, 30),
  DisgustProbability           DECIMAL(65, 30),
  AngerProbability             DECIMAL(65, 30),
  SurpriseProbability          DECIMAL(65, 30),
  FearProbability              DECIMAL(65, 30),
  HappinessProbability         DECIMAL(65, 30),
  RectangleLeft                int(11),
  RectangleTop                 int(11),
  RectangleWidth               int(11),
  RectangleHeight              int(11)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
