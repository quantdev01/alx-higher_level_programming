-- Root user with all privilege
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd';
GRANT ALL 
ON *.*
TO user_0d_1@localhost;
