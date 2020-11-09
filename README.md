# MaxKart
An application for your all day to day needs and services.  



## _How to Setup_

#### 1. Fork this repository.
#### 2. Clone it in your DEVICE.
#### 3.  Set the original repo as your upstream repo
      
```
git remote add upstream https://github.com/Zexeret/MaxKart.git

git remote -v        [To check your connections]
```

   >- For updating your local repo with original repo
 ```
git fetch upstream
git checkout main
git merge upstream/main
 ```

#### 4. Setting up models in your device

Open terminal and run the following commands in directory containing manage.py

```
python manage.py makemigrations

python manage.py migrate

```


## Owners
 - Shyam Rathod
 - Ojus Bhutani

         




