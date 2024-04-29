from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=100)
    # uid = serializers.IntegerField(required=True, max_value=5000)
    name = serializers.CharField(required=True, max_length=200)
    privilege = serializers.IntegerField(required=True, max_value=60000)
    password = serializers.CharField(required=True, max_length=200)
    # group_id = serializers.CharField(required=False, max_length=200)

    # card = serializers.IntegerField(max_value=300)


class UserDeleteSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=True, max_value=5000)


class AttendanceSerializer(serializers.Serializer):
    uid = serializers.IntegerField(required=True, max_value=60000)
    user_id = serializers.CharField(required=True, max_length=100)
    timestamp = serializers.DateTimeField()
    # Which is check-in = 0, check-out = 1, Break-out = 2,
    # Break-in = 3, Overtime-in = 4 and Overtime-in = 5
    punch = serializers.CharField(max_length=100)
    # currently if u are check in finger it status =0 or
    # if u checked on face status = 15 and pwd status = 3
    status = serializers.CharField(max_length=199)
