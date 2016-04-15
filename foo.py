
class SelfWrapper(ModuleType):
    def __init__(self, self_module, baked_args={}):
    	pass

    def __setattr__(self, name, value):
    	print self, name, value

    def __getattr__(self, name):
        print self, name

    # accept special keywords argument to define defaults for all operations
    # that will be processed with given by return SelfWrapper
    def __call__(self, **kwargs):
        return SelfWrapper(self.__self_module, kwargs)

self = sys.modules[__name__]
sys.modules[__name__] = SelfWrapper(self)