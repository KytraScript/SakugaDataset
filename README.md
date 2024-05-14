![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/img/teaser.png)

<h1 align="center"><a href="https://arxiv.org/abs/2403.06977">Sakuga-42M Dataset: Scaling Up Cartoon Research</a></h1>
<div align="center">
 
[Zhenglin Pan](https://github.com/zhenglinpan), [Yu Zhu](https://github.com/UNKNOWNTIMER), [Yuxuan Mu](https://yxmu.foo)

</div>

<div align="center">
 
[![Paper](https://img.shields.io/badge/cs.CV-2405.07425-b31b1b?logo=arxiv&logoColor=red)](https://arxiv.org/abs/2405.07425)


</div>

## <img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/img/icon.png" alt="Icon" width="20" height="20"> Introduction
This is the official GitHub repository of **Sakuga-42M Dataset**.

**Sakuga-42M Dataset** is the first large-scale cartoon animation dataset, comprising 42 million keyframes. We hope that our efforts in providing this fundamental large-scale dataset could somehow alleviate the data scarcity that has haunted this research domain for years and make it possible to introduce large-scale models and approaches that lead to more robust and transferable applications, which could help animators create more easily.

We anticipate more researchers join us on this journey to explore the potential of cartoon animation research. Suggestions and contributions are always welcome.

**note:** We are still working on the repo&website, so please stay tuned for more updates!😉


## <img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/img/icon.png" alt="Icon" width="20" height="20"> TO-DO
- [x] Release the dataset parquet files
- [x] Release the dataset preparation codes
- [ ] Release the pre-trained models
- [ ] Release the tagging/rating, captioning, and text detection pipelines


## <img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/img/icon.png" alt="Icon" width="20" height="20"> Download

### Dataset
  | Split           | Download | # Keyframes | # Clips | # Videos | Storage|
  |-----------------|----------|-----------------|-----------|----------------|--------------|
  | Training(Full) | [link](https://drive.google.com/file/d/1lIHg-QdC3UaU0eT23bOrsYJF5Clmi43U/view?usp=drive_link) (529 MB) | 38,137,371 | 1,117,898 | 142,089  | ~441 GB  |
  | Training (Aesthetic)    | [link](https://drive.google.com/file/d/115w27NosKhwDK_2BbAQ3twS6n3vDvAxV/view?usp=drive_link) (74.5 MB)  | 6,154,562     | 139,989      | 61,273  | ~56 GB |
  | Training (Small)         | [link](https://drive.google.com/file/d/17CWls-_i7O2x2v4QzfSVNefELv3Rtyx1/view?usp=drive_link) (53.6 MB)  | 3,811,189     | 111,790      | 68,326  | ~45 GB |
  | Validation  | [link](https://drive.google.com/file/d/1hppEnwjAXKV2UWgt04NPRfpnQAz7Mttf/view?usp=drive_link) (28.6 MB)  | 2,035,853 | 59,717 | 44,564 | ~25 GB |
  |  Testing  | [link](https://drive.google.com/file/d/1PAweBehBfQ5WbvzpzAx2kXsxi8v0lk7O/view?usp=drive_link) (28.5 MB) | 2,018,545   | 59,718  | 44,247 | ~25 GB |

## <img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/img/icon.png" alt="Icon" width="20" height="20"> Preperation
![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/img/pipeline.png)

Please follow the instructions below to prepare the complete dataset.

#### 1. Setup environment

```bash
git clone https://github.com/zhenglinpan/SakugaDataset.git
cd SakugaDataset

conda create -n sakuga -y
conda activate sakuga

pip install -r requirement.txt
```

#### 2. Download Dataset

One-key solution for downloading all videos😉:
  ```bash
  cd download
  bash download.sh
  ```
Or step by step:
   
1. Download the parquet files from the following links and put them into `./download/parquet` folder.

2. Run `./download/download.py` to download the videos, files will be saved in `./download/download` by default.

**note:** this step takes at least `15` hours.

#### 3. Split Videos
Run the code to split videos into smaller clips
```bash
cd prepare_dataset
python split_video.py
```

#### 4. Extract Keyframes
And remove the repetitive frames
```bash
cd prepare_dataset
python detect_keyframes.py
```

#### 5. Good-To-Go !
At this time, you should have the dataset ready for your research. Enjoy!

We will be releasing the code for our tagging/rating, captioning, and text detection in near future in case users want to expand the dataset. Stay tuned.

## <img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/img/icon.png" alt="Icon" width="20" height="20"> Supporting Research
![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/img/future_research.png)

## <img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/img/icon.png" alt="Icon" width="20" height="20"> Demonstration

### Diversity
  <table class="center">
    <tr style="text-align: center;">
      <td width=33.3% style="border: none; font-weight: bold;">Rough Sketch</td>
      <td width=33.3% style="border: none; font-weight: bold;">Tiedown(TP)</td>
    </tr>
    <tr>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/rough.gif"></td>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/undead_unluck.gif"></td>
    </tr>

  </table>

  <table class="center">
    <tr style="text-align: center;">
    <td width="33.3%" style="border: none; font-weight: bold;">Western</td>
    <td width="33.3%" style="border: none; font-weight: bold;">Asian</td>
    </tr>
    <tr>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/mickey.gif"></td>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/miyamori.gif"></td>
    </tr>
  </table>

  <table class="center">
    <tr style="text-align: center;">
      <td width=33.3% style="border: none; font-weight: bold;">Cell-Look</td>
      <td width=33.3% style="border: none; font-weight: bold;">Illus-Look</td>
    </tr>
    <tr>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/sakura.gif"></td>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/diamond.gif"></td>
    </tr>
  </table>

### Video-Text Descriptions Pairs
  <table class="center">
    <tr>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/♪❤muteki❤no❤idoru❤♪-Scene-0091_1_fps14.gif"></td>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/cthulhu_musume_(zannenn)-Scene-0021_1_fps14.gif"></td>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/👓miraiinaimiraiwawatashigahoshikunainnda!👓-Scene-0011_1_fps14.gif"></td>
    </tr>
    <tr style="text-align: center;">
      <td width=33.3% style="border: none">multiple girls with blonde, red, and brown hair, wearing idol outfits, dance in a line on stage...
</td>
      <td width=33.3% style="border: none">Nyarlathotep holds out her arms with a glowing face. The second frame shows her in a store..</td>
      <td width=33.3% style="border: none">Her hair is now curled back as she smiles, still in the same outfit and setting...</td>
    </tr>
  </table>

  <table class="center">
    <tr>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/naruto!doushida!-Scene-0101_1_fps14.gif"></td>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/bluefat_and_his_friends-Scene-0011_1_fps14.gif"></td>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/★pokemon★getto★daze★!-Scene-0081_1_fps14.gif"></td>
    </tr>
    <tr style="text-align: center;">
      <td width=33.3% style="border: none">an anime character kneels on a red surface while a man in white and black stands behind...</td>
      <td width=33.3% style="border: none">a diverse group of cartoon characters gathers around a table, enjoying a meal with a variety of dishes...</td>
      <td width=33.3% style="border: none">a cute green cat with fangs, tongue, and a smile, jumps with energy and glowing aura...</td>
    </tr>
  </table>

  <table class="center">
    <tr>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/nobitanofriend-Scene-0021_1_fps14.gif"></td>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/ribai!!_1_fps14.gif"></td>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/ekubo!!!-Scene-0021_1_fps14.gif"></td>
    </tr>
    <tr style="text-align: center;">
      <td width=33.3% style="border: none">the dinosaur emerges from the egg shell, curled up in the blanket...</td>
      <td width=33.3% style="border: none">in an anime clip, a man in a suit falls from a building, holding onto a rope...</td>
      <td width=33.3% style="border: none">a beam shoots out from his clenched fist in a battle scene. The man, now standing on a hill... </td>
    </tr>
  </table>


## <img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/img/icon.png" alt="Icon" width="20" height="20"> Citation
If you find this project useful for your research, please cite our paper. 🤗

```latex
@article{sakuga42m2024,
    title   = {Sakuga-42M Dataset: Scaling Up Cartoon Research},
    author  = {Zhenglin Pan, Yu Zhu, Yuxuan Mu},
    journal = {arXiv preprint arXiv:2405.07425},
    year    = {2024}
}
```

## <img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/img/icon.png" alt="Icon" width="20" height="20"> Disclaimer
Sakuga-42M Dataset is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/), and is designed only for academic research purposes, copyrights of images and videos in the dataset are owned by their respective creators, we will remove the works from the dataset upon request to protect the author's rights.

## <img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/img/icon.png" alt="Icon" width="20" height="20"> Contact
**Zhenglin Pan**: zhengli3@ualberta.ca
