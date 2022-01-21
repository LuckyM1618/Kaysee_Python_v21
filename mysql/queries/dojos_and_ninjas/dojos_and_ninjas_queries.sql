-- Create 3 new dojos
INSERT INTO `mydb`.`dojos` (`id`, `name`, `created_at`, `updated_at`) VALUES ('1', 'Burbank', '2010-02-01 00:00:01', '2010-02-01 00:00:01');
INSERT INTO `mydb`.`dojos` (`id`, `name`, `created_at`, `updated_at`) VALUES ('2', 'San Antonio', '2010-02-01 00:00:01', '2010-02-01 00:00:01');
INSERT INTO `mydb`.`dojos` (`id`, `name`, `created_at`, `updated_at`) VALUES ('3', 'Anchorage', '2010-02-01 00:00:01', '2010-02-01 00:00:01');

-- Delete the 3 dojos you just created
DELETE FROM dojos WHERE id <= 3;

-- Create 3 more dojos
INSERT INTO `mydb`.`dojos` (`id`, `name`, `created_at`, `updated_at`) VALUES ('4', 'San Francisco', '2010-02-01 00:00:01', '2010-02-01 00:00:01');
INSERT INTO `mydb`.`dojos` (`id`, `name`, `created_at`, `updated_at`) VALUES ('5', 'Chicago', '2010-02-01 00:00:01', '2010-02-01 00:00:01');
INSERT INTO `mydb`.`dojos` (`id`, `name`, `created_at`, `updated_at`) VALUES ('6', 'Central', '2010-02-01 00:00:01', '2010-02-01 00:00:01');

-- Create 3 ninjas that belong to the first dojo
INSERT INTO `mydb`.`ninjas` (`id`, `first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`) VALUES ('1', 'Ermnam', 'Fireguard', '35', '2010-02-01 00:00:01', '2010-02-01 00:00:01', '4');
INSERT INTO `mydb`.`ninjas` (`id`, `first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`) VALUES ('2', 'Bandal', 'Trollblade', '41', '2010-02-01 00:00:01', '2010-02-01 00:00:01', '4');
INSERT INTO `mydb`.`ninjas` (`id`, `first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`) VALUES ('3', 'Tygron', 'Thunderanvil', '29', '2010-02-01 00:00:01', '2010-02-01 00:00:01', '4');

-- Create 3 ninjas that belong to the second dojo
INSERT INTO `mydb`.`ninjas` (`id`, `first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`) VALUES ('4', 'Baernik', 'Firsteye', '33', '2010-02-01 00:00:01', '2010-02-01 00:00:01', '5');
INSERT INTO `mydb`.`ninjas` (`id`, `first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`) VALUES ('5', 'Murthrum', 'Drarenn', '38', '2010-02-01 00:00:01', '2010-02-01 00:00:01', '5');
INSERT INTO `mydb`.`ninjas` (`id`, `first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`) VALUES ('6', 'Gimmun', 'Strelbren', '26', '2010-02-01 00:00:01', '2010-02-01 00:00:01', '5');

-- Create 3 ninjas that belong to the third dojo
INSERT INTO `mydb`.`ninjas` (`id`, `first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`) VALUES ('7', 'Emkyl', 'Tullinn', '54', '2010-02-01 00:00:01', '2010-02-01 00:00:01', '6');
INSERT INTO `mydb`.`ninjas` (`id`, `first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`) VALUES ('8', 'Mornam', 'Budug', '46', '2010-02-01 00:00:01', '2010-02-01 00:00:01', '6');
INSERT INTO `mydb`.`ninjas` (`id`, `first_name`, `last_name`, `age`, `created_at`, `updated_at`, `dojo_id`) VALUES ('9', 'Krumrak', 'Fofden', '64', '2010-02-01 00:00:01', '2010-02-01 00:00:01', '6');

-- Retrieve all ninjas from the first dojo
SELECT * FROM dojos
LEFT JOIN ninjas
ON dojos.id = ninjas.dojo_id
WHERE dojos.id = (
SELECT id FROM dojos
ORDER BY id ASC
LIMIT 1
);

-- Retrieve all ninjas from the last dojo
SELECT * FROM dojos
LEFT JOIN ninjas
ON dojos.id = ninjas.dojo_id
WHERE dojos.id = (
SELECT id FROM dojos
ORDER BY id DESC
LIMIT 1
);

-- Retrieve the last ninja's dojo
SELECT * from dojos
LEFT JOIN ninjas
ON dojos.id = ninjas.dojo_id
WHERE ninjas.id = (
SELECT id FROM ninjas
ORDER BY id DESC
LIMIT 1
);