DROP DATABASE if EXISTS oci_emotions;
CREATE DATABASE oci_emotions;
USE oci_emotions;

CREATE TABLE ImageCatalog (
  imageId   int(11) NOT NULL AUTO_INCREMENT UNIQUE,
  frameNumber     varchar(255) COLLATE utf8_unicode_ci,
  numFace         int(4),
  sadness         DECIMAL(65, 30),
  neutral         DECIMAL(65, 30),
  contempt        DECIMAL(65, 30),
  disgust         DECIMAL(65, 30),
  anger           DECIMAL(65, 30),
  surprise        DECIMAL(65, 30),
  fear            DECIMAL(65, 30),
  happiness       DECIMAL(65, 30)
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
