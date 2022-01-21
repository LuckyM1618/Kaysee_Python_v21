-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema twitter
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema twitter
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `twitter` DEFAULT CHARACTER SET utf8 ;
USE `twitter` ;

-- -----------------------------------------------------
-- Table `twitter`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `twitter`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL DEFAULT NULL,
  `last_name` VARCHAR(255) NULL DEFAULT NULL,
  `handle` VARCHAR(255) NULL DEFAULT NULL,
  `birthday` DATE NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `twitter`.`tweets`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `twitter`.`tweets` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tweet` VARCHAR(140) NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tweets_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_tweets_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `twitter`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 13
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `twitter`.`faves`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `twitter`.`faves` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `tweet_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_faves_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_faves_tweets1_idx` (`tweet_id` ASC) VISIBLE,
  CONSTRAINT `fk_faves_tweets1`
    FOREIGN KEY (`tweet_id`)
    REFERENCES `twitter`.`tweets` (`id`),
  CONSTRAINT `fk_faves_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `twitter`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `twitter`.`follows`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `twitter`.`follows` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `followed_id` INT NOT NULL,
  `follower_id` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_follows_users_idx` (`followed_id` ASC) VISIBLE,
  CONSTRAINT `fk_follows_users`
    FOREIGN KEY (`followed_id`)
    REFERENCES `twitter`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
