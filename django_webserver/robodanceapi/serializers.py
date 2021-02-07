from rest_framework import serializers
from .models import Robot, DanceOff


def create_model(danceoff):
    winner = danceoff.get('winner')
    opponents = danceoff.get('opponents')
    # find loser
    loser = opponents[1] if winner == opponents[0] else opponents[0]
    new_danceoff = DanceOff(winner=winner, loser=loser)
    new_danceoff.save()
    return new_danceoff


def validate_opponents(opponents):
    if len(opponents) == 2 and opponents[0] == opponents[1]:
        raise serializers.ValidationError(
            "Opponents must be two distinctive robots")


class DanceOffListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        danceoffs = [create_model(item) for item in validated_data]
        return danceoffs


class DanceOffSerializer(serializers.ModelSerializer):
    opponents = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(queryset=Robot.objects.all()),
        write_only=True,
        min_length=2,
        max_length=2,
        validators=[validate_opponents])

    class Meta:
        model = DanceOff
        fields = '__all__'
        read_only_fields = ['id', 'loser', 'dancedAt']
        list_serializer_class = DanceOffListSerializer

    def create(self, validated_data):
        return create_model(validated_data)

    def validate(self, data):
        opponents = data.get('opponents')
        winner = data.get('winner')
        if winner not in opponents:
            raise serializers.ValidationError(
                'Winner must be one of the opponents')
        return data


class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = '__all__'
