-- 1. 创建数据库（如果你之前已经建了 bigdata2601，这一句会安全跳过）
CREATE DATABASE IF NOT EXISTS test DEFAULT CHARACTER SET utf8mb4;

-- 2. 切换到这个数据库
USE test;

-- 3. 创建 user 表
CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY COMMENT '主键ID',
    name VARCHAR(50) NOT NULL COMMENT '用户名',
    age INT COMMENT '年龄',
    email VARCHAR(100) COMMENT '邮箱'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户测试表';

-- 4. 插入几条初始测试数据，方便我们等下用 MyBatis 查询
INSERT INTO user (name, age, email) VALUES 
('丫堀困', 22, 'yakukunn@example.com'),
('张三', 20, 'zhangsan@test.com'),
('李四', 25, 'lisi@test.com');


SELECT * FROM user;