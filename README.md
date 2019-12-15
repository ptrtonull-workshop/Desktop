## requirements
- MySQL
- mysqlclient
- python 3.7
## download
run
```
mkdir workspace
cd workspace
git clone https://github.com/ptrtonull-workshop/Desktop
```
## built
run
```
pip3 install pyinstaller -i http://mirrors.aliyun.com/pypi/simple  --trusted-host mirrors.aliyun.com
pyinstaller -F -w index.py
```
after the prcocess finsh, you will see a exe file in `./dist`

## run
### run with python
make your Python 3.7 has been installed in your windows and the path has been add to your windows
run
```
python index.py
```
### run with exe
At first, you should build this project, and run index.exe in `./dist`