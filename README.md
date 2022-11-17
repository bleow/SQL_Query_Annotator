## SQL Query Annotator
<p align="center">
  <img src = https://user-images.githubusercontent.com/49341007/202511240-5e08371f-c15d-46aa-9ebf-5f4143602d35.png>
  
  <img src = https://user-images.githubusercontent.com/49341007/202511166-9b47f2bc-0f22-4fa1-a925-b805ff9cf206.png>
</p>

## Setting Up

### Using cmd
1. Open command prompt

<p align="center">
<img src = https://user-images.githubusercontent.com/49341007/202510783-d15fe5b9-803c-4fc4-89d4-5745d598ed22.png>
</p>

2. Type the following:
```sh
cd C:/[file_directory]
pip install -r requirements.txt
python project.py
```

### Using an IDE like PyCharm
1.	Make sure there is a requirements.txt file in the same folder as the 4 python files containing the following text:
```sh
numpy==1.22.3
psycopg2==2.9.5
PyQt6==6.4.0
pyqtgraph==0.13.1
```

2.	Open in Pycharm
<p align="center">
<img src = https://user-images.githubusercontent.com/49341007/202510510-0a6928c8-fd70-4354-b8d4-03840a90bbc4.png>
</p>


3.	Two warnings should appear. Click Configure Python Interpreter
<p align="center">
<img src = https://user-images.githubusercontent.com/49341007/202510527-1cdf72ed-2617-4776-8930-6fc6fa16ffb4.png>
</p>


4.	Click Add New Interpreter > Add Local Interpreter
<p align="center">
<img src = https://user-images.githubusercontent.com/49341007/202510538-297c0729-3176-4d0f-86bb-05db3daa99a3.png>
</p>


5.	Select Virtualenv Environment, location is current directory \venv and base interpreter is python.exe
<p align="center">
<img src = https://user-images.githubusercontent.com/49341007/202510572-e6dd7eb3-0672-482f-ac39-ac8d07007459.png>
</p>


6.	Select Ok and venv folder should be created
<p align="center">
<img src = https://user-images.githubusercontent.com/49341007/202510596-4a0d2141-882c-4f39-ac0e-dd9714f70503.png>
</p>


7.	Wait for Indexing to complete
<p align="center">
<img src = https://user-images.githubusercontent.com/49341007/202510617-7159ca4a-e933-4cab-9236-667796b0ca80.png>
</p>


8.	One of the warnings from step 2 should disappear, leaving 1 warning
<p align="center">
<img src = https://user-images.githubusercontent.com/49341007/202510632-6cb394e4-7086-4fef-be12-1610de246df1.png>
</p>


9.	Click on Install requirements
<p align="center">
<img src = https://user-images.githubusercontent.com/49341007/202510640-3fc33701-54d6-418d-957e-e9ea4aa612f6.png>
</p>


10.	Install all requirements
<p align="center">
<img src = https://user-images.githubusercontent.com/49341007/202510659-2ecb6371-9b30-4ad9-9cc8-c9117a6ec2c2.png>
</p>


11.	Wait for installation to finish
<p align="center">
<img src = https://user-images.githubusercontent.com/49341007/202510674-3c91e3f0-84b0-45b7-8ee4-04a116c233f5.png>
</p>


12.	Click on run project
<p align="center">
<img src = https://user-images.githubusercontent.com/49341007/202510687-2fef0618-6001-472b-933b-8ff4ed9c1b27.png>
</p>


13.	If the above does not exist, go to project.py and click on the run button beside if __name__ == ‘__main__’
<p align="center">
<img src = https://user-images.githubusercontent.com/49341007/202510701-59a48822-3d18-4702-8b8d-37c3f3ac1c70.png>
</p>

