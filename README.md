
![alt text](https://github.com/maikherbig/AIDeveloper/blob/master/art/main_icon_simple_04_text2.png "AIDeveloper Logo with Text")  

AIDeveloper is a software tool that allows you to train, evaluate and apply deep neural nets 
for image classification within a graphical user-interface (GUI).  

# Installation  
There is a tutorial video (ca. 1min. short) on YouTube.  
In this video, I show you how to get AIDeveloper running on your PC.  
[![Alternate Text](/art/Youtube_Link_Tutorial0_v01.png)](https://youtu.be/uqygHsVlCCM "AIDeveloper Tutorial 0")  

  
**_If you dont want to watch the video:_**   
Go through the following 5 steps and you are good to go:    
* Go to https://github.com/maikherbig/AIDeveloper/releases
* Download a zip-file (this file contains the **_standalone executable_**)   
* Unzip it  
* Go into the unzipped folder and scroll down until you find an executable (full name is for example "AIDeveloper_0.0.6.exe")  
* DoubleClick this .exe to run it (no installation is required) 

# Tutorials  
## Basic usage  
There is a tutorial video (ca. 13min. short) on YouTube.  
In this video only the very basic functionality of AID is presented. Furthermore, AIDeveloper contains many tooltips, which should help you to proceed further.  
[![Alternate Text](/art/Youtube_Link_Tutorial1_v04.png)](https://youtu.be/dvFiSRnwoto "AIDeveloper Tutorial 1")
  
  
## Transfer learning    
In a second tutorial (28min), the 'Expert' options of AID are exploited to perform transfer learning.  
First, an existing CNN is loaded into AID. This CNN was trained previously on CIFAR-10 (grayscale) until a validation accuracy of 83%. Next, the Fashion-MNIST dataset is loaded into AID and training of the model is continued on this dataset. At the beginning, only the last layer of the CNN is trained, but later more and more layers are included into training. Also the dropout rates are optimized during the training process until a possibly record breaking testing accuracy of above 92% is reached.  
[![Alternate Text](art/Youtube_Link_Tutorial2_v04.png)](https://youtu.be/NWhv4PF0C4g "AIDeveloper Tutorial 2")
  
  
## Detecting COVID-19 using chest X-ray images  
In this tutorial, AID is used to tackle a biomedical question that is currently of high interest: diagnosis of COVID-19. One problem is the scarcity of COVID-19 X-ray images, which results in a need of modern regularization techniques to prevent overfitting. First, two other large datasets are used to pre-train a model. Next, this model is optimized for images of COVID-19.
More information and step by step instructions are available [here](https://github.com/maikherbig/AIDeveloper/tree/master/Tutorial%205%20COVID-19%20Chest%20X-ray%20images).  
Furthermore, there is a video showing the analysis procedure from beginning to end:  
[![Alternate Text](art/Youtube_Link_Tutorial5_v03.png)](https://www.youtube.com/watch?v=KRDJBJD7CsA "AIDeveloper Tutorial 5")


# Prerequisites  
Since version 0.0.6, the standalone [executables](https://github.com/maikherbig/AIDeveloper/releases) of AIDeveloper are compatible to Windows, Mac and Linux.

The script based version was tested using Python 3.5 on Windows, Mac and Linux. See below to find installation instructions.

# Installation instructions to run AIDeveloper from script
**_you only need to do this if you are a developer/programmer_**
* Install [Visual studio build tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/). During installation, make sure to check C++ Buildtools:
![alt text](https://github.com/maikherbig/AIDeveloper/blob/master/art/VS_Build_Tools.png "Installation of VS Build tools")
* Get a Python distribution. AIDeveloper was developed using Anaconda3 5.3.1 64bit. You can find this particular version in the installer archive of Anconda: https://repo.continuum.io/archive/
* Download the entire GitHub repository of AIDeveloper: find the green button on the top right ("Clone or download"), click it and then click "Download ZIP"
* Unzip the folder for example to C:\Users\MyPC\Downloads\AIDeveloper_0.0.6
* open Anaconda Prompt
* navigate to the folder where you put AIDeveloper `cd C:\Users\MyPC\Downloads\AIDeveloper_0.0.6`
* Generate an environment using the provided .yml file (AID_myenv_Win7.yml): `conda env create -f AID_myenv_Win7.yml`
* This will create a new environment called "myenv"
* Activate it: `conda activate myenv`
* Run AIDeveloper using `python AIDeveloper.py`
  
  
# AIDeveloper in scientific literature  
[1]	[M. Kräter et al., “AIDeveloper: deep learning image classification in life science and beyond,” bioRxiv, p. 2020.03.03.975250, Mar. 2020.](https://www.biorxiv.org/content/10.1101/2020.03.03.975250v1)  
[2]	[A. A. Nawaz et al., “Using real-time fluorescence and deformability cytometry and deep learning to transfer molecular specificity to label-free sorting,” bioRxiv, p. 862227, Dec. 2019.](https://www.biorxiv.org/content/10.1101/862227v2)    
[3]	[T. Krüger et al., “Reliable isolation of human mesenchymal stromal cells from bone marrow biopsy specimens in patients after allogeneic hematopoietic cell transplantation,” Cytotherapy, vol. 22, no. 1, pp. 21–26, Jan. 2020.](https://www.ncbi.nlm.nih.gov/pubmed/31883948)    
