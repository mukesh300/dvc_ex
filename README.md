create env

```bash
conda create -n wineq python=3.9 -y
```

activate env

```bash
conda activate wineq
```

create a requirement file 

install the requirements
```bash
pip install -r requirements.txt
```
download the data

https://drive.google.com/drive/folders/1xw0XX-WK74uxtFFLySbtnX-ODdmdK5Ec

initialize git and dvc 

```bash
git init

dvc init

dvc add data_given/winequality.csv

git add .

git commit -m "initial commit"
```