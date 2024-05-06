gdown --fuzzy https://drive.google.com/file/d/1lIHg-QdC3UaU0eT23bOrsYJF5Clmi43U/view?usp=drive_link -O ./parquet/sakugadataset_train_full.parquet
gdown --fuzzy https://drive.google.com/file/d/115w27NosKhwDK_2BbAQ3twS6n3vDvAxV/view?usp=drive_link -O ./parquet/sakugadataset_train_aesthetic.parquet
gdown --fuzzy https://drive.google.com/file/d/17CWls-_i7O2x2v4QzfSVNefELv3Rtyx1/view?usp=drive_link -O ./parquet/sakugadataset_train_small.parquet
gdown --fuzzy https://drive.google.com/file/d/1hppEnwjAXKV2UWgt04NPRfpnQAz7Mttf/view?usp=drive_link -O ./parquet/sakugadataset_val.parquet
gdown --fuzzy https://drive.google.com/file/d/1PAweBehBfQ5WbvzpzAx2kXsxi8v0lk7O/view?usp=drive_link -O ./parquet/sakugadataset_test.parquet

python download.py