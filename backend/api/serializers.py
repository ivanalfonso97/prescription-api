from rest_framework import serializers

class UserPrescriptionInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='prescription-detail',
        lookup_field='pk',
        read_only=True
    )
    patient_name = serializers.CharField(read_only=True)

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    other_prescriptions = serializers.SerializerMethodField(read_only=True)

    def get_other_prescriptions(self, obj):
        print(obj)
        user = obj
        my_prescriptions_queryset = user.prescription_set.all()[:5]
        return UserPrescriptionInlineSerializer(my_prescriptions_queryset, many=True, context=self.context).data