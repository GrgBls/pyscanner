# pyscanner

A python program to scan items in a market.

![scanner_img](https://github.com/GrgBls/pyscanner/assets/24195309/ab8c37a0-0181-4788-b004-fc104c7f4530)



## Installation
The program requires opencv, tkinter, pyzbar and numpy 1.x to work. First, you need to install those libraries:
```bash
pip install opencv-python
pip install tk
pip install pyzbar
pip install numpy==1.26.4
```

Next, you can clone and run pyscanner just by cloning the repository:
```
git clone github.com/GrgBls/pyscanner.git
cd pyscanner
./main.py
```
## How to use // Database
    
By clicking the Database button, you will be able to search, insert and remove items, as well as update their prices and how much stock there is left. 

To perform any action, first input the product's barcode and then click on the specific action. The program will guide you for the next steps.

## How to use // Scanner

After importing your products into the database, you can begin scanning them. The program supports two types of scanning, both through camera and manually.

To scan using your camera, just click the scan button and put the product's barcode in front of the camera. When the camera detects the barcode, it will close and you will be able to click Enter.

To scan manually, just insert the barcode into the text box and press Enter.

All scanned items will appear at the right side of the screen. You may edit the products, if you have made a mistake by clicking the Edit Button.

After you have finished scanning all your items, you can click End and the total amount of money will be shown to you.
