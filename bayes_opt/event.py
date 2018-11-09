class Events:
    MAXIMIZE_START = 'maximize:start'
    MAXIMIZE_END = 'maximize:end'
    PROBE_STEP = 'probe:step'

    ELEMENT_ADDED_TO_QUEUE = ""
    QUEUE_IS_EMPTY = ""


DEFAULT_EVENTS = [
    Events.MAXIMIZE_START,
    Events.MAXIMIZE_END,
    Events.PROBE_STEP,
    Events.ELEMENT_ADDED_TO_QUEUE,
    Events.QUEUE_IS_EMPTY,
]
