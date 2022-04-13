import graphene
import graphql_jwt

import myapp.schema



class AuthMutation(myapp.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()



class Query(myapp.schema.Query, graphene.ObjectType):
    pass



class Mutation(AuthMutation, graphene.ObjectType):
       pass
   
   
schema = graphene.Schema( query=Query,  mutation=Mutation)