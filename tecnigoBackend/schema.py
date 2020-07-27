import graphene

import tecnigo.schema


class Query(tecnigo.schema.Query, graphene.ObjectType):
    pass


class Mutation(tecnigo.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
