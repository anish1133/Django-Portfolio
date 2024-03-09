from django.db import models
from ckeditor.fields import RichTextField


class UserDetails(models.Model):
    intro = models.CharField(max_length=30, blank=True, verbose_name="Introduction")
    name = models.CharField(max_length=50)
    dev_domain = models.CharField(max_length=50, blank=True)
    bio = models.TextField(default="", blank=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to="", blank=True)
    hire_me = models.CharField(max_length=255, default="Hire Me", null=True)
    resume = models.URLField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "User Section"

    def __str__(self):
        return self.name


class AboutMe(models.Model):
    """This class contains all the school degree and college degree section"""

    """Education-1"""
    branch = models.CharField(
        max_length=300, blank=True, null=True, help_text="eg: computer science"
    )
    college = models.CharField(
        max_length=300, blank=True, null=True, help_text="eg: IIT Delhi"
    )
    college_description = models.CharField(
        max_length=300, blank=True, null=True, help_text="eg: about the college"
    )
    duration = models.CharField(
        max_length=50, blank=True, null=True, help_text="eg: 2021-2025"
    )
    college_location = models.CharField(
        max_length=300, blank=True, null=True, help_text="eg: Delhi"
    )
    country = models.CharField(
        max_length=300, blank=True, null=True, help_text="eg:India"
    )
    grade_col = models.CharField(
        max_length=10, blank=True, null=True, help_text="your cgpa"
    )
    """Education-2"""
    school = models.CharField(
        max_length=300, blank=True, null=True, help_text="eg:DPS RK puram"
    )
    stream = models.CharField(
        max_length=300, blank=True, null=True, help_text="eg:Pure Science"
    )
    school_location = models.CharField(
        max_length=300, blank=True, null=True, help_text="eg:Delhi"
    )
    duration1 = models.CharField(
        max_length=50, blank=True, null=True, help_text="eg: 2018-2020"
    )
    grade1 = models.CharField(max_length=50, blank=True, help_text="eg: 77.6%")
    """Education-3"""
    school1 = models.CharField(
        max_length=300, blank=True, null=True, help_text="For Matriculation Section"
    )
    stream1 = models.CharField(max_length=300, blank=True, null=True, help_text="eg:")
    duration2 = models.CharField(max_length=50, blank=True, null=True, help_text="eg:")
    school_location1 = models.CharField(
        max_length=300, blank=True, null=True, help_text="eg:"
    )
    grade2 = models.CharField(max_length=50, blank=True, help_text="eg:")
    Achievement1 = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="eg: your achievements till date",
    )
    Achievement2 = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="eg: your achievements till date",
    )
    Achievement3 = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="eg: your achievements till date",
    )
    Achievement4 = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="eg: your achievements till date",
    )
    resume = models.URLField(blank=True, null=True, help_text="google drive link")

    class Meta:
        verbose_name_plural = "About Me Section"

    def __str__(self):
        return self.branch


class ServicesOffered(models.Model):
    icon_image = models.ImageField(upload_to="services")
    service_name = models.CharField(max_length=40, blank=True, null=True)
    shadow_icon = models.CharField(max_length=40, blank=True, null=True)
    service_description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Services Section"


class LanguagesSkills(models.Model):
    EXP_CHOICES = (
        ("Beginner", "Beginner"),
        ("Junior", "Junior"),
        ("Intermediate", "Intermediate"),
        ("Experienced", "Experienced"),
    )

    icon = models.CharField(
        max_length=1000, blank=True, verbose_name="language Icon Image:(icons8.com)"
    )
    lang_name = models.CharField(
        max_length=100, blank=True, verbose_name="Language Name"
    )
    exp_level = models.CharField(
        max_length=200, blank=True, choices=EXP_CHOICES, verbose_name="Experience Level"
    )

    class Meta:
        verbose_name_plural = "Skills Section"

    def __str__(self):
        return self.lang_name


class Project(models.Model):
    language_used = models.CharField(max_length=100, blank=True, null=True)
    Project_Image = models.ImageField(blank=True, null=True)
    updated_on = models.DateTimeField(
        auto_now_add=False, null=True, auto_now=True, blank=True
    )
    Project_title = models.CharField(max_length=90, blank=True, null=True)
    Project_info = models.TextField(blank=True, null=True)
    project_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Projects Section"

    def __str__(self):
        return self.Project_title


class SocialMediaLinks(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    social_icon = models.CharField(
        max_length=60, blank=True, null=True, verbose_name="Icon (eg: fa -fa-twitter)"
    )

    class Meta:
        verbose_name_plural = "Social Media Links"

    def __str__(self):
        return self.social_icon
