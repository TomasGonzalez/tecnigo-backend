import graphene

from graphene_django.types import DjangoObjectType

from tecnigo.models import TecnicalSupportStaff


class TecnicalSupportStaffType(DjangoObjectType):
    class Meta:
        model = TecnicalSupportStaff


class Query(graphene.ObjectType):
    all_tecnical_support_staff = graphene.List(TecnicalSupportStaffType)

    def resolve_all_tecnical_support_staff(self, info, **kwargs):
        return TecnicalSupportStaff.objects.all()


class CreateTecnicalSupportStaff(graphene.Mutation):
    supportStaff = graphene.Field(TecnicalSupportStaffType)

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String()
        age = graphene.Int()
        address = graphene.String()
        profession = graphene.String()
        cell_phone = graphene.Int()
        phone = graphene.Int()
        education = graphene.String()
        story = graphene.String()
        phone_os = graphene.Int()  # where = 0 is android and 1 ios
        home_location_longitude = graphene.Float()
        home_location_latitude = graphene.Float()
        q1_answer = graphene.String()

    def mutate(
        self,
        info,
        first_name,
        last_name,
        age,
        address,
        profession,
        cell_phone,
        phone,
        education,
        story,
        phone_os,
        home_location_longitude,
        home_location_latitude,
        q1_answer,
        **kwargs
    ):
        supportStaff = TecnicalSupportStaff(
            first_name=first_name,
            last_name=last_name,
            age=age,
            address=address,
            profession=profession,
            cell_phone=cell_phone,
            phone=phone,
            education=education,
            story=story,
            phone_os=phone_os,
            home_location_longitude=home_location_longitude,
            home_location_latitude=home_location_latitude,
            q1_answer=q1_answer,
        )

        supportStaff.save()
        return CreateTecnicalSupportStaff(supportStaff=supportStaff)


class Mutation(graphene.ObjectType):
    create_tecnical_support_staff = CreateTecnicalSupportStaff.Field()
