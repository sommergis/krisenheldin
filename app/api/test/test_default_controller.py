# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from api.models.contract import Contract  # noqa: E501
from api.models.employee import Employee  # noqa: E501
from api.models.employer import Employer  # noqa: E501
from api.models.job import Job  # noqa: E501
from api.models.job_application import JobApplication  # noqa: E501
from api.models.login_credentials import LoginCredentials  # noqa: E501
from api.models.picture import Picture  # noqa: E501
from api.models.user import User  # noqa: E501
from api.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_applications_application_id_delete(self):
        """Test case for applications_application_id_delete

        deletes an application
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/applications/{applicationId}'.format(application_id=2),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_applications_application_id_get(self):
        """Test case for applications_application_id_get

        Returns an application.
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/applications/{applicationId}'.format(application_id=2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_applications_application_id_put(self):
        """Test case for applications_application_id_put

        Update changes to application
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/applications/{applicationId}'.format(application_id=2),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_applications_post(self):
        """Test case for applications_post

        Creates a new application
        """
        body = JobApplication()
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/applications',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_contracts_contract_id_get(self):
        """Test case for contracts_contract_id_get

        Returns the specified contract of jobs.
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/contracts/{contractId}'.format(contract_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_employees_employee_id_delete(self):
        """Test case for employees_employee_id_delete

        deletes an employee profile. Admin only
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/employees/{employeeId}'.format(employee_id=2),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_employees_employee_id_get(self):
        """Test case for employees_employee_id_get

        Returns an employee by ID.
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/employees/{employeeId}'.format(employee_id=2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_employees_employee_id_put(self):
        """Test case for employees_employee_id_put

        Update changes to employer
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/employees/{employeeId}'.format(employee_id=2),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_employees_get(self):
        """Test case for employees_get

        Returns a list of employees.
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/employees',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_employees_post(self):
        """Test case for employees_post

        Creates a new employee
        """
        body = Employer()
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/employees',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_employers_employer_id_delete(self):
        """Test case for employers_employer_id_delete

        deletes an employer profile. Admin only
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/employers/{employerId}'.format(employer_id=2),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_employers_employer_id_get(self):
        """Test case for employers_employer_id_get

        Returns an employer by ID.
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/employers/{employerId}'.format(employer_id=2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_employers_employer_id_put(self):
        """Test case for employers_employer_id_put

        Update changes to employer
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/employers/{employerId}'.format(employer_id=2),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_employers_get(self):
        """Test case for employers_get

        Returns a list of employers.
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/employers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_employers_post(self):
        """Test case for employers_post

        Creates a new employer
        """
        body = Employer()
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/employers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_get(self):
        """Test case for jobs_get

        Returns a list of available jobs.
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/jobs',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_job_id_delete(self):
        """Test case for jobs_job_id_delete

        deletes a job
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/jobs/{jobId}'.format(job_id=2),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_job_id_get(self):
        """Test case for jobs_job_id_get

        Returns a job.
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/jobs/{jobId}'.format(job_id=2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_job_id_pictures_get(self):
        """Test case for jobs_job_id_pictures_get

        Returns a list of pictures for the specified job.
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/jobs/{jobId}/pictures'.format(job_id='job_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_job_id_pictures_picture_id_delete(self):
        """Test case for jobs_job_id_pictures_picture_id_delete

        deletes a picture
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/jobs/{jobId}/pictures/{pictureId}'.format(job_id=2, picture_id=2),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_job_id_pictures_picture_id_get(self):
        """Test case for jobs_job_id_pictures_picture_id_get

        gets a picture
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/jobs/{jobId}/pictures/{pictureId}'.format(job_id=2, picture_id=2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_job_id_pictures_post(self):
        """Test case for jobs_job_id_pictures_post

        Creates a new job picture
        """
        body = Picture()
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/jobs/{jobId}/pictures'.format(job_id='job_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_job_id_put(self):
        """Test case for jobs_job_id_put

        Update changes to job
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/jobs/{jobId}'.format(job_id=2),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_near_get(self):
        """Test case for jobs_near_get

        Returns a list of jobs in the specified search area.
        """
        query_string = [('lat', 1.2),
                        ('lng', 1.2),
                        ('radius', 1.2),
                        ('limit', 56)]
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/jobs_near',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_post(self):
        """Test case for jobs_post

        Creates a new job
        """
        body = Job()
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/jobs',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login_post(self):
        """Test case for login_post

        Userlogin, returns the users jwttoken for authentication. WARNING potentially insecure, revision required
        """
        body = LoginCredentials()
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_get(self):
        """Test case for users_get

        Returns a list of users.
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/users',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_post(self):
        """Test case for users_post

        Creates a new user
        """
        body = User()
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_user_id_get(self):
        """Test case for users_user_id_get

        Returns a users by ID.
        """
        response = self.client.open(
            '/sommergis/krisenheldin/1.0.1/users/{userId}'.format(user_id=2),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
