from .django.db import ModelSerializer


class FAQ(models.Model):
    question models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):




class MenuCategorySerializer(serializer.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id','name']



        

class MenuCategorySerializer(serializer.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', name','description','price', 'image' 'is_available']   # Only essential details
         