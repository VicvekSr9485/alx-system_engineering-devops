sudo mysql
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'replica_user';
GRANT REPLICATION SLAVE ON *.* to 'replica_user'@'%';
GRANT SELECT ON TABLE mysql.user TO 'holberton_user'@'localhost';
