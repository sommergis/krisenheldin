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

    :param application_id: The ID of the application to return.
    :type application_id: str

    :rtype: None
    """
    return 'do some magic!'


def applications_application_id_get(application_id):  # noqa: E501
    """Returns an application.

    :param application_id: The ID of the application to return.
    :type application_id: str

    :rtype: JobApplication
    """
    return 'do some magic!'


def applications_application_id_put(application_id):  # noqa: E501
    """Update changes to application

    :param application_id: The ID of the application to return.
    :type application_id: str

    :rtype: JobApplication
    """
    return 'do some magic!'


def applications_post(body):  # noqa: E501
    """Creates a new application

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = JobApplication.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def contract_contract_id_get(contract_id):  # noqa: E501
    """Returns the specified contract of jobs in the specified search area.

    :param contract_id: 
    :type contract_id: str

    :rtype: List[Contract]
    """
    return 'do some magic!'


def employee_get():  # noqa: E501
    """Returns a list of employees.

    :rtype: None
    """
    try:
        print("employee_get()")
        emps = []

        # # Create the list of employees from our data; join with DBUser for first_name, last_name
        # explicit join:
        for a, e, u in db.session.query(DBAddress, DBEmployee, DBUser) \
            .filter(DBAddress.Id==DBEmployee.AddressId) \
            .filter(DBUser.Id==DBEmployee.UserId) \
            .order_by(DBEmployee.Id) \
            .all():

            # Construct Swagger model for Employee
            emps.append( Employee(id=e.Id, first_name=u.FirstName, 
                                    last_name=u.LastName, street=a.Street, house_number=a.HouseNumber,
                                    postal_code=a.PostalCode, city=a.City, state=a.State)
                        )

        return dict(content=emps, status="success")
        
    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))


def employee_post(body):  # noqa: E501
    """Creates a new employee

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Employer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def employees_employee_id_delete(employee_id):  # noqa: E501
    """deletes an employee profile. Admin only

    :param employee_id: The ID of the employee to return.
    :type employee_id: str

    :rtype: None
    """
    try:
        print("employees_employee_id_delete()")

        # throws a ValueError if not valid
        int(employee_id)
        
        # Get employer object by primary key
        employee = db.session.query(DBEmployee).get(employee_id)

        if employee:
            db.session.delete(employee)
            db.session.commit()

            return dict(status="success", message="Deleted Employee id {0}".format(employee_id))

        else:
            return dict(status="error", message="Employee id {0} not found!".format(employee_id))

    except ValueError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Not a valid integer value: {0}!".format(employee_id))

    except TypeError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Employee id {0} not found!".format(employee_id))

    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))


def employees_employee_id_get(employee_id):  # noqa: E501
    """Returns an employee by ID.

    :param employee_id: The ID of the employee to return.
    :type employee_id: str

    :rtype: Employee
    """
    try:
        print("employees_employee_id_get()")

        # throws a ValueError if not valid
        int(employee_id)
        
        # Get employer object by primary key
        # throws an TypeError 'cannot unpack non-iterable NoneType object' if nothing is found
        a, e, u = db.session.query(DBAddress, DBEmployee, DBUser) \
            .filter(DBEmployer.Id==employee_id) \
            .filter(DBAddress.Id==DBEmployee.AddressId) \
            .filter(DBUser.Id==DBEmployee.UserId) \
            .first() # should return only one!

        if a and e and u:
            # Construct Swagger model for Employee
            employee_out = Employee(id=e.Id, first_name=u.FirstName, 
                                    last_name=u.LastName, street=a.Street, house_number=a.HouseNumber,
                                    postal_code=a.PostalCode, city=a.City, state=a.State)

            return dict(content=employee_out, status="success")

        else:
            return dict(status="error", message="Employee id {0} not found!".format(employee_id))

    except ValueError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Not a valid integer value: {0}!".format(employee_id))

    except TypeError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Employee id {0} not found!".format(employee_id))

    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))


def employees_employee_id_put(employee_id):  # noqa: E501
    """Update changes to employer

    :param employee_id: The ID of the employee to return.
    :type employee_id: str

    :rtype: Employee
    """
    return 'do some magic!'


def employer_employer_id_delete(employer_id):  # noqa: E501
    """deletes an employer profile. Admin only

    :param employer_id: The ID of the employer to return.
    :type employer_id: str

    :rtype: None
    """
    try:
        print("employer_employer_id_delete()")

        # throws a ValueError if not valid
        int(employer_id)
        
        # Get employer object by primary key
        employer = db.session.query(DBEmployer).get(employer_id)

        if employer:
            db.session.delete(employer)
            db.session.commit()

            return dict(status="success", message="Deleted Employer id {0}".format(employer_id))

        else:
            return dict(status="error", message="Employer id {0} not found!".format(employer_id))

    except ValueError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Not a valid integer value: {0}!".format(employer_id))

    except TypeError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Employer id {0} not found!".format(employer_id))

    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))


def employer_employer_id_get(employer_id):  # noqa: E501
    """Returns an employer by ID.

    :param employer_id: The ID of the employer to return.
    :type employer_id: str

    :rtype: Employer
    """
    try:
        print("employer_employer_id_get()")

        # throws a ValueError if not valid
        int(employer_id)
        
        # Get employer object by primary key
        # throws an TypeError 'cannot unpack non-iterable NoneType object' if nothing is found
        a, e, u = db.session.query(DBAddress, DBEmployer, DBUser) \
            .filter(DBEmployer.Id==employer_id) \
            .filter(DBAddress.Id==DBEmployer.AddressId) \
            .filter(DBUser.Id==DBEmployer.UserId) \
            .first() # should return only one!

        if a and e and u:
            # Construct Swagger model for Employer
            employer_out = Employer(id=e.Id, default_picture_id=None, first_name=u.FirstName, 
                                    last_name=u.LastName, street=a.Street, house_number=a.HouseNumber,
                                    postal_code=a.PostalCode, city=a.City, state=a.State)

            return dict(content=employer_out, status="success")

        else:
            return dict(status="error", message="Employer id {0} not found!".format(employer_id))

    except ValueError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Not a valid integer value: {0}!".format(employer_id))

    except TypeError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Employer id {0} not found!".format(employer_id))

    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))


def employer_employer_id_put(employer_id):  # noqa: E501
    """Update changes to employer

    :param employer_id: The ID of the employer to return.
    :type employer_id: str

    :rtype: Employer
    """
    return 'do some magic!'


def employer_get():  # noqa: E501
    """Returns a list of employers.

    :rtype: list of Employers
    """

    try:
        print("employer_get()")
        emps = []

        # # Create the list of employers from our data; join with DBUser for first_name, last_name
        # explicit join:
        for a, e, u in db.session.query(DBAddress, DBEmployer, DBUser) \
            .filter(DBAddress.Id==DBEmployer.AddressId) \
            .filter(DBUser.Id==DBEmployer.UserId) \
            .order_by(DBEmployer.Id) \
            .all():

            # Construct Swagger model for Employer
            emps.append( Employer(id=e.Id, default_picture_id=None, first_name=u.FirstName, 
                                    last_name=u.LastName, street=a.Street, house_number=a.HouseNumber,
                                    postal_code=a.PostalCode, city=a.City, state=a.State)
                        )

        return dict(content=emps, status="success")
        
    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))
    

def employer_post(body):  # noqa: E501
    """Creates a new employer

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Employer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def jobs_get():  # noqa: E501
    """Returns a list of available jobs.

    :rtype: list of Jobs
    """
    try:
        print("jobs_get()")
        jobs = []

        # # Create the list of jobs from our data
        for j in db.session.query(DBJob) \
            .order_by(DBJob.Id) \
            .all():

            # Serialize the data for the response
            # important for WKB deserialization
            job_schema = DBJobSchema(many=False)
            jobs_dict = job_schema.dump(j)

            # Construct Swagger model for Job
            jobs.append( Job(id=j.Id, employer_id=j.EmployerId, 
                            default_image_picture_id=j.DefaultImagePictureId, 
                            description=j.Description, 
                            salary_hourly=j.SalaryHourly,
                            work_hours_per_day=j.WorkHoursPerDay,
                            work_days_per_week=j.WorkDaysPerWeek,
                            accommodation_available=j.AccommodationAvailable,
                            acommodation_cost_per_day=j.AccommodationCostPerDay,
                            with_meals=j.WithMeals,
                            meal_cost_per_day=j.MealCostPerDay,
                            spoken_languages=j.SpokenLanguages,
                            location= jobs_dict["Location"], #job.Location fails, because of WKB -> WKT
                            location_description=j.LocationDescription,
                            start_date=j.StartDate,
                            end_date=j.EndDate,
                            special_requirements=j.SpecialRequirements,
                            contingent=j.Contingent,
                            is_active=j.IsActive,
                            visible_from=None,
                            visible_to=None)
                        )

        return dict(content=jobs, status="success")
        
    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))


def jobs_job_id_delete(job_id):  # noqa: E501
    """deletes a job

    :param job_id: The ID of the job to delete.
    :type job_id: str

    :rtype: str
    """
    try:
        print("jobs_job_id_delete()")
        
        # throws a ValueError if not valid
        int(job_id)

        # Get job object by primary key
        job = db.session.query(DBJob).get(job_id)
        if job:
            db.session.delete(job)
            db.session.commit()

            return dict(status="success", message="Deleted job id {0}".format(job_id))

        else:
            return dict(status="error", message="Job id {0} not found!".format(job_id))
        
    except ValueError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Not a valid integer value: {0}!".format(job_id))

    except TypeError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Job id {0} not found!".format(job_id))

    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))


def jobs_job_id_get(job_id):  # noqa: E501
    """Returns a job.

    :param job_id: The ID of the job to return.
    :type job_id: str

    :rtype: Job
    """
    try:
        print("jobs_job_id_get()")
        
        # throws a ValueError if not valid
        int(job_id)

        # Get job object by primary key
        job = db.session.query(DBJob).get(job_id)
        if job:
            # Serialize the data for the response
            # important for WKB deserialization
            job_schema = DBJobSchema(many=False)
            jobs_dict = job_schema.dump(job)

            # Construct Swagger model for Job
            job_out = Job(id=job.Id, employer_id=job.EmployerId, 
                            default_image_picture_id=job.DefaultImagePictureId, 
                            description=job.Description, 
                            salary_hourly=job.SalaryHourly,
                            work_hours_per_day=job.WorkHoursPerDay,
                            work_days_per_week=job.WorkDaysPerWeek,
                            accommodation_available=job.AccommodationAvailable,
                            acommodation_cost_per_day=job.AccommodationCostPerDay,
                            with_meals=job.WithMeals,
                            meal_cost_per_day=job.MealCostPerDay,
                            spoken_languages=job.SpokenLanguages,
                            location= jobs_dict["Location"], #job.Location fails, because of WKB -> WKT
                            location_description=job.LocationDescription,
                            start_date=job.StartDate,
                            end_date=job.EndDate,
                            special_requirements=job.SpecialRequirements,
                            contingent=job.Contingent,
                            is_active=job.IsActive,
                            visible_from=None,
                            visible_to=None)

            return dict(content=job_out, status="success")

        else:
            return dict(status="error", message="Job id {0} not found!".format(job_id))
        
    except ValueError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Not a valid integer value: {0}!".format(job_id))

    except TypeError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Job id {0} not found!".format(job_id))

    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))


def jobs_job_id_pictures_get(job_id):  # noqa: E501
    """Returns a list of pictures for the specified job.

    :param job_id: The ID of the job
    :type job_id: str

    :rtype: List[Picture]
    """
    return 'do some magic!'


def jobs_job_id_pictures_picture_id_delete(job_id, picture_id):  # noqa: E501
    """deletes a picture

    :param job_id: The ID of the job to return.
    :type job_id: str
    :param picture_id: The ID of the picture to delete.
    :type picture_id: str

    :rtype: None
    """
    return 'do some magic!'


def jobs_job_id_pictures_picture_id_get(job_id, picture_id):  # noqa: E501
    """gets a picture

    :param job_id: The ID of the job to return.
    :type job_id: str
    :param picture_id: The ID of the picture to show.
    :type picture_id: str

    :rtype: None
    """
    return 'do some magic!'


def jobs_job_id_pictures_post(body):  # noqa: E501
    """Creates a new picture

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Picture.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def jobs_job_id_put(job_id):  # noqa: E501
    """Update changes to job

    :param job_id: The ID of the job to return.
    :type job_id: str

    :rtype: Job
    """
    return 'do some magic!'


def jobs_near_get(lat=None, lng=None, radius=None, limit=100):  # noqa: E501
    """Returns a list of jobs in the specified search area.

    :param lat: latitude
    :type lat: float
    :param lng: longitude
    :type lng: float
    :param radius: search radius in meters
    :type radius: float
    :param limit: limit the results
    :type limit: int

    :rtype: List[Job]
    """
    try:
        print("jobs_near_get()")
        jobs = []

        try:
            float(lat)
        except ValueError as ex:
            print("Error: {0}".format(ex))
            return dict(status="error", message="Not a valid float value for lat: {0}!".format(lat))

        try:
            float(lng)
        except ValueError as ex:
            print("Error: {0}".format(ex))
            return dict(status="error", message="Not a valid float value for lng: {0}!".format(lng))

        try:
            float(radius)
        except ValueError as ex:
            print("Error: {0}".format(ex))
            return dict(status="error", message="Not a valid float value for radius: {0}!".format(radius))

        try:
            int(limit)
        except ValueError as ex:
            print("Error: {0}".format(ex))
            return dict(status="error", message="Not a valid integer value for limit: {0}!".format(limit))
            

        point = WKTElement('POINT({0} {1})'.format(lat, lng), srid=4326)

        # # Create the list of jobs from our data
        for j in db.session.query(DBJob) \
            .filter(func.ST_DWithin(DBJob.Location, point, radius)) \
            .order_by(DBJob.Id) \
            .limit(limit) \
            .all():

            # Serialize the data for the response
            # important for WKB deserialization
            job_schema = DBJobSchema(many=False)
            jobs_dict = job_schema.dump(j)

            # Construct Swagger model for Job
            jobs.append( Job(id=j.Id, employer_id=j.EmployerId, 
                            default_image_picture_id=j.DefaultImagePictureId, 
                            description=j.Description, 
                            salary_hourly=j.SalaryHourly,
                            work_hours_per_day=j.WorkHoursPerDay,
                            work_days_per_week=j.WorkDaysPerWeek,
                            accommodation_available=j.AccommodationAvailable,
                            acommodation_cost_per_day=j.AccommodationCostPerDay,
                            with_meals=j.WithMeals,
                            meal_cost_per_day=j.MealCostPerDay,
                            spoken_languages=j.SpokenLanguages,
                            location= jobs_dict["Location"], #job.Location fails, because of WKB -> WKT
                            location_description=j.LocationDescription,
                            start_date=j.StartDate,
                            end_date=j.EndDate,
                            special_requirements=j.SpecialRequirements,
                            contingent=j.Contingent,
                            is_active=j.IsActive,
                            visible_from=None,
                            visible_to=None)
                        )

        return dict(content=jobs, status="success")

    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))


def jobs_post(body):  # noqa: E501
    """Creates a new job

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Job.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def login_post(body):  # noqa: E501
    """Userlogin, returns the users jwttoken for authentication. WARNING potentially insecure, revision required

    :param body: 
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = LoginCredentials.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


# import has to be at the end - don't know why yet
from api.run import db
from sqlalchemy import func
from geoalchemy2 import WKTElement
from api.models.db_model import ( 
    DBUser, DBEmployer, DBEmployee, DBEmployeeDocument, 
    DBEmployerPicture, DBJob, DBJobApplication, DBJobPicture, 
    DBAddress, DBContract,
    DBUserSchema, DBEmployerSchema, DBEmployeeSchema, DBEmployeeDocumentSchema,
    DBEmployerPictureSchema, DBJobSchema, DBJobApplicationSchema, DBJobPictureSchema,
    DBAddressSchema, DBContractSchema
)
