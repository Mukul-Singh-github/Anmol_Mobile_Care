from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category   = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    brand_name = models.CharField(max_length=50)

    def __str__(self):
        return  self.category.name +" "+self.brand_name

class Image(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    img1 = models.ImageField(upload_to='static/Images')
    img2 = models.ImageField(upload_to='static/Images')
    img3 = models.ImageField(upload_to='static/Images', blank=True)
    img4 = models.ImageField(upload_to='static/Images', blank=True)
    img5 = models.ImageField(upload_to='static/Images', blank=True)
    img6 = models.ImageField(upload_to='static/Images', blank=True)

    def __str__(self):
        return "Product Images: "+ self.subcategory.brand_name +" "+self.subcategory.category.name


class Camera(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    primary_cam = models.CharField(max_length=100)
    primary_cam_features = models.TextField()
    secondary_cam = models.CharField(max_length=100)
    secondary_cam_features = models.TextField()
    flash = models.CharField(max_length=50)
    video_rec_resolution = models.TextField()
    frame_rate = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return "Camera Features: "+ self.subcategory.brand_name +" "+self.subcategory.category.name

class Processor(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    os = models.CharField(max_length=50)
    processor = models.CharField(max_length=100)
    clock_speed = models.CharField(max_length=100)
    processor_core = models.CharField(max_length=50)

    def __str__(self):
        return "Processor Details: "+ self.subcategory.brand_name +" "+self.subcategory.category.name

class Display(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    display_dimension = models.CharField(max_length=50)
    resolution = models.CharField(max_length=50)
    gpu = models.CharField(max_length=50)
    graphics_ppi = models.CharField(max_length=30 , blank=True)

    def __str__(self):
        return "Display Details: "+ self.subcategory.brand_name +" "+self.subcategory.category.name

class Memory(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    internal_memory = models.CharField(max_length=20)
    ram = models.CharField(max_length=50)
    expandable_storage = models.CharField(max_length=50)
    microsd = models.CharField(max_length=50)

    def __str__(self):
        return "Memory Details: "+ self.subcategory.brand_name +" "+self.subcategory.category.name

class OtherDetail(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    touchscreen_type = models.CharField(max_length=50)
    sim_count        = models.CharField(max_length=30,null=True, blank=True)
    sim_size         =  models.CharField(max_length=50)
    ui               = models.CharField(max_length=50)
    sensors          = models.CharField(max_length=200)
    gps_type         = models.CharField(max_length=100, blank=True)
    fingerprint      = models.CharField(max_length=10, blank=True)
    fingerprint_type = models.CharField(max_length=50, blank=True)
    call_recording   = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return "Other Details: "+ self.subcategory.brand_name +" "+self.subcategory.category.name


class Mobile(models.Model):
    category    = models.ForeignKey(Category,   on_delete=models.CASCADE,null=True)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,null=True)
    img         = models.ForeignKey(Image ,     on_delete=models.CASCADE, null=True, blank=True)
    camera      = models.ForeignKey(Camera,     on_delete=models.CASCADE, null=True, blank=True)
    processor   = models.ForeignKey(Processor,  on_delete=models.CASCADE, null=True, blank=True)
    display     = models.ForeignKey(Display,    on_delete=models.CASCADE, null=True, blank=True)
    memory      = models.ForeignKey(Memory,     on_delete=models.CASCADE, null=True, blank=True)
    other_detail= models.ForeignKey(OtherDetail,on_delete=models.CASCADE, null=True, blank=True)
    brand       = models.CharField(max_length=50)
    model_no    = models.CharField(max_length=50)
    description = models.TextField()
    price       = models.IntegerField()
    offer       = models.BooleanField()
    rate        = models.CharField(max_length=5)
    warranty    = models.CharField(max_length=100,null=True, blank=True)

    #HEADPHONES SPECIFIC
    connector_size  = models.CharField(max_length=15, blank=True, null=True)
    driver_size     = models.CharField(max_length=15, blank=True, null=True)
    with_mic        = models.CharField(max_length=10, blank=True, null=True)
    connectivity    = models.CharField(max_length=30, blank=True, null=True)
    bluetooth_range = models.CharField(max_length=15, blank=True, null=True)
    charging_time   = models.CharField(max_length=15, blank=True, null=True)
    play_time       = models.CharField(max_length=15, blank=True, null=True)

    #CHARGER SPECIFIC
    fast_charging	= models.CharField(max_length=50, blank=True, null=True)
    designed_for	= models.CharField(max_length=50, blank=True, null=True)
    connector_type	= models.CharField(max_length=50, blank=True, null=True)
    cable_included	= models.CharField(max_length=50, blank=True, null=True)
    output_current	= models.CharField(max_length=50, blank=True, null=True)
    number_of_connector	= models.CharField(max_length=50, blank=True, null=True)

    #ACCESSORY SPECIFIC
    material         = models.CharField(max_length=15, blank=True, null=True)
    flexible         = models.CharField(max_length=15, blank=True, null=True)
    compatible_brand = models.CharField(max_length=30, blank=True, null=True)
    compatible_model = models.CharField(max_length=50, blank=True, null=True)
    capacity         = models.CharField(max_length=30, blank=True, null=True)


    def __str__(self):
        return self.category.name +": "+ self.brand +" "+ self.model_no+" "
