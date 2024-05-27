from rest_framework import serializers


# Mapper createUser
class UserCreateSerializer(serializers.Serializer):

    name = serializers.CharField(required=True, max_length=200)
    privilege = serializers.IntegerField(required=True, max_value=60000)
    password = serializers.CharField(required=True, max_length=200)
    # group_id = serializers.CharField(required=False, max_length=200)
    # card = serializers.IntegerField(max_value=300)


# mapper update
class UserUpdateSerializer(serializers.Serializer):
    uid = serializers.IntegerField(required=True, max_value=5000)
    name = serializers.CharField(required=True, max_length=200)
    privilege = serializers.IntegerField(required=True, max_value=60000)
    password = serializers.CharField(required=True, max_length=200)


# Maper getUser
class UserGetSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(max_value=100)
    uid = serializers.IntegerField(required=True, max_value=5000)
    name = serializers.CharField(required=True, max_length=200)
    privilege = serializers.IntegerField(required=True, max_value=60000)
    password = serializers.CharField(required=True, max_length=200)


# Maper DeletUser
class UserDeleteSerializer(serializers.Serializer):
    uid = serializers.IntegerField(required=True)


#Mapper atendances
class AttendanceSerializer(serializers.Serializer):
    uid = serializers.IntegerField(required=True, max_value=6000)
    user_id = serializers.CharField(required=True, max_length=100)
    timestamp = serializers.DateTimeField()
    # Which is check-in = 0, check-out = 1, Break-out = 2,
    # Break-in = 3, Overtime-in = 4 and Overtime-in = 5
    punch = serializers.IntegerField(max_value=100)
    # currently if u are check in finger it status =0 or
    # if u checked on face status = 15 and pwd status = 3
    status = serializers.CharField(max_length=199)

