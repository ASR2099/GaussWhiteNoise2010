# whitenoise

To run the code, open terminal/cmd and run the following commands

 `pip install wavio`,
 `pip install pydub`,
 `pip install numpy`
 
 Then run `python whitenoise.py` and it will play the generated white noise.

asgiref==3.3.4
beautifulsoup4==4.9.3
boto3==1.17.79
botocore==1.20.79
bs4==0.0.1
certifi==2020.12.5
chardet==4.0.0
click==7.1.2
dj-database-url==0.5.0
Django==3.2.3
django-filter==2.4.0
django-heroku==0.3.1
django-storages==1.11.1
Flask==1.1.2
futures==3.1.1
goslate==1.5.1
gunicorn==20.1.0
idna==2.10
itsdangerous==1.1.0
Jinja2==2.11.3
jmespath==0.10.0
joblib==1.0.1
MarkupSafe==1.1.1
nltk==3.5
pep8==1.7.1
Pillow==8.2.0
psycopg2==2.8.6
PyDictionary==2.0.1
PyPDF2==1.26.0
python-dateutil==2.8.1
pytz==2021.1
regex==2021.4.4
requests==2.25.1
s3transfer==0.4.2
six==1.16.0
soupsieve==2.2.1
sqlparse==0.4.1
tqdm==4.60.0
urllib3==1.26.4
Werkzeug==1.0.1
whitenoise==5.2.0






# RIR-Generator

加混响代码，编译后可在python3环境下使用

## 环境配置

要在python3的环境下进行，setup.py需要相应的运行环境

```
$ pip install -r requirements.txt
```

## 编译

```
$ make
```

`make`成功后会生成`librirgen.so`, `pyrirgen.cpp`, `rirgen.o`, `pyrirgen.cpython-35m-x86_64-linux-gnu.so`四个文件，以及一个文件夹`build`。实际使用中保留`librirgen.so`和`pyrirgen.cpython-35m-x86_64-linux-gnu.so`即可。

使用python加载时，如果出现找不到`.so`库的情况，需要将生成的so文件的路径添加到环境变量，比如:

```
$ export LD_LIBRARY_PATH=/*/*/*/RIR-Generator:$LD_LIBRARY_PATH
```


参考：
- [RIR-Generator](https://github.com/ehabets/RIR-Generator/tree/5eb70f066b74ff18c2be61c97e8e666f8492c149)
- [py-RIR-Generator](https://github.com/srikanthrajch/py-RIR-Generator)
