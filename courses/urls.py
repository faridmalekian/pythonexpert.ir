from django.urls import path
from .views import Courses, course_detail, SearchCoursesView, CoursesByCategory

urlpatterns = [
    path('courses',Courses.as_view()),
    path('courses/<category_name>',CoursesByCategory.as_view()),
    path('course/<pk>/<slug>',course_detail),
    path('search',SearchCoursesView.as_view()),
    
]