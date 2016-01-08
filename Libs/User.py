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

    def GetUserData(self):
        query = UserData.objects.get(Username = "Pati")

        return query.Photos




    # This is description for this function. Thats very very long
    # use:
    # You can use that for create or edit user

    def SetUserData(self, data):
        UserData.objects.filter(Username="Patrycja").update(**data)
        return 1

