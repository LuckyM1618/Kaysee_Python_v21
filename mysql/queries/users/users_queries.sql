-- Create 3 new users
INSERT INTO `mydb`.`users` (`id`, `first_name`, `last_name`, `email`, `created_at`, `updated_at`) VALUES ('1', 'Edward', 'Elric', 'fullmetalalchemist@amestris.gov', '2010-02-01 00:00:01', '2010-02-01 00:00:01');
INSERT INTO `mydb`.`users` (`id`, `first_name`, `last_name`, `email`, `created_at`, `updated_at`) VALUES ('2', 'Roy', 'Mustang', 'flamelalchemist@amestris.gov', '2010-02-01 00:00:01', '2010-02-01 00:00:01');
INSERT INTO `mydb`.`users` (`id`, `first_name`, `last_name`, `email`, `created_at`, `updated_at`) VALUES ('3', 'Riza', 'Hawkeye', 'rhawkeye@amestris.gov', '2010-02-01 00:00:01', '2010-02-01 00:00:01');

-- Retrieve all the users
SELECT * FROM users;

-- Retrieve the first user using their email address
SELECT * FROM users
WHERE email = 'fullmetalalchemist@amestris.gov';

-- Retrieve the last user using their id
SELECT * FROM users
ORDER BY id DESC
LIMIT 1;

-- Change the user with id=3 so their last name is Pancakes
UPDATE users
SET last_name = "Pancakes"
WHERE id = 3;

-- Delete the user with id=2 from the database
DELETE FROM users WHERE id = 2;

-- Get all the users, sorted by their first name
SELECT * FROM users
ORDER BY first_name;

-- Get all the users, sorted by their first name in descending order
SELECT * FROM users
ORDER BY first_name DESC;