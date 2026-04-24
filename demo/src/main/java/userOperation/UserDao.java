package userOperation;

import java.util.List;

public interface UserDao {
    // 根据 ID 查询用户的方法
    User getUserById(Long id);
    
    // 查询所有用户
    List<User> getAllUsers();
    
    // 添加用户
    void insertUser(User user);
    
    // 更新用户（根据 ID）
    void updateUser(User user);
    
    // 删除用户（根据 ID）
    void deleteUser(int id);
}