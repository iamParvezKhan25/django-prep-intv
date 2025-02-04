from rest_framework import serializers

'''
API Class 
'''


class ATMWithdrawalSerializer(serializers.Serializer):
    atm_pin = serializers.CharField(min_length=6, max_length=6)
    amount = serializers.IntegerField()

    def validate(self, data):
        amount = data.get('amount')

        if amount % 100 != 0:
            raise serializers.ValidationError({"amount": "Amount must be a multiple of 100."})
        if amount < 100 or amount > 1000:
            raise serializers.ValidationError({"amount": "Amount must be between 100 and 1000."})
        return data


'''
Add a custom validation method in the serializer to ensure that the title of a blog post is unique
'''
from prep_app.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

    def validate_title(self, value):
        if BlogPost.objects.filter(title=value).exists():
            raise serializers.ValidationError("Title must be unique.")
        return value