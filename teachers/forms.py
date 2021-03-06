from django import forms
from students.models import *
from django.utils import timezone
from students.models import *

class TestCreateFrom(forms.ModelForm):
    class Meta:
        model=Test
        fields ='__all__'
        exclude=('teacher','subject')

  #   <label for="appt-time">Choose an appointment time: </label>
  # <input id="appt-time" type="time" name="appt-time" step="2">


        widgets = {
                'duration': forms.TimeInput(attrs={ "type":"time","step":"2"},),

               'exam_start_time': forms.DateTimeInput(attrs={"type":"datetime-local" },),

               'exam_end_time': forms.DateTimeInput(attrs={"type":"datetime-local" },)

        }



class SubjectCreateFrom(forms.ModelForm):
    class Meta:
        model=Subject
        exclude=('hod',)

        widgets = {
            'teachers': forms.CheckboxSelectMultiple(),


        }


class QuestionCreateFrom(forms.ModelForm):
    class Meta:
        model=Question
        exclude=('teacher','test')

        widgets = {


        }


class StudentVerificationFrom(forms.ModelForm):
    class Meta:
        model=Student
        exclude=('user','verify')

        widgets = {
            'student_subjects': forms.CheckboxSelectMultiple(),

        }

class TeacherVerificationFrom(forms.ModelForm):
    class Meta:
        model=Teacher
        exclude=('user','verify')

        widgets = {
            'teacher_subjects': forms.CheckboxSelectMultiple(),

        }

