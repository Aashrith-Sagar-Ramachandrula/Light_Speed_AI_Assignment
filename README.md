# Light_Speed_AI_Assignment

Greetings!!

In order to run the project,
-- Please run the local host instance on 3306 port
-- Create a database named Test2 
-- Create the table using the below SQL code

CREATE TABLE `config_table` (
  `device_name` varchar(20) NOT NULL,
  `MAR` varchar(5) NOT NULL,
  `MDR` varchar(5) NOT NULL,
  `IR` varchar(5) NOT NULL,
  `AC` varchar(5) NOT NULL,
  `time_Stamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



-- If you want to dump some random data to the created table, please use the below SQL codes

INSERT INTO `config_table` (`device_name`, `MAR`, `MDR`, `IR`, `AC`, `time_Stamp`) VALUES
('device1', '2', '1', '4', '3', '2022-08-11 06:42:55'),
('device1', '4', '2', '4', '6', '2022-08-11 06:43:15'),
('device2', '7', '2', '6', '0', '2022-08-11 13:04:39'),
('device3', '4', '1', '5', '5', '2022-08-11 07:52:21'),
('device3', '3', '8', '5', '9', '2022-08-11 12:32:51'),
('device4', '4', '0', '4', '10', '2022-08-11 07:47:38'),
('device5', '7', '5', '8', '5', '2022-08-11 12:33:43');


----------------------

Download the images from the folder into a folder named "images"
----------------------

Run the Project

Please check the sample output screenshots to see how the application looks like

-------------------------

The solution to the second question i.e Implementing Stacks using Two Queues is given in the pdf file named "LightSpeedAI_Assignment - 2.pdf"

---------------------------


Thank & Regards
Ramachandrula Aashrith Sagar



