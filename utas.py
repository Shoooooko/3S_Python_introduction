# coding: utf-8
# In[ ]:
class UTCourse:
    def __init__(self, dic):
        for k, v in dic.items():
            if "year" in k:
                self.year = int(v)
            else:
                setattr(self, k, v)
