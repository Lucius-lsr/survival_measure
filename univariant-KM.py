from lifelines.utils import median_survival_times
from lifelines import KaplanMeierFitter
from lifelines.datasets import load_dd
from matplotlib import pyplot as plt
from lifelines.statistics import logrank_test

data = load_dd()
T = data["duration"]
E = data["observed"]

kmf = KaplanMeierFitter()

dem = (data["democracy"] == "Democracy")
kmf.fit(T[dem], event_observed=E[dem], label="Democratic Regimes")

ax = plt.subplot(111)
kmf.plot(ax=ax)
print("Median survival time of democratic:", kmf.median_survival_time_)
kmf.fit(T[~dem], event_observed=E[~dem], label="Non-democratic Regimes")
kmf.plot(ax=ax)
print("Median survival time of non-democratic:", kmf.median_survival_time_)

plt.ylim(0, 1)
plt.title("Lifespans of different global regimes")
plt.show()

results = logrank_test(T[dem], T[~dem], E[dem], E[~dem], alpha=.99)
results.print_summary()