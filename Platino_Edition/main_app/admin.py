from django.contrib import admin
from .models import Car, Realestate, Jet, Yacht, Multimg, Booking

# Register your models here.
# admin.site.register(Car)
# admin.site.register(Realestate)
# admin.site.register(Jet)
# admin.site.register(Yacht)
admin.site.register(Booking)


# multiple cars image 
class CarImageAdmin(admin.StackedInline):
    model = Multimg

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageAdmin]

    class Meta:
        model = Car

# multiple realestates image 
class RealestateImageAdmin(admin.StackedInline):
    model = Multimg

@admin.register(Realestate)
class RealestateAdmin(admin.ModelAdmin):
    inlines = [RealestateImageAdmin]

    class Meta:
        model = Realestate

# multiple jets image 
class JetImageAdmin(admin.StackedInline):
    model = Multimg

@admin.register(Jet)
class JetAdmin(admin.ModelAdmin):
    inlines = [JetImageAdmin]

    class Meta:
        model = Jet


# multiple yachts image 
class YachtImageAdmin(admin.StackedInline):
    model = Multimg

@admin.register(Yacht)
class YachtAdmin(admin.ModelAdmin):
    inlines = [YachtImageAdmin]

    class Meta:
        model = Yacht













@admin.register(Multimg)
class MultimgAdmin(admin.ModelAdmin):
    pass
