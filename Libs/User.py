from App.models import UserData


class UserLib:

    # This is description for this function. Thats very very long
    # use:
    # You can use that for create or edit user

    def UserEdit(self):
        print('\033[93m' + 'This is the first library!');
        return 1




    # This is description for this function. Thats very very long
    # use:
    # You can use that for create or edit user

    def GetUserData(self, user, item):
        query = UserData.objects.get(Username = user)

        return getattr(query,item)




    # This is description for this function. Thats very very long
    # use:
    # You can use that for create or edit user

    def SetUserData(self, user, data):
        UserData.objects.filter(Username= user).update(**data)

    def CreateUser(self, data):
        data = UserData.objects.create(**data)
        data.save()


