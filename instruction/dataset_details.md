# Dataset Details

![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/img/dataset_composition.png)

### Download
  | Split           | Download | # Keyframes | # Clips | # Videos | Storage|
  |-----------------|----------|-----------------|-----------|----------------|--------------|
  |  Example  | [link](https://drive.google.com/file/d/1vEP5qzfep2aAvjJ5HUeMl62JEn9sS20a/view?usp=drive_link) (27 KB) | 51   | 1  | 1 | ~2 MB |
  | Training | [link](https://drive.google.com/file/d/1r71XniKSqIqZM3prtaj9-mWez9bR48uJ/view?usp=drive_link) (529 MB) | 38,137,371 | 1,117,898 | 142,089  | ~441 GB  |
  | Training (Aesthetic)    | [link](https://drive.google.com/file/d/1d23Y7S2hUtla0FkOkB-ruqsieTpRNbCL/view?usp=drive_link) (74.5 MB)  | 6,154,562     | 139,989      | 61,273  | ~56 GB |
  | Training (Small)         | [link](https://drive.google.com/file/d/1PfSSRFM7jAQPNzPPeXeXsTAy9lLjOAVp/view?usp=drive_link) (53.6 MB)  | 3,811,189     | 111,790      | 68,326  | ~45 GB |
  | Validation  | [link](https://drive.google.com/file/d/13H_LGs1CiYbwDKEbn790km71hqmPsaZn/view?usp=drive_link) (28.6 MB)  | 2,035,853 | 59,717 | 44,564 | ~25 GB |
  |  Testing  | [link](https://drive.google.com/file/d/1-Sb4MkWf3bPItT610FiOsJj_PSmqxCfp/view?usp=drive_link) (28.5 MB) | 2,018,545   | 59,718  | 44,247 | ~25 GB |

  ### Taxonomy
  | Taxonomy        |  Class   | Label | Number | Demo |
  |-----------------|----------|-------|--------|------|
  |  Time           | Daylight |  0    |251,515 |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/2183775-Scene-0071_1_fps10.gif)|
  |                 | Night    |  1    |284,179 |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/134442-Scene-0021_1_fps10.gif)|
  |                 | Sunset   |  2    |61,605  |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/216981-Scene-0011_1_fps10.gif)|
  |                 | Others   |  -1   |640,034 |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/112207-Scene-0071_1_fps10.gif)|
  |  Vene           | outdoors |  0    |540,697  |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/219204-Scene-0031_1_fps10.gif)|
  |                 | indoors  |  1    |297,682  |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/26962-Scene-0421_1_fps10.gif)|
  |                 | Others   |  -1   |398,954  |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/191848-Scene-0011_1_fps10.gif)|
  |  Media          | sketch   |  0    |145,803  |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/44449-Scene-0011_1_fps10.gif)|
  |                 |color_trace|  1   |63,141   |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/154558-Scene-0041_1_fps10.gif)|
  |                 | Others   |  -1   |1,028,389 |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/33826-Scene-0121_1_fps10.gif)|
  |  Filming        | looking_at_viewer|  0     |568,025|![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/222849-Scene-0051_1_fps10.gif)|
  |                 | looking_away|  1 |103,036  |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/212048-Scene-0031_1_fps10.gif)|
  |                 | Others   |  -1   |566,272  |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/29797-Scene-0031_1_fps10.gif)|
  |  Filming        | full_body|  0    |57,809   |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/156127-Scene-0041_1_fps10.gif)|
  |                 |upper_body|  1    |744,137  |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/118197-Scene-0101_1_fps10.gif)|
  |                 |lower_body|  2    |8,939    |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/216931-Scene-0011_1_fps10.gif)|
  |                 | out_of_frame| 3  |132,422  |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/2221570-Scene-0051_1_fps10.gif)|
  |                 | Others   |  -1   |294,026  |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/154059-Scene-0051_1_fps10.gif)|
  |  Character      | no_humans|  0    |114,152  |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/198723-Scene-0021_1_fps10.gif)|
  |                 |solo      |  1    |679,208  |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/20417-Scene-0021_1_fps10.gif)|
  |                 |multiple  |  2    |443,869  |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/198036-Scene-0111_1_fps10.gif)|
  |                 | Others   | -1    |104     |![img1](https://github.com/zhenglinpan/SakugaDataset/blob/main/assets/gif_taxonomy/201970-Scene-0101_1_fps10.gif)|