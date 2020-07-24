import graphene

from graphene_django.types import DjangoObjectType

from tecnigo.models import TecnicalSupportStaff

class TecnicalSupportStaffType(DjangoObjectType):
    class Meta:
        model = TecnicalSupportStaff 

class Query(graphene.ObjectType):
    all_tecnical_support_staff = graphene.List(TecnicalSupportStaffType)

    def resolve_all_tecnical_support_staff(self,info, **kwargs):
        return TecnicalSupportStaff.objects.all()

