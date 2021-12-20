from django.test import TestCase, Client
from .models import Consulting


class ConsultingTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for i in range(10):
            Consulting.objects.create(name=f"name{i}", email=f"name{i}@gmail.com", tel=f"09{i}{i}{i}{i}{i}{i}{i}{i}{i}",
                                      add=f"name{i},address{i},street{i}").save()

        cls.consulting_all_info = Consulting.objects.all()

    def test_consulting(self):
        c = Client()

        for i in range(5, 16):
            self.temp1_dict_data = {"name": f"firstname{i}", "email": f"name{i}@gmail.com",
                                    "tel": f"09{i}{i}{i}{i}{i}{i}{i}{i}{i}",
                                    "add": f"firstname{i} address{i} street{i}"}  ### this data is available in consulting table so view return status code 406
            self.response_status_code = c.post("http://127.0.0.1:8000/consulting", self.temp1_dict_data).status_code

            print(self.temp1_dict_data, "--->", self.response_status_code, " --Final Result--> ",
                  "Pass" if self.response_status_code == 200 else "Fail")

            self.temp2_dict_data = {"name": f"firstnameeeee{i}", "email": f"name{i}@gmail.com",
                                    "tel": f"091{i}{i}{i}{i}{i}{i}{i}{i}",
                                    "add": f"firstname{i} address{i} street{i}"}  ### this data is not available in consulting table so this data isn't dublicate and this is unique

            self.response_status_code = c.post("http://127.0.0.1:8000/consulting", self.temp2_dict_data).status_code

            print(self.temp2_dict_data, "--->", self.response_status_code, " --Final Result--> ",
                  "Pass" if self.response_status_code == 200 else "Fail")
