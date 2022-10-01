import pickle

with open("sim_berlinale.pkl", "rb") as pklfile:
  events = pickle.load(pklfile)
events_new = dict(events)
print(len(events_new['x']))
events_new['x'][:] = events_new['x'][779161:]
events_new['y'][:] = events_new['y'][779161:]
events_new['timestamp'][:] = events_new['timestamp'][779161:]
events_new['pol'][:] = events_new['pol'][779161:]
with open("sim_berlinale_short48.pkl", "wb") as pklfile:
  pickle.dump(events_new, pklfile)

