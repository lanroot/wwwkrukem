from haystack import indexes
from userdir.models import Person, Div

class PersonIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    pri = indexes.CharField(model_attr='div__pri')
    email = indexes.CharField(model_attr='email')
    name = indexes.CharField(model_attr='name')
    pers_id = indexes.CharField(model_attr='pers_id')
#    div_id = indexes.CharField(model_attr='div_id')
#    div = indexes.CharField(model_attr='div')
    div = indexes.CharField(model_attr='div')

    content_auto = indexes.EdgeNgramField(use_template=True)

    def get_model(self):
        return Person

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
#        return self.get_model().objects.filter(visible=1).order_by('email')
#        return self.get_model().objects.filter(visible=1).order_by('div_pri')
        return self.get_model().objects.filter(visible=1)
