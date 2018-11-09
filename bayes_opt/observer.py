"""
observers...
"""
import os
import json
from datetime import datetime
from .event import Events


class _Clock:
    def __init__(self):
        self._start_time = None
        self._previous_time = None

    def _time_metrics(self):
        now = datetime.now()
        if self._start_time is None:
            self._start_time = now
        if self._previous_time is None:
            self._previous_time = now

        time_elapsed = now - self._start_time
        time_delta = now - self._previous_time

        self._previous_time = now
        return time_elapsed.total_seconds(), time_delta.total_seconds()


class ScreenLogger(_Clock):
    def __init__(self, verbose=0):
        self._verbose = verbose
        super(ScreenLogger, self).__init__()

    @property
    def verbose(self):
        return self._verbose

    @verbose.setter
    def verbose(self, v):
        self._verbose = v

    def update(self, event, instance):
        if event == Events.OPTMIZATION_START:
            print("Optimization has started.")
        elif event == Events.OPTMIZATION_STEP:
            print("Optimization step finished, current max: ",
                  instance.max)
        elif event == Events.OPTMIZATION_END:
            print("Optimization finished, maximum value at: ",
                  instance.max)


class JSONLogger(_Clock):
    def __init__(self, path):
        self._path = path if path[-5:] == ".json" else path + ".json"
        try:
            os.remove(self._path)
        except OSError:
            pass

        super(JSONLogger, self).__init__()

    def update(self, event, instance):
        if event == Events.OPTMIZATION_STEP:
            data = dict(instance.res[-1])

            time_elapsed, time_delta = self._time_metrics()
            data["time"] = {
                "elapsed": time_elapsed,
                "delta": time_delta,
            }

            with open(self._path, "a") as f:
                f.write(json.dumps(data) + "\n")


# class PrintLog(object):

#     def __init__(self, params):

#         self.ymax = None
#         self.xmax = None
#         self.params = params
#         self.ite = 1

#         self.start_time = datetime.now()
#         self.last_round = datetime.now()

#         # sizes of parameters name and all
#         self.sizes = [max(len(ps), 7) for ps in params]

#         # Sorted indexes to access parameters
#         self.sorti = sorted(range(len(self.params)),
#                             key=self.params.__getitem__)

#     def reset_timer(self):
#         self.start_time = datetime.now()
#         self.last_round = datetime.now()

#     def print_header(self, initialization=True):

#         if initialization:
#             print("{}Initialization{}".format(BColours.RED,
#                                               BColours.ENDC))
#         else:
#             print("{}Bayesian Optimization{}".format(BColours.RED,
#                                                      BColours.ENDC))

#         print(BColours.BLUE + "-" * (29 + sum([s + 5 for s in self.sizes])) +
#               BColours.ENDC)

#         print("{0:>{1}}".format("Step", 5), end=" | ")
#         print("{0:>{1}}".format("Time", 6), end=" | ")
#         print("{0:>{1}}".format("Value", 10), end=" | ")

#         for index in self.sorti:
#             print("{0:>{1}}".format(self.params[index],
#                                     self.sizes[index] + 2),
#                   end=" | ")
#         print('')

#     def print_step(self, x, y, warning=False):

#         print("{:>5d}".format(self.ite), end=" | ")

#         m, s = divmod((datetime.now() - self.last_round).total_seconds(), 60)
#         print("{:>02d}m{:>02d}s".format(int(m), int(s)), end=" | ")

#         if self.ymax is None or self.ymax < y:
#             self.ymax = y
#             self.xmax = x
#             print("{0}{2: >10.5f}{1}".format(BColours.MAGENTA,
#                                              BColours.ENDC,
#                                              y),
#                   end=" | ")

#             for index in self.sorti:
#                 print("{0}{2: >{3}.{4}f}{1}".format(
#                     BColours.GREEN, BColours.ENDC,
#                     x[index],
#                     self.sizes[index] + 2,
#                     min(self.sizes[index] - 3, 6 - 2)
#                 ),
#                     end=" | ")
#         else:
#             print("{: >10.5f}".format(y), end=" | ")
#             for index in self.sorti:
#                 print("{0: >{1}.{2}f}".format(x[index],
#                                               self.sizes[index] + 2,
#                                               min(self.sizes[index] - 3, 6 - 2)),
#                       end=" | ")

#         if warning:
#             print("{}Warning: Test point chose at "
#                   "random due to repeated sample.{}".format(BColours.RED,
#                                                             BColours.ENDC))

#         print()

#         self.last_round = datetime.now()
#         self.ite += 1

#     def print_summary(self):
#         pass
