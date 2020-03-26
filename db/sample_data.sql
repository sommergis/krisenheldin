INSERT INTO "Users" ("Login","Password","FirstName","LastName")
VALUES ('meister_lampe', 'verysecret', 'Hans', 'Meister');

INSERT INTO "Employers" 
 ("UserId", "DefaultPictureId","CompanyName","Industry","Description","AddressId")
VALUES(1, NULL, 'Meister Lampe GmbH', 'Bäcker', 'Wir backen die besten Semmeln!', NULL);