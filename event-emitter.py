class EventEmitter:
    max_listeners = 9
    callbacks = {}

    def __init__(self, options=None):
        if options is not None and options.max_listeners:
            self.max_listeners = options.max_listeners
        pass

    def on(self, event_name, cb):
        if event_name not in self.callbacks:
            self.callbacks[event_name] = []
        self.callbacks[event_name].append(cb)

    def emit(self, event_name, data):
        self.__process_callbacks(event_name, data)

    def __process_callbacks(self, event_name, data):
        for cb in self.callbacks[event_name]:
            cb(data)


event_emitter = EventEmitter()

event_emitter.on('foo', lambda data: print(data))

event_emitter.emit('foo', 'bla')

