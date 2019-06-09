#Django native imports
from django.db import models
from django.urls import reverse, reverse_lazy

# Import from our apps


def save_directory_path(instance, filename):
    return '{0}/{1}/{2}'.format("netdev", instance.netdev_model, filename)

class Netdev(models.Model):

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, default=None)

    # Model
    device_type = models.CharField("Device type", max_length=30)
    brand = models.CharField("Brand", max_length=20)
    netdev_model = models.CharField("Model", max_length=20)
    generation = models.CharField("Generation", max_length=5, blank=True, default=None)
    manufacture_year = models.IntegerField("Year of manufacture", blank=True, default=None)
    os = models.CharField("Device image", max_length=100, default=None, blank=True)
    port_number = models.IntegerField("Number of physical network ports")
    port_description = models.CharField("Port description", max_length=50)
    serial_number = models.CharField("Serial number", max_length=30, blank=True, default=None)
    warranty = models.CharField("Warranty status", max_length=100)
    condition = models.CharField("Condition", max_length=100)
    file_picture_1 = models.FileField("Front Picture",blank=True, default=None, upload_to=save_directory_path)
    file_picture_2 = models.FileField("Back Picture",blank=True, default=None, upload_to=save_directory_path)
    file_other = models.FileField("Other file/Zip file if many", blank=True, default=None, upload_to=save_directory_path)
    other = models.TextField("Notes", max_length=2000)

    def __str__(self):
        return "{} {}".format(self.device_type, self.netdev_model)

    def get_absolute_url(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('netdev_detail', args=[str(self.pk)])

    def get_detail(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('netdev_detail', args=[str(self.pk)])
    
    def get_item(self):
        item_name = self.__str__()
        return item_name

    def get_class(self):
        """
        Handy way of getting the class of the object for the html templates
        """
        class_name = "Network Device"
        return class_name


    class Meta:
        verbose_name_plural = "Network Devices"
