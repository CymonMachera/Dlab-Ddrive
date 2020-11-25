from rest_framework import serializers

from account.models import CustomUser

class HomeSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=120)
    pillars = serializers.CharField(max_length = 120)
    role = serializers.CharField(max_length = 120)

    # user = CustomUser.objects.all()

    # #clean the pillar names from query to normal list
    # temp_pillar = list(user.pillar.all().values('name'))
    # temp_pillar = [f['name'] for f in temp_pillar]
    # validation = {
    #     'role': user.roles,
    #     'pillars':temp_pillar,
    #     'full_name': user.get_full_name()
    # }
