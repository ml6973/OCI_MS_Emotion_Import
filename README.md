# OCI MS Emotion API Import Tool
Contains the Python library for storing results from the MS Emotion API into a MySQL database.

## Configuration

The configuration file "config.txt" must be created in the configuration directory.  Below is the format:

```
[GlobalInformation]
url = The Request URL for the MS Emotion Recognition API
subKey = The subscription key for the MS Emotion Recognition API
dbIP = The IP Address for the MySQL database the results will be stored
dbUser = User credential for the above database
dbPass = Password credential for the above database
```

## Usage
Ensure the object you are passing is a "file-like" class.
The fileName parameter is mandantory, use it as a *unique* identifier for each file stored in the database.

```
import importTool

picture = open("pathToFile", "rb")
importTool.importToDB(picture, "nameOfFile")
```

The included test.py file shows a simple use case for the importToDB function.
