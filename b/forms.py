from django import forms
from .models import Invite, Bookshop, Choir, Book
# from .models import Book, Topic,  Tropic,  Contact, YafContact
from .models import Praye

CALL_CHOICES = (
        ( 'Yes', 'Yes'),
        ( 'No','No'),
)
PRAYER_OPTION = (
        ( 'Myself','Myself'),
        ('Spouse', 'Spouse'),
        ('Child', 'Child'),
        ('Friend', 'Friend'),
        ('Sibling', 'Siblings')
)

class PrayerForm(forms.Form):
    full_name = forms.CharField()
    residential = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()
    church = forms.CharField()
    city = forms.CharField()
    call = forms.ChoiceField(widget=forms.RadioSelect(),choices=CALL_CHOICES)
    pray_for = forms.ChoiceField(widget=forms.RadioSelect(),choices=PRAYER_OPTION)
    prayer  = forms.CharField()


BOOK_OPTION = (
    ('', '..CHOOSE..'),
    ( 'A', 'Anointing for Exploits' ),
    ('B', ' Born to Win'),
    ('C' ,'Conquering Controlling Powers'),
    ('D' , 'The Riches of Redemption '),
    ('E' ,'Possessing Your Possession' ),
    ('F', 'All you Need to Have Your Needs Met'),
    ('G' , 'In Pursuit of Vision'),
    ('H', 'Understanding Divine Direction'),
    ('I' ,'Understanding Vision'),
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
class BookshopForm(forms.Form):
    buyer_name = forms.CharField(max_length=155)
    mailing_address = forms.CharField(max_length=999)
    email = forms.EmailField()
    book = forms.ChoiceField(choices=BOOK_OPTION, label='Which Book Do you want?')
    copies = forms.IntegerField()
    phone = forms.CharField(max_length=55)
    message = forms.CharField(widget=forms.Textarea)



class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        fields = "__all__"

class choirForm(forms.ModelForm):
    class Meta:
        model = Choir
        fields = "__all__"

    # ('The Miracle Meal', 'The Miracle Meal'),
    # ('The Unlimited Power of Faith', 'The Unlimited Power of Faith'),
    # ('Towards Mental Exploits', 'Towards Mental Exploits'),
    # ('Understanding Divine Direction', 'Understanding Divine Direction'),
    # ('Understanding Financial Prosperity', 'Understanding Financial Prosperity'),
    # ('Understanding the Power of Praise', 'Understanding the Power of Praise'),
    # ('Walking in the Miraculous', 'Walking in the Miraculous'),
    # ('Walking in the Newness of Life', 'Walking in the Newness of Life'),
    # ('Winning Prayer', 'Winning Prayer'),
    # ('You Shall Not Be Barren', 'You Shall Not Be Barren')



    # Full_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'frm_txt_fld', 'placeholder':'Your Full Name'}))
    # class Meta:
    #     model = Prayer
    #     fields = ('full_name', 'residential', 'email', 'phone', 'church', 'city' )




# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ('title', 'author', 'pdf')
#
#
#
# class TopicForm(forms.ModelForm):
#     class Meta:
#         model = Topic
#         fields = ['text']
#         labels = {'text': ''}
#
#
# class TropicForm(forms.ModelForm):
#     class Meta:
#         model = Tropic
#         fields = ['text']
#         labels = {'text': ''}
#
#
# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = "__all__"
#
# class YafContactForm(forms.ModelForm):
#     class Meta:
#         model = YafContact
#         fields = "__all__"
