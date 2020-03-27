CREATE TABLE "Users" (
  "Id" serial PRIMARY KEY,
  "Login" text,
  "Password" text,
  "FirstName" text,
  "LastName" text
);

CREATE TABLE "Address" (
  "Id" serial PRIMARY KEY,
  "Street" text,
  "HouseNumber" text,
  "PostalCode" text,
  "City" text,
  "State" text --enum
);

CREATE TABLE "Employers" (
  "Id" serial PRIMARY KEY,
  "UserId" int,
  "DefaultPictureId" int,
  "CompanyName" text,
  "Industry" text, --enum
  "Description" text,
  "AddressId" int,
  "CreatedAt" timestamp,
  "UpdatedAt" timestamp
);

CREATE TABLE "EmployerPictures" (
  "Id" serial PRIMARY KEY,
  "EmployerId" int,
  "path" text
);

CREATE TABLE "JobPictures" (
  "Id" serial PRIMARY KEY,
  "JobId" int,
  "path" text
);

CREATE TABLE "EmployeeDocuments" (
  "Id" serial PRIMARY KEY,
  "EmployeeId" int,
  "EmployeeeDocumentType" text, --enum
  "path" text
);

CREATE TABLE "Employees" (
  "Id" serial PRIMARY KEY,
  "UserId" int,
  "AddressId" int,
  "Description" text,
  "CreatedAt" timestamp,
  "UpdatedAt" timestamp
);

CREATE TABLE "Jobs" (
  "Id" serial PRIMARY KEY,
  "EmployerId" int,
  "DefaultImagePictureId" int,
  "Description" text,
  "SalaryHourly" decimal,
  "WorkHoursPerDay" decimal,
  "WorkDaysPerWeek" integer,
  "AccommodationAvailable" bool,
  "AccommodationCostPerDay" decimal,
  "WithMeals" bool,
  "MealCostPerDay" decimal,
  "SpokenLanguages" text,
  "Location" geography,
  "LocationDescription" text,
  "StartDate" timestamp,
  "EndDate" timestamp,
  "SpecialRequirements" text,
  "Contingent" integer,
  "IsActive" boolean,
  "CreatedAt" timestamp,
  "UpdatedAt" timestamp
);

CREATE TABLE "JobApplications" (
  "Id" serial PRIMARY KEY,
  "JobId" int,
  "EmployeeId" int,
  "EmployerId" int,
  "EmployeeStatus" text, --enum
  "EmployerStatus" text, --enum
  "CreatedAt" timestamp,
  "UpdatedAt" timestamp
);

CREATE TABLE "JobPoints" (
  "ContractId" int,
  "EmployeeId" int,
  "GivenPoints" int,
  "CreatedAt" timestamp,
  "UpdatedAt" timestamp
);

CREATE TABLE "Contracts" (
  "Id" serial PRIMARY KEY,
  "JobApplicationId" int,
  "CreatedAt" timestamp,
  "EmployeeSigned" timestamp,
  "EmployerSigned" timestamp,
  "UpdatedAt" timestamp
);

ALTER TABLE "Employers" ADD FOREIGN KEY ("UserId") REFERENCES "Users" ("Id");

ALTER TABLE "Employers" ADD FOREIGN KEY ("DefaultPictureId") REFERENCES "EmployerPictures" ("Id");

ALTER TABLE "Employers" ADD FOREIGN KEY ("AddressId") REFERENCES "Address" ("Id");

ALTER TABLE "EmployerPictures" ADD FOREIGN KEY ("EmployerId") REFERENCES "Employers" ("Id");

ALTER TABLE "JobPictures" ADD FOREIGN KEY ("JobId") REFERENCES "Jobs" ("Id");

ALTER TABLE "EmployeeDocuments" ADD FOREIGN KEY ("EmployeeId") REFERENCES "Employees" ("Id");

ALTER TABLE "Employees" ADD FOREIGN KEY ("UserId") REFERENCES "Users" ("Id");

ALTER TABLE "Employees" ADD FOREIGN KEY ("AddressId") REFERENCES "Address" ("Id");

ALTER TABLE "Jobs" ADD FOREIGN KEY ("EmployerId") REFERENCES "Employers" ("Id");

ALTER TABLE "Jobs" ADD FOREIGN KEY ("DefaultImagePictureId") REFERENCES "JobPictures" ("Id");

ALTER TABLE "JobApplications" ADD FOREIGN KEY ("JobId") REFERENCES "Jobs" ("Id");

ALTER TABLE "JobApplications" ADD FOREIGN KEY ("EmployeeId") REFERENCES "Employees" ("Id");

ALTER TABLE "JobApplications" ADD FOREIGN KEY ("EmployerId") REFERENCES "Employers" ("Id");

ALTER TABLE "JobPoints" ADD FOREIGN KEY ("ContractId") REFERENCES "Contracts" ("Id");

ALTER TABLE "JobPoints" ADD FOREIGN KEY ("EmployeeId") REFERENCES "Employees" ("Id");

ALTER TABLE "Contracts" ADD FOREIGN KEY ("JobApplicationId") REFERENCES "JobApplications" ("Id");
