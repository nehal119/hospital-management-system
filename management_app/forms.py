from django import forms 
from django.forms import DateTimeField, DateTimeInput, Form
from management_app.models import Courses, SessionYearModel


class DateInput(forms.DateInput):
    input_type = "date"


class AddStudentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=150, widget=forms.TextInput(attrs={"class":"form-control"}))

    # #For Displaying Courses
    # try:
    #     courses = Courses.objects.all()
    #     course_list = []
    #     for course in courses:
    #         single_course = (course.id, course.course_name)
    #         course_list.append(single_course)
    # except:
    #     course_list = []
    
    # #For Displaying Session Years
    # try:
    #     session_years = SessionYearModel.objects.all()
    #     session_year_list = []
    #     for session_year in session_years:
    #         single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
    #         session_year_list.append(single_session_year)
            
    # except:
    #     session_year_list = []
    
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
    
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    admittime = forms.DateField(label="Admit Time", widget=DateInput(attrs={"class":"form-control"}))
    dischtime = forms.DateField(label="Discharge Time", widget=DateInput(attrs={"class":"form-control"}))
    deathtime = forms.DateField(label="Death Time", widget=DateInput(attrs={"class":"form-control"}))

    admission_type_list = (
        ('UNKNOWN','UNKNOWN'),
        ('EMERGENCY','EMERGENCY'),
        ('ELECTIVE','ELECTIVE'),
        ('URGENT','URGENT'),
    )
    admission_location_list = (
        ('UNKNOWN','UNKNOWN'),
        ('EMERGENCY ROOM ADMIT','EMERGENCY ROOM ADMIT'),
        ('TRANSFER FROM HOSP/EXTRAM','TRANSFER FROM HOSP/EXTRAM'),
        ('PHYS REFERRAL/NORMAL DELI','PHYS REFERRAL/NORMAL DELI'),
        ('CLINIC REFERRAL/PREMATURE','CLINIC REFERRAL/PREMATURE'),
    )
    insurance_list = (
        ('UNKNOWN','UNKNOWN'),
        ('Medicare','Medicare'),
        ('Private','Private')
    )
    marital_status_list = (
        ('UNKNOWN','UNKNOWN'),
        ('SEPARATED','SEPARATED'),
        ('SINGLE','SINGLE'),
        ('DIVORCED','DIVORCED'),
        ('MARRIED','MARRIED'),
        ('WIDOWED','WIDOWED'),
    )

    admission_type = forms.ChoiceField(label="Admission Type", choices=admission_type_list, widget=forms.Select(attrs={"class":"form-control"}))
    admission_location = forms.ChoiceField(label="Admission Location", choices=admission_location_list, widget=forms.Select(attrs={"class":"form-control"}))
    insurance = forms.ChoiceField(label="Insurance", choices=insurance_list, widget=forms.Select(attrs={"class":"form-control"}))
    marital_status = forms.ChoiceField(label="Marital Status", choices=marital_status_list, widget=forms.Select(attrs={"class":"form-control"}))
    diagnosis = forms.CharField(label="Diagnosis", max_length=150, widget=forms.TextInput(attrs={"class":"form-control"}))




class EditStudentForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

    #For Displaying Courses
    try:
        courses = Courses.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        course_list = []

    #For Displaying Session Years
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
            
    except:
        session_year_list = []

    
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
    
    course_id = forms.ChoiceField(label="Course", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Session Year", choices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))
    # session_start_year = forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}))
    # session_end_year = forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Profile Pic", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))