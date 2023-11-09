# gbf-scripts
this is a scripts that help me to play gbf automatically

一时兴起，想到了一个曲线救国的玩gbf的方法：
    在windows上使用wsl安装ubuntu系统，然后在Ubuntu中安装chrome浏览器、chromedriver，使用chrome的远程调试功能，结合selenium写一些脚本来玩GBF。


    步骤：
   
    1.安装wsl:
        在管理员模式下打开 PowerShell 或 Windows 命令提示符，方法是右键单击并选择“以管理员身份运行”，输入 wsl --install 命令，然后重启计算机。
        使用 wsl --install 命令安装的新 Linux 安装将默认设置为 WSL 2
        查看当前通过应用商店提供了哪些发行版，请输入命令：wsl --list --online
        默认情况下，wsl --install 命令将安装 Linux 的 Ubuntu 发行版
        参考：
            https://learn.microsoft.com/zh-cn/training/modules/wsl-introduction/install-and-setup
            https://learn.microsoft.com/zh-cn/windows/wsl/install

    2.安装chrome和chromedriver
        注意chrome版本要和chromedriver版本一一对应
        chrome历史版本：https://www.slimjet.com/chrome/download-chrome.php?file=files%2F103.0.5060.53%2Fgoogle-chrome-stable_current_amd64.deb
        chromedriver版本：https://chromedriver.storage.googleapis.com/index.html
        chrome安装：首先切换到安装包所在路径，然后执行 sudo dpkg -i google-chrome-stable_current_amd64.deb
        chromedriver安装：首先解压 unzip chromedriver 然后拷贝至执行文件目录即可 sudo cp chromedriver /usr/bin

    3.线路代理
        如果网速好的话，不用代理也可以玩
        方法一：
            自己有线路的话，可以直接在ubuntu上配置
        方法二：
            使用windows系统上的代理软件
            在windows上查看ip：
                命令行使用ipconfig回车，查看wsl的地址
            以太网适配器 vEthernet (WSL):
            连接特定的 DNS 后缀 . . . . . . . :
            本地链接 IPv6 地址. . . . . . . . : fe80::6223:4500:9743:216a%36
            IPv4 地址 . . . . . . . . . . . . : 172.30.208.1
            子网掩码  . . . . . . . . . . . . : 255.255.240.0
            默认网关. . . . . . . . . . . . . :
            找到wsl的ip地址：172.30.208.1
            查询windows的代理端口，在计算机的网络设置里面，或者浏览器设置的internet选项里面，我这里是4780
            Ubuntu启动浏览器：
                google-chrome-stable --proxy-server=http://172.30.208.1:4780
            配置完成后，windows上启动代理软件，即可使用windows的代理上网了
            
    4.启动
        打开chromedriver：
            命令：chromedriver
        用远程调试方式打开浏览器：
            命令：google-chrome-stable --remote-debugging-port=9222
        捕捉一下9222端口,看是否有启动
            命令: netstat -a -n | grep 9222
        运行脚本：
            cd gbf-scripts
                




