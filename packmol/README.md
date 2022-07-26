# packmol setting
## 安裝流程
* 至[packmol官網](http://leandro.iqm.unicamp.br/m3g/packmol/userguide.shtml)下載安裝檔案
* 安裝gfortran ``yum install gcc-gfortran``(Centos)  ``sudo apt-get install gfortran``(Ubuntu)
* 解壓縮安裝檔 ``tar -xvzf packmol.tar.gz``
* 進入資料夾並安裝 ``cd packmol`` ``make``
* .bashrc新增路徑  ``export PATH=$PATH:the path of packmol``
## 使用指令
* 編輯inp檔
* 指定粒子數目及系統大小(單位為埃)
* ``packmol < mix.inp``
