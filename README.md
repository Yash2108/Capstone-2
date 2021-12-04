# Capstone-2 Project

Project to create a webapp which detects and counts human in images and videos.
Currently experimenting with 2 ML models: Pointrend (ResNet backbone) & OpenCV's HOG descriptor

#### Install the dependencies by :

``pip install -r requirements.txt``

Download the pointrend_resnet101.pkl from [here](https://drive.google.com/file/d/1NeWpWQGjj2hf_W6wDIJ9e-php9UixYp3/view?usp=sharing) and place it in `humancounter/` folder

### To run the Selenium automation

Please download the respective chromedriver from [this link](https://chromedriver.chromium.org/downloads)  and place it in `humancounter/` folder

#### To run this on a Django Server :

``python manage.py runserver``

#### To run this on Docker :

1. Run ``docker run -d --name myapp ncmohit/capstoneproject -p 8000:8000 myapp``
