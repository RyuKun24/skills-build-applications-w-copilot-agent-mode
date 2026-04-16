from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class ObjectIdStringModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if 'id' in representation and representation['id'] is not None:
            representation['id'] = str(representation['id'])

        for field_name, field in self.fields.items():
            if field_name not in representation or representation[field_name] is None:
                continue

            if isinstance(field, serializers.PrimaryKeyRelatedField):
                value = representation[field_name]
                if isinstance(value, list):
                    representation[field_name] = [str(item) if item is not None else None for item in value]
                else:
                    representation[field_name] = str(value)

        return representation


class TeamSerializer(ObjectIdStringModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class UserSerializer(ObjectIdStringModelSerializer):
    class Meta:
        model = User
        fields = tuple(
            field.name for field in User._meta.fields
            if field.name not in {'is_staff', 'is_superuser'}
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class ActivitySerializer(ObjectIdStringModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class LeaderboardSerializer(ObjectIdStringModelSerializer):
    class Meta:
        model = Leaderboard
        fields = '__all__'


class WorkoutSerializer(ObjectIdStringModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'
