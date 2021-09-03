<h1 align="center">Service Python cx_Loggin and win32 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Version" src="https://img.shields.io/badge/version-1-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/Heidet/Python-Service-Cx_Freeze" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="yes" target="_blank">
    <img alt="License: Yes" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://twitter.com/Null" target="_blank">
    <img alt="Twitter: Null" src="https://img.shields.io/twitter/follow/Null.svg?style=social" />
  </a>
</p>

Build Service Windows Python3.9

## Author
👤 **Antoine Heidet** 
* GitHub: [@https:\/\/github.com\/Heidet\/](https://github.com/Heidet)


## 📝 Doc Build 
Clone Project https :
```-> git clone https://github.com/Heidet/Python-Service-Cx_Freeze.git```

Create VirtualEnv :
```-> YourPathPython39 -m venv ```

Get Requirements :
```-> YourPathPython39 -m pip install -r requirements.txt```

Edit config.py :
```-> change the NAME and DISPLAYNAME variables to put the service name and the name to display as well as DESC```

Edit setup.cfg :
```-> Add your modules and packages```
	
Build setup.py :
```-> YourPathPython39 setup.py build```



## 📝 Doc Install Service

Change directory :
```-> /build/exe.win-amd64-3.9/```

Install Service :
```-> servicename.exe --install <NAMESERVICE>```

Desinstall Service :
```-> servicename.exe --uninstall <NAMESERVICE>```


## License
Copyright © 2021 [Antoine Heidet](https://github.com/Heidet).<br />
This project is [EzAntoine HeidetDEV](https://github.com/Heidet) licensed.
