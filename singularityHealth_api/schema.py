import graphene

import registered_users.schema

class Query(
    registered_users.schema.Query,
    graphene.ObjectType):
    pass


class Mutation(
    registered_users.schema.Mutation,
    graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
