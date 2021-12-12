class Judger:
    
    relationship = {}
    
    @classmethod
    def _register_relationship(cls, entity, register, override):
        if entity in cls.relationship and override==False:
            raise KeyError('{} is already registered as a relationship!')
        cls.relationship[entity] = register

    @classmethod
    def register_relationship(cls, entity, override=True):

        def tmp_func(register_func):
            cls._register_relationship(entity, register_func, override)

        return tmp_func


@Judger.register_relationship(entity='Tom')
def register_Tom(reason):
    print('I like Tom, because he {}'.format(reason))


@Judger.register_relationship(entity='Mike')
def register_Mike(reason):
    print('I love Mike, because he {}'.format(reason))


if __name__ =='__main__':
    Julie = Judger()
    Julie.relationship['Tom']('likes fishing!')
    Julie.relationship['Mike']('is extremely handsome!!!')