CREATE DATABASE IF NOT EXISTS `django_db`;

use django_db;

GRANT ALL ON django_db.* TO 'django';
GRANT ALL PRIVILEGES ON test_django_db.* TO 'django'@'%';