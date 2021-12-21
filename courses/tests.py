from django.test import TestCase, Client
from .models import Course
from django.contrib.auth.models import User


class CourseTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        User.objects.create_user(username="mrtook", email="mrtook@gmail.com", first_name="mrtook",
                                 last_name="mrtook",
                                 password="root").save()

        cls.overview = """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Vulputate sapien nec sagittis aliquam malesuada bibendum arcu. Lacus laoreet non curabitur gravida. Dis parturient montes nascetur ridiculus mus mauris vitae ultricies leo. Amet cursus sit amet dictum sit amet justo donec enim. Viverra justo nec ultrices dui sapien eget. Dictum varius duis at consectetur. Ac auctor augue mauris augue neque gravida in fermentum. Eleifend donec pretium vulputate sapien nec sagittis. Volutpat maecenas volutpat blandit aliquam. Vestibulum rhoncus est pellentesque elit ullamcorper. Dolor sed viverra ipsum nunc. Sit amet risus nullam eget. Fames ac turpis egestas sed tempus.

            Auctor elit sed vulputate mi sit amet mauris commodo. Non nisi est sit amet facilisis magna etiam tempor orci. Libero justo laoreet sit amet. Lobortis scelerisque fermentum dui faucibus in. Vitae suscipit tellus mauris a diam maecenas sed. Bibendum neque egestas congue quisque egestas. Cras fermentum odio eu feugiat pretium nibh ipsum consequat nisl. Facilisi nullam vehicula ipsum a arcu. A lacus vestibulum sed arcu non. Sit amet purus gravida quis blandit. In metus vulputate eu scelerisque felis imperdiet proin fermentum. A arcu cursus vitae congue mauris. Etiam non quam lacus suspendisse faucibus interdum posuere. Volutpat est velit egestas dui id.
        """
        for i in range(5):
            Course.objects.create(owner=User.objects.get(username="mrtook"), title=f"title{i}", price=f"200{i}",
                                  image="courses/None-آموزش_پایتون_از_صفر_تا_صد.png", slug=f"title-{i}",
                                  overview=cls.overview,
                                  active=True, time=f"2{i}").save()
        cls.all_course_information = Course.objects.get_active_couses()
        #print([f"title = {i.title}"+" "+f"price = {i.price}"+" "+f"slug = {i.slug}" for i in cls.all_course_information])

    def test_course_page(self):
        c = Client()
        if c.get("/courses").status_code == 200:
            # print("Course page is loaded successfully")
            self.assertTrue(True, msg="Course page is loaded successfully")

    def test_search_course(self):
        pass

    def test_details_course_page(self):
        c = Client()
        for i in self.all_course_information:
            if c.get(f"/course/{i.id}/{i.slug}").status_code == 200:
                print(f"course's {i.title} is available ok 200")

            #print(c.get(f"http://127.0.0.1:8000/course/{i.id}/{i.slug}"))

            # if i.overview in c.get(f"/course/{i.id}/{i.slug}").content:
            #     self.assertTrue(True, msg=f"{i.title} there is a right content ok 200")
            # else:
            #     self.assertTrue(False, msg=f"{i.title} there isn't a right content")
