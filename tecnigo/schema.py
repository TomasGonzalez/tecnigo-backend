import graphene

from graphene_django.types import DjangoObjectType

from tecnigo.models import TecnicalSupportStaff

class TecnicalSupportStaffType(DjangoObjectType):
    class Meta:
        model = TecnicalSupportStaff 

class Query(object):
    all_TexnicalSupportStaffType = graphene.List(TecnicalSupportStaffType)

    def resolve_all_TecnicalSupportStaff(self,info, **kwargs):
        return Category.objects.all()

