# mrs-sp22-tutorial
Materials for a tutorial on Battery Data Science and MRS SP22

## Machine learning with battery data
Tutorial instructor: Dr. Paul Gasper, Staff Scientist, National Renewable Energy Laboratory

![](figures/eis_to_q.png)

This tutorial walks through the development of a machine-learning model predicting battery capacity from electrochemical impedance spectroscopy data, illustrating basic machine-learning topics such as evaluating model fitness with train/test splits, feature engineering methods, model interrogation, and visualizing predictions using the sklearn library for model development and matplotlib for visualization. The tutorial will use open-source data from Zhang et al, *Nature Communications* (2020) 11:1706 ([paper](https://www.nature.com/articles/s41467-020-15235-7.pdf), [github](https://github.com/YunweiZhang/ML-identify-battery-degradation)). This tutorial uses the following files:
- [ml_predicting_capacity_with_eis.ipynb](/ml_predicting_capacity_with_eis.ipynb): Notebook for the tutorial
- eis/eisplot.py: visualization function for plotting impedance data
- data/data_eis_zhang2020.csv: capacity and EIS measurements from 8 cells throughout their lifetime, from Zhang et al 2020 (see ref. above)
- data/freq_eis_zhang2020.csv: frequency vector for plotting impedance data
