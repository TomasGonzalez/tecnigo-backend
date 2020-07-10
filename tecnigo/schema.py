import graphene

from graphene_django.types import DjangoObjectType

from tecnigo.models import TecnicalSupportStaff

class TecnicalSupportStaffType(DjangoObjectType):
    class Meta:
        model = Ingredient

class Query(object):
    all_TexnicalSupportStaffType = graphane.List(TecnicalSupportStaffType)

    def resolve_all_TecnicalSupportStaff(self,info, **kwargs):
        return Category.objects.all()

