<!--
 █████╗ ███╗   ██╗██╗████████╗ █████╗     ██████╗ ███████╗███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
██╔══██╗████╗  ██║██║╚══██╔══╝██╔══██╗    ██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
███████║██╔██╗ ██║██║   ██║   ███████║    ██████╔╝█████╗  ███████╗█████╗  ███████║██████╔╝██║     ███████║
██╔══██║██║╚██╗██║██║   ██║   ██╔══██║    ██╔══██╗██╔══╝  ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
██║  ██║██║ ╚████║██║   ██║   ██║  ██║    ██║  ██║███████╗███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                                                                          
-->


![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/img/teaser.png)

<h1 align="center"><a href="https://arxiv.org/abs/2403.06977">Sakuga-42M Dataset: Scaling Up Cartoon Reasearch</a></h1>
<div align="center">
 
[Zhenglin Pan](www.google.com), [Yu Zhu](www.google.com), [Yuxuan Mu](www.google.com)

</div>

<div align="center">
 
[![Paper](https://img.shields.io/badge/cs.CV-2403.06977-b31b1b?logo=arxiv&logoColor=red)](https://arxiv.org/abs/2403.06977)
[![Project Page](https://img.shields.io/badge/Project-Website-green)](https://snap-research.github.io/Panda-70M)
[![Project Page](https://img.shields.io/badge/Dataset-Website-blue)](https://snap-research.github.io/Panda-70M)


</div>

## Introduction
This is the offical Github repository of **Sakuga-42M**. 

Sakuga-42M Dataset is the first large-scale cartoon animation dataset, comprising 42 million keyframes. We hope our efforts on providing this foundamental large-scale dataset could somehow alleviate the data scarcity haunting this reseach domain for years, and make possible introducing large-scale models&approaches that leads to more robust and transferable applications that could help animators to create more easily.

We hope more researchers could join us in this journey to explore the potential of cartoon animation research. Suggestions and contributions are always welcome.

## Content

This repository contains the following:
- Dataset itself
- Data Preperation Pipelines
- Pretrained Models

### Download
  | Split           | Download | # Keyframes | # Clips | # Videos | Storage|
  |-----------------|----------|-----------------|-----------|----------------|--------------|
  |  Example  | [link](https://drive.google.com/file/d/1vEP5qzfep2aAvjJ5HUeMl62JEn9sS20a/view?usp=drive_link) (27 KB) | 51   | 1  | 1 | ~2 MB |
  | Training | [link](https://drive.google.com/file/d/1r71XniKSqIqZM3prtaj9-mWez9bR48uJ/view?usp=drive_link) (529 MB) | 38,137,371 | 1,117,898 | 142,089  | ~441 GB  |
  | Training (Aesthetic)    | [link](https://drive.google.com/file/d/1d23Y7S2hUtla0FkOkB-ruqsieTpRNbCL/view?usp=drive_link) (74.5 MB)  | 6,154,562     | 139,989      | 61,273  | ~56 GB |
  | Training (Small)         | [link](https://drive.google.com/file/d/1PfSSRFM7jAQPNzPPeXeXsTAy9lLjOAVp/view?usp=drive_link) (53.6 MB)  | 3,811,189     | 111,790      | 68,326  | ~45 GB |
  | Validation  | [link](https://drive.google.com/file/d/13H_LGs1CiYbwDKEbn790km71hqmPsaZn/view?usp=drive_link) (28.6 MB)  | 2,035,853 | 59,717 | 44,564 | ~25 GB |
  |  Testing  | [link](https://drive.google.com/file/d/1-Sb4MkWf3bPItT610FiOsJj_PSmqxCfp/view?usp=drive_link) (28.5 MB) | 2,018,545   | 59,718  | 44,247 | ~25 GB |


Detailed Explation for each attributes can be found in [Dataset Dataloading](./dataset_dataloading) section.

### Collection Pipeline
<p align="center" width="100%">
<a target="_blank"><img src="assets/collection_pipeline.gif" style="width: 100%; min-width: 200px; display: block; margin: auto;"></a>
</p>

## Demonstration

### Supporting Research
![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/img/feature_research.png)

### Diversity
  <table class="center">
    <tr style="text-align: center;">
      <td width=33.3% style="border: none">Rough Sketch</td>
      <td width=33.3% style="border: none">Tiedown(TP)</td>
    </tr>
    <tr>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/rough.gif"></td>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/undead_unluck.gif"></td>
    </tr>

  </table>

  <table class="center">
    <tr style="text-align: center;">
      <td width=33.3% style="border: none">Western</td>
      <td width=33.3% style="border: none">Asian</td>
    </tr>
    <tr>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/mickey.gif"></td>
      <td width=33.3% style="border: none"><img src="https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif/miyamori.gif"></td>
    </tr>
  </table>

  <table class="center">
    <tr style="text-align: center;">
      <td width=33.3% style="border: none">Cell-Look</td>
      <td width=33.3% style="border: none">Illus-Look</td>
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
      <td width=33.3% style="border: none">Multiple girls with blonde, red, and brown hair, wearing idol outfits, dance in a line on stage...
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
      <td width=33.3% style="border: none">A cute green cat with fangs, tongue, and a smile, jumps with energy and glowing aura...</td>
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
      <td width=33.3% style="border: none">Aa smiling man clenches his teeth, looking at the viewer. A beam shoots out...</td>
    </tr>
  </table>


## Citation
If you find this project useful for your research, please cite our paper. 🤗

```latex

```

## Contact
**Zhenglin Pan**: zhengli3@ualberta.ca
