# Burp Suite JSON/JS-Beautifier



This is a Burp Extension for beautifying JSON and JavaScript output to make the body parameters more human readable.
It is diffcult for web application security researchers to analyse the JS files which are compressed to increase the loading speed. This Burp Suite open source extension makes it easier to analyse displaying decompressed version of such resources.

#### This extension is based on the following module/library :
JS files of http://jsbeautifier.org/


## Installation
* Download Burp Suite : http://portswigger.net/burp/download.html
* Download Jython standalone JAR: https://www.jython.org/download
* Open burp -> Extender -> Options -> Python Environment -> Select File -> Choose the Jython standalone JAR
* Install packages from requirements.txt using pip install -r requirements (use jython's pip!)
* Specify "Folder for loading modules" in Extender->Options->Python environment. It should reflect your global or virtualenv site-packages. E.g. "C:\jython2.7\lib\site-packages" for WIN, or /opt/jython/Lib/site-packages fo Archlinux. If you use virtualenv (you should!) - it would be /path/to/virtualenv/Lib/site-packages.
* Download the extension .py file.
* Open Burp -> Extender -> Extensions -> Add -> Choose the file.


Before:
![alt text](https://raw.githubusercontent.com/Manjesh24/JSON-JS-Beautifier/master/Images/Before.png)

After:
![alt text](https://raw.githubusercontent.com/Manjesh24/JSON-JS-Beautifier/master/Images/After.png)


## Tested on:
This extension has been tested on Burp Suite Pro v2.1.01
