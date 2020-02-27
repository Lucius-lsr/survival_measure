import math as m
from matplotlib import pyplot as plt
from lifelines.datasets import load_waltons
import random


def Breslow_estimator(data, target):  # data是一个三元组的列表，每个元素的格式为(time,status,risk)
    assert len(data[0]) == 3
    # 归一化
    norm_data = []
    for tuple in data:
        norm_data.append([tuple[0], tuple[1], m.exp(tuple[2]) / m.exp(target)])

    # sort by time
    sorted_data = sorted(norm_data, key=lambda student: student[0])
    record_sum_risk = dict()  # 存储二元组，(时间,大小)
    sorted_data.reverse()
    print(sorted_data)

    risk_sum = 0
    for time, status, risk in sorted_data:
        risk_sum += risk
        record_sum_risk[time] = risk_sum
    print(record_sum_risk)

    Delta_H0 = []
    sorted_data.reverse()
    for time, status, risk in sorted_data:
        if status == 1:
            if len(Delta_H0) > 0 and Delta_H0[-1][0] == time:  # 重复的情况
                Delta_H0[-1][1] += 1 / record_sum_risk[time]
            else:
                Delta_H0.append([time, 1 / record_sum_risk[time]])  # 没有重复的情况
    print(Delta_H0)

    H0 = []
    delta_sum = 0
    for time, delta in Delta_H0:
        delta_sum += delta
        H0.append((time, delta_sum))
    print(H0)

    return H0


def hazard_function(H0):
    times = []
    cumulative_risk = []
    for time, H0_time in H0:
        times.append(time)
        cumulative_risk.append(H0_time)

    plt.plot(times, cumulative_risk)
    plt.show()


def survival_function(H0):
    times = []
    survival_probability = []
    for time, H0_time in H0:
        times.append(time)
        survival_probability.append(m.exp(-H0_time))

    plt.plot(times, survival_probability)
    plt.show()


if __name__ == '__main__':
    df = load_waltons()  # returns a Pandas DataFrame
    T = df['T']
    E = df['E']
    length = len(T)
    data = []
    for i in range(length):
        data.append((T[i], E[i], random.randint(4, 6)))

    H0 = Breslow_estimator(data, 5)
    survival_function(H0)
