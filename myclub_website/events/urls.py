
from django.urls import path
from . import views

urlpatterns = [
    # int: numbers
    # str: strings
    # path: whole urls / 
    # slug: hypen-and_underscores_stuff
    # UUID: universally unique identifier  
    path('',views.home, name = "home"), 
    path('flash/',views.flash, name = "flash"), 
    path('aituevents/',views.aituevents, name = "aituevents"),
    path('editevents/',views.editevents, name = "editevents"),

    path('club_form/',views.createClub, name = "createclub"),
    path('update_club/<str:pk>',views.updateClub, name = "updateclub"),
    path('delete_club/<str:pk>',views.deleteClub, name = "deleteclub"),

    path('editcourses/',views.editcourses, name = "editcourses"),

    
    path('course_form/',views.createCourse, name = "createcourse"),
    path('update_course/<str:pk>',views.updateCourse, name = "updatecourse"),
    path('delete_course/<str:pk>',views.deleteCourse, name = "deletecourse"),


    path('videoresource_form/',views.createVresource, name = "createvideoresource"),
    path('update_videoresource/<str:pk>',views.updateVresource, name = "updatevideoresource"),
    path('delete_videoresource/<str:pk>',views.deleteVresource, name = "deletevideoresource"),


    path('resource_form/',views.createResource, name = "createresource"),
    path('update_resource/<str:pk>',views.updateResource, name = "updateresource"),
    path('delete_resource/<str:pk>',views.deleteResource, name = "deleteresource"),


    path('student_form/',views.createStudent, name = "createstudent"),
    path('update_student/<str:pk>',views.updateStudent, name = "updatestudent"),
    path('delete_student/<str:pk>',views.deleteStudent, name = "deletestudent"),


    path('subject_form/',views.createSubject, name = "createsubject"),
    path('update_subject/<str:pk>',views.updateSubject, name = "updatesubject"),
    path('delete_subject/<str:pk>',views.deleteSubject, name = "deletesubject"),

    path('profile/',views.profile, name = "profile"),
    path('accsettings/',views.accSettings, name = "accsettings"),
    path('editstudent/',views.editstudent, name = "editstudent"),
    path('show_club/<club_id>',views.show_club, name = "show-club"),
    path('exampreparation/',views.prepare, name = "prepare"),
    path('show_course/<course_id>',views.show_subject, name = "show-subject"),
    path('firstsubject',views.firstsubject, name = "firstsubject"),
    path('deadline/',views.deadline, name = "deadline"),
    path('GPAcalculator/',views.calculator, name = "calculator"), 
    path('1club/',views.firstclub, name = "fclub"),
    path('debate/',views.debate, name = "debate"),
    path('2course/',views.secondcourse, name = "2course"),
    path('3course/',views.thirdcourse, name = "3course"),
    path('faqs/',views.faqpage, name = "faq")


    #path('<int:year>/<str:month>',views.home, name = "home"), 
]
