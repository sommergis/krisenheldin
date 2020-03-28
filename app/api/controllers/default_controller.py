import connexion
import six

from api.models.contract import Contract  # noqa: E501
from api.models.employee import Employee  # noqa: E501
from api.models.employer import Employer  # noqa: E501
from api.models.job import Job  # noqa: E501
from api.models.job_application import JobApplication  # noqa: E501
from api.models.login_credentials import LoginCredentials  # noqa: E501
from api.models.picture import Picture  # noqa: E501
from api.models.user import User
from api import util

from datetime import datetime

def applications_application_id_delete(application_id):
    """deletes an application

    :param application_id: The ID of the application to return.
    :type application_id: str

    :rtype: None
    """
    try:
        print("applications_application_id_get()")

        # throws a ValueError if not valid
        int(application_id)
        
        # Get employer object by primary key
        application = db.session.query(DBJobApplication).get(application_id)

        if application:
            db.session.delete(application)
            db.session.commit()

            return dict(status="success", message="Deleted Application id {0}".format(application_id))

        else:
            return dict(status="error", message="Application id {0} not found!".format(application_id))

    except ValueError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Not a valid integer value: {0}!".format(application_id))

    except TypeError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Application id {0} not found!".format(application_id))

    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))


def applications_application_id_get(application_id): 
    """Returns an application.

    :param application_id: The ID of the application to return.
    :type application_id: str

    :rtype: JobApplication
    """
    try:
        print("applications_application_id_get()")

        # throws a ValueError if not valid
        int(application_id)
        
        # Get Application object by primary key
        # throws an TypeError 'cannot unpack non-iterable NoneType object' if nothing is found
        app = db.session.query(DBJobApplication).get(application_id)

        if app:
            # Construct Swagger model for Application
            application_out = JobApplication(id=app.Id, job_id=app.JobId, employee_id=app.EmployeeId, 
                                        employee_status=app.EmployeeStatus, employer_status=app.EmployerStatus)

            return dict(content=application_out, status="success")

        else:
            return dict(status="error", message="Application id {0} not found!".format(application_id))

    except ValueError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Not a valid integer value: {0}!".format(application_id))

    except TypeError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Application id {0} not found!".format(application_id))

    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))

# TODO
def applications_application_id_put(application_id):  
    
    """Update changes to application

    :param application_id: The ID of the application to return.
    :type application_id: str

    :rtype: JobApplication
    """
    return 'do some magic!'


def applications_post(body):  
    """Creates a new application

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    try:
        print("applications_post()")

        if connexion.request.is_json:
            print(connexion.request)
            print(connexion.request.get_json())
            app = JobApplication.from_dict(connexion.request.get_json())

        if app:
            
            # Construct DB model for JobApplication
            dbapplication = DBJobApplication(Id=app.id,
                                                JobId=app.job_id,
                                                EmployeeId=app.employee_id,
                                                EmployeeStatus=app.employee_status,
                                                EmployerStatus=app.employer_status)

            # save to db
            db.session.add(dbapplication)
            db.session.commit()

            return dict(content="Application created!", status="success")

        else:
            return dict(status="error", message="Error creating application!")

    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))


def contracts_contract_id_get(contract_id): 
    """Returns the specified contract of jobs.

    :param contract_id: 
    :type contract_id: str

    :rtype: Contract
    """
    try:
        print("contract_contract_id_get()")

        # throws a ValueError if not valid
        int(contract_id)
        
        # Get Contract object by primary key
        # throws an TypeError 'cannot unpack non-iterable NoneType object' if nothing is found
        con = db.session.query(DBContract).get(contract_id)

        if con:
            # Construct Swagger model for Contract
            contract_out = Contract(id=con.Id, job_application_id=con.JobApplicationId, 
                                        employee_signed=con.EmployeeSigned, 
                                        employer_signed=con.EmployerSigned)

            return dict(content=contract_out, status="success")

        else:
            return dict(status="error", message="Contract id {0} not found!".format(contract_id))

    except ValueError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Not a valid integer value: {0}!".format(contract_id))

    except TypeError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Contract id {0} not found!".format(contract_id))

    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))


def employees_get():
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
            emps.append( Employee(id=e.Id, user_id=u.Id, first_name=u.FirstName, 
                                    last_name=u.LastName, description=e.Description, street=a.Street, 
                                    house_number=a.HouseNumber,
                                    postal_code=a.PostalCode, city=a.City, state=a.State)
                        )

        return dict(content=emps, status="success")
        
    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))

def employees_post(body):
    """Creates a new employee

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    try:
        print("employee_post()")

        if connexion.request.is_json:
            print(connexion.request)
            print(connexion.request.get_json())
            employee = Employee.from_dict(connexion.request.get_json())

        if employee:
            # Constrcut DB model for Address
            dbadress = DBAddress(PostalCode=employee.postal_code, HouseNumber=employee.house_number, 
                                    State=employee.state, Street=employee.street, City=employee.city)

            db.session.add(dbadress)

            # Construct DB model for Employee
            dbemployee = DBEmployee(UserId=employee.user_id, AddressId=dbadress.Id, 
                                        Description=employee.description)

            # save to db
            db.session.add(dbemployee)
            db.session.commit()

            return dict(content="Employee created!", status="success")

        else:
            return dict(status="error", message="Error creating employee!")

    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))


def employees_employee_id_delete(employee_id):
    """deletes an employee profile. Admin only

    :param employee_id: The ID of the employee to return.
    :type employee_id: str

    :rtype: None
    """
    try:
        print("employees_employee_id_delete()")

        # throws a ValueError if not valid
        int(employee_id)
        
        # Get employee object by primary key
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


def employees_employee_id_get(employee_id):
    """Returns an employee by ID.

    :param employee_id: The ID of the employee to return.
    :type employee_id: str

    :rtype: Employee
    """
    try:
        print("employees_employee_id_get()")

        # throws a ValueError if not valid
        int(employee_id)
        
        # Get employee object by primary key
        # throws an TypeError 'cannot unpack non-iterable NoneType object' if nothing is found
        a, e, u = db.session.query(DBAddress, DBEmployee, DBUser) \
            .filter(DBEmployee.Id==employee_id) \
            .filter(DBAddress.Id==DBEmployee.AddressId) \
            .filter(DBUser.Id==DBEmployee.UserId) \
            .first() # should return only one!

        if a and e and u:
            # Construct Swagger model for Employee
            employee_out = Employee(id=e.Id, user_id=u.Id, first_name=u.FirstName, 
                                    last_name=u.LastName, description=e.Description, street=a.Street, 
                                    house_number=a.HouseNumber,
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

# TODO
def employees_employee_id_put(employee_id):
    """Update changes to employer

    :param employee_id: The ID of the employee to return.
    :type employee_id: str

    :rtype: Employee
    """
    return 'do some magic!'


def employers_employer_id_delete(employer_id):
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


def employers_employer_id_get(employer_id): 
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
            employer_out = Employer(id=e.Id, user_id=u.Id, default_picture_id=None, company_name=e.CompanyName,
                                    industry=e.Industry, description=e.Description, first_name=u.FirstName, 
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

# TODO
def employers_employer_id_put(employer_id):
    """Update changes to employer

    :param employer_id: The ID of the employer to return.
    :type employer_id: str

    :rtype: Employer
    """
    return 'do some magic!'


def employers_get():
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
            emps.append( Employer(id=e.Id, user_id=u.Id, default_picture_id=None, company_name=e.CompanyName,
                                    industry=e.Industry, description=e.Description, first_name=u.FirstName, 
                                    last_name=u.LastName, street=a.Street, house_number=a.HouseNumber,
                                    postal_code=a.PostalCode, city=a.City, state=a.State)
                        )

        return dict(content=emps, status="success")
        
    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))


def employers_post(body):
    """Creates a new employer

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    try:
        print("employer_post()")


        if connexion.request.is_json:
            print(connexion.request)
            print(connexion.request.get_json())
            employer = Employer.from_dict(connexion.request.get_json())

        if employer:
            # Constrcut DB model for Address
            dbadress = DBAddress(PostalCode=employer.postal_code, HouseNumber=employer.house_number, 
                                    State=employer.state, Street=employer.street, City=employer.city)

            db.session.add(dbadress)

            # Construct DB model for Employer
            dbemployer = DBEmployer(UserId=employer.user_id, CompanyName=employer.company_name, 
                                    Industry=employer.industry, 
                                    Description=employer.description, AddressId=dbadress.Id)

            # save to db
            db.session.add(dbemployer)
            db.session.commit()

            return dict(content="Employer created!", status="success")

        else:
            return dict(status="error", message="Error creating employer!")

    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))


def jobs_get():
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


def jobs_job_id_delete(job_id):
    """deletes a job

    :param job_id: The ID of the job to delete.
    :type job_id: int

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


def jobs_job_id_get(job_id):
    """Returns a job.

    :param job_id: The ID of the job to return.
    :type job_id: int

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


def jobs_post(body):
    """Creates a new job

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """    
    try:
        print("jobs_post()")

        if connexion.request.is_json:
            print(connexion.request)
            print(connexion.request.get_json())
            job = Job.from_dict(connexion.request.get_json())

        if job:
            
            # Construct DB model for Job
            dbjob = DBJob(EmployerId=job.employer_id, 
                            DefaultImagePictureId=job.default_image_picture_id, 
                            Description=job.description, 
                            SalaryHourly=job.salary_hourly,
                            WorkHoursPerDay=job.work_hours_per_day,
                            WorkDaysPerWeek=job.work_days_per_week,
                            AccommodationAvailable=job.accommodation_available,
                            AccommodationCostPerDay=job.acommodation_cost_per_day,
                            WithMeals=job.with_meals,
                            MealCostPerDay=job.meal_cost_per_day,
                            SpokenLanguages=job.spoken_languages,
                            Location='POINT({0} {1})'.format(job.location.lat, job.location.lng),
                            LocationDescription=job.location_description,
                            StartDate=datetime.strptime(job.start_date, '%d.%m.%Y'),
                            EndDate=datetime.strptime(job.end_date, '%d.%m.%Y'),
                            SpecialRequirements=job.special_requirements,
                            Contingent=job.contingent,
                            IsActive=job.is_active)
            # save to db
            db.session.add(dbjob)
            db.session.commit()

            return dict(content="Job created!", status="success")

        else:
            return dict(status="error", message="Error creating job!")

    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))


# TODO
def jobs_job_id_put(job_id):
    """Update changes to job

    :param job_id: The ID of the job to return.
    :type job_id: str

    :rtype: Job
    """
    return 'do some magic!'


# TODO
def jobs_job_id_pictures_get(job_id):
    """Returns a list of pictures for the specified job.

    :param job_id: The ID of the job
    :type job_id: str

    :rtype: List[Picture]
    """
    return 'do some magic!'

# TODO
def jobs_job_id_pictures_picture_id_delete(job_id, picture_id):
    """deletes a picture

    :param job_id: The ID of the job to return.
    :type job_id: str
    :param picture_id: The ID of the picture to delete.
    :type picture_id: str

    :rtype: None
    """
    return 'do some magic!'

# TODO
def jobs_job_id_pictures_picture_id_get(job_id, picture_id):
    """gets a picture

    :param job_id: The ID of the job to return.
    :type job_id: str
    :param picture_id: The ID of the picture to show.
    :type picture_id: str

    :rtype: None
    """
    return 'do some magic!'

# TODO
def jobs_job_id_pictures_post(body):
    """Creates a new job picture

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    try:
        print("jobs_job_id_pictures_post()")

        if connexion.request.is_json:
            print(connexion.request)
            print(connexion.request.get_json())
            picture = Picture.from_dict(connexion.request.get_json())

        if picture:
            
            # Construct DB model for JobPicture
            dbpicture = DBJobPicture()

            # save to db
            db.session.add(dbpicture)
            db.session.commit()

            return dict(content="JobPicture created!", status="success")

        else:
            return dict(status="error", message="Error creating job picture!")

    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))


def jobs_near_get(lat=None, lng=None, radius=None, limit=100):
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


def users_get():
    """Returns a list of users.

    :rtype: list of Users
    """
    try:
        print("users_get()")
        users = []

        # # Create the list of users from our data
        for u in db.session.query(DBUser) \
            .order_by(DBUser.Id) \
            .all():

            # Construct Swagger model for Job
            users.append( User(id=u.Id, login=u.Login))

        return dict(content=users, status="success")
        
    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))


def users_user_id_get(user_id):
    """Returns a user by ID.

    :param user_id: The ID of the user to return.
    :type user_id: int

    :rtype: User
    """
    try:
        print("users_user_id_get()")
        
        # throws a ValueError if not valid
        int(user_id)

        # Get user object by primary key
        user = db.session.query(DBUser).get(user_id)
        if user:

            # Construct Swagger model for User
            user_out = User(id=user.Id, login=user.Login)

            return dict(content=user_out, status="success")

        else:
            return dict(status="error", message="User id {0} not found!".format(user_id))
        
    except ValueError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="Not a valid integer value: {0}!".format(user_id))

    except TypeError as ex:
        print("Error: {0}".format(ex))
        return dict(status="error", message="User id {0} not found!".format(user_id))

    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))

    
def users_post(body):
    """Creates a new user

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    try:
        print("users_post()")

        if connexion.request.is_json:
            print(connexion.request)
            print(connexion.request.get_json())
            user = User.from_dict(connexion.request.get_json())

        if user:
            
            # Construct DB model for User
            dbuser = DBUser(Id=user.id, Login=user.login, Password=user.password)

            # save to db
            db.session.add(dbuser)
            db.session.commit()

            return dict(content="User created!", status="success")

        else:
            return dict(status="error", message="Error creating user!")

    except Exception as ex:
        print("Error: {0}".format(ex))
        # only for dev stage - turn to the following in production
        # return dict(status="error", message="An unknown error occurred!")
        return dict(status="error", message="{0}".format(ex))

def login_post(body):
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
