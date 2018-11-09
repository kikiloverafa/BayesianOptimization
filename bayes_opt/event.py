class Events:
    OPTMIZATION_START = 'optmization:start'
    OPTMIZATION_STEP = 'optmization:step'
    OPTMIZATION_END = 'optmization:end'

    ELEMENT_ADDED_TO_QUEUE = ""
    QUEUE_IS_EMPTY = ""


DEFAULT_EVENTS = [
    Events.OPTMIZATION_START,
    Events.OPTMIZATION_STEP,
    Events.OPTMIZATION_END,
    Events.ELEMENT_ADDED_TO_QUEUE,
    Events.QUEUE_IS_EMPTY,
]
