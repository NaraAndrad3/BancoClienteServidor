

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Banco-POO
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Banco` ;

-- -----------------------------------------------------
-- Schema Banco-POO
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Banco` ;
USE `Banco` ;

-- -----------------------------------------------------
-- Table `Banco-POO`.`Cliente`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Banco`.`Cliente` ;

CREATE TABLE IF NOT EXISTS `Banco`.`Cliente` (
  `idCliente` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `CPF` VARCHAR(11) NOT NULL,
  `Nascimento` VARCHAR(8) NOT NULL,
  PRIMARY KEY (`idCliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Banco-POO`.`Conta`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Banco`.`Conta` ;

CREATE TABLE IF NOT EXISTS `Banco`.`Conta` (
  `idConta` INT NOT NULL AUTO_INCREMENT,
  `numero` VARCHAR(3) NOT NULL,
  `Saldo` FLOAT NOT NULL,
  `Limite` FLOAT NOT NULL,
  `Senha` VARCHAR(45) NOT NULL,
  `Cliente_idCliente` INT NOT NULL,
  PRIMARY KEY (`idConta`),
  INDEX `fk_Conta_Cliente_idx` (`Cliente_idCliente` ASC) VISIBLE,
  CONSTRAINT `fk_Conta_Cliente`
    FOREIGN KEY (`Cliente_idCliente`)
    REFERENCES `Banco`.`Cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Banco-POO`.`Historico`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Banco`.`Historico` ;

CREATE TABLE IF NOT EXISTS `Banco`.`Historico` (
  `idHistorico` INT NOT NULL AUTO_INCREMENT,
  `TipoTransação` VARCHAR(45) NOT NULL,
  `Valor` FLOAT NOT NULL,
  `Data` DATETIME NOT NULL,
  `Conta_idConta` INT NOT NULL,
  PRIMARY KEY (`idHistorico`),
  INDEX `fk_Historico_Conta1_idx` (`Conta_idConta` ASC) VISIBLE,
  CONSTRAINT `fk_Historico_Conta1`
    FOREIGN KEY (`Conta_idConta`)
    REFERENCES `Banco`.`Conta` (`idConta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
