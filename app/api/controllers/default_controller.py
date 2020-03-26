import connexion
import six

from api.models.contract import Contract  # noqa: E501
from api.models.employee import Employee  # noqa: E501
from api.models.employer import Employer  # noqa: E501
from api.models.job import Job  # noqa: E501
from api.models.job_application import JobApplication  # noqa: E501
from api.models.login_credentials import LoginCredentials  # noqa: E501
from api.models.picture import Picture  # noqa: E501
from api import util

def applications_application_id_delete(application_id):  # noqa: E501
    """deletes an application

     # noqa: E501

    :param application_id: The ID of the application to return.
    :type application_id: str

    :rtype: None
    """
    return 'do some magic!'


def applications_application_id_get(application_id):  # noqa: E501
    """Returns an application.

     # noqa: E501

    :param application_id: The ID of the application to return.
    :type application_id: str

    :rtype: JobApplication
    """
    return 'do some magic!'


def applications_application_id_put(application_id):  # noqa: E501
    """Update changes to application

     # noqa: E501

    :param application_id: The ID of the application to return.
    :type application_id: str

    :rtype: JobApplication
    """
    return 'do some magic!'


def applications_post(body):  # noqa: E501
    """Creates a new application

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = JobApplication.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def contract_contract_id_get(contract_id):  # noqa: E501
    """Returns the specified contract of jobs in the specified search area.

     # noqa: E501

    :param contract_id: 
    :type contract_id: str

    :rtype: List[Contract]
    """
    return 'do some magic!'


def employee_get():  # noqa: E501
    """Returns a list of employees.

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def employee_post(body):  # noqa: E501
    """Creates a new employee

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Employer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def employees_employee_id_delete(employee_id):  # noqa: E501
    """deletes an employee profile. Admin only

     # noqa: E501

    :param employee_id: The ID of the employee to return.
    :type employee_id: str

    :rtype: None
    """
    return 'do some magic!'


def employees_employee_id_get(employee_id):  # noqa: E501
    """Returns an employee by ID.

     # noqa: E501

    :param employee_id: The ID of the employee to return.
    :type employee_id: str

    :rtype: Employee
    """
    return 'do some magic!'


def employees_employee_id_put(employee_id):  # noqa: E501
    """Update changes to employer

     # noqa: E501

    :param employee_id: The ID of the employee to return.
    :type employee_id: str

    :rtype: Employee
    """
    return 'do some magic!'


def employer_employer_id_delete(employer_id):  # noqa: E501
    """deletes an employer profile. Admin only

     # noqa: E501

    :param employer_id: The ID of the employer to return.
    :type employer_id: str

    :rtype: None
    """
    return 'do some magic!'


def employer_employer_id_get(employer_id):  # noqa: E501
    """Returns an employer by ID.

     # noqa: E501

    :param employer_id: The ID of the employer to return.
    :type employer_id: str

    :rtype: Employer
    """
    return 'do some magic!'


def employer_employer_id_put(employer_id):  # noqa: E501
    """Update changes to employer

     # noqa: E501

    :param employer_id: The ID of the employer to return.
    :type employer_id: str

    :rtype: Employer
    """
    return 'do some magic!'


def employer_get():  # noqa: E501
    """Returns a list of employers.

     # noqa: E501


    :rtype: None
    """

    try:
        print("employer_get()")
        emps = []

        # Create the list of employers from our data; join with DBUser for first_name, last_name
        for a, e, u in db.session.query(DBAddress, DBEmployer, DBUser) \
            .filter(DBAddress.Id==DBEmployer.AddressId) \
            .filter(DBUser.Id==DBEmployer.UserId) \
            .order_by(DBEmployer.Id) \
            .all():
    

            # Serialize the data for the response
            # employer_schema = DBEmployerSchema(many=False)
            # employers_dict = employer_schema.dump(e)
            # print(employers_dict)

            # user_schema = DBUserSchema(many=False)
            # users_dict = user_schema.dump(u)
            # print(users_dict)

            # Construct Swagger model for Employer
            emps.append( Employer(id=e.Id, default_picture_id=None, first_name=u.FirstName, 
                                    last_name=u.LastName, street=a.Street, house_number=a.HouseNumber,
                                    postal_code=a.PostalCode, city=None, state=a.State)
                        )
        return emps
        
    except Exception as ex:
        print("Error: {0}".format(ex))
    

def employer_post(body):  # noqa: E501
    """Creates a new employer

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Employer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def jobs_get():  # noqa: E501
    """Returns a list of available jobs.

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def jobs_job_id_delete(job_id):  # noqa: E501
    """deletes a job

     # noqa: E501

    :param job_id: The ID of the job to return.
    :type job_id: str

    :rtype: None
    """
    return 'do some magic!'


def jobs_job_id_get(job_id):  # noqa: E501
    """Returns a job.

     # noqa: E501

    :param job_id: The ID of the job to return.
    :type job_id: str

    :rtype: Job
    """
    return 'do some magic!'


def jobs_job_id_pictures_get(job_id):  # noqa: E501
    """Returns a list of pictures for the specified job.

     # noqa: E501

    :param job_id: The ID of the job
    :type job_id: str

    :rtype: List[Picture]
    """
    return 'do some magic!'


def jobs_job_id_pictures_picture_id_delete(job_id, picture_id):  # noqa: E501
    """deletes a picture

     # noqa: E501

    :param job_id: The ID of the job to return.
    :type job_id: str
    :param picture_id: The ID of the picture to delete.
    :type picture_id: str

    :rtype: None
    """
    return 'do some magic!'


def jobs_job_id_pictures_picture_id_get(job_id, picture_id):  # noqa: E501
    """gets a picture

     # noqa: E501

    :param job_id: The ID of the job to return.
    :type job_id: str
    :param picture_id: The ID of the picture to show.
    :type picture_id: str

    :rtype: None
    """
    return 'do some magic!'


def jobs_job_id_pictures_post(body):  # noqa: E501
    """Creates a new picture

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Picture.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def jobs_job_id_put(job_id):  # noqa: E501
    """Update changes to job

     # noqa: E501

    :param job_id: The ID of the job to return.
    :type job_id: str

    :rtype: Job
    """
    return 'do some magic!'


def jobs_near_get(lat=None, lng=None, radius=None, limit=None):  # noqa: E501
    """Returns a list of jobs in the specified search area.

     # noqa: E501

    :param lat: 
    :type lat: float
    :param lng: 
    :type lng: float
    :param radius: 
    :type radius: float
    :param limit: 
    :type limit: int

    :rtype: List[Job]
    """
    return 'do some magic!'


def jobs_post(body):  # noqa: E501
    """Creates a new job

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Job.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def login_post(body):  # noqa: E501
    """Userlogin, returns the users jwttoken for authentication. WARNING potentially insecure, revision required

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = LoginCredentials.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


# import has to be at the end - don't know why yet
from api.run import db
from api.models.db_model import ( 
    DBUser, DBEmployer, DBEmployee, DBEmployeeDocument, 
    DBEmployerPicture, DBJob, DBJobApplication, DBJobPicture, 
    DBAddress, DBContract,
    DBUserSchema, DBEmployerSchema, DBEmployeeSchema, DBEmployeeDocumentSchema,
    DBEmployerPictureSchema, DBJobSchema, DBJobApplicationSchema, DBJobPictureSchema,
    DBAddressSchema, DBContractSchema
)
