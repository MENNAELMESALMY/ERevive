CREATE TABLE `movie_actor` (
  `id` int(11) NOT NULL,
  `pid` int(11),
  `aid` varchar(255),
  PRIMARY KEY (`id`),
  CONSTRAINT `aid` FOREIGN KEY (`aid`) REFERENCES `actor` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `pid` FOREIGN KEY (`pid`) REFERENCES `movie` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8;