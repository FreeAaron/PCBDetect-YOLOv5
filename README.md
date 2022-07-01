# PCBDetect - YOLOv5

![Python](https://img.shields.io/badge/Python-3.8-blueviolet)
<a href="https://github.com/ultralytics/yolov5/actions/workflows/ci-testing.yml"><img src="https://github.com/ultralytics/yolov5/actions/workflows/ci-testing.yml/badge.svg" alt="CI CPU testing"></a>

> [資料集介紹](PCBDatasets/README.md)：[DeepPCB](https://github.com/tangsanli5201/DeepPCB) > <br> > [YOLOv5 介紹](YOLOv5/README.md)：[YOLOv5 🚀 in PyTorch](https://github.com/ultralytics/yolov5)

## <div align="center">📝Quick Start</div>

## 1. 將欲測試之照片放入指定資料夾

> 將欲測試之照片放入 **`YOLOv5\data\images`** 資料夾中

> 大小為 **640 x 640**

![](https://i.imgur.com/jiwc6CV.png)

<br>

## 2. 執行 detect.py

Open your terminal/command prompt from your project directory and run the detect.py file by executing the command `python detect.py`.

```bash
cd YOLOv5
python detect.py
```

<br>

A Few Seconds Later

Done！

![](https://i.imgur.com/CPWs0kY.jpg)

預設路徑放於　`YOLOv5\runs\detect` `\exp` 開頭之資料夾下<br>
(如欲更改資料夾名稱可於 detect.py 下之第 72 行進行修改)

<br>

## 訓練及驗證結果

[train log：Wandb.ai](https://wandb.ai/freeaaron/train/runs/1fmauuce?workspace=user-freeaaron)

-   Results
    ![results](https://i.imgur.com/uxEEWAc.png)

-   PR_curve
    ![PR_curve](https://i.imgur.com/zmuqR5U.png)

<br>

> Validation

-   val_batch0_pred
    ![val_batch0_pred](https://i.imgur.com/CsGLc6t.jpg)

-   val_batch2_labels
    ![val_batch2_labels](https://i.imgur.com/j20zy9t.jpg)

路徑 `YOLOv5\runs\train\PCBDetect` 下可看到其他結果

<br>

## Model Use

-   Here I select [YOLOv5s](https://github.com/ultralytics/yolov5/blob/master/models/yolov5s.yaml), the smallest and fastest model available. See YOLOv5 README [table](https://github.com/ultralytics/yolov5#pretrained-checkpoints) for a full comparison of all models.

![](https://i.imgur.com/yN7xGjW.png)

-   [參考資料：Train Custom Data](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)

---

<br>
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

<br>

## Contact

如果有漏洞與功能或其他問題，歡迎與我聯繫。
<br>
by FreeAaron

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
