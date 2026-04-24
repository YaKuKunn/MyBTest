package userOperation;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import java.io.InputStream;

public class UserTest {
    public static void main(String[] args) {
        try {
            // 1. 读取 MyBatis 的“总指挥部”配置文件
            String resource = "configuration.xml";
            InputStream inputStream = Resources.getResourceAsStream(resource);
            
            // 2. 建立一个“数据库连接工厂”
            SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
            
            // 3. 开启一次数据库会话 (Session)
            try (SqlSession session = sqlSessionFactory.openSession()) {
                
                // 4. ✨ 见证奇迹：获取接口的代理对象（MyBatis 自动把接口和 XML 连起来了）
                UserDao userDao = session.getMapper(UserDao.class);
                
                // 5. 执行查询！我们查查刚才用 SQL 插入的 ID 为 1 的数据（应该是丫堀困）
                System.out.println("正在向数据库发送查询请求...");
                User user = userDao.getUserById(1L);
                
                // 6. 打印结果
                if (user != null) {
                    System.out.println("🎉 查询成功！数据如下：");
                    System.out.println("ID: " + user.getId());
                    System.out.println("名字: " + user.getName());
                    System.out.println("邮箱: " + user.getEmail());
                } else {
                    System.out.println("没有找到 ID 为 1 的用户哦。");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}