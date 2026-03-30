from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super().__init__(*args, **kwargs) #Calls the parents init --> runs the chain up till the first parent. Orderfield --> Positiveintegerfield --> integerField --> Filed

    def pre_save(self, model_instance, add):
        #gettattr takes a key to check for value. does model_instamce.attname (so there should be an att name colume)
        if getattr(model_instance, self.attname) is None: #is none if its a foreign key field not a normal field
        # no current value
            try:
                qs = self.model.objects.all()
                if self.for_fields:
                # filter by objects with the same field values
                # for the fields in "for_fields"
                    query = {
                    field: getattr(model_instance, field) # getattr(module, 'course'), Checks the field before saving, returns a py course object with that field
                    for field in self.for_fields
                    }
                    qs = qs.filter(**query)
                    # get the order of the last item
                    last_item = qs.latest(self.attname)
                    value = getattr(last_item, self.attname) + 1
            except ObjectDoesNotExist:
                value = 0
                setattr(model_instance, self.attname, value)
            
            return value
        else:
            return super().pre_save(model_instance, add)