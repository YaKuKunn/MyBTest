# !/apps/venv/bin/python
import pymysql

import yaml

def config() -> [str, str, str]:
    with open('/apps/account.yml', 'r') as f:
        conf = yaml.load(f, Loader=yaml.FullLoader)
        host = conf['database']['host']
        username = conf['database']['username']
        password = conf['database']['password']
        return host, username, password
def sql_write(sql_info: str) -> None:
    try:
        cursor.execute(sql_info)
        print("SQL执行成功")
    except Exception as e:
        print(f"SQL执行失败", e)
    finally:
        conn.commit()


def sql_read(sql_info: str) -> ():
    try:
        cursor.execute(sql_info)
        return cursor.fetchall()
    except Exception as e:
        print(f"SQL执行失败", e)


if __name__ == "__main__":
    # 1、创建连接
    db_host, db_user, db_passwd = config()
    conn = pymysql.connect(host=db_host, port=3306, user=db_user,
                           passwd=db_passwd, db='commodity', charset="utf8")

    # 2、创建游标
    cursor = conn.cursor()

    # 3、Bob将自己的订单《三体》都改为5本
    sql_order_item_id = """
    SELECT oi.`order_item_id`
      FROM orders o
      LEFT JOIN users u ON o.user_id= u.user_id
      LEFT JOIN order_items oi ON o.order_id= oi.order_id
      LEFT JOIN books b ON oi.book_id= b.book_id
     WHERE b.name= '三体'
       AND u.`user_name`= 'Bob'
    """
    # Bob购买《三体》的订单项ID
# Bob购买《三体》的订单项ID
results = sql_read(sql_order_item_id)

# 检查是否有结果
if not results:
    print("Bob没有购买《三体》的记录，跳过更新")
else:
    # 提取 order_item_id
    order_item_ids = []
    for row in results:
        for value in row:  # 遍历每一行的每个字段
            if value is not None:  # 确保值不是 None
                order_item_ids.append(str(value))
    
    if not order_item_ids:
        print("没有找到有效的订单项ID，跳过更新")
    else:
        # 构建IN子句
        ids_str = ','.join(order_item_ids)
        sql = f"""
        UPDATE `order_items`
           SET `quantity`= 5
         WHERE `order_item_id` IN ({ids_str})
        """
        sql_write(sql)

    # 4、关闭游标
    cursor.close()

    # 5、关闭连接
    conn.close()