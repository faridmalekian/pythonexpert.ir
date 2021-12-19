from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Course, Comment, Module
from account.models import UserProfile
from django.contrib.auth import get_user_model
from .forms import CommentForm
from courses_category.models import Category


class Courses(ListView):
    template_name = 'courses/courses_list.html'

    paginate_by = 6

    def get_queryset(self):
        return Course.objects.get_active_couses()


class CoursesByCategory(ListView):
    template_name = 'courses/courses_list.html'

    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = Category.objects.filter(slug__iexact=category_name)

        if category is None:
            raise Http404()

        return Course.objects.get_courses_by_category(category_name)


def course_detail(request, pk, slug):
    course = Course.objects.get_by_id(pk)
    teacher = UserProfile.objects.get_queryset().filter(user_id=(course.owner.id)).first()
    # tag = [tag for tag in Tag.objects.all() if tag in Course.objects.get_by_id(pk).tag.all()]
    tag = course.tag_set.all()
    post = get_object_or_404(Course, id=pk)
    comments = post.comments.filter(active=True)
    modules = Module.objects.filter(course_id=course.id)
    new_comment = None
    # Comment posted

    user = get_user_model()

    students = [student for student in user.objects.get_queryset().all() if
                student in course.students.get_queryset().all()]
    if request.user.is_authenticated:
        students_flag = user.objects.get_queryset().filter(id=request.user.id)[0] in students
    else:
        students_flag = False

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid() and request.user.is_authenticated and (
                user.objects.get_queryset().filter(id=request.user.id)[0] in students):
            owner_id = request.user.id
            body = comment_form.cleaned_data.get("body")
            # Create Comment object but don't save to database yet
            # new_comment = comment_form.save(commit=False)
            new_comment = Comment(owner_id=owner_id, body=body)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    if course is None:
        raise Http404

    if course.active:

        context = {
            "course": course,
            "teacher": teacher,
            "tag": tag,
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form,
            'modules': modules,
            'students_flag': students_flag

        }
        return render(request, 'courses/course_detail.html', context)
    else:
        raise Http404


class SearchCoursesView(ListView):
    template_name = 'courses/courses_list.html'

    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')

        if query is not None:
            return Course.objects.search(query)

        return Course.objects.get_active_couses()
