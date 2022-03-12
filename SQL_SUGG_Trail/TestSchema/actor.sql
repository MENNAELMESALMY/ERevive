CREATE TABLE `actor` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `nationality` int(11) NOT NULL,
  `birth_dates` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

