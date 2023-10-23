# AYALED
用于[decky-loader](https://github.com/SteamDeckHomebrew/decky-loader)的插件  
为部分ayaneo设备提供摇杆灯光控制

## 支持设备
- AYANEO AIR
- AYANEO AIR 1S
- AYANEO AIR Pro
- AYANEO 2
- AYANEO 2S
- AYANEO GEEK
- AYANEO GEEK 1S

## 手动安装

1. 安装[decky-loader](https://github.com/SteamDeckHomebrew/decky-loader)
2. 下载[Releases](https://github.com//ayaled/releases) ayaled.tar.gz
3. 调整插件目录权限 `chmod -R 777 ${HOME}/homebrew/plugins`
4. 解压到/home/xxxx/homebrew/plugins/下
5. 重启 decky-loader, `sudo systemctl restart plugin_loader.service`
6. 进入游戏模式，即可在decky页面使用该插件

## 一键安装
```
curl -L https://raw.githubusercontent.com/honjow/ayaled/main/install.sh | sh
```