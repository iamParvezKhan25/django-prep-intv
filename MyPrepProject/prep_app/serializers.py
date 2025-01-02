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
