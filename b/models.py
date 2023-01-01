from django.db import models
from django.urls import reverse


##################################### PASTOR HOME PAGE WELCOME SPEECH ####################

class Welcome_Speech(models.Model):
    welcome_speech = models.TextField( verbose_name='WELCOME SPEECH')
    Ending_speech = models.TextField(verbose_name='ENDING SPEECH')
    ministry_name = models.CharField(max_length=500)
    ministry_address = models.CharField(max_length=500)
    ministry_city = models.CharField(max_length=100)
    ministry_state = models.CharField(max_length=25)
    ministry_country = models.CharField(max_length=25)
    minister_name = models.CharField(max_length=200, default="Pastor SAMUEL Ajayi")
    minister_email = models.EmailField(default="admin@jesus.com")

    class Meta:
        verbose_name_plural = 'HOME PAGE PASTORAL ADDRESS'

    def __str__(self):
        return self.ministry_name

##################################################################################################################################

class Category(models.Model):
    title = models.CharField(max_length=200)
    category_image = models.ImageField(upload_to='Category/img/')

    class Meta:
        verbose_name_plural = 'CATEGORY'

    def __str__(self):
        return self.title


class Video(models.Model):
    name = models.CharField(max_length=555)
    videofile = models.FileField(upload_to='Videos/messages', null=True,)


    def __str__(self):
        return self.name



class Services(models.Model):
    img = models.ImageField(upload_to='Service/img')
    img_pst = models.ImageField(upload_to='Service/pastor', verbose_name='PASTOR PICTURE', blank=True,null=True)
 #   category = models.ForeignKey(Category, on_delete=models.CASCADE)
    d = models.CharField(max_length=4, verbose_name='Day')
    sup = models.CharField(max_length=2, verbose_name='e.g st, nd, rd, th ')
    m = models.CharField(max_length=15, verbose_name='Month')
    y = models.CharField(max_length=4, verbose_name='Year')
    Theme = models.CharField(max_length=678)
    Theme_reference = models.CharField(max_length=899)
    bible = models.CharField(max_length=79)
    message = models.TextField( verbose_name='MESSAGES')


    def __str__(self):
        return self.Theme

    class Meta:
        verbose_name_plural = 'MESSAGES HERE'

Foundation = (
        ('Yes', 'Yes'),
        ('No','No'),
)

BORN_AGAIN = (
        ('Yes', 'Yes'),
        ('NO','No'),
)

MARITAL = (
    ('Married', 'Married'),
    ('Single', 'Single'),
    ('Widowed', 'Widowed'),
    ('Separated', 'Separated'),
    ('Divorced', 'Divorced'),
)
Job = (
    ('Day', 'Day'),
    ('Night', 'Night'),
    ('Shift', 'Shift'),
    ('Sunday', 'Sunday'),
)


class USHERING(models.Model):
    full_name = models.CharField(max_length=125)
    residence = models.CharField(max_length=678)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    born_again = models.CharField(choices=BORN_AGAIN,max_length=3)
    joined_date = models.DateField()
    new_birth_date = models.DateField()
    occupation = models.CharField(max_length=678)
    foundation_class = models.CharField(choices=Foundation, max_length=15)
    job = models.CharField(max_length=7, choices=Job)
    status = models.CharField(max_length=9, choices=MARITAL)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'USHERING UNIT'

Foundation = (
        ( 'Yes', 'Yes'),
        ( 'No','No'),
)

BORN_AGAIN= (
        ( 'Yes', 'Yes'),
        ( 'NO','No'),
)

MARITAL = (
    ('Married', 'Married'),
    ('Single', 'Single'),
    ('Widowed', 'Widowed'),
    ('Separated', 'Separated'),
    ('Divorced', 'Divorced'),
)
Job = (
    ('Day', 'Day'),
    ('Night', 'Night'),
    ('Shift', 'Shift'),
    ('Sunday', 'Sunday'),
)


class TECHNICAL(models.Model):
    full_name = models.CharField(max_length=125)
    residence = models.CharField(max_length=678)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    born_again = models.CharField(choices=BORN_AGAIN,max_length=3)
    joined_date = models.DateField()
    new_birth_date = models.DateField()
    occupation = models.CharField(max_length=678)
    foundation_class = models.CharField(choices=Foundation, max_length=15)
    job = models.CharField(max_length=7, choices=Job)
    status = models.CharField(max_length=9, choices=MARITAL)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'TECHNICAL UNIT'

class SPIRITUAL(models.Model):
    img = models.ImageField(upload_to='spiritual/week')
    m_y = models.CharField(max_length=798, verbose_name='MONTH & YEAR')
    start = models.CharField(max_length=700, verbose_name='STARTING DATE')
    end = models.CharField(max_length=700, verbose_name='ENDING DATE')
    year = models.CharField(max_length=700, verbose_name='YEAR')
    remark_1 = models.CharField(max_length=999, verbose_name='SHORT COMMENT', blank=True)
    remark_2 = models.CharField(max_length=999, verbose_name='THEME OF THE YEAR', blank=True)

    class Meta:
        verbose_name_plural = 'SPIRITUAL WEEK OF EMPHASIS'

class PROPHET_FOCUS(models.Model):
    img = models.ImageField(upload_to='prophetic/month')
    month =  models.CharField(max_length=345)
    year = models.BigIntegerField()
    theme = models.CharField(max_length=345)
    reference = models.CharField(max_length=202)
    body = models.TextField(verbose_name='BODY')
    book = models.TextField( verbose_name='BOOKS of THE Month')


    class Meta:
        verbose_name_plural = 'PROPHETIC FOCUS'

    def __str__(self):
        return self.month

class WSF(models.Model):
    location = models.CharField(max_length=333)
    centre = models.CharField(max_length=666)
    residence = models.CharField(max_length=999)
    Host = models.CharField(max_length=777)
    minister = models.CharField(max_length=888)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.location

    class Meta:
        verbose_name_plural = 'WSF'
class Recommended_Books_Time(models.Model):
    month = models.CharField(max_length=17, null=True)
    year = models.CharField(max_length=17, null=True)

    def __str__(self):
        return self.month

    class Meta:
        verbose_name_plural = ' RECOMMENDED BOOKS MONTH and YEAR'

class Recommended_Books(models.Model):
    book_img = models.ImageField(upload_to='month/book/img')
    book_title = models.CharField(max_length=799)
    book_body = models.TextField(verbose_name='BOOK BODY')

    def __str__(self):
        return self.book_title

    class Meta:
        verbose_name_plural = ' RECOMMENDED BOOKS'



class BOOKS_of_the_Months(models.Model):
    name = models.CharField(max_length=890)
    book = models.CharField(max_length=700)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'BOOKS OF THE MONTH'




CALL_CHOICES = (
        ( 'Yes', 'Yes'),
        ( 'NO','No'),
)
PRAYER_OPTION = (
        ( 'Myself','Myself'),
        ('Spouse', 'Spouse'),
        ('Child', 'Child'),
        ('Friend', 'Friend'),
        ('Sibling', 'Siblings')
)

class Praye(models.Model):
    msg_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=489, help_text="YOUR FULLNAME")
    residential = models.CharField(max_length=1000)
    email = models.EmailField()
    phone = models.IntegerField()
    church = models.CharField(max_length=333)
    city = models.CharField(max_length=100)
    call = models.CharField(verbose_name="Will You Want a Call Back?", max_length=3, choices=CALL_CHOICES)
    pray_for = models.CharField(verbose_name="This prayer is for", max_length=8, choices=PRAYER_OPTION)
    prayer = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'PRAYER REQUEST'


class Testimony(models.Model):
    msg_id = models.AutoField(primary_key=True)
    t_img = models.ImageField(upload_to='Test/img', verbose_name="Testifier Image")
    t_month = models.CharField(max_length=50, verbose_name="Testimony Month")
    t_day = models.IntegerField(verbose_name="Testimony Day")
    t_year = models.BigIntegerField(verbose_name="Testimony Year")
    t_name = models.CharField(max_length=999, verbose_name="Testifier Name")
    t_title = models.CharField(max_length=200, verbose_name="Testimony Title")
    t_body = models.TextField( verbose_name="TESTIMONY")

    class Meta:
        verbose_name_plural = "TESTIMONY"


class WOFBI(models.Model):
    img = models.ImageField(upload_to='Wofbi/img', verbose_name="WOFBI Image")
    jbs_title = models.CharField(max_length=99, blank=True)
    jbs_st_dt = models.CharField(max_length=99, verbose_name='JBS (START DATE)', blank=True)
    jbs_st_sup = models.CharField(max_length=4, verbose_name='JBS (e.g th, nd, st)', blank=True)
    jbs_sp_dt = models.CharField(max_length=99, verbose_name='JBS (STOP DATE)', blank=True)
    jbs_sp_sup = models.CharField(max_length=4, verbose_name='JBS (e.g th, nd, st)', blank=True)
    jbs_orient = models.CharField(max_length=222, verbose_name='JUNIOR BIBLE SCHOOL (JBS) Orientation Date', blank=True)
    jbs_orient_sup = models.CharField(max_length=5, verbose_name='JBS Orientation (e.g th, nd, st)', blank=True)
    jbs_orient_remark = models.CharField(max_length=222, verbose_name='JBS Orientation Remark', blank=True)
    jbs_resume = models.CharField(max_length=222,  verbose_name='JBS Resumption Date', blank=True)
    jbs_resume_sup = models.CharField(max_length=6, verbose_name='JBS Resumption (e.g th, nd, st)', blank=True)
    jbs_resume_remark = models.CharField(max_length=222, verbose_name='JBS Resumption Remark', blank=True)
    jbs_graduate = models.CharField(max_length=222, verbose_name='JBS Graduation Date', blank=True)
    jbs_graduate_sup = models.CharField(max_length=5, verbose_name='JBS Graduation (e.g th, nd, st)', blank=True)
    jbs_graduate_remark = models.CharField(max_length=222, verbose_name='JBS Graduation Remark', blank=True)
    bcc_title = models.CharField(max_length=99, blank=True)
    bcc_st_dt = models.CharField(max_length=99, verbose_name='BCC (START DATE)', blank=True)
    bcc_st_sup = models.CharField(max_length=4, verbose_name='BCC (e.g th, nd, st)', blank=True)
    bcc_sp_dt = models.CharField(max_length=99, verbose_name='BCC (STOP DATE)', blank=True)
    bcc_sp_sup = models.CharField(max_length=4, verbose_name='BCC (e.g th, nd, st)', blank=True)
    bcc_orient = models.CharField(max_length=222, verbose_name='BASIC CERTIFICATE COURSE (BBC) Orientation Date', blank=True)
    bcc_orient_sup = models.CharField(max_length=5, verbose_name='BBC Orientation (e.g th, nd, st)', blank=True)
    bcc_orient_remark = models.CharField(max_length=222, verbose_name='BBC Orientation Remark', blank=True)
    bcc_resume = models.CharField(max_length=222, verbose_name='BBC Resumption Date', blank=True)
    bcc_resume_sup = models.CharField(max_length=6, verbose_name='BBC Resumption (e.g th, nd, st)', blank=True)
    bcc_resume_remark = models.CharField(max_length=222, verbose_name='BBC Resumption Remark', blank=True)
    bcc_graduate = models.CharField(max_length=222, verbose_name='BBC Graduation Date', blank=True)
    bcc_graduate_sup = models.CharField(max_length=5, verbose_name='BBC Graduation (e.g th, nd, st)', blank=True)
    bcc_graduate_remark = models.CharField(max_length=222, verbose_name='BBC Graduation Remark', blank=True)
    lcc_title = models.CharField(max_length=99, blank=True)
    lcc_st_dt = models.CharField(max_length=99, verbose_name='LCC (START DATE)', blank=True)
    lcc_st_sup = models.CharField(max_length=4, verbose_name='LCC (e.g th, nd, st)', blank=True)
    lcc_sp_dt = models.CharField(max_length=99, verbose_name='LCC (STOP DATE)', blank=True)
    lcc_sp_sup = models.CharField(max_length=4, verbose_name='LCC (e.g th, nd, st)', blank=True)
    lcc_orient = models.CharField(max_length=222, verbose_name='LEADERSHIP CERTIFICATE COURSE (LCC) Orientation Date', blank=True)
    lcc_orient_sup = models.CharField(max_length=5, verbose_name='LCC Orientation (e.g th, nd, st)', blank=True)
    lcc_orient_remark = models.CharField(max_length=222, verbose_name='LCC Orientation Remark', blank=True)
    lcc_resume = models.CharField(max_length=222, verbose_name='LCC Resumption Date', blank=True)
    lcc_resume_sup = models.CharField(max_length=6, verbose_name='LCC Resumption (e.g th, nd, st)', blank=True)
    lcc_resume_remark = models.CharField(max_length=222, verbose_name='LCC Resumption Remark', blank=True)
    lcc_graduate = models.CharField(max_length=222, verbose_name='LCC Graduation Date', blank=True)
    lcc_graduate_sup = models.CharField(max_length=5, verbose_name='LCC Graduation (e.g th, nd, st)', blank=True)
    lcc_graduate_remark = models.CharField(max_length=222, verbose_name='LCC Graduation Remark', blank=True)
    ldc_title = models.CharField(max_length=99, blank=True)
    ldc_st_dt = models.CharField(max_length=99, verbose_name='LDC (START DATE)', blank=True)
    ldc_st_sup = models.CharField(max_length=4, verbose_name='LDC (e.g th, nd, st)', blank=True)
    ldc_sp_dt = models.CharField(max_length=99, verbose_name='LDC (STOP DATE)', blank=True)
    ldc_sp_sup = models.CharField(max_length=4, verbose_name='LDC (e.g th, nd, st)', blank=True)
    ldc_orient = models.CharField(max_length=222, verbose_name='LEADERSHIP DIPLOMA COURSE (LDC) Orientation Date', blank=True)
    ldc_orient_sup = models.CharField(max_length=5, verbose_name='LDC Orientation (e.g th, nd, st)', blank=True)
    ldc_orient_remark = models.CharField(max_length=222, verbose_name='LDC Orientation Remark', blank=True)
    ldc_resume = models.CharField(max_length=222, verbose_name='LDC Resumption Date', blank=True)
    ldc_resume_sup = models.CharField(max_length=6, verbose_name='LDC Resumption (e.g th, nd, st)', blank=True)
    ldc_resume_remark = models.CharField(max_length=222, verbose_name='LDC Resumption Remark', blank=True)
    ldc_graduate = models.CharField(max_length=222, verbose_name='LDC Graduation Date', blank=True)
    ldc_graduate_sup = models.CharField(max_length=5, verbose_name='LDC Graduation (e.g th, nd, st)', blank=True)
    ldc_graduate_remark = models.CharField(max_length=222, verbose_name='LDC Graduation Remark', blank=True)

    class Meta:
        verbose_name_plural = "WOFBI"


class Book(models.Model):
    buk = models.CharField(max_length=999, verbose_name='BOOK')


class Bookshop(models.Model):

    BOOK_OPTION = (
        ('', '..CHOOSE..'),
        ('A', 'Anointing for Exploits'),
        ('B', ' Born to Win'),
        ('C', 'Conquering Controlling Powers'),
        ('D', 'The Riches of Redemption '),
        ('E', 'Possessing Your Possession'),
        ('F', 'All you Need to Have Your Needs Met'),
        ('G', 'In Pursuit of Vision'),
        ('H', 'Understanding Divine Direction'),
        ('I', 'Understanding Vision'),
        ('J', 'Following God’s Plan for your life'),
        ('K', 'How to be led by the Spirit'),
        ('L', 'Breaking the Curses of Life'),
        ('M', 'Pillars of Destiny'),
        ('N', 'Commanding the Supernatural'),
        ('O', 'Keys to Divine Health'),
        ('P', 'Pillars of Destiny'),
        ('Q', 'Ruling Your World'),
        ('R', 'Satan Get Lost'),
        ('S', 'Signs & Wonders Today'),
        ('T', 'The Blood Triumph'),
        ('U', 'The Healing Balm'),
        ('V', 'The Force of Freedom')
    )
    buyer_name = models.CharField(max_length=155)
    mailing_address = models.CharField(max_length=999)
    email = models.EmailField()
    book = models.CharField(max_length=270, choices=BOOK_OPTION)
    copies = models.IntegerField()
    phone = models.CharField(max_length=55)
    message = models.TextField()

    def __str__(self):
        return self.books

    class Meta:
        verbose_name_plural = 'DOMINION BOOKSHOP'



CALL_ME = (
        ( 'Yes', 'Yes'),
        ( 'NO','No'),
)
COUNSEL_OPTION = (
        ( 'Welfare','Welfare'),
        ('Education', 'Education'),
        ('Employment', 'Employment'),
        ('Family', 'Family'),
        ('Health/Sickness', 'Health/Sickness'),
        ('Travel', 'Travel'),
        ('Other', 'Other')
)

class Counsel(models.Model):
    msg_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=489, help_text="YOUR FULLNAME")
    residential = models.CharField(max_length=1000)
    email = models.EmailField()
    phone = models.IntegerField()
    church = models.CharField(max_length=333)
    city = models.CharField(max_length=100)
    call = models.CharField(verbose_name="Will You Want a Call Back?", max_length=3, choices=CALL_ME)
    counsel = models.CharField(verbose_name="This prayer is for", max_length=15, choices=COUNSEL_OPTION)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'COUNSELLING'


class Invite(models.Model):
    msg_id = models.AutoField(primary_key=True)
    y_full_name = models.CharField(max_length=489, help_text="YOUR FULLNAME")
    y_email = models.EmailField()
    next_sunday_date = models.DateTimeField()
    y_friend_full_name = models.CharField(max_length=489)
    y_friend_email = models.EmailField()
    theme = models.CharField(max_length=555)
    message = models.TextField()


    def __str__(self):
        return self.msg_id

    class Meta:
        verbose_name_plural = 'INVITEE'


Foundation = (
        ( 'Yes', 'Yes'),
        ( 'No','No'),
)

BORN_AGAIN= (
        ( 'Yes', 'Yes'),
        ( 'NO','No'),
)

MARITAL = (
    ('Married', 'Married'),
    ('Single', 'Single'),
    ('Widowed', 'Widowed'),
    ('Separated', 'Separated'),
    ('Divorced', 'Divorced'),
)
Job = (
    ('Day', 'Day'),
    ('Night', 'Night'),
    ('Shift', 'Shift'),
    ('Sunday', 'Sunday'),
)


class HOSPITALITY(models.Model):
    full_name = models.CharField(max_length=125)
    residence = models.CharField(max_length=678)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    born_again = models.CharField(choices=BORN_AGAIN,max_length=3)
    joined_date = models.DateField()
    new_birth_date = models.DateField()
    occupation = models.CharField(max_length=678)
    foundation_class = models.CharField(choices=Foundation, max_length=15)
    job = models.CharField(max_length=7, choices=Job)
    status = models.CharField(max_length=9, choices=MARITAL)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'HOSPITALITY UNIT'


class PDF(models.Model):
    title = models.CharField(max_length=567, verbose_name='Resource Name')
    date_day = models.IntegerField()
    date_month = models.CharField(max_length=256)
    date_year = models.BigIntegerField(default=2021, verbose_name='YEAR')
    language = models.CharField(max_length=100)
    size = models.IntegerField()
    document = models.FileField(upload_to='pdf')

    # def __str__(self):
    #     return self.title

    class Meta:
        verbose_name_plural = "PDF"

Foundation = (
        ( 'Yes', 'Yes'),
        ( 'No','No'),
)

BORN_AGAIN= (
        ( 'Yes', 'Yes'),
        ( 'NO','No'),
)

MARITAL = (
    ('Married', 'Married'),
    ('Single', 'Single'),
    ('Widowed', 'Widowed'),
    ('Separated', 'Separated'),
    ('Divorced', 'Divorced'),
)
Job = (
    ('Day', 'Day'),
    ('Night', 'Night'),
    ('Shift', 'Shift'),
    ('Sunday', 'Sunday'),
)


class SANCTUARY(models.Model):
    full_name = models.CharField(max_length=125)
    residence = models.CharField(max_length=678)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    born_again = models.CharField(choices=BORN_AGAIN, max_length=3)
    joined_date = models.DateField()
    new_birth_date = models.DateField()
    occupation = models.CharField(max_length=678)
    foundation_class = models.CharField(choices=Foundation, max_length=15)
    job = models.CharField(max_length=7, choices=Job)
    status = models.CharField(max_length=9, choices=MARITAL)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'SANCTUARY UNIT'


Foundation = (
        ( 'Yes', 'Yes'),
        ( 'No','No'),
)

BORN_AGAIN= (
        ( 'Yes', 'Yes'),
        ( 'NO','No'),
)

MARITAL = (
    ('Married', 'Married'),
    ('Single', 'Single'),
    ('Widowed', 'Widowed'),
    ('Separated', 'Separated'),
    ('Divorced', 'Divorced'),
)
Job = (
    ('Day', 'Day'),
    ('Night', 'Night'),
    ('Shift', 'Shift'),
    ('Sunday', 'Sunday'),
)


class HARVESTER(models.Model):
    full_name = models.CharField(max_length=125)
    residence = models.CharField(max_length=678)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    born_again = models.CharField(choices=BORN_AGAIN, max_length=3)
    joined_date = models.DateField()
    new_birth_date = models.DateField()
    occupation = models.CharField(max_length=678)
    foundation_class = models.CharField(choices=Foundation, max_length=15)
    job = models.CharField(max_length=7, choices=Job)
    status = models.CharField(max_length=9, choices=MARITAL)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'HARVESTER AND FOLLOW-UP UNIT'

Foundation = (
        ( 'Yes', 'Yes'),
        ( 'No','No'),
)

BORN_AGAIN= (
        ( 'Yes', 'Yes'),
        ( 'NO','No'),
)

MARITAL = (
    ('Married', 'Married'),
    ('Single', 'Single'),
    ('Widowed', 'Widowed'),
    ('Separated', 'Separated'),
    ('Divorced', 'Divorced'),
)
Job = (
    ('Day', 'Day'),
    ('Night', 'Night'),
    ('Shift', 'Shift'),
    ('Sunday', 'Sunday'),
)


class HEALTH_WORKERS(models.Model):
    full_name = models.CharField(max_length=125)
    residence = models.CharField(max_length=678)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    born_again = models.CharField(choices=BORN_AGAIN, max_length=3)
    joined_date = models.DateField()
    new_birth_date = models.DateField()
    occupation = models.CharField(max_length=678)
    foundation_class = models.CharField(choices=Foundation, max_length=15)
    job = models.CharField(max_length=7, choices=Job)
    status = models.CharField(max_length=9, choices=MARITAL)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'GILEAD TEAM '

Foundation = (
        ( 'Yes', 'Yes'),
        ( 'No','No'),
)

BORN_AGAIN= (
        ( 'Yes', 'Yes'),
        ( 'NO','No'),
)

MARITAL = (
    ('Married', 'Married'),
    ('Single', 'Single'),
    ('Widowed', 'Widowed'),
    ('Separated', 'Separated'),
    ('Divorced', 'Divorced'),
)
Job = (
    ('Day', 'Day'),
    ('Night', 'Night'),
    ('Shift', 'Shift'),
    ('Sunday', 'Sunday'),
)


class DRAMA(models.Model):
    full_name = models.CharField(max_length=125)
    residence = models.CharField(max_length=678)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    born_again = models.CharField(choices=BORN_AGAIN, max_length=3)
    joined_date = models.DateField()
    new_birth_date = models.DateField()
    occupation = models.CharField(max_length=678)
    foundation_class = models.CharField(choices=Foundation, max_length=15)
    job = models.CharField(max_length=7, choices=Job)
    status = models.CharField(max_length=9, choices=MARITAL)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'DRAMA UNIT'

class PF(models.Model):
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pf/img')
    document = models.FileField(upload_to='pf/pdf')

    class Meta:
        verbose_name_plural = "PRAYER FORCE"
        
        

BORN_AGAIN= (
        ( 'Yes', 'Yes'),
        ( 'NO','No'),
)

D_Licen = (
    ('Yes-G', 'Yes-G'),
    ('Yes-G2', 'Yes-G'),
    ('Yes-G1', 'Yes-G'),
    ('No', 'No'),
)


Job = (
    ('Day', 'Day'),
    ('Night', 'Night'),
    ('Shift', 'Shift'),
    ('Sunday', 'Sunday'),
)



class TRANSPORTATION(models.Model):
    full_name = models.CharField(max_length=125)
    residence = models.CharField(max_length=678)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    born_again = models.CharField(choices=BORN_AGAIN, max_length=3)
    joined_date = models.DateField()
    new_birth_date = models.DateField()
    occupation = models.CharField(max_length=678)
    foundation_class = models.CharField(choices=Foundation, max_length=15)
    job = models.CharField(max_length=7, choices=Job)
    status = models.CharField(max_length=9, choices=D_Licen)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'TRANSPORTATION UNIT'
        
        
        

class Ivpg(models.Model):
    msg_id = models.AutoField(primary_key=True)
    sun_no = models.IntegerField(verbose_name='date')
    sun_sup = models.CharField(max_length=200)
    sun_alp = models.CharField(max_length=200, verbose_name='month')
    sun_year = models.BigIntegerField(default=2021, verbose_name='YEAR')
    sun_img = models.ImageField(upload_to='sunday//%y/%m/%d/', verbose_name="Sunday's Image")
    theme = models.CharField(max_length=999)


    def __str__(self):
        return self.sun_alp

    class Meta:
        verbose_name_plural = "IV"


class ChoirPage1(models.Model):
    img = models.ImageField(upload_to='home/choir')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.img



    class Meta:
        verbose_name_plural = "CHOIR CAROUSEL"

class ChoirPage2(models.Model):
    img = models.ImageField(upload_to='home/choir')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.img


    class Meta:
        verbose_name_plural = "CHOIR SIDE CAROUSEL"


PART = (
        ( 'Soprano', 'Soprano'),
        ( 'Alto','Alto'),
        ('Tenor', 'Tenor'),
        ('No Idea', 'No Idea'),
)
Foundation = (
        ( 'Yes', 'Yes'),
        ( 'No','No'),
)
BORN_AGAIN= (
        ( 'Yes', 'Yes'),
        ( 'No','No'),
)
MARITAL = (
    ('MARRIED', 'MARRIED'),
    ('SINGLE', 'SINGLE'),
    ('WIDOWED', 'WIDOWED'),
    ('SEPARATED', 'SEPARATED'),
    ('DIVORCED', 'DIVORCED'),
)

class Choir(models.Model):
    full_name = models.CharField(max_length=125)
    residence = models.CharField(max_length=678)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    born_again = models.CharField(choices=BORN_AGAIN,max_length=3)
    church = models.DateField()
    date_of_new_birth = models.DateField()
    instrument = models.CharField(max_length=58)
    foundation_class = models.CharField(choices=Foundation, max_length=15)
    part_sing = models.CharField(max_length=7, choices=PART)
    marital_status = models.CharField(max_length=9, choices=MARITAL)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'CHOIR UNIT'




Foundation = (
        ( 'Yes', 'Yes'),
        ( 'No','No'),
)

BORN_AGAIN= (
        ( 'Yes', 'Yes'),
        ( 'NO','No'),
)

MARITAL = (
    ('Married', 'Married'),
    ('Single', 'Single'),
    ('Widowed', 'Widowed'),
    ('Separated', 'Separated'),
    ('Divorced', 'Divorced'),
)
Job = (
    ('Day', 'Day'),
    ('Night', 'Night'),
    ('Shift', 'Shift'),
    ('Sunday', 'Sunday'),
)


class CHILDREN(models.Model):
    full_name = models.CharField(max_length=125)
    residence = models.CharField(max_length=678)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    born_again = models.CharField(choices=BORN_AGAIN,max_length=3)
    joined_date = models.DateField()
    new_birth_date = models.DateField()
    occupation = models.CharField(max_length=678)
    foundation_class = models.CharField(choices=Foundation, max_length=15)
    job = models.CharField(max_length=7, choices=Job)
    status = models.CharField(max_length=9, choices=MARITAL)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'CHILDREN UNIT'


Foundation = (
        ( 'Yes', 'Yes'),
        ( 'No','No'),
)

BORN_AGAIN= (
        ( 'Yes', 'Yes'),
        ( 'NO','No'),
)

MARITAL = (
    ('Married', 'Married'),
    ('Single', 'Single'),
    ('Widowed', 'Widowed'),
    ('Separated', 'Separated'),
    ('Divorced', 'Divorced'),
)
Job = (
    ('Day', 'Day'),
    ('Night', 'Night'),
    ('Shift', 'Shift'),
    ('Sunday', 'Sunday'),
)


class Security(models.Model):
    full_name = models.CharField(max_length=125)
    residence = models.CharField(max_length=678)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    born_again = models.CharField(choices=BORN_AGAIN,max_length=3)
    joined_date = models.DateField()
    new_birth_date = models.DateField()
    occupation = models.CharField(max_length=678)
    foundation_class = models.CharField(choices=Foundation, max_length=15)
    job = models.CharField(max_length=7, choices=Job)
    status = models.CharField(max_length=9, choices=MARITAL)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'SECURITY UNIT'


Foundation = (
        ( 'Yes', 'Yes'),
        ( 'No','No'),
)

BORN_AGAIN= (
        ( 'Yes', 'Yes'),
        ( 'NO','No'),
)

MARITAL = (
    ('Married', 'Married'),
    ('Single', 'Single'),
    ('Widowed', 'Widowed'),
    ('Separated', 'Separated'),
    ('Divorced', 'Divorced'),
)
Job = (
    ('Day', 'Day'),
    ('Night', 'Night'),
    ('Shift', 'Shift'),
    ('Sunday', 'Sunday'),
)


class Decoration(models.Model):
    full_name = models.CharField(max_length=125)
    residence = models.CharField(max_length=678)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    born_again = models.CharField(choices=BORN_AGAIN,max_length=3)
    joined_date = models.DateField()
    new_birth_date = models.DateField()
    design_experience = models.CharField(max_length=678)
    foundation_class = models.CharField(choices=Foundation, max_length=15)
    job = models.CharField(max_length=7, choices=Job)
    status = models.CharField(max_length=9, choices=MARITAL)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'DECORATION UNIT'







class HomeCarousel(models.Model):
    img = models.ImageField(upload_to='home/carousel')
    title = models.CharField(max_length=150)


    def __str__(self):
        return self.title


    class Meta:
        # verbose_name_Plural = 'CHURCH CAROUSEL'
        verbose_name_plural = 'CHURCH HOME CAROUSEL'

class ChoirSong(models.Model):
    title = models.CharField(max_length=50)
    song = models.FileField(upload_to='choir/song')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'CHOIR SONG'


class imgCool(models.Model):
    # img = models.ImageField(upload_to='gallery')
    title = models.CharField(max_length=78)
    date = models.DateField(auto_now_add=False, default='2001/01/01')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'FOR GALLERY'

class Gal(models.Model):
    img = models.ImageField(upload_to='gallery')
    number = models.CharField(max_length=5)
    topic = models.ForeignKey(imgCool, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.number

    class Meta:
        verbose_name_plural = 'GALLERY'


class CA(models.Model):
    scr = models.TextField( verbose_name='SCRIPTURE')
        # models.TextField(verbose_name='SCRIPTURE')
    ref = models.CharField(verbose_name='BIBLE REFERENCE', max_length=100)



    def __str__(self):
        return self.ref


    class Meta:
        verbose_name_plural = 'CHURCH ACCOUNTANT'



class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Pastor_Desk(models.Model):
    topic = models.CharField(max_length=333)
    name = models.CharField(max_length=200)
    week = models.CharField(max_length=555, help_text=" e.g ==> Week of Divine Favour")
    scripture = models.CharField(max_length=1000)
    scripture_reference = models.CharField(max_length=190)
    bible_version = models.CharField(max_length=234, default='KJV')
    message = models.TextField( verbose_name='MESSAGE')
    designation = models.CharField(max_length=345)
    presenter = models.CharField(max_length=300)


    def __str__(self):
        return self.topic


    class Meta:
        verbose_name_plural = 'PASTORS DESK'




# from django.utils import timezone

#
#
#
# class Carousel(models.Model):
#     img = models.ImageField(upload_to='pics/%y/%m/%d/')
#     title = models.CharField(max_length=150)
#     sub_title = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.title
#
#
#
#
#
# class Book(models.Model):
#     title = models.CharField(max_length=222)
#     author = models.CharField(max_length=222)
#     pdf = models.FileField(upload_to='Books/Month/')
#
#
#     class Meta:
#         verbose_name_plural = "WSF"
#
#
#     def __str__(self):
#         return self.title
#
#
#
#
#
#
#
# class Bookshop(models.Model):
#     title = models.CharField(max_length=222)
#     author = models.CharField(max_length=222)
#     pdf = models.FileField(upload_to='Books/Month/')
#
#
#     def __str__(self):
#         return self.title
#
#
# class Topic(models.Model):
#     text = models.CharField(max_length=1000)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#
#     class Meta:
#         verbose_name_plural = 'LIVING FAITH PASTORATE HEADLINES'
#
#
#     def __str__(self):
#         return self.text
#
# class Post(models.Model):
#     title = models.CharField(max_length=353)
#     description = models.TextField()
#     image = models.ImageField(blank=True)
#     def __str__(self):
#         return self.title
#
#
# class PostImage(models.Model):
#     post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='C/')
#
#     def __str__(self):
#         return self.post.title
#
#
#
# class Entry(models.Model):
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     text = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name_plural = 'LIVING FAITH PASTORATE'
#
#         def __str__(self):
#             return self.text[:50] + "..."
#
#
# class Tropic(models.Model):
#     text = models.CharField(max_length=1000)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#
#     class Meta:
#         verbose_name_plural = 'TESTIMONY HEADLINE'
#
#     def __str__(self):
#         return self.text
#
#
# class Dentry(models.Model):
#     tropic = models.ForeignKey(Tropic, on_delete=models.CASCADE)
#     text = models.TextField()
#     testifier = models.CharField(max_length=234)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name_plural = 'TESTIMONY'
#
#         def __str__(self):
#             return self.text[:50] + "..."
#
#
# class Contact(models.Model):
#
# 	STATUS = (
#         (1, 'New'),
#         (2, 'Read'),
#     )
# 	msg_id = models.AutoField(primary_key=True)
# 	name = models.CharField(max_length=222)
# 	email = models.EmailField()
# 	phone = models.CharField(max_length=20, default="")
# 	message = models.TextField(max_length=2222, default="")
# 	date_created = models.DateTimeField(auto_now_add=True)
# 	status = models.IntegerField(choices=STATUS,default=1)
# 	created = models.DateTimeField(default=timezone.now)
# 	updated = models.DateTimeField(auto_now=True)
#
# 	def __str__(self):
# 		return self.name
#
#
#
# class YafContact(models.Model):
#     STATUS = (
#         (1, 'New'),
#         (2, 'Read'),
#     )
#     name = models.CharField(max_length=222)
#     email = models.EmailField()
#     subject = models.CharField(max_length=200)
#     message = models.TextField()
#     date_created = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS,default=1)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.email
#
#     class Meta:
#         verbose_name = 'Youth Alive Contact'
#         verbose_name_plural = 'Youth Alive Contacts'
#
#
# class YafContactForm(ModelForm):
#     class Meta:
#         model = YafContact
#         fields = ['name', 'email', 'subject', 'message']
#         widgets = {
#             'name' : TextInput(attrs={'class': 'input', 'placeholder': 'Name & Surname....'}),
#             'subject' : TextInput(attrs={'class': 'input', 'placeholder': 'Your HeadLine......'}),
#             'email' : TextInput(attrs={'class': 'input', 'placeholder': 'realbuar@gmail.com'}),
#             'message': Textarea(attrs={'class': 'input', 'placeholder': 'Your Message........'}),
#         }
#
#
#
#
#
#
# class Now(models.Model):
#     gallery = models.FileField(upload_to='photo/%Y/%m/%d', blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#     topic = models.CharField(max_length=234)
#
#     def __str__(self):
#         return self.topic
#
#
# class New(models.Model):
#     top = models.ForeignKey(Now, on_delete=models.CASCADE)
#     text = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.text[:50] + "..."
#
#
# class One(models.Model):
#     name = models.CharField(max_length=333)
#     date_created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name






