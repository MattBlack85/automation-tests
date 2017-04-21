import requests
import json

class ApiObjects():
    api_base = 'https://dev.qrcontacts.net/api/v1'
    register = '/register'
    change_password = '/password_change'
    reset_password_point = '/dpassword_reset'
    preferences = '/me'
    login = '/login'
    facebook_login = '/facebook'
    google_login = '/google'
    logout = '/logout'
    logout_all = '/all'
    profiles = '/profiles'
    logo = '/logo'
    avatar = '/avatar'
    contacts = '/contacts'

    def register_user(self, email, password):
        payload = {'password': password, 'email': email}
        r = requests.post(self.api_base + self.register, json=payload)
        return json.loads(r.text)

    def request_email(self, user_id):
        r = requests.post(self.api_base + self.register + '/' + user_id)
        return json.loads(r.text)

    def change_password_for_current_user(self, auth_token, old_pass, new_pass):
        payload = {'old_password': old_pass, "new_password": new_pass}
        headers = {'Authorization':  'Token '+auth_token}
        r = requests.post(self.api_base + self.change_password, data=payload, headers=headers)
        return json.loads(r.text)

    def reset_password(self, email):
        payload = {'email': email}
        r = requests.post(self.api_base + self.reset_password_point, data=payload)
        return json.loads(r.text)

    def get_current_user_prefs(self, auth_token):
        headers = {'Authorization':  'Token '+auth_token}
        r = requests.get(self.api_base + self.preferences, headers=headers)
        return json.loads(r.text)

    def create_preferences(self, auth_token, language):
        headers = {'Authorization':  'Token '+auth_token}
        payload = {'language': language}
        r = requests.post(self.api_base + self.preferences, json=payload, headers=headers)
        return json.loads(r.text)

    def update_preferences(self, auth_token, language):
        headers = {'Authorization':  'Token '+auth_token}
        payload = {'language': language}
        r = requests.put(self.api_base + self.preferences, json=payload, headers=headers)
        return json.loads(r.text)

    def login_user(self, login, password, device_id, device_os):
        payload = {"login": login, "password": password,  "device_id": device_id, "device_os": device_os}
        r = requests.post(self.api_base + self.login, json=payload)
        return json.loads(r.text)

    def login_user_by_facebook(self, access_token, code, device_id, device_os):
        payload = {"access_token": access_token, "code": code, "device_id": device_id, "device_os": device_os}
        r = requests.post(self.api_base + self.login + self.facebook_login, json=payload)
        return json.loads(r.text)

    def login_user_by_google(self, access_token, code, device_id, device_os):
        payload = {"access_token": access_token, "code": code, "device_id": device_id, "device_os": device_os}
        r = requests.post(self.api_base + self.login + self.google_login, json=payload)
        return json.loads(r.text)

    def logout_uesr(self, auth_token):
        headers = {'Authorization':  'Token '+auth_token}
        r = requests.post(self.api_base + self.logout, headers=headers)
        return r.status_code

    def logout_user_from_all_devices(self, auth_token):
        headers = {'Authorization':  'Token '+auth_token}
        r = requests.post(self.api_base + self.logout + self.logout_all, headers=headers)
        return r.status_code

    def create_profile(self, auth_token, user_payload):
        payload = user_payload
        headers = {'Authorization':  'Token '+auth_token}
        r = requests.post(self.api_base + self.profiles, json=payload, headers=headers)
        return json.loads(r.text)

    def retrieve_profiles_data(self, auth_token):
        headers = {'Authorization':  'Token '+auth_token}
        r = requests.get(self.api_base + self.profiles, headers=headers)
        return json.loads(r.text)

    def update_profile(self, auth_token, user_payload, profile_id):
        payload = user_payload
        headers = {'Authorization':  'Token '+auth_token}
        r = requests.put(self.api_base + self.profiles + '/' + profile_id, json=payload, headers=headers)
        return json.loads(r.text)

    def retrieve_profile_data(self, auth_token, profile_id):
        headers = {'Authorization':  'Token '+auth_token}
        r = requests.get(self.api_base + self.profiles + '/' + profile_id, headers=headers)
        return json.loads(r.text)

    def delete_profile(self, auth_token, profile_id):
        headers = {'Authorization':  'Token '+auth_token}
        r = requests.delete(self.api_base + self.profiles + '/' + profile_id, headers=headers)
        return json.loads(r.text)

    def get_logo(self, auth_token, profile_id):
        headers = {'Authorization':  'Token '+auth_token}
        r = requests.get(self.api_base + self.profiles + '/' + profile_id + self.logo, headers=headers)
        return json.loads(r.text)

    def get_avatar(self, auth_token, profile_id):
        headers = {'Authorization':  'Token '+auth_token}
        r = requests.get(self.api_base + self.profiles + '/' + profile_id + self.avatar, headers=headers)
        return json.loads(r.text)

    def retrieve_all_contacts(self, auth_token):
        headers = {'Authorization':  'Token '+auth_token}
        r = requests.get(self.api_base + self.profiles + self.avatar, headers=headers)
        return json.loads(r.text)