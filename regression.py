from lifelines import CoxPHFitter
from lifelines.datasets import load_rossi
from matplotlib import pyplot as plt

rossi_dataset = load_rossi()

print(rossi_dataset)

cph = CoxPHFitter(penalizer=0.05, l1_ratio=0.5)
# cph = CoxPHFitter(penalizer=0.05, l1_ratio=1.0) # 惩罚系数

cph.fit(rossi_dataset, duration_col='week', event_col='arrest')

# cph.print_summary()

# 显示预测的关键值
# print(cph.predict_partial_hazard(rossi_dataset))
# print(cph.predict_survival_function(rossi_dataset))
# print(cph.predict_median(rossi_dataset))

# 图形化表达系数大小
# cph.plot()

# 考虑一个变量，固定其他变量
# cph.plot_covariate_groups('prio', [0, 2, 4, 6, 8, 10], cmap='coolwarm')
#
cph.plot_covariate_groups(
    ['age', 'fin'],
    [
        [27, 1],

    ],
    cmap='coolwarm')

plt.show()



