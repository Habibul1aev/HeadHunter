from rest_framework import serializers

from account.models import User
from headhunter.models import Work, Category, Country, City, Skills


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = {
            'id',
            'first_name',
            'last_name',
            'phone',
            'email'
        }


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('created_at', 'updated_at')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        exclude = ('created_at', 'updated_at')


class CitySerializer(serializers.ModelSerializer):
    countries = CountrySerializer()
    class Meta:
        model = City
        exclude = ('created_at', 'updated_at')


class AddressSerializer(serializers.ModelSerializer):
    country_city = CitySerializer()
    class Meta:
        model = Country
        exclude = ('created_at', 'updated_at')



class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        exclude = ('created_at', 'updated_at')


class WorkListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    skills = SkillSerializer(many=True)
    user = UserSerializer()
    country = CountrySerializer()
    city = CitySerializer()
    address = AddressSerializer()

    class Meta:
        model = Work
        exclude = ('created_at', 'updated_at')

class WorkDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    skills = SkillSerializer(many=True)
    user = UserSerializer()
    country = CountrySerializer()
    city = CitySerializer()
    address = AddressSerializer()

    class Meta:
        model = Work
        fields = '__all__'

class WorkUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Work
        exclude = ('user', 'created_at', 'updated_at')

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Цена не может быть отрицательной')
        return value

class WorkCreatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Work
        exclude = ('user', )

    def create(self, validated_data):
        skill = validated_data.pop('skill')

        validated_data['user'] = self.context['request'].user

        work = super().create(validated_data)
        work.skill.add(*skill)






