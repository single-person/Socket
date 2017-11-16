from models import Model
from models.comment import Comment


class Weibo(Model):
    """
    微博类
    """
    content: str
    # 和别的数据关联的方式, 用 user_id 表明拥有它的 user 实例
    user_id: int

    def is_owner(self, id):
        return self.user_id == id

    def comments(self):
        return Comment.find_all(weibo_id=self.id)