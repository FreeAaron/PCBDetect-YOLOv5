# PCBDetect - YOLOv5

![Python](https://img.shields.io/badge/Python-3.8-blueviolet)
   <a href="https://github.com/ultralytics/yolov5/actions/workflows/ci-testing.yml"><img src="https://github.com/ultralytics/yolov5/actions/workflows/ci-testing.yml/badge.svg" alt="CI CPU testing"></a>

> [資料集介紹](PCBDatasets/README.md)：[DeepPCB](https://github.com/tangsanli5201/DeepPCB)
> [YOLOv5介紹](YOLOv5/README.md)：[YOLOv5 🚀 in PyTorch](https://github.com/ultralytics/yolov5)

## :memo: Quick Start

## <div align="center">1. 將欲測試之照片放入指定資料夾</div>

#### 將欲測試之照片放入 **`YOLOv5\data\images`** 資料夾中
#### 大小為 **640 x 640**


![](https://i.imgur.com/jiwc6CV.png)


## <div align="center">2. 執行 detect.py</div>

#### Open your terminal/command prompt from your project directory and run the detect.py file by executing the command `python detect.py`.

```bash
cd YOLOv5
python detect.py 
```
#### A Few Seconds Later
### Done！

![](https://i.imgur.com/CPWs0kY.jpg)

預設路徑放於　`YOLOv5\runs\detect` `\exp` 開頭之資料夾下
(如欲更改資料夾名稱可於 detect.py 下之第72行進行修改)


---
## <div align="center">訓練及驗證結果</div>
[Wandb.ai](https://wandb.ai/freeaaron/train/runs/1fmauuce?workspace=user-freeaaron)

- PR_curve
![PR_curve](https://i.imgur.com/zmuqR5U.png)

- val_batch2_labels
![val_batch2_labels](https://i.imgur.com/j20zy9t.jpg)


## Model Use

- 本訓練模型使用 YOLOv5s Model 進行，小且快速且效果佳。

![](https://i.imgur.com/yN7xGjW.png)


- [參考資料：Train Custom Data](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)

```javascript=16
var s = "JavaScript syntax highlighting";
alert(s);
```
---
<details open>
<summary>必要時可安裝</summary>

Clone repo and install [requirements.txt](https://github.com/ultralytics/yolov5/blob/master/requirements.txt) in a
[**Python>=3.7.0**](https://www.python.org/) environment, including
[**PyTorch>=1.7**](https://pytorch.org/get-started/locally/).

```bash
cd YOLOv5
pip install -r requirements.txt  # install
```
</details>

---
## <div align="center">Contact</div>

如果有漏洞與功能或其他問題，歡迎與我聯繫。
FreeAaron

<br>

<div align="center">
    <a href="https://github.com/FreeAaron">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-github.png" width="3%"/>
    </a>
    <img width="3%" />
    <a href="https://www.linkedin.com/in/freeaaron/">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-linkedin.png" width="3%"/>
    </a>
    <img width="3%" />
    <a href="https://www.facebook.com/FreeBoss.Lee">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-facebook.png" width="3%"/>
    </a>
    <img width="3%" />
    <a href="https://www.instagram.com/aaronlee730/">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-instagram.png" width="3%"/>
    </a>
</div>