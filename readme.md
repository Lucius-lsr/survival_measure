# metrics to measure survival analysis

- AUC-curve: 首先通过实际数据将样本分为良好预后、不良预后两组。然后，通过计算出的样本风险值score，调整预测分组的阈值，检验score是否分布合理
- KM-curve：基础的方法，通过全部样本集推测整体生存曲线
- Breslow-estimator：Cox回归的最后一步，通过单个样本的风险值，预测该样本生存曲线
- parametric-methods：给定概率分布的情况下，直接给出样本集的整体生存函数
- regression：经典的Cox回归，多变量/单变量
- univariant-KM：通过某种方法，将样本分为两组，比较这两组是否明显不同