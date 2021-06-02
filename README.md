# 实验步骤
## 指纹图像处理实验
### FingerprintFeature
运行 main.py，生成 featureData.txt
## 指纹特征生成实验
### FeatureExtraction 
features文件夹为原始数据
运行 dataProcess.py，对原始数据进行清洗，得到cleanFeatures文件夹
运行 n-gons.py，生成n-gon，得到5-gon-translation文件夹
运行 dataIntegration.py，生成整个的5-gon-translation.txt文件
运行 n-gon-quantize.py，生成5-gon-translation-quan文件夹
运行 featureGenerator.py，生成feature664文件夹
运行 dataIntegration.py，生成整个的feature664.txt文件
## 指纹匹配实验
### Match
运行 match.py，生成dist-5-gon-translation-quan664文件夹
运行 find.py，生成类内距与类间距图像
运行 regi_very.py，生成FAR，FRR数据
## 模糊锁机制实验
### FuzzyVault
运行 fuzzyVault.py
## Schnorr签名机制实验
### Schnorr
运行 Main.java
