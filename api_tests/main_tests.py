import unittest

from helpers.helpers import read_data_from_json, create_random_string

from api_objects.qrcontacts_api_objects import ApiObjects


class MainTests(unittest.TestCase):

    def setUp(self):
        self.api_objects = ApiObjects()

    def test_register_user_and_create_and_update_profile(self):
        mail = create_random_string(5) + "@example.com"
        self.api_objects.register_user(mail, "password@@3")

        dict = self.api_objects.login_user( mail, 'password@@3', "126gs8a6sd78y1991y28u01u0i2h1091uw90j", "ios")
        token = dict['token']

        data = read_data_from_json("test_data.json")
        user_payload = data["user_json"]

        profile_info = self.api_objects.create_profile(token, user_payload)
        profile_id = profile_info['id']
        data_one = self.api_objects.retrieve_profile_data(token, profile_id)
        self.assertTrue(data_one['first_name'] == user_payload['first_name'])
        user_payload["first_name"] = "Johannes"
        profile_info2 = self.api_objects.update_profile(token, user_payload, profile_id)
        profile_id2 = profile_info2['id']
        data_two = self.api_objects.retrieve_profile_data(token, profile_id2)
        self.assertTrue(data_two['first_name'] == user_payload['first_name'])

    def test_wrong_login(self):
        self.assertTrue('device_os' in self.api_objects.login_user( 'a.k.jezierski+5@gmail.com', 'password@@3', "", "").keys())
        self.assertTrue('login' in self.api_objects.login_user('', 'password@@3', "", "ios").keys())
        self.assertTrue('Invalid credentials' in self.api_objects.login_user('xxxxx', 'password@@3', "", "ios")['error'])
        self.assertTrue('Invalid credentials' in
                        self.api_objects.login_user('a.k.jezierski+5@gmail.com', '@@3', "", "ios")['error'])

    def test_log_in_and_log_out(self):
        mail = create_random_string(5) + "@example.com"
        self.api_objects.register_user(mail, "password@@3")

        dict = self.api_objects.login_user(mail, 'password@@3', "126gs8a6sd78y1991y28u01u0i2h1091uw90j", "ios")
        token = dict['token']
        self.assertEqual(204, self.api_objects.logout_uesr(token))

        self.assertTrue('Invalid token.' in self.api_objects.retrieve_profiles_data(token)['detail'])

    def test_double_login(self):
        mail = create_random_string(5) + "@example.com"
        self.api_objects.register_user(mail, "password@@3")

        dict = self.api_objects.login_user(mail, 'password@@3', "126gs8a6sd78y1991y28u01u0i2h1091uw90j", "ios")
        token = dict['token']
        dict2 = self.api_objects.login_user(mail, 'password@@3', "126gs8a6sd78y1991y28u01u0i2h1091uw90j", "ios")
        token2 = dict2['token']

        data = read_data_from_json("test_data.json")
        user_payload = data["user_json"]

        self.api_objects.create_profile(token2, user_payload)
        self.assertEqual(204, self.api_objects.logout_uesr(token))
        self.assertTrue(self.api_objects.retrieve_profiles_data(token2))
        self.assertTrue('Invalid token.' in self.api_objects.retrieve_profiles_data(token)['detail'])

    def test_logout_on_all(self):
        mail = create_random_string(5) + "@example.com"
        self.api_objects.register_user(mail, "password@@3")

        dict = self.api_objects.login_user(mail, 'password@@3', "126gs8a6sd78y1991y28u01u0i2h1091uw90j", "ios")
        token = dict['token']
        dict2 = self.api_objects.login_user(mail, 'password@@3', "126gs8a6sd78y1991y28u01u0i2h1091uw90j", "ios")
        token2 = dict2['token']

        self.assertEqual(204, self.api_objects.logout_user_from_all_devices(token))
        self.assertTrue('Invalid token.' in self.api_objects.retrieve_profiles_data(token2)['detail'])
        self.assertTrue('Invalid token.' in self.api_objects.retrieve_profiles_data(token)['detail'])

    def test_user_preferences(self):
        mail = create_random_string(5) + "@example.com"
        self.api_objects.register_user(mail, "password@@3")

        dict = self.api_objects.login_user(mail, 'password@@3', "126gs8a6sd78y1991y28u01u0i2h1091uw90j", "ios")
        token = dict['token']
        self.assertTrue('Not found.' in self.api_objects.get_current_user_prefs(token)['detail'])
        self.api_objects.create_preferences(token, 'it')
        self.assertTrue('it' in self.api_objects.get_current_user_prefs(token)['language'])
        self.api_objects.update_preferences(token, 'en')
        self.assertTrue('en' in self.api_objects.get_current_user_prefs(token)['language'])
